/* =====================================================================================
   demo.js — DEMO-ONLY helpers (never shipped): „Salient žymės“ developer overlay (reads
   data-salient), demo form confirmations (forms never send data), ?domina= pre-select
   (production: Fluent Forms {get.domina}), ?kodas=SGP-DEMO tracking result, cookie
   banner memory (production: Complianz).
   ===================================================================================== */
(function () {
  'use strict';
  const d = document, w = window;
  const $ = (s, c) => (c || d).querySelector(s), $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const store = { get: k => { try { return w.localStorage.getItem(k); } catch (e) { return null; } }, set: (k, v) => { try { w.localStorage.setItem(k, v); } catch (e) { /* private mode */ } } };

  /* ---- „Salient žymės“: one fixed layer of labels placed from each tagged element's rect ---- */
  const btn = $('#sgp-tagbtn');
  const tags = { on: false, layer: null, list: [], timer: 0 };
  const shown = el => (el.checkVisibility ? el.checkVisibility({ opacityProperty: false, visibilityProperty: true }) : el.offsetParent !== null);
  function build() {
    const layer = tags.layer = d.createElement('div');
    layer.className = 'sgp-stags'; layer.setAttribute('aria-hidden', 'true');
    tags.list = $$('[data-salient]').filter(el => !el.closest('#slide-out-widget-area, .sub-menu')).map(el => {
      const s = d.createElement('span'); s.className = 'sgp-stag'; s.textContent = el.dataset.salient; layer.appendChild(s);
      return { el, s, w: 0, h: 0 };
    });
    d.body.appendChild(layer);
    tags.list.forEach(t => { t.w = t.s.offsetWidth; t.h = t.s.offsetHeight; });
  }
  function place() {
    if (!tags.on || !tags.layer) return;
    const vw = d.documentElement.clientWidth, vh = w.innerHeight, M = 8, placed = [];
    const rects = tags.list.map(t => (shown(t.el) ? t.el.getBoundingClientRect() : null));
    tags.list.forEach((t, i) => {
      const r = rects[i], on = !!r && r.width + r.height > 0 && r.bottom > 0 && r.top < vh;
      t.s.style.visibility = on ? '' : 'hidden';
      if (!on) return;
      const x = Math.max(M, Math.min(r.left + M, vw - t.w - M));
      let y = r.top + M;
      if (y < M) y = Math.min(M, r.bottom - t.h - M);
      for (let n = 0; n < 60; n++) {
        const hit = placed.find(p => x < p.x + p.w && x + t.w > p.x && y < p.y + p.h && y + t.h > p.y);
        if (!hit) break;
        y = hit.y + hit.h + 4;
      }
      placed.push({ x, y, w: t.w, h: t.h });
      t.s.style.transform = `translate(${Math.round(x)}px,${Math.round(y)}px)`;
    });
  }
  if (btn) {
    btn.addEventListener('click', () => {
      tags.on = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(tags.on));
      clearInterval(tags.timer);
      if (tags.layer) { tags.layer.remove(); tags.layer = null; tags.list = []; }
      if (!tags.on) return;
      build(); place();
      tags.timer = setInterval(place, 400);
    });
    w.addEventListener('scroll', () => { if (tags.on) w.requestAnimationFrame(place); }, { passive: true });
  }

  /* ---- demo forms: validate, never send, show the confirmation text ---- */
  /* the error text joins the field's description only while it is shown (as Fluent Forms inserts its error nodes) */
  const describe = (g, input, bad) => {
    const err = input && $('.error', g);
    if (!err) return;
    if (!err.id) err.id = `${input.id || 'f'}-err`;
    if (input.dataset.describedby === undefined) input.dataset.describedby = input.getAttribute('aria-describedby') || '';   /* helper text stays */
    const ids = [input.dataset.describedby, bad ? err.id : ''].filter(Boolean).join(' ');
    if (ids) input.setAttribute('aria-describedby', ids); else input.removeAttribute('aria-describedby');
  };
  $$('form[data-demo-form]').forEach(f => {
    f.setAttribute('novalidate', '');
    f.addEventListener('submit', e => {
      e.preventDefault();
      let ok = true;
      $$('.ff-el-group', f).forEach(g => {
        const input = $('input, select, textarea', g);
        const bad = input && !input.checkValidity();
        g.classList.toggle('ff-el-is-error', !!bad);
        if (input) input.setAttribute('aria-invalid', bad ? 'true' : 'false');
        describe(g, input, bad);
        if (bad && ok) { ok = false; input.focus(); }
      });
      if (!ok) return;
      if (f.dataset.demoForm === 'tracking') {
        const code = ($('input[name="kodas"]', f) || {}).value || '';
        const u = new URL(f.getAttribute('action') || location.href, location.href);
        u.searchParams.set('kodas', code.trim()); u.hash = f.dataset.target || 'rezultatas';
        location.href = u.toString();
        return;
      }
      const okMsg = $('.ff-message-success', f.parentElement);
      f.hidden = true;
      if (okMsg) { okMsg.hidden = false; okMsg.focus(); }
    });
    $$('input, select, textarea', f).forEach(i => i.addEventListener('input', () => { const g = i.closest('.ff-el-group'); if (g && i.checkValidity()) { g.classList.remove('ff-el-is-error'); i.setAttribute('aria-invalid', 'false'); describe(g, i, false); } }));
  });
  /* ?domina=<service name> pre-selects „Kas Jus domina?“ (production: Fluent Forms default value {get.domina}) */
  const q = new URLSearchParams(location.search);
  const domina = q.get('domina');
  if (domina) $$('select[name="domina"]').forEach(s => { const o = Array.from(s.options).find(x => x.text === domina || x.value === domina); if (o) s.value = o.value; });
  /* ?kodas=SGP-DEMO → demo tracking result callout ([data-demo-result]) */
  const kodas = (q.get('kodas') || '').trim();
  $$('[data-demo-result]').forEach(box => {
    if (!kodas) return;
    const ok = kodas.toUpperCase() === 'SGP-DEMO';
    const good = $('[data-demo-result-ok]', box), bad = $('[data-demo-result-none]', box);
    box.hidden = false;
    if (good) good.hidden = !ok;
    if (bad) bad.hidden = ok;
    $$('[data-demo-code]', box).forEach(x => { x.textContent = kodas; });
  });

  /* ---- cookie banner (production: Complianz) ---- */
  const cb = $('.cmplz-cookiebanner');
  if (cb) {
    $$('[data-cookie]', cb).forEach(b => b.addEventListener('click', () => { store.set('sgp-cookies', b.dataset.cookie); cb.hidden = true; }));
    if (!store.get('sgp-cookies')) cb.hidden = false;
    /* „Keisti slapukų nustatymus“ re-opens the banner (production: Complianz [cmplz-manage-consent]) */
    $$('.cmplz-manage-consent').forEach(a => a.addEventListener('click', e => {
      e.preventDefault();
      cb.hidden = false;
      const first = $('button', cb);
      if (first) first.focus();
    }));
  }
})();
