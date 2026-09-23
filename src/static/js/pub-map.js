/* pub-map.js - the small map on a paper's own page: where this one happened.
 *
 * Static, not interactive. A single dot for this publication, ringed, with
 * every other mapped place shown faintly behind it - a lone dot on an empty
 * world says "somewhere in Slovenia" and nothing else, whereas the faded
 * backdrop puts it among everywhere the work has been.
 *
 * The world itself is drawn by world-map.js, shared with /events/.
 */
function initPubMap(options) {
  'use strict';

  var host = document.getElementById('pubmap-canvas');
  var dataEl = document.getElementById('pubmap-data');
  if (!host || !dataEl) { return; }

  var data = JSON.parse(dataEl.textContent || 'null');
  var block = host.closest('.pubmap');
  if (!data || !data.focus) { block.style.display = 'none'; return; }

  WorldMap.draw(host, 520, options.worldUrl, function (world) {
    if (!world) { block.style.display = 'none'; return; }

    var svg = world.svg;
    var projection = world.projection;

    // context first, so the focused dot is painted over it
    svg.append('g').attr('class', 'worldmap-dots worldmap-dots--context')
      .selectAll('circle')
      .data(data.context || [])
      .enter().append('circle')
      .attr('cx', function (d) { return projection([d[1], d[0]])[0]; })
      .attr('cy', function (d) { return projection([d[1], d[0]])[1]; })
      .attr('r', 2.6);

    var xy = projection([data.focus.lon, data.focus.lat]);

    svg.append('circle')
      .attr('class', 'worldmap-halo')
      .attr('cx', xy[0]).attr('cy', xy[1])
      .attr('r', 9);

    svg.append('circle')
      .attr('class', 'worldmap-focus')
      .attr('cx', xy[0]).attr('cy', xy[1])
      .attr('r', 4.2);
  });
}
