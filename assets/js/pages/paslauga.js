/* =========================================================
   SGP v2 · paslauga.js (page-owned: pages-service-template) — service detail template (§6.5)
   1 · „Kas Jus domina?“ pre-selects this service (GS-Arrival) when the URL has no ?domina=
   2 · T4 Privalumai — sticky media swap + counter (M64)
   3 · Keleiviai „Patogumai“ — Image With Hotspots (§4.26, M69): hover / tap / keyboard, list ⇄ marker link
   4 · Gyvūnai „Prieš kelionę“ — demo documents checklist (per visitor, localStorage in try/catch)
   Shared behaviour (reveal, rail, submenu spy incl. „nothing active above chapter 1“, accordions, stacking, videos) lives in sgp.js.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP;
  if (!S) return;
  const d = document;

  /* ---------- 1 · form pre-select ---------- */
  const hero = S.$('[data-svc]');
  const sel = S.$('select[data-domina]');
  if (hero && sel && !new URLSearchParams(location.search).get('domina')) {
    const o = [...sel.options].find(x => x.text === hero.dataset.svc);
    if (o) sel.value = o.value || o.text;
  }

  /* ---------- 2 · sticky media swap (M64) ---------- */
  const why = S.$('.sv-why');
  if (why) {
    const blocks = S.$$('.sv-why__b', why);
    const imgs = S.$$('.sv-why__img', why);
    const count = S.$('[data-why-count]', why);
    const frame = S.$('.sv-why__frame', why);
    let cur = -1;
    const set = i => {
      if (i === cur) return;
      cur = i;
      const b = blocks[i];
      blocks.forEach((x, j) => x.classList.toggle('is-active', j === i));
      const m = b ? +b.dataset.whyM : 0;
      imgs.forEach(x => x.classList.toggle('is-active', +x.dataset.whyM === m));
      if (count) count.textContent = String(i + 1).padStart(2, '0');
      if (frame) frame.style.setProperty('--why-p', ((i + 1) / blocks.length).toFixed(3));
    };
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) set(blocks.indexOf(e.target));
    }), { rootMargin: '-42% 0px -48% 0px' });
    blocks.forEach(b => io.observe(b));
    set(0);
  }

  /* ---------- 3 · Image With Hotspots ---------- */
  const hs = S.$('.sv-hs');
  if (hs) {
    const marks = S.$$('.sv-hs__m', hs);
    const tips = S.$$('.sv-hs__tip', hs);
    const items = S.$$('[data-hs-item]', hs);
    let pinned = null, quiet = false;
    const tip = n => tips.find(t => t.dataset.hsTip === n);
    const mark = n => marks.find(m => m.dataset.hs === n);
    const show = (n, on) => {
      const m = mark(n), t = tip(n), li = items.find(x => x.dataset.hsItem === n);
      if (t) {
        if (on) { /* keep the tooltip inside the viewport (phones: markers near the edges) */
          t.style.setProperty('--dx', '0px');
          const r = t.getBoundingClientRect(), vw = d.documentElement.clientWidth, pad = 12;
          const dx = r.left < pad ? pad - r.left : (r.right > vw - pad ? vw - pad - r.right : 0);
          t.style.setProperty('--dx', Math.round(dx) + 'px');
        }
        t.classList.toggle('is-open', on);
      }
      if (m) { m.classList.toggle('is-hot', on); m.setAttribute('aria-expanded', String(on)); }
      if (li) li.classList.toggle('is-hot', on);
    };
    const closeAll = except => marks.forEach(m => { if (m.dataset.hs !== except) show(m.dataset.hs, false); });
    marks.forEach((m, i) => {
      const n = m.dataset.hs, t = tip(n);
      m.style.setProperty('--d', (i * 0.25) + 's');
      if (t && parseFloat(t.style.getPropertyValue('--y')) < 32) t.classList.add('is-low');
      m.addEventListener('click', () => {
        const open = pinned !== n;
        closeAll(n); pinned = open ? n : null; show(n, open);
      });
      m.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse' && !pinned) { closeAll(n); show(n, true); } });
      m.addEventListener('pointerleave', e => { if (e.pointerType === 'mouse' && !pinned) show(n, false); });
      m.addEventListener('focus', () => { if (!pinned && !quiet) { closeAll(n); show(n, true); } });
      m.addEventListener('blur', () => { if (!pinned) show(n, false); });
    });
    items.forEach(li => {
      const n = li.dataset.hsItem;
      li.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse' && !pinned) { closeAll(n); show(n, true); } });
      li.addEventListener('pointerleave', e => { if (e.pointerType === 'mouse' && !pinned) show(n, false); });
    });
    d.addEventListener('keydown', e => { if (e.key === 'Escape' && (pinned || tips.some(t => t.classList.contains('is-open')))) { const n = pinned; pinned = null; closeAll(); if (n) { const m = mark(n); if (m) { quiet = true; m.focus(); quiet = false; } } } });
    d.addEventListener('pointerdown', e => { if (pinned && !e.target.closest('.sv-hs__m, .sv-hs__tip')) { pinned = null; closeAll(); } });
    /* markers pulse twice when the figure enters (M69) */
    S.io([hs], (e, o) => { if (e.isIntersecting) { hs.classList.add('in'); o.unobserve(hs); } }, { rootMargin: '0px 0px -25% 0px' });
  }

  /* ---------- 4 · documents checklist (demo, per visitor) ---------- */
  const chk = S.$('.sv-chk');
  if (chk) {
    const boxes = S.$$('input[data-chk]', chk);
    const cnt = S.$('[data-chk-count]', chk), bar = S.$('[data-chk-bar]', chk), status = S.$('[data-chk-status]', chk);
    const KEY = 'sgp-gyvunai-pries-kelione';
    let saved = [];
    try { saved = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { saved = []; }
    const upd = announce => {
      const done = boxes.filter(b => b.checked);
      boxes.forEach(b => { const it = b.closest('.sv-chk__item'); if (it) it.classList.toggle('is-done', b.checked); });
      if (cnt) cnt.textContent = String(done.length);
      if (bar) bar.style.setProperty('--p', (done.length / boxes.length).toFixed(3));
      if (announce && status) status.textContent = 'Pasiruošta ' + done.length + ' iš ' + boxes.length;
      try { localStorage.setItem(KEY, JSON.stringify(done.map(b => b.dataset.chk))); } catch (e) { /* storage blocked */ }
    };
    boxes.forEach(b => {
      if (Array.isArray(saved) && saved.includes(b.dataset.chk)) b.checked = true;
      b.addEventListener('change', () => upd(true));
    });
    upd(false);
  }
})();
