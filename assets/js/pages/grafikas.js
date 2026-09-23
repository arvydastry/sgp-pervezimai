/* =========================================================
   SGP v2 · pervezimu-grafikas page JS (page-owned: pages-schedule-tracking-rules)
   The table route codes are split-flap tiles from the shared [sgp_grafikas variant="table"] (sgp.js flaps them
   once, desktop, when each tab panel first comes into view). The 02 „Laiko juosta“ lane chart is the shared
   {{grafikas:lane}} variant (build time + sgp.js re-render for the visitor's date); this file only
   1) lays out the stop labels (keep them inside the track, lift one above the lane when it would touch its neighbour)
   2) starts the lane draw when the chart enters.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP; if (!S) return;
  const fig = S.$('[data-sched="lane"]');
  if (!fig) return;
  const span = (() => { const w = S.$$('.gr-lane__tick[data-wk]', fig); return w.length ? (+w[w.length - 1].dataset.wk + 7) : 21; })();

  /* label placement: keep labels inside the track and lift a label above the lane when it would touch its neighbour */
  function layout() {
    const tr = S.$('.gr-lane__track', fig); if (!tr) return;
    const W = tr.clientWidth;
    /* week ticks: every week when there is room, otherwise every second week */
    const step = W / (span / 7) < 74 ? 14 : 7;
    const t0 = S.$('.gr-lane__tick--0', fig), minX = (t0 ? t0.offsetWidth : 80) + 40;
    S.$$('.gr-lane__tick[data-wk]', fig).forEach(t => { const x = +t.dataset.wk / span; t.hidden = (+t.dataset.wk % step) !== 0 || x > 0.95 || x * W < minX; });
    S.$$('.gr-lane__track', fig).forEach(track => {
      let prev = null;
      S.$$('.gr-lane__stop', track).forEach(st => {
        st.classList.remove('is-up', 'is-edge-l', 'is-edge-r');
        const lbl = S.$('.gr-lane__lbl', st), w = lbl.offsetWidth, x = parseFloat(st.style.getPropertyValue('--x')) * W;
        if (x < w / 2 + 2) st.classList.add('is-edge-l'); else if (W - x < w / 2 + 2) st.classList.add('is-edge-r');
        if (prev && !prev.up && x - prev.x < (prev.w + w) / 2 + 14) st.classList.add('is-up');
        prev = { x, w, up: st.classList.contains('is-up') };
      });
    });
  }
  layout();
  S.onResize(layout);

  if (S.reduce) fig.classList.add('in');
  else S.io(fig, (e, o) => { if (e.isIntersecting) { fig.classList.add('in'); o.disconnect(); } }, { rootMargin: '0px 0px -18% 0px' });
})();
