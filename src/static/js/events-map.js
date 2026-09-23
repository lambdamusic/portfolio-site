/* events-map.js - the world map beside the /events/ listing.
 *
 * One dot per talk location, sized by how many talks happened there.
 * Hovering a list row lights up its dot; hovering a dot lights up every row
 * at that place. Coordinates come frozen from the server (see
 * researchapp/event_locations.py) and the outlines from a vendored TopoJSON
 * file, so nothing here talks to a tile server or a geocoding API - which is
 * what lets the wget-mirrored static site keep working.
 *
 * The d3 v4 build vendored in libs/d3-v4 predates geoNaturalEarth1, hence
 * geoEquirectangular. It suits this data anyway: the talks cluster in the
 * northern mid-latitudes, where equirectangular wastes less height than
 * Mercator and distorts less.
 */
function initEventsMap(options) {
  'use strict';

  var host = document.getElementById('eventsmap-canvas');
  var dataEl = document.getElementById('eventsmap-data');
  if (!host || !dataEl || typeof d3 === 'undefined' || typeof topojson === 'undefined') {
    return;
  }

  var points = JSON.parse(dataEl.textContent || '[]');
  if (!points.length) {
    host.closest('.eventsmap').style.display = 'none';
    return;
  }

  var wrap = host.closest('.eventsmap-sticky');
  var caption = document.getElementById('eventsmap-caption');
  var detail = document.getElementById('eventsmap-detail');
  var rows = Array.prototype.slice.call(
    document.querySelectorAll('.speakingitem[data-event]'));

  // Group talks by place: one dot per location, not per talk, so repeat
  // visits read as a bigger dot rather than as dots stacked invisibly.
  var byPlace = {};
  points.forEach(function (p) {
    var key = p.lat + ',' + p.lon;
    if (!byPlace[key]) {
      byPlace[key] = { lat: p.lat, lon: p.lon, place: p.place, talks: [] };
    }
    byPlace[key].talks.push(p);
  });
  // Biggest first, so they are painted underneath: a small dot overlapping a
  // large one stays clickable, and the large one keeps an exposed ring.
  var places = Object.keys(byPlace)
    .map(function (k) { return byPlace[k]; })
    .sort(function (a, b) { return b.talks.length - a.talks.length; });

  // index -> place, for the list -> map direction
  var placeByEventIndex = {};
  places.forEach(function (pl) {
    pl.talks.forEach(function (t) { placeByEventIndex[t.i] = pl; });
  });

  // Crop to 84N..56S: no talks happen in Antarctica or the high Arctic, and
  // dropping those empty bands lets the populated latitudes fill the panel
  // instead of floating in a tall white box.
  var WIDTH = 420;
  var NORTH = 84, SOUTH = -56;

  // equirectangular puts y at translateY - scale * latitude_in_radians, so
  // pinning NORTH to y=0 fixes the translate and SOUTH fixes the height
  var scale = WIDTH / (2 * Math.PI);
  var translateY = scale * NORTH * Math.PI / 180;
  var HEIGHT = Math.round(translateY - scale * SOUTH * Math.PI / 180);

  var svg = d3.select(host).append('svg')
    .attr('viewBox', '0 0 ' + WIDTH + ' ' + HEIGHT)
    .attr('preserveAspectRatio', 'xMidYMid meet')
    .attr('class', 'eventsmap-svg')
    // the map restates what the list already says; screen readers get the
    // list, not a bag of unlabelled circles
    .attr('aria-hidden', 'true')
    .attr('focusable', 'false');

  var projection = d3.geoEquirectangular()
    .scale(scale)
    .translate([WIDTH / 2, translateY]);

  var path = d3.geoPath().projection(projection);

  // wget rewrites src/href attributes to relative paths when it mirrors the
  // site, but not URLs sitting inside a script block - those would stay
  // root-absolute and break if the site were ever served from a sub-path.
  // Deriving the outlines URL from the topojson <script> that wget *did*
  // rewrite keeps it correct wherever the mirror is mounted.
  function worldUrl() {
    var tag = document.querySelector('script[src$="topojson-client.min.js"]');
    return tag ? tag.src.replace(/topojson-client\.min\.js$/, 'countries-110m.json')
               : options.worldUrl;
  }

  d3.json(worldUrl(), function (error, world) {
    if (error) {
      host.closest('.eventsmap').style.display = 'none';
      return;
    }

    svg.append('g').attr('class', 'eventsmap-land')
      .selectAll('path')
      .data(topojson.feature(world, world.objects.countries).features)
      .enter().append('path')
      .attr('d', path);

    svg.append('path').attr('class', 'eventsmap-borders')
      .datum(topojson.mesh(world, world.objects.countries, function (a, b) { return a !== b; }))
      .attr('d', path);

    var dots = svg.append('g').attr('class', 'eventsmap-dots')
      .selectAll('circle')
      .data(places)
      .enter().append('circle')
      .attr('cx', function (d) { return projection([d.lon, d.lat])[0]; })
      .attr('cy', function (d) { return projection([d.lon, d.lat])[1]; })
      .attr('r', function (d) { return 3.2 + Math.min(d.talks.length - 1, 3) * 1.5; })
      .on('mouseenter', function (d) { hoverPlace(d); })
      .on('mouseleave', function () { hoverPlace(null); })
      .on('click', function (d) {
        d3.event.stopPropagation();
        pin(pinned === d ? null : d);
      });

    // A ring drawn over the top: with fifty dots and half of them inside
    // Europe, recolouring one of them is not enough to find it.
    var halo = svg.append('circle')
      .attr('class', 'eventsmap-halo')
      .attr('r', 9)
      .style('display', 'none');

    // Hovering only previews. Clicking pins, because the whole point of the
    // detail list is to click through to a talk, and reaching it means
    // moving the cursor off the dot - which would clear a hover-only panel
    // before you got there.
    var pinned = null;

    // Set from JS, never in the template: if the map failed to draw there is
    // nothing to click and the hint would be a lie.
    var IDLE_HINT = 'Click a dot for details';

    function hoverPlace(place) {
      if (pinned) { return; }        // a pin wins until it is cleared
      focusPlace(place);
    }

    function pin(place) {
      pinned = place;
      wrap.classList.toggle('is-pinned', !!place);
      focusPlace(place);
    }

    function focusPlace(place) {
      dots.classed('is-active', function (d) { return d === place; });
      svg.classed('is-focused', !!place);

      if (place) {
        var xy = projection([place.lon, place.lat]);
        halo.attr('cx', xy[0]).attr('cy', xy[1]).style('display', null);
      } else {
        halo.style('display', 'none');
      }

      rows.forEach(function (row) {
        var pl = placeByEventIndex[+row.dataset.event];
        row.classList.toggle('is-mapped-active', !!place && pl === place);
      });

      if (place) {
        renderCaption(place);
        renderDetail(place);
      } else {
        caption.textContent = IDLE_HINT;
        detail.innerHTML = '';
      }
    }

    function renderCaption(place) {
      var n = place.talks.length;
      caption.textContent = place.place + ' · ' + n + (n === 1 ? ' talk' : ' talks');

      if (pinned === place) {
        var clear = document.createElement('button');
        clear.type = 'button';
        clear.className = 'eventsmap-clear';
        clear.textContent = 'clear';
        clear.addEventListener('click', function (e) {
          e.stopPropagation();
          pin(null);
        });
        caption.appendChild(document.createTextNode(' · '));
        caption.appendChild(clear);
      }
    }

    // Somewhere visited four times has its other talks scrolled far off
    // screen, so list them here rather than jerking the page to them.
    function renderDetail(place) {
      detail.innerHTML = '';
      place.talks.forEach(function (t) {
        var li = document.createElement('li');
        var year = document.createElement('b');
        year.textContent = t.year;
        var a = document.createElement('a');
        a.href = t.url;
        a.textContent = t.title;
        li.appendChild(year);
        li.appendChild(document.createTextNode(' '));
        li.appendChild(a);
        detail.appendChild(li);
      });
    }

    // list -> map. Pointer only: this is decoration, and a keyboard user
    // tabbing through the talk links should not be yanked sideways by it.
    rows.forEach(function (row) {
      row.addEventListener('mouseenter', function () {
        hoverPlace(placeByEventIndex[+row.dataset.event] || null);
      });
      row.addEventListener('mouseleave', function () { hoverPlace(null); });
    });

    // Let go of a pin the ways people expect: Escape, or a click anywhere
    // that is not the panel itself (clicking a talk link inside the panel
    // navigates away, so it never needs to survive).
    document.addEventListener('click', function (e) {
      if (pinned && !wrap.contains(e.target)) { pin(null); }
    });
    document.addEventListener('keydown', function (e) {
      if (pinned && (e.key === 'Escape' || e.keyCode === 27)) { pin(null); }
    });

    focusPlace(null);   // puts the hint in place now the map is drawn
  });
}
