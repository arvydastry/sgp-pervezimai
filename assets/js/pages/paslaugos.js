/* =========================================================
   SGP v2 · /pervezimo-paslaugos/ (page-owned) — runs after sgp.js, uses window.SGP
   1 · ticket tilt = Fancy Box → Parallax Hover Effect (M67) — fine pointers, ≥1000 px, motion allowed
   2 · group cards: row hover/focus swaps the card image to that service (M64-style crossfade) + SD hover video (M33);
       a service photo is fetched only on the first hover/focus of its row (.is-warm)
   (3 · group index = shared: data-spy="scroll" + data-spy-count; anchor jumps land on the card's natural position)
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP; if (!S) return;
  const { $, $$ } = S;
  const motion = () => S.desk() && !S.reduce;

  /* ---------- 1 · tilt (M67) ---------- */
  if (S.fine && !S.reduce) {
    $$('.ps-tk[data-tilt]').forEach(el => {
      let raf = 0, px = 0, py = 0;
      const apply = () => {
        raf = 0;
        el.style.setProperty('--rx', (-py * 12).toFixed(2) + 'deg');
        el.style.setProperty('--ry', (px * 14).toFixed(2) + 'deg');
        el.style.setProperty('--mx', (px * 2).toFixed(3));
        el.style.setProperty('--my', (py * 2).toFixed(3));
      };
      el.addEventListener('pointermove', e => {
        if (!motion() || e.pointerType !== 'mouse') return;
        const r = el.getBoundingClientRect();
        px = S.clamp((e.clientX - r.left) / r.width) - 0.5;
        py = S.clamp((e.clientY - r.top) / r.height) - 0.5;
        el.classList.add('is-tilt');
        if (!raf) raf = requestAnimationFrame(apply);
      });
      el.addEventListener('pointerleave', () => {
        px = 0; py = 0; el.classList.remove('is-tilt');
        if (!raf) raf = requestAnimationFrame(apply);
      });
    });
  }

  /* ---------- 2 · group cards: media swap + hover video ---------- */
  const videoOK = () => S.fine && !S.reduce && !S.saveData && S.desk();
  function playLayer(layer) {
    const v = $('video', layer);
    if (!v || !videoOK()) return;
    if (!v.getAttribute('src') && v.dataset.src) v.src = v.dataset.src;
    const p = v.play();
    if (p) p.then(() => { if (layer.classList.contains('is-on')) layer.classList.add('is-playing'); }).catch(() => {});
  }
  function stopLayer(layer) {
    const v = $('video', layer);
    layer.classList.remove('is-playing');
    if (v && !v.paused) v.pause();
  }
  $$('.ps-grp').forEach(card => {
    const layers = $$('.ps-grp__layer', card);
    const base = layers.find(l => !l.dataset.for) || layers[0];
    const cap = $('[data-ps-cap]', card);
    let leaveT = 0, current = null;
    const show = (row) => {
      clearTimeout(leaveT);
      if (!S.desk()) return;
      const slug = row ? row.dataset.for : '';
      if (current === slug) return;
      current = slug;
      const target = (slug && layers.find(l => l.dataset.for === slug)) || base;
      const apply = () => {
        if (current !== slug) return;            /* the pointer moved on while the photo was loading */
        layers.forEach(l => {
          const on = l === target;
          l.classList.toggle('is-on', on);
          if (on) playLayer(l); else stopLayer(l);
        });
        if (cap) {
          cap.textContent = row ? row.dataset.cap + ' · ' + ($('.ps-row__t', row) || row).textContent : '';
          cap.classList.toggle('is-on', !!row);
        }
      };
      /* first use of a service layer: un-hide its lazy <img> (.is-warm, see paslaugos.css) so the browser fetches it now,
         keep the current photo on until it has loaded, then crossfade — photos of rows never hovered are never downloaded */
      const img = target !== base && $('img', target);
      target.classList.add('is-warm');
      if (img && !(img.complete && img.naturalWidth)) {
        img.addEventListener('load', apply, { once: true });
        img.addEventListener('error', apply, { once: true });
        return;
      }
      apply();
    };
    $$('.ps-row', card).forEach(row => {
      row.addEventListener('pointerenter', () => show(row));
      row.addEventListener('focus', () => show(row));
    });
    card.addEventListener('pointerleave', () => { leaveT = setTimeout(() => show(null), 140); });
    card.addEventListener('focusout', e => { if (!card.contains(e.relatedTarget)) show(null); });
  });

  /* 3 · group index: shared scroll spy (data-spy="scroll" + data-spy-count) and the shared anchor handler,
     which lands a sticky stacked card at its natural (un-stuck) position — see sgp.js §13 / §20 */
})();
