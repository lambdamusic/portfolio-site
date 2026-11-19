/*
 * The Topic and Type rows above the projects grid (#18, pages/projects.html).
 *
 * Filtering happens here rather than with ?query URLs, so the static site has
 * one projects page instead of one per combination. The state lives in the
 * URL hash (#topic=…&type=…), so a filtered view can be linked to: the
 * keywords under each tile and on project pages are such links.
 */
(function () {
  'use strict';

  var grid = document.querySelector('.tilegrid');
  var filter = document.querySelector('.pfilter');
  if (!grid || !filter) return;

  var tiles = [].slice.call(grid.querySelectorAll('.thumb-div[data-type]'));
  var count = filter.querySelector('.pfilter-count');
  var state = { topic: '', type: '' };

  function readHash() {
    state = { topic: '', type: '' };
    location.hash.replace(/^#/, '').split('&').forEach(function (part) {
      var kv = part.split('=');
      if (kv[0] in state) state[kv[0]] = decodeURIComponent(kv[1] || '');
    });
  }

  function writeHash() {
    var parts = [];
    if (state.topic) parts.push('topic=' + state.topic);
    if (state.type) parts.push('type=' + state.type);
    var url = location.pathname + location.search + (parts.length ? '#' + parts.join('&') : '');
    history.replaceState(null, '', url);
  }

  function apply() {
    var shown = 0;
    tiles.forEach(function (t) {
      var ok = (!state.topic || (' ' + t.getAttribute('data-topics') + ' ').indexOf(' ' + state.topic + ' ') > -1) &&
               (!state.type || t.getAttribute('data-type') === state.type);
      t.classList.toggle('is-hidden', !ok);
      if (ok) shown++;
    });
    ['topic', 'type'].forEach(function (k) {
      filter.querySelectorAll('[data-' + k + ']').forEach(function (chip) {
        var on = chip.getAttribute('data-' + k) === state[k];
        chip.classList.toggle('is-current', on);
        chip.classList.toggle('chip--quiet', !on);
      });
    });
    count.textContent = (shown === tiles.length ? '' : shown + ' of ') + tiles.length + ' projects';
  }

  document.addEventListener('click', function (e) {
    // links only: the tiles carry data-type too, and a click on a project's
    // name or picture must go to its page
    var link = e.target.closest('a[data-topic], a[data-type]');
    if (!link || !(link.closest('.pfilter') || link.closest('.tilegrid'))) return;
    e.preventDefault();
    if (link.hasAttribute('data-topic')) state.topic = link.getAttribute('data-topic');
    if (link.hasAttribute('data-type')) state.type = link.getAttribute('data-type');
    writeHash();
    apply();
    // a keyword under a tile: bring the filter rows back into view
    if (link.closest('.tilegrid')) filter.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });

  window.addEventListener('hashchange', function () { readHash(); apply(); });
  readHash();
  apply();
})();
