/* =========================================================
   SGP v2 · home.js (page-owned) — demo emulation of Salient
   Sticky Content Sections → Horizontal Scrolling for the services road (M30).
   Off below 1000 px width, below 620 px height and under reduced motion
   (then the road is a vertical lane / horizontal scroll-snap list).
   Rail stops, counter and hover videos are shared (sgp.js: data-stops, data-hover-video).
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP;
  if (!S) return;
  const svc = document.getElementById('paslaugos');
  const pin = document.getElementById('svcPin');
  const track = document.getElementById('svcTrack');
  if (!svc || !pin || !track) return;

  let over = 0, pinned = false;

  function layout() {
    track.style.transform = '';
    pinned = S.desk() && !S.reduce && S.vh() >= 620;
    svc.classList.toggle('is-pinned', pinned);
    if (pinned) {
      const last = track.lastElementChild;
      const padR = parseFloat(getComputedStyle(track).paddingRight) || 24;
      over = Math.max(0, last.getBoundingClientRect().right - track.getBoundingClientRect().left + padR - document.documentElement.clientWidth);
      pin.style.height = (S.vh() + over) + 'px';
    } else {
      over = 0;
      pin.style.height = '';
    }
    update();
  }

  function update() {
    if (!pinned) return;
    const b = pin.getBoundingClientRect();
    const p = over ? S.clamp(-b.top / over) : 0;
    track.style.transform = 'translate3d(' + (-p * over).toFixed(1) + 'px,0,0)';
  }

  S.onFrame(update);
  S.onResize(layout);
  layout();

  /* keyboard: bring a focused card into view inside the pinned track */
  track.addEventListener('focusin', function (e) {
    if (!pinned || !over) return;
    const c = e.target.closest('.sgp-svc, .h-svc__end');
    if (!c) return;
    const want = S.clamp((c.offsetLeft - S.vw() * 0.3) / over) * over;
    const top = pin.getBoundingClientRect().top + window.scrollY + want;
    if (S.lenis) S.lenis.scrollTo(top, { immediate: true });
    else window.scrollTo(0, top);
  });
})();
