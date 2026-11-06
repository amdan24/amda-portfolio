/* Lupe: folgt Maus/Finger/Pfeiltasten; ohne Eingabe wandert sie von allein. */
(function () {
  'use strict';
  var held = document.getElementById('lupe');
  if (!held) return;
  var ruhig = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var b, x, y, tx, ty, r = 0, tr, gross = false, nutzer = false, sichtbar = true, laeuft = false, wartet = null;

  function mass() { b = held.getBoundingClientRect(); }
  function basis() { return Math.max(105, Math.min(175, b.width * 0.13)); }
  function setze(px, py) { tx = px; ty = py; }

  mass();
  x = tx = b.width * 0.62; y = ty = b.height * 0.48; tr = basis();
  if (ruhig) r = tr;

  function zeiger(e) {
    mass();
    nutzer = true; clearTimeout(wartet);
    setze(e.clientX - b.left, e.clientY - b.top);
    tr = basis();
  }
  held.addEventListener('pointermove', zeiger);
  held.addEventListener('pointerdown', function (e) {
    zeiger(e);
    if (e.pointerType === 'mouse') gross = true;
  });
  addEventListener('pointerup', function (e) {
    gross = false;
    if (e.pointerType !== 'mouse') {
      clearTimeout(wartet);
      wartet = setTimeout(function () { nutzer = false; }, 2500);
    }
  });
  held.addEventListener('pointerleave', function (e) {
    if (e.pointerType === 'mouse') { tr = 0; nutzer = true; }
  });
  held.addEventListener('pointerenter', function (e) {
    if (e.pointerType === 'mouse') { tr = basis(); }
  });
  held.addEventListener('keydown', function (e) {
    var s = 48, m = { ArrowLeft: [-s, 0], ArrowRight: [s, 0], ArrowUp: [0, -s], ArrowDown: [0, s] }[e.key];
    if (m) {
      e.preventDefault(); mass(); nutzer = true; tr = basis();
      setze(Math.max(0, Math.min(b.width, tx + m[0])), Math.max(0, Math.min(b.height, ty + m[1])));
    } else if (e.key === ' ' || e.key === 'Enter') {
      e.preventDefault(); gross = !gross;
    }
  });
  addEventListener('resize', mass);

  function schritt(t) {
    laeuft = true;
    if (!nutzer && !ruhig) {
      setze(b.width * (0.58 + 0.2 * Math.sin(t / 2600)), b.height * (0.46 + 0.16 * Math.cos(t / 1900)));
      tr = basis();
    }
    var ziel = gross ? Math.hypot(b.width, b.height) : tr;
    var f = ruhig ? 1 : 0.16;
    x += (tx - x) * f; y += (ty - y) * f;
    r += (ziel - r) * (ruhig ? 1 : (gross ? 0.07 : 0.14));
    held.style.setProperty('--mx', x.toFixed(1) + 'px');
    held.style.setProperty('--my', y.toFixed(1) + 'px');
    held.style.setProperty('--r', Math.max(0, r).toFixed(1) + 'px');
    if (sichtbar) requestAnimationFrame(schritt); else laeuft = false;
  }

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      sichtbar = es[0].isIntersecting;
      if (sichtbar && !laeuft) { mass(); requestAnimationFrame(schritt); }
    }).observe(held);
  }
  requestAnimationFrame(schritt);
})();
