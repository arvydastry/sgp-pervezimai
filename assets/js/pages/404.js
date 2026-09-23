/* =========================================================
   SGP v2 · 404.js (page-owned: pages-about-contact) — 404 „Maršrutas nerastas“ §6.11
   Measures the desktop lane (hero top → neutral end ring) and starts the „wrong turn“
   sequence: red lane draws down, breaks into a dashed ghost segment, the neutral ring appears.
   Phones get the same story as a short horizontal route (CSS only). Reduced motion = drawn.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP;
  if (!S) return;
  const hero = S.$('.e4-hero');
  const end = hero && S.$('.e4-end', hero);
  const lane = hero && S.$('.e4-lane', hero);
  if (!hero || !end || !lane) return;
  function size() {
    const r = end.getBoundingClientRect();
    const h = Math.max(0, Math.round(r.top - hero.getBoundingClientRect().top + r.height / 2 - lane.offsetTop));
    hero.style.setProperty('--e4-lane', h + 'px');
    hero.style.setProperty('--e4-gap', Math.round(Math.min(170, h * 0.42)) + 'px');
  }
  size();
  S.onResize(size);
  requestAnimationFrame(() => requestAnimationFrame(() => hero.classList.add('is-lost')));
})();
