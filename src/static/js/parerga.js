/* parerga.js - behaviour for the left "INSIDE" drawer.
 *
 * The original theme opened the drawer on :hover only, which is unreachable
 * on touch devices and invisible to keyboard users. Hover still works (it is
 * handled in CSS); this adds an explicit toggle, Escape-to-close, and a scrim
 * so the drawer is usable everywhere.
 */
(function () {
  'use strict';

  function ready(fn) {
    if (document.readyState !== 'loading') { fn(); }
    else { document.addEventListener('DOMContentLoaded', fn); }
  }

  ready(function () {
    var rail = document.getElementById('site-rail');
    if (!rail) { return; }

    var handle = rail.querySelector('.rail-handle');
    var scrim = document.createElement('div');
    scrim.className = 'rail-scrim';
    document.body.appendChild(scrim);

    function setOpen(open) {
      rail.classList.toggle('is-open', open);
      scrim.classList.toggle('is-visible', open);
      if (handle) { handle.setAttribute('aria-expanded', open ? 'true' : 'false'); }
    }

    if (handle) {
      handle.addEventListener('click', function (e) {
        e.preventDefault();
        setOpen(!rail.classList.contains('is-open'));
      });
    }

    scrim.addEventListener('click', function () { setOpen(false); });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) { setOpen(false); }
    });

    // Closing on pointer-leave keeps the hover behaviour of the original
    // feeling the same once the drawer has been opened by hover.
    rail.addEventListener('mouseleave', function () {
      if (window.matchMedia('(min-width: 861px)').matches) { setOpen(false); }
    });
  });
})();
