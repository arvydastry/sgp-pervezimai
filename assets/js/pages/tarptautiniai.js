/* =========================================================
   SGP v2 · /pervezimo-paslaugos/tarptautiniai-pervezimai/ (page-owned) — runs after sgp.js, uses window.SGP
   1 · Image With Hotspots on the both-routes schematic: marker layer inside the SVG stage, disclosure tooltips
       (click/tap toggles, hover previews on fine pointers via CSS, Esc closes), M69 pulse via CSS
   2 · Sticky Scroll Pinned Sections → Overlapping (M65): chapters pin once their bottom meets the viewport bottom
       (≥1000 px, motion allowed); the covered chapter darkens as the next one slides over (shared rAF loop)
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP; if (!S) return;
  const { $, $$ } = S;

  /* ---------- 1 · hotspots ---------- */
  const hot = $('[data-hotspots]');
  if (hot) {
    /* the marker layer moves into the schematic's stage (.sgp-map__stage = the SVG box), so --x/--y are plain % */
    const stage = $('.sgp-map__stage', hot), layer = $('.tp-hot__layer', hot), grid = hot.closest('.tp-routes__grid');
    if (stage && layer) { stage.append(layer); layer.hidden = false; if (grid) grid.classList.add('has-hot'); }
    const spots = $$('.tp-hs', layer || hot);
    const set = (s, open) => {
      s.classList.toggle('is-open', open);
      const b = $('.tp-hs__btn', s); if (b) b.setAttribute('aria-expanded', String(open));
    };
    const closeAll = except => spots.forEach(s => { if (s !== except) set(s, false); });
    spots.forEach(s => {
      const b = $('.tp-hs__btn', s); if (!b) return;
      b.addEventListener('click', e => {
        e.stopPropagation();
        const open = !s.classList.contains('is-open');
        closeAll(s); set(s, open);
      });
    });
    document.addEventListener('click', e => { if (layer && !layer.contains(e.target)) closeAll(); });
    document.addEventListener('keydown', e => {
      if (e.key !== 'Escape') return;
      const o = spots.find(s => s.classList.contains('is-open'));
      if (o) { set(o, false); const b = $('.tp-hs__btn', o); if (b) b.focus(); }
    });
  }

  /* ---------- 2 · overlapping chapters (M65) ---------- */
  const over = $('[data-over]');
  if (over) {
    const chs = $$(':scope > .tp-ch', over);
    const measure = () => {
      const on = S.desk() && !S.reduce && chs.length > 1;
      over.classList.toggle('is-pin', on);
      chs.forEach(c => c.style.setProperty('--tp-h', c.offsetHeight + 'px'));
      if (!on) chs.forEach(c => c.style.removeProperty('--tp-dim'));
    };
    S.onResize(measure);
    measure();
    S.onFrame(() => {
      if (!over.classList.contains('is-pin')) return;
      const vh = S.vh();
      for (let i = 0; i < chs.length - 1; i++) {
        const nt = chs[i + 1].getBoundingClientRect().top;
        chs[i].style.setProperty('--tp-dim', (S.clamp((vh - nt) / vh) * 0.6).toFixed(3));
      }
    });
  }
})();
