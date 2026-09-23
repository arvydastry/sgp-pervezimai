/* =========================================================
   SGP v2 · taisykles page JS (page-owned: pages-schedule-tracking-rules)
   Vertical Sticky Scrolling emulation: the index lane fills from stop to stop while the reader
   moves from one section head to the next; stops already passed get .is-passed
   (sgp.js data-spy sets .is-active + aria-current on the current one). Desktop (≥1000) only.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP; if (!S) return;
  S.$$('.tr-ban__list li').forEach((li, i) => li.style.setProperty('--xi', i));
  const box = S.$('.tr-index__box'), lane = S.$('.tr-index__lane', box || document);
  if (!box || !lane) return;
  const items = S.$$('.tr-index__list li', box);
  const secs = items.map(li => { const a = S.$('a', li); return a ? document.getElementById(a.getAttribute('href').slice(1)) : null; });
  if (!items.length || secs.some(s => !s)) return;
  let centers = [], last = '';

  function measure() {
    const b = box.getBoundingClientRect();
    centers = items.map(li => { const r = S.$('.sgp-ring', li).getBoundingClientRect(); return r.top + r.height / 2 - b.top; });
    lane.style.top = centers[0] + 'px';
    lane.style.bottom = 'auto';
    lane.style.height = Math.max(0, centers[centers.length - 1] - centers[0]) + 'px';
    last = '';
    update();
  }
  function update() {
    if (!S.desk()) { if (last !== 'off') { lane.style.removeProperty('--p'); items.forEach(li => li.classList.remove('is-passed')); last = 'off'; } return; }
    if (!centers.length) return;
    const mid = S.vh() * 0.5;
    const tops = secs.map(s => s.getBoundingClientRect().top);
    let i = -1; tops.forEach((t, k) => { if (t < mid) i = k; });
    let px = 0;
    if (i >= 0) {
      const n = centers.length;
      if (i >= n - 1) px = centers[n - 1] - centers[0];
      else {
        const f = S.clamp((mid - tops[i]) / Math.max(1, tops[i + 1] - tops[i]));
        px = centers[i] - centers[0] + f * (centers[i + 1] - centers[i]);
      }
    }
    const H = Math.max(1, centers[centers.length - 1] - centers[0]);
    const p = (px / H).toFixed(3);
    const key = p + '|' + i;
    if (key === last) return;
    last = key;
    lane.style.setProperty('--p', p);
    items.forEach((li, k) => li.classList.toggle('is-passed', k <= i));
  }
  S.onFrame(update);
  S.onResize(measure);
  measure();
})();
