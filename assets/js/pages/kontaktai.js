/* =========================================================
   SGP v2 · kontaktai.js (page-owned: pages-about-contact) — /kontaktai/ §6.9
   1. Header: the rail lane arrives at the terminus ring (lane height measured, ≥1000 px).
   2. Contact form (demo, shared data-demo-form does validation + success):
      choosing a route lights up the matching phone row („Greičiau – telefonu“) and
      pre-fills „Žinutės tema“ (only while the visitor has not typed their own subject).
   No network calls. Everything degrades to plain static content without JS.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP;
  if (!S) return;

  /* ---------- 1 · rail terminus in the header ---------- */
  const hero = S.$('.kt-hero');
  const term = hero && S.$('.kt-term', hero);
  const lane = hero && S.$('.kt-hero__lane', hero);
  if (hero && term && lane) {
    const size = () => {
      const h = term.getBoundingClientRect().top - hero.getBoundingClientRect().top + term.offsetHeight / 2 - lane.offsetTop;
      hero.style.setProperty('--kt-lane', Math.max(0, Math.round(h)) + 'px');
    };
    size();
    S.onResize(size);
    requestAnimationFrame(() => requestAnimationFrame(() => hero.classList.add('is-arrived')));
  }

  /* ---------- 2 · contact form helpers ---------- */
  const form = S.$('form[data-kt-form]');
  if (!form) return;
  const subject = S.$('input[name="tema"]', form);
  const rows = S.$$('[data-kt-tel]');
  let auto = true; /* subject is ours until the visitor types in it */

  if (subject) subject.addEventListener('input', () => { auto = subject.value.trim() === ''; });

  function update() {
    const r = S.$('input[name="kryptis"]:checked', form);
    const key = r ? r.dataset.route || '' : '';
    rows.forEach(a => a.classList.toggle('is-match', !!key && a.dataset.ktTel === key));
    if (!subject || !auto) return;
    const what = S.$$('input[name="vezame"]:checked', form).map(c => c.value);
    const parts = [];
    if (r && r.value !== 'Kita') parts.push(r.value);
    if (what.length) parts.push(what.join(', '));
    subject.value = parts.join(' · ');
    /* keep the shared validation state in sync with the programmatic value */
    if (subject.value) subject.dispatchEvent(new Event('input', { bubbles: true }));
    auto = true;
  }
  form.addEventListener('change', e => {
    if (e.target && (e.target.name === 'kryptis' || e.target.name === 'vezame')) update();
  });
})();
