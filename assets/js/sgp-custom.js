/* sgp-custom.js — the ONLY custom JS (Theme Options → Custom JS (Head), pasted verbatim). Budget ≤ 30 lines. Plan §4.3 J-1 + J-2. */
(function (d, w) {
  var h = d.documentElement, rm = !!(w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches), opts = w.nectarOptions;
  /* J-1 reduced motion: flag the page and switch Salient's Lenis smooth scroll off before the theme reads nectarOptions */
  if (rm) {
    h.classList.add('sgp-rm');
    Object.defineProperty(w, 'nectarOptions', { configurable: true, get: function () { return opts; },
      set: function (v) { if (v) { v.smooth_scroll = 'false'; } opts = v; } });
    if (opts) { opts.smooth_scroll = 'false'; }
  }
  /* J-2 motion pause (WCAG 2.2.2): Button Extra Class sgp-motion-toggle lands on div.nectar-cta; the focusable
     element is its a.link_text[role=button]. Pauses/plays row videos (.nectar-video-wrap), Scrolling Text, Content Trail. */
  function link(b) { return b.querySelector('.link_text') || b; }
  function setPaused(on) {
    h.classList.toggle('sgp-paused', on);
    d.querySelectorAll('.nectar-video-wrap video, video.nectar-video-bg').forEach(function (v) { if (on) { v.pause(); } else if (v.currentSrc) { v.play().catch(function () {}); } });
    d.querySelectorAll('.sgp-motion-toggle').forEach(function (b) { link(b).setAttribute('aria-pressed', on ? 'true' : 'false'); });
  }
  function onToggle(e) {
    var b = e.target.closest ? e.target.closest('.sgp-motion-toggle') : null;
    if (b && (e.type === 'click' || e.key === ' ')) { e.preventDefault(); setPaused(!h.classList.contains('sgp-paused')); }
  }
  d.addEventListener('click', onToggle);
  d.addEventListener('keydown', onToggle);
  d.addEventListener('DOMContentLoaded', function () {
    d.querySelectorAll('.sgp-motion-toggle').forEach(function (b) { b = link(b); b.setAttribute('role', 'button'); b.setAttribute('aria-pressed', 'false'); });
    if (rm) { setPaused(true); }
  });
})(document, window);
