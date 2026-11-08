/* parerga.js - behaviour for the sidebar (components/site-sidebar.html).
 *
 * On wide screens the sidebar is always open and needs no script. Below 860px
 * it folds into a top bar, and the Menu button opens and closes its body.
 * Escape closes it too.
 */
(function () {
  'use strict';

  function ready(fn) {
    if (document.readyState !== 'loading') { fn(); }
    else { document.addEventListener('DOMContentLoaded', fn); }
  }

  ready(function () {
    var side = document.getElementById('sidebar');
    if (!side) { return; }
    var btn = side.querySelector('.sidebar-toggle');
    if (!btn) { return; }

    function setOpen(open) {
      side.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    btn.addEventListener('click', function () {
      setOpen(!side.classList.contains('is-open'));
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' || e.keyCode === 27) { setOpen(false); }
    });
  });
})();
