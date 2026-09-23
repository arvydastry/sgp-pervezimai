/* =========================================================
   SGP v2 · privatumo-politika.js (page-owned: pages-about-contact) — /privatumo-politika/ §6.10
   1. Mini-TOC lane = reading progress through the document (--pp-p, inside the shared rAF loop).
      Active stop + ring fill = shared data-spy.
   2. „Keisti slapukų nustatymus“ re-opens the shared cookie bar (production: consent plugin's
      „Manage consent“). Demo only — the stored choice lives in localStorage (try/catch).
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP;
  if (!S) return;

  /* ---------- 1 · reading progress ---------- */
  const toc = S.$('.pp-toc');
  const main = S.$('.pp-doc__main');
  if (toc && main) {
    const parts = S.$$('.pp-part', main);
    const first = parts[0], last = parts[parts.length - 1];
    const upd = () => {
      if (!first || !last) return;
      const a = first.getBoundingClientRect().top, b = last.getBoundingClientRect().top;
      const line = S.vh() * 0.22; /* reading line just under the header */
      const p = b === a ? 0 : S.clamp((line - a) / (b - a));
      toc.style.setProperty('--pp-p', p.toFixed(3));
    };
    S.onFrame(upd);
    S.onResize(upd);
    upd();
  }

  /* ---------- 2 · re-open the cookie bar (shared SGP.cookie.open: forgets the stored choice, shows + focuses the bar) ---------- */
  const btn = S.$('[data-pp-cookie]');
  if (btn && S.cookie) btn.addEventListener('click', () => S.cookie.open());
})();
