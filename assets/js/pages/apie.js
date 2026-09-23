/* =========================================================
   SGP v2 · apie.js (page-owned: pages-about-contact) — /apie-imone/ §6.2
   03 Kelyje gallery = Salient Image Gallery → Flickity emulation (M68):
   Flickity 2.3.0 (vendor: flickity) · Touch & Total indicator „01 / 05“ · image parallax
   (drag-driven, ≥691 px, not under reduced motion) · drag indicator (fine pointers, ≥1000 px).
   Without Flickity (CDN blocked) the row stays a native scroll-snap list and the
   arrow buttons scroll it. Stacking cards, stops lane, reveals = shared sgp.js.
   ========================================================= */
(function () {
  'use strict';
  const S = window.SGP;
  if (!S) return;
  const track = S.$('#abGallery');
  if (!track) return;
  const wrap = track.closest('.ab-gal__wrap');
  const sec = track.closest('section');
  const now = S.$('[data-gal-now]', sec);
  const prev = S.$('[data-gal-prev]', sec);
  const next = S.$('[data-gal-next]', sec);
  const cells = S.$$('.ab-gal__cell', track);
  const imgs = cells.map(c => S.$('img', c));
  const pad = n => String(n).padStart(2, '0');

  /* lazy images inside an overflow:hidden slider never "intersect" — load them all once the row is near */
  S.io(sec, (e, o) => {
    if (!e.isIntersecting) return;
    imgs.forEach(i => { if (i) i.loading = 'eager'; });
    o.disconnect();
  }, { rootMargin: '600px 0px' });

  /* ---------- fallback: native scroll-snap row ---------- */
  if (typeof window.Flickity !== 'function') {
    const step = dir => {
      const c = cells[0]; if (!c) return;
      track.scrollBy({ left: dir * (c.getBoundingClientRect().width + 24), behavior: S.reduce ? 'auto' : 'smooth' });
    };
    if (prev) prev.addEventListener('click', () => step(-1));
    if (next) next.addEventListener('click', () => step(1));
    S.io(cells, e => {
      if (e.isIntersecting && e.intersectionRatio > 0.6 && now) now.textContent = pad(cells.indexOf(e.target) + 1);
    }, { root: track, threshold: [0.6] });
    return;
  }

  /* ---------- Flickity ---------- */
  const flkty = new window.Flickity(track, {
    cellAlign: 'center',
    wrapAround: true,
    prevNextButtons: false,
    pageDots: false,
    percentPosition: false,
    accessibility: true,
    dragThreshold: 6,
    selectedAttraction: S.reduce ? 1 : 0.035,
    friction: S.reduce ? 1 : 0.34
  });
  if (prev) prev.addEventListener('click', () => flkty.previous());
  if (next) next.addEventListener('click', () => flkty.next());
  flkty.on('change', i => { if (now) now.textContent = pad(i + 1); });

  /* image parallax inside the cells (Salient „Image Parallax“): image moves at ~ -12 % of the slide offset */
  const parMQ = window.matchMedia('(min-width:691px)');
  let par = false;
  function setPar() {
    par = !S.reduce && parMQ.matches;
    wrap.classList.toggle('is-par', par);
    if (!par) imgs.forEach(i => { if (i) i.style.transform = ''; });
    else parallax();
  }
  function parallax() {
    if (!par) return;
    const W = flkty.slideableWidth;
    flkty.slides.forEach((slide, i) => {
      const img = imgs[i]; if (!img) return;
      let x = slide.target + flkty.x;
      if (W) x = ((x % W) + W * 1.5) % W - W / 2;          /* wrapAround: nearest copy */
      const cw = slide.outerWidth || 1;
      const off = S.clamp(-x * 0.12, -cw * 0.12, cw * 0.12);
      img.style.transform = 'translate3d(' + off.toFixed(1) + 'px,0,0)';
    });
  }
  flkty.on('scroll', parallax);
  parMQ.addEventListener('change', setPar);
  setPar();
  S.onResize(() => { flkty.resize(); parallax(); });

  /* drag indicator (Salient carousel „drag indicator“): fine pointers, desktop, motion allowed */
  const drag = S.$('.ab-gal__drag', wrap);
  if (drag && S.fine && !S.reduce) {
    const vp = S.$('.flickity-viewport', track) || track;
    let raf = 0, px = 0, py = 0;
    const place = () => { raf = 0; drag.style.translate = px + 'px ' + py + 'px'; };
    vp.addEventListener('pointerenter', () => { if (S.desk()) wrap.classList.add('is-hover'); });
    vp.addEventListener('pointerleave', () => wrap.classList.remove('is-hover', 'is-down'));
    vp.addEventListener('pointermove', e => {
      if (!S.desk()) { wrap.classList.remove('is-hover'); return; }
      const r = wrap.getBoundingClientRect();
      px = e.clientX - r.left; py = e.clientY - r.top;
      wrap.classList.add('is-hover');
      if (!raf) raf = requestAnimationFrame(place);
    });
    vp.addEventListener('pointerdown', () => wrap.classList.add('is-down'));
    window.addEventListener('pointerup', () => wrap.classList.remove('is-down'));
  }
})();
