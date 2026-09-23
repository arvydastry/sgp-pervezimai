/* =========================================================
   SGP v2 · siuntos-sekimas page JS (page-owned: pages-schedule-tracking-rules)
   DEMO ONLY — no network requests. Production replaces the .sk-screen states with
   <iframe src="https://siuntos.sgp-pervezimai.lt/sekimas.php?embed=1&kodas=…">.
   States: idle → load → none („Toks siuntos kodas neegzistuoja!“ + demo note) | found (only the sample code SGP-DEMO).
   Empty submit is handled by sgp.js (data-track) with the verbatim „Neįvestas siuntos kodas!“; a non-empty code
   arrives as the cancelable `sgp:track` event (sgp.js §14) — this page cancels the GET and runs the demo lookup.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP; if (!S) return;
  const form = S.$('.sk-track'), screen = S.$('[data-sk-screen]');
  if (!form || !screen) return;
  const input = S.$('input', form);
  const live = S.$('[data-sk-live]', screen), codeEl = S.$('[data-sk-code]', screen);
  const states = {}; S.$$('[data-sk-state]', screen).forEach(el => { states[el.dataset.skState] = el; });
  const DEMO = 'SGP-DEMO';
  const MSG_EMPTY = 'Neįvestas siuntos kodas!', MSG_NONE = 'Toks siuntos kodas neegzistuoja!';
  const MSG_DEMO = 'Demonstracinė versija – paieška veikia tik tikroje svetainėje.';   /* §8.1 p. 25 — a real code is never presented as non-existent without it */
  const norm = v => String(v || '').trim().toUpperCase().replace(/\s+/g, '');
  let timer = 0;

  /* stagger indexes for the found state */
  S.$$('.sk-trip__stop', screen).forEach((li, i) => li.style.setProperty('--k', i));
  S.$$('.sk-log li', screen).forEach((li, i) => li.style.setProperty('--k', i));

  function show(name, code) {
    screen.dataset.state = name;
    Object.keys(states).forEach(k => {
      const el = states[k], on = k === name;
      el.hidden = !on; el.classList.remove('is-in');
      if (on) { void el.offsetWidth; el.classList.add('is-in'); }
    });
    if (code !== undefined) codeEl.textContent = code || '—';
  }
  const setError = msg => S.track.error(form, msg);   /* shared field error (msg omitted = the verbatim empty-code text) */
  const clearError = () => S.track.clear(form);
  const resetUrl = () => { if (location.search && history.replaceState) history.replaceState(null, '', location.pathname); };
  function reveal() {
    /* bring the result into view when it is below the fold (never on load without a code) */
    const r = screen.getBoundingClientRect();
    if (r.top > innerHeight * 0.55 || r.bottom < 0) {
      const off = -((S.$('.sgp-bar') || { offsetHeight: 64 }).offsetHeight + 24);
      if (S.lenis) S.lenis.scrollTo(screen, { offset: off, duration: 1.1 });
      else scrollTo({ top: r.top + scrollY + off, behavior: S.reduce ? 'auto' : 'smooth' });
    }
  }
  function search(raw, opts) {
    const code = norm(raw);
    clearTimeout(timer);
    if (!code) { show('idle', ''); setError(); live.textContent = MSG_EMPTY; resetUrl(); return; }
    input.value = code;
    if (history.replaceState) history.replaceState(null, '', '?kodas=' + encodeURIComponent(code));
    show('load', code); live.textContent = 'Ieškoma…';
    if (!opts || opts.scroll !== false) reveal();
    timer = setTimeout(() => {
      if (code === DEMO || code === 'SGPDEMO') {
        clearError(); show('found', DEMO);
        live.textContent = 'Siunta rasta – demonstracinis pavyzdys: Lietuva → Ispanija, kelyje.';
      } else {
        setError(MSG_NONE); show('none', code); live.textContent = MSG_NONE + ' ' + MSG_DEMO;
      }
    }, S.reduce ? 0 : 900);
  }

  /* sgp.js dispatches sgp:track on every submit: an empty code is already prevented + flagged there */
  form.addEventListener('sgp:track', e => {
    if (!norm(e.detail.code)) { clearTimeout(timer); show('idle', ''); live.textContent = MSG_EMPTY; resetUrl(); return; }
    e.preventDefault();                                 /* cancels the GET: demo lookup instead */
    search(e.detail.code);
  });

  /* demo helper: fill the sample code and search */
  S.$$('[data-sk-try]').forEach(b => b.addEventListener('click', () => {
    input.value = b.dataset.skTry; clearError(); search(input.value);
  }));

  /* ?kodas= (e.g. from the home strip) → run the search on load */
  const q = new URLSearchParams(location.search).get('kodas');
  if (q !== null) {
    if (norm(q)) { input.value = norm(q); setTimeout(() => search(q), S.reduce ? 0 : 450); }
    else { setError(); }
  }
})();
