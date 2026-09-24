/* =====================================================================================
   emul.js — EMULATION of Salient 18.2.1 front-end behaviour for the static SGP demo.
   NOT SHIPPED: in WordPress, Salient + Salient Core provide all of this natively.
   Own code (no theme code copied); timings/easings/trigger lines = docs/salient-18-2-1-parinktys.md §3.
   Behaviour is keyed on the data-* attributes of docs/build-notes/kit.md (Kit API).
   Modules: 1 core · 2 header/off-canvas · 3 rows & columns · 4 typography · 5 buttons & media ·
            6 lists & cards · 7 toggles/tabs/submenu · 8 sticky content sections · 9 init
   ===================================================================================== */
(function () {
  'use strict';
  /* ================= 1 · core: helpers, one rAF scroll engine, trigger lines, Lenis ================= */
  const d = document, w = window, root = d.documentElement;
  const $ = (s, c) => (c || d).querySelector(s);
  const $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const opts = w.nectarOptions || {};
  const MQ = {
    desk: w.matchMedia('(min-width:1000px)'), phone: w.matchMedia('(max-width:690px)'),
    fine: w.matchMedia('(hover:hover) and (pointer:fine)'), rm: w.matchMedia('(prefers-reduced-motion: reduce)')
  };
  const RM = () => root.classList.contains('sgp-rm') || MQ.rm.matches;
  const device = () => (MQ.desk.matches ? 'desktop' : MQ.phone.matches ? 'phone' : 'tablet');
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const mix = (a, b, t) => a + (b - a) * t;
  const num = (v, f) => { const n = parseFloat(v); return Number.isFinite(n) ? n : (f || 0); };
  const isSafari = /^((?!chrome|android|crios|fxios).)*safari/i.test(navigator.userAgent);
  const isTouch = ('ontouchstart' in w) || navigator.maxTouchPoints > 0;
  const SVGNS = 'http://www.w3.org/2000/svg';
  let vh = w.innerHeight, vw = root.clientWidth, uid = 0;
  const nextId = p => `${p}-${++uid}`;
  const PARALLAX = { fast: 0.2, medium_fast: 0.28, medium: 0.4, slow: 0.6, very_subtle: 0.12, minimum: 0.09, subtle: 0.2, regular: 0.28, high: 0.6 };

  /* one frame loop: every handler reads in phase 1 and returns a writer for phase 2 (no layout thrash) */
  const scrollFns = [], resizeFns = [];
  let ticking = false;
  function frame() {
    ticking = false;
    const y = w.scrollY, writers = [];
    for (const fn of scrollFns) { const wr = fn(y); if (typeof wr === 'function') writers.push(wr); }
    for (const wr of writers) wr();
  }
  const requestTick = () => { if (!ticking) { ticking = true; w.requestAnimationFrame(frame); } };
  const onScroll = fn => { scrollFns.push(fn); };
  const onResize = fn => { resizeFns.push(fn); };
  w.addEventListener('scroll', requestTick, { passive: true });
  let rzT = 0;
  w.addEventListener('resize', () => {
    clearTimeout(rzT);
    rzT = setTimeout(() => { vh = w.innerHeight; vw = root.clientWidth; resizeFns.forEach(f => f()); requestTick(); }, 120);
  });
  /* near-viewport flag for scroll-linked elements (skips work off-screen) */
  const visIO = new IntersectionObserver(es => es.forEach(e => { e.target._near = e.isIntersecting; if (e.isIntersecting) requestTick(); }), { rootMargin: '40% 0px' });
  const watchNear = el => { el._near = false; visIO.observe(el); };
  /* progress of an element through a viewport range: a/b = % of the viewport the top has travelled (Salient "Viewport Trigger Offset") */
  const rangeProgress = (rect, a, b) => {
    const start = vh * (1 - a / 100), end = vh * (1 - b / 100);
    return end === start ? (rect.top <= end ? 1 : 0) : clamp((start - rect.top) / (start - end), 0, 1);
  };

  /* trigger lines (Waypoints offsets): cb fires once when the element top crosses `line` % of the viewport,
     or immediately if the element is already above the viewport (page reloaded mid-way) */
  const trigIO = {};
  function onEnter(el, line, cb) {
    line = line || 88;
    if (!trigIO[line]) {
      trigIO[line] = new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting || e.boundingClientRect.bottom < 0) {
          trigIO[line].unobserve(e.target);
          const fn = e.target._enter; e.target._enter = null;
          if (fn) fn(e.target);
        }
      }), { rootMargin: `0px 0px -${100 - line}% 0px`, threshold: 0 });
    }
    const prev = el._enter;
    el._enter = prev ? t => { prev(t); cb(t); } : cb;
    trigIO[line].observe(el);
  }
  const delayOf = el => num(el.dataset.delay, 0);
  /* Waypoint offset 'bottom-in-view' (Animated Text, Divider, Highlighted Text): fires once the element's BOTTOM edge is inside
     the viewport (or already above it). Hidden elements (0 × 0, e.g. in a closed tab) wait until they are laid out. */
  const pendingBottom = [];
  function onBottomIn(el, cb) {
    if (!pendingBottom.length && !onBottomIn.bound) {
      onBottomIn.bound = true;
      onScroll(() => {
        if (!pendingBottom.length) return null;
        const hit = [];
        for (let i = pendingBottom.length - 1; i >= 0; i--) {
          const p = pendingBottom[i], r = p.el.getBoundingClientRect();
          if ((r.width || r.height) && r.bottom <= vh) { hit.push(p); pendingBottom.splice(i, 1); }
        }
        return hit.length ? () => hit.forEach(p => p.cb(p.el)) : null;
      });
    }
    pendingBottom.push({ el, cb });
  }

  /* ---- Smooth Scrolling (Lenis 1.1.13): lerp = 0.17 × (1.5 − strength/100); desktop, never Safari/touch ---- */
  let lenis = null;
  function initLenis() {
    if (opts.smooth_scroll !== 'true' || RM() || isSafari || isTouch || !MQ.fine.matches || typeof w.Lenis !== 'function') return;
    const strength = clamp(num(opts.smooth_scroll_strength, 50), 1, 100);
    lenis = new w.Lenis({ lerp: 0.17 * (1.5 - strength / 100), smoothWheel: true });
    lenis.on('scroll', requestTick);
    const raf = t => { lenis.raf(t); w.requestAnimationFrame(raf); };
    w.requestAnimationFrame(raf);
    root.classList.add('lenis');
  }
  const headerOffset = () => { const h = $('#header-outer'); return (h ? Math.min(h.offsetHeight, 90) : 70) + 16; };
  function scrollToEl(el, instant) {
    if (!el) return;
    if (lenis) { lenis.scrollTo(el, { offset: -headerOffset(), immediate: !!instant }); return; }
    const y = el.getBoundingClientRect().top + w.scrollY - headerOffset();
    w.scrollTo({ top: y, behavior: RM() || instant ? 'auto' : 'smooth' });
  }
  /* One Page Scrolling: animated anchor links to Row IDs */
  function initAnchors() {
    d.addEventListener('click', e => {
      const a = e.target.closest ? e.target.closest('a[href*="#"]') : null;
      if (!a || e.defaultPrevented || a.target === '_blank' || e.metaKey || e.ctrlKey) return;
      const url = new URL(a.href, location.href);
      if (url.pathname !== location.pathname || !url.hash || url.hash === '#') return;
      const target = d.getElementById(decodeURIComponent(url.hash.slice(1)));
      if (!target) return;
      e.preventDefault();
      if (d.body.classList.contains('off-canvas-open')) closeOffCanvas(false);
      scrollToEl(target);
      history.pushState(null, '', url.hash);
      if (target.matches('main, [tabindex]')) target.focus({ preventScroll: true });
    });
  }

  /* ================= 2 · header: transparency, resize on scroll, mega menu, off-canvas ================= */
  const HO = $('#header-outer');
  function initHeader() {
    if (!HO) return;
    const transparent = HO.dataset.transparentHeader === 'true', resize = HO.dataset.headerResize === '1';
    let last = null;
    onScroll(y => {
      const down = y > 1;
      if (down === last) return null;
      last = down;
      return () => {
        HO.classList.toggle('scrolled-down', down);
        HO.classList.toggle('small-nav', resize && down);
        HO.classList.toggle('transparent', transparent && !down);
        root.style.setProperty('--submenu-top', down ? 'var(--header-h-small)' : 'calc(var(--header-h) + var(--ticker-h))');
      };
    });
    /* Dropdown / Mega Menu (hover + keyboard), Animation: Fade In Up */
    $$('.sf-menu > li').forEach(li => {
      const sub = $(':scope > .sub-menu', li), a = $(':scope > a', li);
      if (!sub || !a) return;
      /* popup semantics only where the dropdown exists (desktop ≥ 1000 px); on phones the item is a plain link */
      const aria = () => {
        if (MQ.desk.matches) { a.setAttribute('aria-haspopup', 'true'); a.setAttribute('aria-expanded', String(li.classList.contains('sfHover'))); }
        else { a.removeAttribute('aria-haspopup'); a.removeAttribute('aria-expanded'); }
      };
      aria(); MQ.desk.addEventListener('change', aria);
      let t = 0;
      const open = () => {
        if (!MQ.desk.matches) return;
        clearTimeout(t);
        $$('.sf-menu > li.sfHover').forEach(o => { if (o !== li) close(o, true); });
        li.classList.add('sfHover'); aria();
        if (li.classList.contains('megamenu')) HO.classList.add('megamenu-open');
      };
      const close = (el, now) => {
        const it = el || li;
        const run = () => { it.classList.remove('sfHover'); if (MQ.desk.matches) $(':scope > a', it).setAttribute('aria-expanded', 'false'); if (!$('.sf-menu > li.megamenu.sfHover')) HO.classList.remove('megamenu-open'); };
        if (now) run(); else { clearTimeout(t); t = setTimeout(run, 180); }
      };
      li.addEventListener('mouseenter', open);
      li.addEventListener('mouseleave', () => close());
      li.addEventListener('focusin', open);
      li.addEventListener('focusout', e => { if (!li.contains(e.relatedTarget)) close(null, true); });
      li.addEventListener('keydown', e => { if (e.key === 'Escape') { close(null, true); a.focus(); } });
    });
  }

  /* Off Canvas Menu → Fullscreen Cover Split (phones/tablets): items rise .85s with 20 ms stagger, right side +.3s */
  const OC = $('#slide-out-widget-area');
  const OCBtn = $('.slide-out-widget-area-toggle button');
  let ocReturn = null;
  function focusables(c) { return $$('a[href],button:not([disabled]),input,select,textarea,[tabindex]:not([tabindex="-1"])', c).filter(el => el.offsetParent !== null || el === OCBtn); }
  function openOffCanvas() {
    if (!OC) return;
    ocReturn = d.activeElement;
    d.body.classList.add('off-canvas-open');
    OC.removeAttribute('inert'); OC.setAttribute('aria-hidden', 'false');
    OCBtn.setAttribute('aria-expanded', 'true'); OCBtn.setAttribute('aria-label', 'Uždaryti meniu');
    if (lenis) lenis.stop();
    setTimeout(() => { const f = $('.off-canvas-menu-container a', OC); if (f) f.focus({ preventScroll: true }); }, 60);
  }
  function closeOffCanvas(restore) {
    if (!OC || !d.body.classList.contains('off-canvas-open')) return;
    d.body.classList.remove('off-canvas-open');
    OC.setAttribute('aria-hidden', 'true'); OC.setAttribute('inert', '');
    OCBtn.setAttribute('aria-expanded', 'false'); OCBtn.setAttribute('aria-label', 'Meniu');
    if (lenis) lenis.start();
    if (restore !== false && ocReturn && ocReturn.focus) ocReturn.focus({ preventScroll: true });
  }
  function initOffCanvas() {
    if (!OC || !OCBtn) return;
    OC.setAttribute('inert', '');
    $$('.off-canvas-menu-container > li', OC).forEach((li, i) => $$('a', li).forEach(a => a.style.setProperty('--i', i)));
    OCBtn.addEventListener('click', () => (d.body.classList.contains('off-canvas-open') ? closeOffCanvas() : openOffCanvas()));
    d.addEventListener('keydown', e => {
      if (!d.body.classList.contains('off-canvas-open')) return;
      if (e.key === 'Escape') { closeOffCanvas(); return; }
      if (e.key !== 'Tab') return;
      const list = [OCBtn].concat(focusables(OC));
      const i = list.indexOf(d.activeElement);
      if (e.shiftKey && (i <= 0)) { e.preventDefault(); list[list.length - 1].focus(); }
      else if (!e.shiftKey && i === list.length - 1) { e.preventDefault(); list[0].focus(); }
      else if (i === -1) { e.preventDefault(); list[0].focus(); }
    });
    OC.addEventListener('click', e => { const a = e.target.closest('a[href]'); if (a && !a.getAttribute('href').startsWith('tel:')) closeOffCanvas(false); });
    MQ.desk.addEventListener('change', () => { if (MQ.desk.matches) closeOffCanvas(false); });
  }

  /* ================= 3 · rows, sections, columns ================= */
  /* Video Background (.nectar-video-wrap > video.nectar-video-bg, sibling of .row-bg-wrap as in vc_row.php): desktop only
     (Disable Video Backgrounds On Mobile), lazy src, paused off-screen or under html.sgp-paused */
  function initBgVideos() {
    $$('.nectar-video-wrap video.nectar-video-bg[data-src]').forEach(v => {
      const io = new IntersectionObserver(es => es.forEach(e => {
        if (!MQ.desk.matches || RM()) return;
        if (e.isIntersecting) {
          if (!v.src) { v.src = v.dataset.src; v.load(); }
          if (!root.classList.contains('sgp-paused')) v.play().catch(() => {});
        } else if (v.src) v.pause();
      }), { rootMargin: '25% 0px' });
      v.addEventListener('playing', () => v.classList.add('is-playing'));
      io.observe(v.closest('.nectar-video-wrap'));
    });
  }
  /* Parallax Background Media On Scroll (Row/Section: Subtle .20 · Regular .28 · Medium .40 · High .60 · Fixed) +
     Section Scroll Effect „Parallax Fade“; column BG image parallax (Minimum .09 … High .60). Off below 1000 px. */
  function initParallax() {
    const items = [];
    $$('[data-parallax-speed]').forEach(host => {
      const inner = $(':scope > .row-bg-wrap .inner-wrap', host) || $(':scope > .column-image-bg-wrap .inner-wrap', host);
      if (!inner) return;
      items.push({ host, inner, s: PARALLAX[host.dataset.parallaxSpeed] || 0.2, fixed: host.dataset.parallaxSpeed === 'fixed', fade: host.dataset.parallax === 'parallax_fade', ext: 0 });
    });
    $$('.wpb_column[data-bg-parallax]').forEach(host => {
      const inner = $(':scope > .column-image-bg-wrap .inner-wrap', host);
      if (inner) items.push({ host, inner, s: PARALLAX[host.dataset.bgParallax] || 0.12, ext: 0 });
    });
    if (!items.length) return;
    const on = () => MQ.desk.matches && !RM();
    /* the layer is oversized by emul/grid.css (top/bottom = −ext) from the first paint; JS keeps ext only as the translate clamp */
    const size = () => items.forEach(it => {
      const h = it.host.offsetHeight;
      it.ext = on() ? Math.ceil(it.s * (vh + h) / 2) : 0;
      if (it.fixed) { it.inner.style.top = '0'; it.inner.style.bottom = 'auto'; it.inner.style.height = on() ? `${vh}px` : ''; }
      if (!on()) { it.inner.style.transform = ''; it.inner.style.opacity = ''; }
    });
    items.forEach(it => watchNear(it.host));
    size(); onResize(size);
    onScroll(() => {
      if (!on()) return null;
      const reads = items.filter(it => it.host._near).map(it => [it, it.host.getBoundingClientRect()]);
      return () => reads.forEach(([it, r]) => {
        let ty;
        if (it.fixed) ty = -r.top;
        else ty = clamp(-((r.top + r.height / 2) - vh / 2) * it.s, -it.ext, it.ext);
        it.inner.style.transform = `translate3d(0,${ty.toFixed(1)}px,0)`;
        if (it.fade) it.inner.style.opacity = (1 - clamp(-r.top / r.height, 0, 1) * 0.85).toFixed(3);
      });
    });
  }
  /* Background Layer Animation (Row + Column): Fade In · Zoom Out · Zoom Out Slowly · (Slight) Zoom Out Reveal · Mask Reveal · Reveal Rotate */
  function initBgAnimations() {
    $$('.wpb_row[data-bg-animation]:not([data-bg-animation="clip-path"]),.vc_section[data-bg-animation]').forEach(row => {
      const run = () => setTimeout(() => row.classList.add('bg-animated-in'), num(row.dataset.bgDelay, 0) + 30);
      onEnter(row, 100, run);
    });
    $$('.wpb_column[data-bg-animation]').forEach(col => onEnter(col, 88, () => { col.style.setProperty('--delay', `${delayOf(col)}ms`); col.classList.add('bg-animated-in'); }));
  }
  /* Clip Path Inset: Triggered Once (first row 1.3s (.25,.1,.18,1) · others 2s (.6,.06,.18,1)) or Scroll Position (interpolated) */
  const parseBox = s => { const p = String(s || '0').trim().split(/\s+/); while (p.length < 4) p.push(p[p.length === 1 ? 0 : p.length - 2] || '0'); return p.map(v => ({ n: num(v), u: (String(v).match(/[a-z%]+$/i) || ['px'])[0] })); };
  const clipStr = (a, b, t, ra, rb) => `inset(${a.map((v, i) => `${mix(v.n, b[i].n, t).toFixed(2)}${v.n === 0 && b[i].n !== 0 ? b[i].u : v.u}`).join(' ')} round ${mix(ra, rb, t).toFixed(1)}px)`;
  function initClipPath() {
    const rows = $$('[data-bg-animation="clip-path"]');
    rows.forEach((row, idx) => {
      const target = row.dataset.clipApplies === 'row' ? row : $(':scope > .row-bg-wrap', row);
      if (!target) return;
      const A = parseBox(row.dataset.clipStart || '0 6% 0 6%'), B = parseBox(row.dataset.clipEnd || '0');
      const [ra, rb] = String(row.dataset.clipRound || '0,0').split(',').map(v => num(v));
      const [oa, ob] = String(row.dataset.clipOffset || '0,50').split(',').map(v => num(v));
      const addon = row.dataset.clipAddon || '';
      const layer = $(':scope > .row-bg-wrap .row-bg-layer', row);
      const paint = t => {
        target.style.clipPath = clipStr(A, B, t, ra, rb);
        if (addon && layer) { layer.style.transform = addon === 'zoom-fade-in' ? `scale(${mix(1.2, 1, t).toFixed(3)})` : ''; layer.style.opacity = clamp(t * 1.6, 0, 1).toFixed(3); }
      };
      if (RM()) { paint(1); return; }
      if (row.dataset.clipType === 'scroll') {
        watchNear(row); paint(0);
        onScroll(() => { if (!row._near) return null; const r = row.getBoundingClientRect(); return () => paint(rangeProgress(r, oa, ob)); });
      } else {
        paint(0);
        const first = idx === 0 && row.getBoundingClientRect().top < vh;
        target.style.transition = first ? 'clip-path 1.3s cubic-bezier(.25,.1,.18,1)' : 'clip-path 2s cubic-bezier(.6,.06,.18,1)';
        if (layer) layer.style.transition = 'transform 1.3s cubic-bezier(.25,.1,.18,1),opacity 1.3s ease';
        onEnter(row, 88, () => requestAnimationFrame(() => paint(1)));
      }
    });
  }
  /* Color Change Section: the page background/text switch to the section's colours at ≥ 40 % visibility (0.8s) */
  function initColorChange() {
    const secs = $$('[data-color-change]');
    if (!secs.length) return;
    root.style.setProperty('--page-color-change-section-transition-time', '0s');
    secs.forEach(s => {
      const cs = getComputedStyle(s);
      s._cc = { bg: cs.backgroundColor, fg: cs.color, tone: s.dataset.textColor || 'dark' };
      /* rows with their own background media keep their tone; the rest follow the active section's text colour */
      if ($(':scope > .row-bg-wrap', s)) s.setAttribute('data-cc-own', '');
      s.style.setProperty('--bg', 'transparent');
      watchNear(s);
    });
    let cur = null;
    onScroll(() => {
      let best = null, bestR = 0.399;
      secs.forEach(s => {
        if (!s._near) return;
        const r = s.getBoundingClientRect();
        const vis = clamp(Math.min(r.bottom, vh) - Math.max(r.top, 0), 0, vh) / Math.min(vh, r.height || 1);
        if (vis > bestR) { bestR = vis; best = s; }
      });
      if (!best || best === cur) return null;
      cur = best;
      return () => { root.style.setProperty('--nectar-page-background-color', best._cc.bg); root.style.setProperty('--nectar-page-text-color', best._cc.fg); root.dataset.ccTone = best._cc.tone; };
    });
    setTimeout(() => { root.style.setProperty('--page-color-change-section-transition-time', '.8s'); d.body.classList.add('has-color-change-section-bg-color'); }, 100);
  }
  /* Column / Inner Column entrances (88 %; Reveal From X 70 %), Border Animation, Sticky Middle, Scroll Position Advanced */
  function initColumns() {
    $$('.wpb_column[data-animation]').forEach(col => {
      if (col.dataset.animationType === 'scroll_pos_advanced') return;
      const a = col.dataset.animation, line = a.startsWith('reveal-from') ? 70 : 88;
      if (!MQ.desk.matches && opts.column_animation_mobile === 'disable') { col.classList.add('animated-in'); return; }
      col.style.setProperty('--delay', `${delayOf(col)}ms`);
      /* after the entrance the column drops its transform / clip-path (.animation-done), so fixed children (phone hotspot sheets) are not trapped */
      const inn = () => { col.classList.add('animated-in'); setTimeout(() => col.classList.add('animation-done'), delayOf(col) + 1500); };
      onEnter(col, line, () => (a === 'mask-reveal' ? whenImgReady(col, inn) : inn()));
    });
    $$('.wpb_column[data-border-animation]').forEach(col => onEnter(col, 88, () => { col.style.setProperty('--border-delay', `${num(col.dataset.borderDelay, delayOf(col))}ms`); col.classList.add('border-animated-in'); }));
    const mids = $$('.wpb_column[data-sticky="middle"] > .vc_column-inner');
    if (mids.length) { const m = () => mids.forEach(el => el.style.setProperty('--sticky-h', `${el.offsetHeight}px`)); m(); onResize(m); }
    const parseState = s => { const o = { tx: 0, ty: 0, s: 1, o: 1 }; String(s || '').split(';').forEach(p => { const [k, v] = p.split(':'); if (k && v !== undefined) o[k.trim()] = num(v); }); return o; };
    $$('.wpb_column[data-animation-type="scroll_pos_advanced"]').forEach(col => {
      const A = parseState(col.dataset.scrollStart), B = parseState(col.dataset.scrollEnd);
      const [oa, ob] = String(col.dataset.scrollOffset || '0,100').split(',').map(v => num(v));
      const on = () => !RM() && (MQ.desk.matches || col.hasAttribute('data-scroll-mobile'));
      watchNear(col);
      onScroll(() => {
        if (!on()) { if (col.style.transform) return () => { col.style.transform = ''; col.style.opacity = ''; }; return null; }
        if (!col._near) return null;
        const t = rangeProgress(col.getBoundingClientRect(), oa, ob);
        return () => {
          col.style.transform = `translate3d(${mix(A.tx, B.tx, t).toFixed(1)}px,${mix(A.ty, B.ty, t).toFixed(1)}px,0) scale(${mix(A.s, B.s, t).toFixed(4)})`;
          col.style.opacity = mix(A.o, B.o, t).toFixed(3);
        };
      });
    });
    $$('.wpb_column[data-animation-type="parallax"]').forEach(col => {
      const k = num(col.dataset.movement, 20) / 100, axis = col.dataset.axis === 'x' ? 'x' : 'y';
      watchNear(col);
      onScroll(() => {
        if (RM() || !MQ.desk.matches || !col._near) return null;
        const r = col.getBoundingClientRect(), v = -((r.top + r.height / 2) - vh / 2) * k;
        return () => { col.style.translate = axis === 'x' ? `${v.toFixed(1)}px 0` : `0 ${v.toFixed(1)}px`; };
      });
    });
  }

  /* ================= 4 · typography elements ================= */
  /* Animated Text (split_line_heading): words (or letters) wrapped once; the text stays one accessible string.
     Words 1.2s (.25,1,.5,1), stagger 500 ms / words clamped 15–50 ms; letters 400 / n clamped 20–35 ms. Waypoint bottom-in-view. */
  function splitWords(target, letters) {
    const inners = [];
    const walk = node => {
      Array.from(node.childNodes).forEach(n => {
        if (n.nodeType === 3) {
          const parts = n.textContent.split(/([ \t\r\n]+)/), frag = d.createDocumentFragment();
          parts.forEach(p => {
            if (!p) return;
            if (/^[ \t\r\n]+$/.test(p)) { frag.appendChild(d.createTextNode(' ')); return; }
            const word = d.createElement('span'), inner = d.createElement('span');
            word.className = 'word'; inner.className = 'inner';
            if (letters) Array.from(p).forEach(ch => { const c = d.createElement('span'); c.className = 'char'; c.textContent = ch; inner.appendChild(c); });
            else inner.textContent = p;
            word.appendChild(inner); frag.appendChild(word); inners.push(inner);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && n.tagName !== 'BR' && !n.classList.contains('word')) walk(n);
      });
    };
    walk(target);
    return inners;
  }
  function initAnimatedText() {
    $$('.nectar-split-heading').forEach(wrap => {
      const target = wrap.firstElementChild;
      if (!target || wrap.dataset.textEffect === 'none') return;
      const effect = wrap.dataset.textEffect || 'default', letters = effect.startsWith('letter');
      if (letters && !target.hasAttribute('aria-label')) target.setAttribute('aria-label', target.textContent.replace(/\s+/g, ' ').trim());
      const inners = splitWords(target, letters);
      if (letters) $$('.word', target).forEach(wd => wd.setAttribute('aria-hidden', 'true'));
      const base = delayOf(wrap);
      if (effect === 'scroll-opacity-reveal') {
        watchNear(wrap);
        onScroll(() => {
          if (!wrap._near) return null;
          const r = wrap.getBoundingClientRect(), p = rangeProgress(r, 12, 62), n = inners.length;
          return () => inners.forEach((el, i) => el.style.setProperty('--o', (0.2 + 0.8 * clamp(p * n - i, 0, 1)).toFixed(3)));
        });
        return;
      }
      if (letters) {
        const chars = $$('.char', target), step = clamp(400 / chars.length, 20, 35);
        chars.forEach((c, i) => c.style.setProperty('--wd', `${Math.round(base + i * step)}ms`));
      } else {
        const step = wrap.dataset.stagger === 'false' ? 0 : clamp(500 / inners.length, 15, 50);
        inners.forEach((el, i) => el.style.setProperty('--wd', `${Math.round(base + i * step)}ms`));
      }
      if (!MQ.desk.matches && wrap.hasAttribute('data-m-rm-animation')) { wrap.classList.add('animated-in'); return; }
      onBottomIn(wrap, () => wrap.classList.add('animated-in'));
    });
  }
  /* Highlighted Text: background-size 0 → 100 % .9s (.15,.75,.4,1) · Waypoint bottom-in-view */
  function initHighlighted() {
    $$('.nectar-highlighted-text').forEach(el => {
      $$('em', el).forEach((em, i) => em.style.setProperty('--hd', `${delayOf(el) + i * 150}ms`));
      onBottomIn(el, () => el.classList.add('animated'));
    });
  }
  /* Scrolling Text (nectar_scrolling_text.php): .nectar-scrolling-text-inner > .nectar-scrolling-text-inner__text-chunk × n; every CHUNK
     runs the loop (translateX −20 % → −120 %, 45 / 30 / 14 / 7 / 4 s — element-scrolling-text.css). Custom divider = span.custom(.spin)[data-scale]
     > span INSIDE the text element; Move on Scroll offsets the strip, Spin on Scroll rotates the divider. */
  function initScrollingText() {
    $$('.nectar-scrolling-text').forEach(el => {
      const src = el.firstElementChild;
      if (!src || el._built) return;
      el._built = true;
      const divider = el.dataset.divider || 'none';
      const chunk = d.createElement('div'); chunk.className = 'nectar-scrolling-text-inner__text-chunk';
      chunk.appendChild(src);
      if (divider !== 'none') {
        const dv = d.createElement('span');
        if (divider === 'space') dv.innerHTML = '&nbsp;';
        else {
          const scale = { half: 'half', 'three-quarters': 'three-fourths' }[el.dataset.dividerSize] || 'full';
          dv.className = el.hasAttribute('data-spin-divider') ? 'custom spin' : 'custom'; dv.dataset.scale = scale;
          const i = d.createElement('span'); i.textContent = divider; dv.appendChild(i);
        }
        dv.setAttribute('aria-hidden', 'true');
        src.appendChild(dv);
      }
      const inner = d.createElement('div'); inner.className = 'nectar-scrolling-text-inner';
      inner.appendChild(chunk); el.appendChild(inner);
      const fill = () => {
        $$('.nectar-scrolling-text-inner__text-chunk[aria-hidden]', inner).forEach(c => c.remove());
        const cw = chunk.getBoundingClientRect().width || 200;
        const n = Math.max(num(el.dataset.repeat, 3), Math.ceil((vw * 1.6) / cw) + 2);
        for (let i = 1; i < n; i++) { const c = chunk.cloneNode(true); c.setAttribute('aria-hidden', 'true'); $$('[id]', c).forEach(x => x.removeAttribute('id')); inner.appendChild(c); }
      };
      fill(); onResize(fill);
      if (d.fonts && d.fonts.ready) d.fonts.ready.then(fill);
      const move = el.hasAttribute('data-move-on-scroll'), spin = el.hasAttribute('data-spin-divider');
      if (move || spin) {
        watchNear(el);
        const dir = el.dataset.sDir === 'rtl' ? 1 : -1;
        onScroll(y => {
          if (!el._near || RM()) return null;
          const r = el.getBoundingClientRect();
          return () => {
            if (move) el.style.setProperty('--nst-x', `${(dir * (vh - r.top) * 0.35).toFixed(1)}px`);
            if (spin) el.style.setProperty('--spin', `${(y * 0.25).toFixed(1)}deg`);
          };
        });
      }
    });
  }
  /* Divider → Animate Line (scaleX 0 → 1, entrance curve) · Waypoint bottom-in-view */
  function initDividers() {
    $$('.divider-wrap[data-animate]').forEach(el => { el.style.setProperty('--dd', `${delayOf(el)}ms`); onBottomIn(el, () => el.classList.add('animated-in')); });
  }
  /* Milestone: Count To Value 2.2s easeOutCubic · Motion Blur Slide In (digits 200 ms apart, .65s (0,0,.17,1)) · trigger 98 % */
  function initMilestones() {
    $$('.nectar-milestone').forEach(m => {
      const numEl = $('.number .num', m);
      if (!numEl) return;
      const final = numEl.textContent.trim(), effect = m.dataset.effect || 'count';
      if (effect === 'motion_blur') {
        numEl.setAttribute('aria-hidden', 'true');
        const sr = d.createElement('span'); sr.className = 'screen-reader-text'; sr.textContent = final; numEl.after(sr);
        numEl.innerHTML = Array.from(final).map((c, i) => `<span class="digit"><span style="--i:${i}">${c}</span></span>`).join('');
        m.style.setProperty('--md', `${delayOf(m)}ms`);
        onEnter(m, 98, () => m.classList.add('animated-in'));
      } else if (effect === 'count') {
        const target = num(final.replace(/\s/g, '').replace(',', '.')), dec = (final.split(/[.,]/)[1] || '').length;
        onEnter(m, 98, () => {
          if (RM()) return;
          const t0 = performance.now() + delayOf(m), dur = 2200;
          const tick = now => {
            const t = clamp((now - t0) / dur, 0, 1), e = 1 - Math.pow(1 - t, 3);
            numEl.textContent = t <= 0 ? '0' : (target * e).toFixed(dec);
            if (t < 1) requestAnimationFrame(tick); else numEl.textContent = final;
          };
          requestAnimationFrame(tick);
        });
      }
    });
  }

  /* ================= 5 · buttons, video lightbox, content trail, icons ================= */
  const ARROW_UR = '<path d="M8.4 17 7 15.6 14.6 8H9V6h9v9h-2V9.4z"/>';
  const ICON_ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15.5M13.5 6l6 6-6 6"/></svg>';
  const ICON_DOWN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v15.5M6 13.5l6 6 6-6"/></svg>';
  const ICON_CLOSE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none"><path d="M5.5 5.5l13 13M18.5 5.5l-13 13"/></svg>';
  function initButtons() {
    $$('.nectar-cta').forEach(b => {
      const style = b.dataset.style;
      let lt = $('.link_text', b);
      if (!lt) { lt = d.createElement('span'); lt.className = 'link_text'; while (b.firstChild) lt.appendChild(b.firstChild); b.appendChild(lt); }
      if (style === 'arrow-circle-animation' && !$('.arrow-circle-animation-arrow-wrap', b)) {
        lt.insertAdjacentHTML('beforeend', `<span class="arrow-circle-animation-arrow-wrap" aria-hidden="true"><svg class="arrow-circle-animation-arrow" viewBox="0 0 24 24">${ARROW_UR}</svg><svg class="arrow-circle-animation-arrow hover" viewBox="0 0 24 24">${ARROW_UR}</svg></span>`);
      }
      if (style === 'next-section') {
        if (!$('svg', b)) lt.insertAdjacentHTML('beforeend', ICON_DOWN + ICON_DOWN);   /* Minimal Arrow Alt: two stacked arrows */
        b.addEventListener('click', e => {
          const host = b.closest('.vc_section, .wpb_row:not(.inner_row)');
          const next = host && host.nextElementSibling;
          if (next) { e.preventDefault(); scrollToEl(next); }
        });
      }
      if ((style === 'text-reveal-wave' || style === 'text-reveal') && !b._wave) {
        b._wave = true;
        const t = $('.text', b);
        if (!t) return;
        const txt = t.textContent;
        t.setAttribute('aria-hidden', 'true');
        const esc = c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c] || c);
        t.innerHTML = Array.from(txt).map((c, i) => `<span class="char" data-c="${esc(c)}" style="--i:${i}"><span>${esc(c)}</span></span>`).join('');
        const sr = d.createElement('span'); sr.className = 'screen-reader-text'; sr.textContent = txt; t.after(sr);
      }
    });
    $$('.nectar-button .icon-default-style:empty').forEach(i => { i.innerHTML = ICON_ARROW; i.setAttribute('aria-hidden', 'true'); });
    $$('.nectar-cta [data-icon="arrow"]:empty').forEach(i => { i.outerHTML = ICON_ARROW.replace('<svg', '<svg class="nectar-cta__icon"'); });
  }
  /* Video Lightbox → Play Button With Image – Mouse Follow · click opens a <dialog> player (Esc closes, Lenis paused) */
  let lightbox = null;
  function openLightbox(src, label) {
    if (!lightbox) {
      lightbox = d.createElement('dialog'); lightbox.className = 'nectar-lightbox';
      lightbox.innerHTML = `<button class="nectar-lightbox__close" type="button" aria-label="Uždaryti vaizdo įrašą">${ICON_CLOSE}</button><video controls playsinline></video>`;
      d.body.appendChild(lightbox);
      const close = () => lightbox.close();
      $('.nectar-lightbox__close', lightbox).addEventListener('click', close);
      lightbox.addEventListener('click', e => { if (e.target === lightbox) close(); });
      lightbox.addEventListener('close', () => { const v = $('video', lightbox); v.pause(); v.removeAttribute('src'); v.load(); if (lenis) lenis.start(); });
    }
    const v = $('video', lightbox);
    lightbox.setAttribute('aria-label', label || 'Vaizdo įrašas');
    v.src = src;
    if (lenis) lenis.stop();
    lightbox.showModal();
    v.play().catch(() => {});
  }
  function initVideoLightbox() {
    $$('a.nectar-video-box').forEach(box => {
      if (!$('.play_button_mouse_follow', box)) box.insertAdjacentHTML('beforeend', '<span class="play_button_mouse_follow" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 4.5v15l12.5-7.5z"/></svg></span>');
      if (box.dataset.linkStyle === 'play_button_mouse_follow' && MQ.fine.matches) {
        box.addEventListener('pointermove', e => {
          const r = box.getBoundingClientRect();
          box.style.setProperty('--mx', `${e.clientX - r.left}px`); box.style.setProperty('--my', `${e.clientY - r.top}px`);
          box.classList.add('is-following');
        });
        box.addEventListener('pointerleave', () => box.classList.remove('is-following'));
      }
      box.addEventListener('click', e => { e.preventDefault(); openLightbox(box.getAttribute('href'), box.getAttribute('aria-label')); });
    });
  }
  /* Content Trail → Type: Text (frequency 85 px, life 1.2s, Scale in/out, random rotation) — fine pointers only */
  function initContentTrail() {
    $$('.nectar-content-trail').forEach(tr => {
      const host = tr.closest('.wpb_column') || tr.parentElement;          /* native: spawns only inside its own box */
      const items = String(tr.dataset.items || '').split('|').filter(Boolean);
      const colors = String(tr.dataset.colors || '#EF4539/#0F1417').split(',').map(p => p.split('/'));
      const freq = num(tr.dataset.frequency, 85), life = num(tr.dataset.duration, 1.2);
      if (!items.length) return;
      let lx = null, ly = null, acc = 0, k = 0;
      host.addEventListener('pointermove', e => {
        if (!MQ.fine.matches || RM() || root.classList.contains('sgp-paused')) return;
        if (e.target.closest('a, button, input, select, textarea, .nectar-cta')) { lx = null; return; }
        const r = tr.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
        if (x < 0 || y < 0 || x > r.width || y > r.height) return;
        if (lx !== null) acc += Math.hypot(x - lx, y - ly);
        lx = x; ly = y;
        if (acc < freq) return;
        acc = 0;
        const el = d.createElement('span'), c = colors[k % colors.length];
        el.className = 'trail-item'; el.setAttribute('aria-hidden', 'true'); el.textContent = items[k % items.length]; k++;
        el.style.cssText = `--tx:${x}px;--ty:${y}px;--ti-bg:${c[0]};--ti-fg:${c[1] || '#fff'};--rot:${tr.hasAttribute('data-randomize') ? (Math.random() * 16 - 8).toFixed(1) : 0}deg;--trail-d:${life}s`;
        tr.appendChild(el);
        setTimeout(() => el.remove(), life * 1000 + 50);
      });
    });
  }
  /* Icon (Linea) line draw: stroke-dasharray = path length, drawn on entry (Vivus-like, speed Medium) */
  function initIcons() {
    $$('.nectar_icon_wrap[data-draw]').forEach(wrap => {
      $$('svg path, svg line, svg circle, svg polyline, svg rect', wrap).forEach(p => {
        try { p.style.setProperty('--len', Math.ceil(p.getTotalLength()) + 1); } catch (e) { /* not measurable */ }
      });
      wrap.style.setProperty('--dd', `${delayOf(wrap)}ms`);
      onEnter(wrap, 88, () => wrap.classList.add('animated-in'));
    });
  }

  /* ================= 6 · lists, cards, media ================= */
  /* first image inside el decoded (lazy media are fetched first) → cb; entrance effects never open onto an empty frame */
  function whenImgReady(el, cb) {
    const img = $('img', el);
    if (!img || (img.complete && img.naturalWidth)) { cb(); return; }
    let done = false;
    const go = () => { if (!done) { done = true; cb(); } };
    if (img.loading === 'lazy') img.loading = 'eager';
    (img.decode ? img.decode() : Promise.reject()).then(go, () => img.addEventListener('load', go, { once: true }));
    setTimeout(go, 3000);
  }
  function initLists() {
    /* Horizontal List Item → Border Color (+ Border Animation: the line draws at the 94 % line; only with a Border Color, as in 18.2.1) */
    $$('.nectar-hor-list-item[data-border-color]').forEach(el => el.style.setProperty('--hli-bc', el.dataset.borderColor));
    $$('.nectar-hor-list-item[data-border-animation][data-border-color]').forEach(el => onEnter(el, 94, () => el.classList.add('animated-in')));
    /* Icon List → Animate Element: Waypoint 75 %, items get .animated 300 ms apart (horizontal 100 ms), the list .completed (line draw) */
    $$('.nectar-icon-list[data-animate]').forEach(el => onEnter(el, 75, () => {
      const step = el.dataset.direction === 'horizontal' ? 100 : 300;
      $$('.nectar-icon-list-item', el).forEach((it, i) => setTimeout(() => it.classList.add('animated'), i * step));
      el.classList.add('completed');
    }));
    $$('.nectar-fancy-ul[data-animation]').forEach(el => {
      $$(':scope > li', el).forEach((li, i) => li.style.setProperty('--i', i));
      onEnter(el, 90, () => el.classList.add('animated-in'));
    });
    $$('.img-with-aniamtion-wrap[data-animation]').forEach(el => {
      const a = el.dataset.animation, line = a === 'slide-up' ? 99 : (a === 'ro-reveal-from-left' || a === 'ro-reveal-from-right') ? 75 : 88;
      el.style.setProperty('--delay', `${delayOf(el)}ms`);
      onEnter(el, line, () => whenImgReady(el, () => el.classList.add('animated-in')));
    });
  }
  /* Cascading Images: Waypoint 70 %; layers Time Between Animations apart (default 175 ms); Enable Parallax Scrolling per layer
     (CascadingParallax: Subtle .09 / Medium .15 / High .25) */
  function initCascading() {
    const F = { subtle: 0.09, medium: 0.15, high: 0.25 };
    $$('.nectar_cascading_images').forEach(el => {
      const layers = $$('.cascading-image', el);
      layers.forEach((l, i) => l.style.setProperty('--i', i));
      if (el.dataset.animationTiming) el.style.setProperty('--ci-step', `${num(el.dataset.animationTiming, 175)}ms`);
      onEnter(el, 70, () => whenImgReady(el, () => el.classList.add('animated-in')));
      const px = layers.filter(l => l.dataset.parallax);
      if (!px.length) return;
      watchNear(el);
      onScroll(() => {
        if (!el._near || RM() || !MQ.desk.matches) return null;
        const r = el.getBoundingClientRect(), dd = (r.top + r.height / 2) - vh / 2;
        return () => px.forEach(l => { l.style.translate = `0 ${(-dd * (F[l.dataset.parallax] || 0.09)).toFixed(1)}px`; });
      });
    });
  }
  /* Image With Hotspots (nectar_hotspot.php: .nttip > .inner): markers bounce in 100 ms apart once the image is decoded;
     tooltip on hover AND focus (Show On Hover), click toggles; ≤ 690 px the open tooltip is a full-screen sheet closed by a tap; Esc closes */
  function initHotspots() {
    $$('.nectar_image_with_hotspots').forEach(box => {
      const func = box.dataset.tooltipFunc || 'hover';
      const wraps = $$('.nectar_hotspot_wrap', box);
      const closeAll = except => wraps.forEach(w2 => { if (w2 !== except) { w2.classList.remove('open'); const b = $('.nectar_hotspot', w2); if (b) b.setAttribute('aria-expanded', 'false'); } });
      const place = (wrap, tip) => {
        tip.style.marginLeft = '';
        if (MQ.phone.matches) return;
        const r = tip.getBoundingClientRect(), m = 10;
        if (r.left < m) tip.style.marginLeft = `${m - r.left}px`;
        else if (r.right > vw - m) tip.style.marginLeft = `${vw - m - r.right}px`;
      };
      wraps.forEach(wrap => {
        const btn = $('.nectar_hotspot', wrap), tip = $('.nttip', wrap);
        if (!btn || !tip) return;
        if (!$(':scope > .inner', tip)) { const inner = d.createElement('div'); inner.className = 'inner'; while (tip.firstChild) inner.appendChild(tip.firstChild); tip.appendChild(inner); }
        if (!$('.tipclose', tip)) $(':scope > .inner', tip).insertAdjacentHTML('afterbegin', '<span class="tipclose" aria-hidden="true"></span>');
        if (!tip.id) tip.id = nextId('nttip');
        btn.setAttribute('aria-describedby', tip.id); btn.setAttribute('aria-expanded', 'false');
        const open = () => { closeAll(wrap); wrap.classList.add('open'); btn.setAttribute('aria-expanded', 'true'); place(wrap, tip); };
        const close = () => { wrap.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); };
        if (func === 'hover') {
          wrap.addEventListener('mouseenter', () => { if (!MQ.phone.matches) open(); }); wrap.addEventListener('mouseleave', () => { if (!MQ.phone.matches) close(); });
          btn.addEventListener('focus', () => { if (!MQ.phone.matches) open(); }); btn.addEventListener('blur', () => { if (!MQ.phone.matches) close(); });
        }
        btn.addEventListener('click', () => (wrap.classList.contains('open') && (func !== 'hover' || MQ.phone.matches) ? close() : open()));
        tip.addEventListener('click', () => { if (MQ.phone.matches) { close(); btn.focus({ preventScroll: true }); } });
        btn.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
      });
      d.addEventListener('click', e => { if (!box.contains(e.target)) closeAll(); });
      if (box.hasAttribute('data-animation')) {
        wraps.forEach(w2 => w2.addEventListener('animationend', e => { if (e.animationName === 'nectarBounceIn') w2.classList.add('animation-done'); }));
        onEnter(box, 85, () => whenImgReady(box, () => wraps.forEach((w2, i) => setTimeout(() => w2.classList.add('animated-in'), i * 100))));
      }
    });
  }
  /* Fancy Box → Parallax Hover Effect (3D tilt) */
  function initFancyBoxes() {
    $$('.nectar-fancy-box[data-style="parallax_hover"]').forEach(box => {
      const layer = $('.parallax-layer', box);
      if (!layer || !MQ.fine.matches) return;
      box.addEventListener('pointermove', e => {
        if (RM()) return;
        const r = box.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        layer.style.setProperty('--rx', `${(x * 10).toFixed(2)}deg`); layer.style.setProperty('--ry', `${(-y * 10).toFixed(2)}deg`);
      });
      box.addEventListener('pointerleave', () => { layer.style.setProperty('--rx', '0deg'); layer.style.setProperty('--ry', '0deg'); });
    });
  }
  /* Image Gallery → Flickity Style: Touch Indicator and Total Visualized, Image Parallax, Subtle Image Scale When Dragging */
  function initGalleries() {
    $$('.nectar-flickity').forEach(el => {
      const cells = $$('.cell', el), n = cells.length;
      const total = d.createElement('div'); total.className = 'fl-total'; total.setAttribute('aria-hidden', 'true');
      total.innerHTML = `<span class="fl-cur">01</span><span class="fl-bar"><i></i></span><span>${String(n).padStart(2, '0')}</span>`;
      el.after(total);
      const cur = $('.fl-cur', total), bar = $('.fl-bar', total);
      const setCur = i => { cur.textContent = String(i + 1).padStart(2, '0'); bar.style.setProperty('--fl-p', ((i + 1) / n).toFixed(3)); };
      setCur(0);
      if (typeof w.Flickity !== 'function') {
        el.addEventListener('scroll', () => setCur(Math.round(el.scrollLeft / ((cells[0] && cells[0].offsetWidth) || 1))), { passive: true });
        return;
      }
      const f = new w.Flickity(el, { cellSelector: '.cell', cellAlign: 'left', contain: true, pageDots: false, prevNextButtons: false, dragThreshold: 6, freeScroll: el.hasAttribute('data-free-scroll') });
      f.on('change', setCur);
      if (el.hasAttribute('data-drag-scale')) { f.on('dragStart', () => el.classList.add('is-dragging')); f.on('dragEnd', () => el.classList.remove('is-dragging')); }
      if (el.hasAttribute('data-image-parallax')) {
        f.on('scroll', () => f.slides.forEach((s, i) => { const img = $('img', f.cells[i] && f.cells[i].element); if (img) img.style.setProperty('--px', `${((s.target + f.x) * -0.18).toFixed(1)}px`); }));
      }
      if (MQ.fine.matches) {
        const ind = d.createElement('span'); ind.className = 'fl-indicator'; ind.setAttribute('aria-hidden', 'true'); ind.textContent = '← →';
        el.appendChild(ind);
        el.addEventListener('pointermove', e => { const r = el.getBoundingClientRect(); ind.style.setProperty('--mx', `${e.clientX - r.left}px`); ind.style.setProperty('--my', `${e.clientY - r.top}px`); });
      }
    });
  }

  /* ================= 7 · Toggle Panels, Tabs, Page Submenu ================= */
  const qs = new URLSearchParams(location.search);
  /* Toggle Panels: Animated Circle (.85s (.76,0,.24,1)) / Minimal Shadow / Default; Accordion; First Toggle Open; deep link ?toggle=N */
  function initToggles() {
    let n = 0;
    const want = num(qs.get('toggle'), 0);
    $$('.toggles').forEach(group => {
      const acc = group.hasAttribute('data-accordion');
      const items = $$(':scope > .toggle', group);
      const wantHere = want > n && want <= n + items.length;   /* a deep link into an accordion replaces First Toggle Open */
      const set = (t, on) => {
        t.classList.toggle('open', on);
        const b = $('.toggle-title button', t), p = $('.inner-toggle-wrap', t);
        if (b) b.setAttribute('aria-expanded', String(on));
        if (p) { if (on) p.removeAttribute('inert'); else p.setAttribute('inert', ''); }
      };
      items.forEach((t, i) => {
        n++;
        const title = $('.toggle-title', t), panel = $('.inner-toggle-wrap', t);
        if (!title || !panel) return;
        let btn = $('button', title);
        if (!btn) { btn = d.createElement('button'); btn.type = 'button'; btn.innerHTML = `<span class="toggle-heading">${title.innerHTML}</span>`; title.innerHTML = ''; title.appendChild(btn); }
        /* icon = toggle.php markup: svg.nectar-toggle-icon > circle.nectar-toggle-icon-circle(-hover) + line.plus-line */
        if (!$('.nectar-toggle-icon', btn)) btn.insertAdjacentHTML('beforeend', '<svg class="nectar-toggle-icon" viewBox="0 0 40 40" aria-hidden="true" focusable="false"><circle class="nectar-toggle-icon-circle" cx="20" cy="20" r="18"/><circle class="nectar-toggle-icon-circle-hover" cx="20" cy="20" r="18" pathLength="115"/><line class="plus-line plus-line-vertical" x1="20" y1="14" x2="20" y2="26"/><line class="plus-line plus-line-horizontal" x1="14" y1="20" x2="26" y2="20"/></svg>');
        if (!panel.firstElementChild || !panel.firstElementChild.classList.contains('toggle-inner')) {
          const inner = d.createElement('div'); inner.className = 'toggle-inner'; while (panel.firstChild) inner.appendChild(panel.firstChild); panel.appendChild(inner);
        }
        if (!panel.id) panel.id = nextId('toggle');
        if (!btn.id) btn.id = `${panel.id}-btn`;
        btn.setAttribute('aria-controls', panel.id);
        panel.setAttribute('role', 'region'); panel.setAttribute('aria-labelledby', btn.id);
        set(t, (i === 0 && group.hasAttribute('data-first-open') && !(acc && wantHere)) || t.classList.contains('open') || want === n);
        if (want === n) {
          /* deep link ?toggle=N: land on the title once layout (lazy media, sticky sections, Lenis) has settled */
          const go = () => scrollToEl($('.toggle-title', t) || t, true);
          const run = () => { setTimeout(go, 450); setTimeout(() => { const r = t.getBoundingClientRect(); if (r.top < headerOffset() - 8 || r.top > vh * 0.5) go(); }, 1300); };
          if (d.readyState === 'complete') run(); else w.addEventListener('load', run, { once: true });
        }
        btn.addEventListener('click', () => {
          const on = !t.classList.contains('open');
          if (acc && on) items.forEach(o => { if (o !== t) set(o, false); });
          set(t, on);
        });
      });
    });
  }
  /* Tabs: Minimal / Minimal Alt (4 px underline .3s) · Toggle Button (70 × 28 switch .45s) · Vertical Sticky Scrolling (active by scroll);
     ←/→ keys; deep link ?tab=<panel id without "tab-"> */
  function initTabs() {
    $$('.tabbed').forEach(tb => {
      const style = tb.dataset.style || 'minimal';
      const nav = $(':scope > .wpb_tabs_nav', tb), links = nav ? $$(':scope > li:not(.vs-cta) > a', nav) : [], panels = $$(':scope > .wpb_tab', tb);
      if (!nav || !links.length) return;
      if (style === 'vertical_scrolling') {
        nav.removeAttribute('role');
        links.forEach(a => { a.removeAttribute('role'); a.removeAttribute('aria-selected'); a.setAttribute('href', `#${(a.getAttribute('href') || '').replace(/^#/, '')}`); });
        panels.forEach(p => { p.removeAttribute('role'); p.hidden = false; });
        /* Sticky Aspect „Tab Links“: 3 px indicator on the 1 px track; Mobile Display „Visible Above Each Section“ */
        let ind = null;
        if ((tb.dataset.stickyAspect || 'default') === 'default') {
          ind = d.createElement('li'); ind.className = 'vs-line'; ind.setAttribute('aria-hidden', 'true'); nav.prepend(ind);
          if (tb.dataset.mDisplay === 'visible') links.forEach((a, i) => { if (panels[i]) panels[i].insertAdjacentHTML('afterbegin', `<div class="vs-mobile-title" aria-hidden="true">${a.innerHTML}</div>`); });
        }
        const moveInd = i => { if (!ind || !links[i]) return; const li = links[i].parentElement; ind.style.setProperty('--vs-y', `${li.offsetTop}px`); ind.style.setProperty('--vs-h', `${links[i].offsetHeight}px`); };
        watchNear(tb);
        let active = -1;
        onResize(() => moveInd(Math.max(active, 0)));
        onScroll(() => {
          if (!tb._near) return null;
          let idx = 0;
          panels.forEach((p, i) => { if (p.getBoundingClientRect().top < vh * 0.42) idx = i; });
          if (idx === active) return null;
          active = idx;
          return () => { links.forEach((a, i) => { a.classList.toggle('active-tab', i === idx); if (i === idx) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); }); panels.forEach((p, i) => p.classList.toggle('active-tab', i === idx)); moveInd(idx); };
        });
        return;
      }
      nav.setAttribute('role', 'tablist');
      let line = null, sw = null;
      if (style === 'minimal' || style === 'minimal_alt') { line = d.createElement('li'); line.className = 'magic-line'; line.setAttribute('role', 'presentation'); line.setAttribute('aria-hidden', 'true'); nav.appendChild(line); }
      if (style === 'toggle_button' && links.length === 2) {
        const li = d.createElement('li'); li.className = 'toggle-switch'; li.setAttribute('role', 'presentation'); li.setAttribute('aria-hidden', 'true');
        li.addEventListener('click', () => select(links[0].getAttribute('aria-selected') === 'true' ? 1 : 0, true));
        nav.appendChild(li); sw = li;
      }
      const select = (i, focus) => {
        links.forEach((a, k) => { const on = k === i; a.setAttribute('aria-selected', String(on)); a.tabIndex = on ? 0 : -1; a.parentElement.classList.toggle('active-tab', on); });
        panels.forEach((p, k) => { p.hidden = k !== i; });
        if (focus) links[i].focus();
        if (line) { const a = links[i]; line.style.setProperty('--ml-w', `${a.offsetWidth}px`); line.style.setProperty('--ml-x', `${a.offsetLeft}px`); }
        if (sw) sw.dataset.on = String(i);
        requestTick();                                                      /* bottom-in-view elements in the newly shown panel */
      };
      links.forEach((a, i) => {
        const p = panels[i];
        if (!p) return;
        if (!p.id) p.id = nextId('tab');
        a.setAttribute('role', 'tab'); a.id = a.id || `${p.id}-tab`;
        a.setAttribute('aria-controls', p.id); a.setAttribute('href', `#${p.id}`);
        a.parentElement.setAttribute('role', 'presentation');
        p.setAttribute('role', 'tabpanel'); p.setAttribute('aria-labelledby', a.id); p.tabIndex = 0;
        a.addEventListener('click', e => { e.preventDefault(); e.stopPropagation(); select(i); });
        a.addEventListener('keydown', e => {
          const k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
          if (k) { e.preventDefault(); select((i + k + links.length) % links.length, true); }
        });
      });
      const want = qs.get('tab');
      let start = panels.findIndex(p => want && (p.id === want || p.id === `tab-${want}`));
      if (start < 0) start = Math.max(0, links.findIndex(a => a.getAttribute('aria-selected') === 'true'));
      select(start);
      onResize(() => select(links.findIndex(a => a.getAttribute('aria-selected') === 'true')));
      if (d.fonts && d.fonts.ready) d.fonts.ready.then(() => select(links.findIndex(a => a.getAttribute('aria-selected') === 'true')));
    });
  }
  /* Page Submenu: Sticky? (sticks under the header, .3s) + scrollspy → .current-menu-item */
  function initPageSubmenu() {
    /* Sticky? → the bar becomes fixed under the header once its row scrolls past (Salient does this in JS too) */
    const sticky = $('.page-submenu[data-sticky]');
    if (sticky) {
      const holder = sticky.parentElement;
      const h = () => { holder.style.minHeight = `${sticky.offsetHeight}px`; root.style.setProperty('--submenu-h', `${sticky.offsetHeight}px`); };
      h(); onResize(h);
      let fixed = false;
      onScroll(() => {
        const hh = parseFloat(getComputedStyle(root).getPropertyValue('--header-h-small')) || 70;
        const on = holder.getBoundingClientRect().top <= hh;
        if (on === fixed) return null;
        fixed = on;
        return () => sticky.classList.toggle('is-fixed', on);
      });
    }
    $$('.page-submenu').forEach(pm => {
      const ul = $('ul', pm), lis = ul ? $$(':scope > li', ul) : [];
      const secs = lis.map(li => { const a = $('a', li); return a ? d.getElementById((a.getAttribute('href') || '').replace(/^.*#/, '')) : null; });
      let cur = -1;
      onScroll(() => {
        const lim = pm.getBoundingClientRect().bottom + 24;
        let idx = -1;
        secs.forEach((s, i) => { if (s && s.getBoundingClientRect().top <= lim) idx = i; });
        if (idx === cur) return null;
        cur = idx;
        return () => {
          lis.forEach((li, i) => { li.classList.toggle('current-menu-item', i === idx); const a = $('a', li); if (i === idx) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
          /* keep the active link visible in the sideways-scrolling strip (phones) */
          const a = idx >= 0 && $('a', lis[idx]);
          if (a && ul.scrollWidth > ul.clientWidth + 2) ul.scrollTo({ left: Math.max(0, a.offsetLeft - ul.offsetLeft - 20), behavior: RM() ? 'auto' : 'smooth' });
        };
      });
    });
  }

  /* ================= 8 · Sticky Content Sections (4 types) ================= */
  /* Effect Enabled per device (data-enabled="desktop tablet"); excluded devices and reduced motion stack the sections */
  function initStickySections() {
    let indicator = null;
    const showIndicator = (text, bg, fg) => {
      if (!indicator) { indicator = d.createElement('span'); indicator.className = 'nsms-indicator'; indicator.setAttribute('aria-hidden', 'true'); d.body.appendChild(indicator); }
      indicator.textContent = text || 'Plačiau';
      indicator.style.setProperty('--ind-bg', bg || ''); indicator.style.setProperty('--ind-fg', fg || '');
      indicator.classList.add('visible');
    };
    if (MQ.fine.matches) d.addEventListener('pointermove', e => { if (indicator) { indicator.style.setProperty('--mx', `${e.clientX}px`); indicator.style.setProperty('--my', `${e.clientY}px`); } }, { passive: true });

    $$('.nectar-sticky-media-sections').forEach(box => {
      const type = box.dataset.type || 'default';
      box.classList.add(`type--${type}`);                                    /* nectar_el_dynamic_classnames → type--{type} */
      const secs = $$(':scope > .nectar-sticky-media-section', box);
      const enabled = () => !RM() && String(box.dataset.enabled || 'desktop tablet').split(/[\s,]+/).includes(device());
      /* Link Mouse Indicator */
      secs.forEach(s => {
        const link = $(':scope > .nsms-link', s);
        if (!link || !s.dataset.indicatorText || !MQ.fine.matches) return;
        s.addEventListener('pointerenter', () => showIndicator(s.dataset.indicatorText, s.dataset.indicatorBg, s.dataset.indicatorFg));
        s.addEventListener('pointerleave', () => indicator && indicator.classList.remove('visible'));
      });
      if (type === 'default') {
        /* nectar_sticky_media_sections.php: __featured-media > __media-wrap(.active) > __media  +  __content > sections */
        const mcol = d.createElement('div'); mcol.className = 'nectar-sticky-media-section__featured-media'; mcol.setAttribute('aria-hidden', 'true');
        const ccol = d.createElement('div'); ccol.className = 'nectar-sticky-media-section__content';
        secs.forEach((s, i) => {
          const bg = $(':scope > .nsms-bg', s), mw = d.createElement('div'), m = d.createElement('div');
          mw.className = i === 0 ? 'nectar-sticky-media-section__media-wrap active' : 'nectar-sticky-media-section__media-wrap';
          m.className = 'nectar-sticky-media-section__media';
          if (bg) { m.innerHTML = bg.innerHTML; $$('img', m).forEach(img => { img.alt = ''; img.loading = 'lazy'; img.decoding = 'async'; }); }
          mw.appendChild(m); mcol.appendChild(mw); ccol.appendChild(s);
        });
        box.appendChild(mcol); box.appendChild(ccol); box.classList.add('js-ready');
        /* the stacked (opacity 0) layers are fetched once the section is within one viewport, so no layer activates empty */
        const eagerIO = new IntersectionObserver(es => {
          if (!es.some(e => e.isIntersecting)) return;
          $$('img', mcol).forEach(img => { img.loading = 'eager'; });
          eagerIO.disconnect();
        }, { rootMargin: '100% 0px' });
        eagerIO.observe(box);
        let cur = -1;
        watchNear(box);
        onScroll(() => {
          if (!box._near) return null;
          let idx = 0, best = Infinity;
          secs.forEach((s, i) => { const r = s.getBoundingClientRect(), dd = Math.abs(r.top + r.height / 2 - vh / 2); if (dd < best) { best = dd; idx = i; } });
          if (idx === cur) return null;
          cur = idx;
          return () => { $$(':scope > .nectar-sticky-media-section__media-wrap', mcol).forEach((m, i) => m.classList.toggle('active', i === idx)); secs.forEach((s, i) => s.classList.toggle('active', i === idx)); };
        });
        return;
      }
      /* pinned / horizontal / layered types: sections live in .nectar-sticky-media-section__content__wrap */
      const wrap = d.createElement('div'); wrap.className = 'nectar-sticky-media-section__content__wrap';
      secs.forEach(s => wrap.appendChild(s));
      box.appendChild(wrap);
      if (type === 'horizontal-scrolling') {
        /* the content wrap is the sticky, translated strip; the element's height = strip height + horizontal distance */
        let dist = 0;
        const size = () => {
          const on = enabled();
          box.classList.toggle('nsms-off', !on);
          wrap.style.transform = '';
          if (!on) { box.style.height = ''; return; }
          dist = Math.max(0, wrap.scrollWidth - vw);
          box.style.height = `${wrap.offsetHeight + dist}px`;
        };
        size(); onResize(size);
        watchNear(box);
        onScroll(() => {
          if (!box._near || box.classList.contains('nsms-off')) return null;
          const r = box.getBoundingClientRect(), p = clamp(-r.top / Math.max(1, box.offsetHeight - wrap.offsetHeight), 0, 1);
          return () => { wrap.style.transform = `translate3d(${(-p * dist).toFixed(1)}px,0,0)`; };
        });
        return;
      }
      /* scroll-pinned-sections / layered-card-reveal */
      const effect = type === 'layered-card-reveal' ? 'scale' : (box.dataset.effect || 'none');
      const stacked = box.hasAttribute('data-stacked'), overlap = num(box.dataset.overlap, 50);
      const markers = secs.map(s => { const m = d.createElement('span'); m.className = 'nsms-marker'; m.setAttribute('aria-hidden', 'true'); s.before(m); return m; });
      let dots = [];
      if (box.hasAttribute('data-nav')) {
        const nav = d.createElement('nav'); nav.className = 'nsms-nav'; nav.setAttribute('aria-label', 'Skyriai');
        nav.innerHTML = '<ul>' + secs.map((s, i) => `<li><button type="button" aria-label="${(s.dataset.title || `Skyrius ${i + 1}`).replace(/"/g, '&quot;')}"></button></li>`).join('') + '</ul>';
        box.appendChild(nav);
        dots = $$('button', nav);
        dots.forEach((b, i) => b.addEventListener('click', () => scrollToEl(markers[i])));
      }
      const size = () => {
        const on = enabled();
        box.classList.toggle('nsms-off', !on);
        if (!on) secs.forEach(s => { s.style.removeProperty('--sc'); s.style.removeProperty('--bl'); s.style.removeProperty('--ty'); s.style.removeProperty('--fo'); });
      };
      size(); onResize(size);
      watchNear(box);
      let act = -1;
      onScroll(() => {
        if (!box._near || box.classList.contains('nsms-off')) return null;
        const rs = secs.map(s => s.getBoundingClientRect()), ms = markers.map(m => m.getBoundingClientRect().top);
        const top = rs.length ? parseFloat(getComputedStyle(secs[0]).top) || 0 : 0;
        const vals = secs.map((s, i) => {
          if (i === secs.length - 1) return 0;
          const h = rs[i].height || vh, nt = ms[i + 1];
          return clamp(1 - (nt - top) / h, 0, 1);
        });
        let idx = 0; ms.forEach((t, i) => { if (t <= top + 2) idx = i; });
        return () => {
          secs.forEach((s, i) => {
            const p = vals[i];
            let sc = 1, bl = 0, ty = 0, fo = 0;
            if (effect === 'scale' || effect === 'scale_blur' || effect === 'fade_scale') sc = 1 - 0.08 * p;
            if (effect === 'scale_blur') bl = 5 * p;
            if (effect === 'fade_scale') fo = 0.7 * p;
            if (effect === 'overlapping') { ty = -p * (rs[i].height || vh) * (overlap / 100) * 0.35; fo = 0.45 * p; }
            if (stacked && effect !== 'overlapping') ty = -54 * p;
            s.style.setProperty('--sc', sc.toFixed(4)); s.style.setProperty('--bl', `${bl.toFixed(2)}px`);
            s.style.setProperty('--ty', `${ty.toFixed(1)}px`); s.style.setProperty('--fo', fo.toFixed(3));
          });
          if (idx !== act && dots.length) { act = idx; dots.forEach((b, i) => { b.classList.toggle('active', i === idx); if (i === idx) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); }); }
        };
      });
    });
  }

  /* ================= 9 · init ================= */
  /* Back To Top Button: shown once scrolled past 350 px (desktop; Keep On Mobile off) */
  function initBackToTop() {
    const b = $('#to-top');
    if (!b) return;
    let on = false;
    onScroll(() => { const v = w.scrollY > 350; if (v === on) return null; on = v; return () => b.classList.toggle('visible', v); });
  }
  function init() {
    const steps = [initLenis, initAnchors, initHeader, initBackToTop, initOffCanvas, initBgVideos, initAnimatedText, initHighlighted,
      initScrollingText, initDividers, initMilestones, initButtons, initVideoLightbox, initContentTrail, initIcons,
      initLists, initCascading, initHotspots, initFancyBoxes, initGalleries, initToggles, initTabs, initPageSubmenu,
      initStickySections, initColumns, initBgAnimations, initClipPath, initParallax, initColorChange];
    steps.forEach(fn => { try { fn(); } catch (err) { if (w.console) console.error(`emul: ${fn.name}`, err); } });
    root.classList.add('nectar-ready');
    requestTick();
    w.addEventListener('load', () => { resizeFns.forEach(f => f()); requestTick(); });
    if (location.hash) {
      const t = d.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (t) setTimeout(() => scrollToEl(t), 120);
    }
  }
  w.nectarEmul = { refresh: () => { resizeFns.forEach(f => f()); requestTick(); }, scrollTo: scrollToEl, get lenis() { return lenis; } };
  if (d.readyState === 'loading') d.addEventListener('DOMContentLoaded', init); else init();
})();
