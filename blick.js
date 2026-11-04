/* Kleine Lupen auf den "Zwei Blicke"-Karten: außen der flüchtige Blick, innen der genaue. */
(function () {
  'use strict';
  var ruhig = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ohneHover = window.matchMedia && matchMedia('(hover: none)').matches;

  document.querySelectorAll('.blick').forEach(function (el) {
    var x, y, tx, ty, r = 0, tr = 0, gross = false, laeuft = false;

    function mass() { return el.getBoundingClientRect(); }
    function basis() { return Math.max(70, Math.min(130, mass().width * 0.24)); }
    function start() { var b = mass(); x = tx = b.width * 0.5; y = ty = b.height * 0.5; }
    start();
    if (ohneHover) { tr = basis(); }   // am Handy ist die Lupe von Anfang an da

    function zeiger(e) {
      var b = mass();
      tx = e.clientX - b.left; ty = e.clientY - b.top;
      tr = gross ? Math.hypot(b.width, b.height) : basis();
      los();
    }
    el.addEventListener('pointerenter', function (e) { zeiger(e); });
    el.addEventListener('pointermove', zeiger);
    el.addEventListener('pointerdown', function (e) { if (e.pointerType === 'mouse') gross = true; zeiger(e); });
    addEventListener('pointerup', function () { gross = false; tr = ohneHover ? basis() : tr; los(); });
    el.addEventListener('pointerleave', function (e) { gross = false; if (e.pointerType === 'mouse') { tr = 0; los(); } });
    addEventListener('resize', start);

    function schritt() {
      var f = ruhig ? 1 : 0.18;
      x += (tx - x) * f; y += (ty - y) * f; r += (tr - r) * (ruhig ? 1 : (gross ? 0.08 : 0.16));
      el.style.setProperty('--mx', x.toFixed(1) + 'px');
      el.style.setProperty('--my', y.toFixed(1) + 'px');
      el.style.setProperty('--r', Math.max(0, r).toFixed(1) + 'px');
      if (Math.abs(tx - x) > 0.3 || Math.abs(ty - y) > 0.3 || Math.abs(tr - r) > 0.3) requestAnimationFrame(schritt);
      else laeuft = false;
    }
    function los() { if (!laeuft) { laeuft = true; requestAnimationFrame(schritt); } }
    los();
  });
})();
