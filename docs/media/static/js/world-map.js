/* world-map.js - draws the world outline both maps on this site share:
 * the one beside the /events/ listing, and the one on a paper's own page.
 *
 * Nothing here talks to a tile server or a geocoding API. The outlines come
 * from a vendored TopoJSON file and the coordinates are frozen server-side
 * (see researchapp/pub_locations.py), which is what lets the wget-mirrored
 * static site keep working offline.
 *
 * The d3 v4 build vendored in libs/d3-v4 predates geoNaturalEarth1, hence
 * geoEquirectangular. It suits this data anyway: the places cluster in the
 * northern mid-latitudes, where equirectangular wastes less height than
 * Mercator and distorts less.
 */
var WorldMap = (function () {
  'use strict';

  // Crop to 84N..56S. Nothing on this site happens in Antarctica or the high
  // Arctic, and dropping those empty bands lets the populated latitudes fill
  // the panel instead of floating in a tall white box.
  var NORTH = 84, SOUTH = -56;

  function available() {
    return typeof d3 !== 'undefined' && typeof topojson !== 'undefined';
  }

  // wget rewrites src/href attributes to relative paths when it mirrors the
  // site, but not URLs sitting inside a script block - those would stay
  // root-absolute and break if the site were ever served from a sub-path.
  // Deriving the outlines URL from the topojson <script> that wget *did*
  // rewrite keeps it correct wherever the mirror is mounted.
  function outlinesUrl(fallback) {
    var tag = document.querySelector('script[src$="topojson-client.min.js"]');
    return tag ? tag.src.replace(/topojson-client\.min\.js$/, 'countries-110m.json')
               : fallback;
  }

  /* Draws land + borders into `host` and hands back the svg selection and the
   * projection, so callers can place their own marks on it.
   *
   *   host      element to draw into
   *   width     viewBox width; height follows from the latitude crop
   *   fallback  outlines URL to use if the script tag cannot be found
   *   done      called with ({svg, projection}) on success, or (null) if the
   *             outlines could not be loaded
   */
  function draw(host, width, fallback, done) {
    if (!available()) { done(null); return; }

    // equirectangular puts y at translateY - scale * latitude_in_radians, so
    // pinning NORTH to y=0 fixes the translate and SOUTH fixes the height
    var scale = width / (2 * Math.PI);
    var translateY = scale * NORTH * Math.PI / 180;
    var height = Math.round(translateY - scale * SOUTH * Math.PI / 180);

    var svg = d3.select(host).append('svg')
      .attr('viewBox', '0 0 ' + width + ' ' + height)
      .attr('preserveAspectRatio', 'xMidYMid meet')
      .attr('class', 'worldmap-svg')
      // the map restates what the page already says in words; screen readers
      // get the text, not a bag of unlabelled circles
      .attr('aria-hidden', 'true')
      .attr('focusable', 'false');

    var projection = d3.geoEquirectangular()
      .scale(scale)
      .translate([width / 2, translateY]);

    var path = d3.geoPath().projection(projection);

    d3.json(outlinesUrl(fallback), function (error, world) {
      if (error) { done(null); return; }

      svg.append('g').attr('class', 'worldmap-land')
        .selectAll('path')
        .data(topojson.feature(world, world.objects.countries).features)
        .enter().append('path')
        .attr('d', path);

      svg.append('path').attr('class', 'worldmap-borders')
        .datum(topojson.mesh(world, world.objects.countries,
                             function (a, b) { return a !== b; }))
        .attr('d', path);

      done({ svg: svg, projection: projection });
    });
  }

  return { draw: draw };
})();
