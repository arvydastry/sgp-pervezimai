/* =========================================================
   SGP v2 · sgp.js — shared runtime (Foundation-owned)
   One IIFE, feature-guarded modules. Page scripts (assets/js/pages/*.js) load after this
   file and use window.SGP (onFrame / onResize / io / lenis ...). See docs/build-notes/foundation.md
   ========================================================= */
(function () {
'use strict';
const d = document, root = d.documentElement;
const $ = (s, c = d) => c.querySelector(s);
const $$ = (s, c = d) => Array.from(c.querySelectorAll(s));
const mq = q => matchMedia(q);
const reduce = mq('(prefers-reduced-motion: reduce)').matches;
const deskMQ = mq('(min-width:1000px)');
const fine = mq('(hover:hover) and (pointer:fine)').matches;
const saveData = !!(navigator.connection && navigator.connection.saveData);
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
let vh = innerHeight, vw = innerWidth;
const frameFns = [], resizeFns = [];
const SGP = window.SGP = {
  $, $$, clamp, reduce, fine, saveData,
  desk: () => deskMQ.matches, vh: () => vh, vw: () => vw,
  onFrame: fn => { frameFns.push(fn); }, onResize: fn => { resizeFns.push(fn); },
  lenis: null,
  io(els, cb, opts) { const o = new IntersectionObserver(es => es.forEach(e => cb(e, o)), opts); [].concat(els).forEach(el => el && o.observe(el)); return o; }
};

/* =========== 1 · schedule — client mirror of tools/build.py Schedule ([sgp_grafikas]) =========== */
const MG = ['sausio', 'vasario', 'kovo', 'balandžio', 'gegužės', 'birželio', 'liepos', 'rugpjūčio', 'rugsėjo', 'spalio', 'lapkričio', 'gruodžio'];
const MA = ['SAUS.', 'VAS.', 'KOV.', 'BAL.', 'GEG.', 'BIRŽ.', 'LIEP.', 'RUGP.', 'RUGS.', 'SPAL.', 'LAPKR.', 'GRUOD.'];
const ORDER = ['lt-ie', 'lt-es', 'ie-lt', 'es-lt'];
const PH = '<svg class="sgp-i" aria-hidden="true"><use href="#i-phone"/></svg>';
const AR = '<svg class="sgp-i" aria-hidden="true"><use href="#i-arrow"/></svg>';
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const params = new URLSearchParams(location.search);
const qToday = params.get('siandien');
const todayISO = /^\d{4}-\d{2}-\d{2}$/.test(qToday || '') ? qToday : (() => {
  try { return new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Vilnius', year: 'numeric', month: '2-digit', day: '2-digit' }).format(new Date()); }
  catch (e) { return new Date().toISOString().slice(0, 10); }
})();
const dnum = iso => { const [y, m, dd] = iso.split('-').map(Number); return Math.round(Date.UTC(y, m - 1, dd) / 864e5); };
const T0 = dnum(todayISO);
const info = iso => { const [y, m, dd] = iso.split('-').map(Number); return { iso, y, m: m - 1, d: dd, diff: dnum(iso) - T0 }; };
const full = (x, up) => { const m = MG[x.m]; return (up ? m.charAt(0).toUpperCase() + m.slice(1) : m) + ' ' + x.d + ' d.'; };
const tile = x => String(x.d).padStart(2, '0') + ' ' + MA[x.m];
const rel = n => n === 0 ? 'šiandien' : n === 1 ? 'rytoj' : 'po ' + n + ' d.';
function joinDates(list) {
  const g = [];
  list.forEach(x => { const l = g[g.length - 1]; if (l && l.m === x.m) l.ds.push(x.d); else g.push({ m: x.m, ds: [x.d] }); });
  return g.map(o => MG[o.m] + ' ' + (o.ds.length > 1 ? o.ds.slice(0, -1).join(', ') + ' ir ' + o.ds[o.ds.length - 1] : o.ds[0]) + ' d.').join(', ');
}
const SCH = window.SGP_SCHEDULE || { routes: [] };
const R = {};
SCH.routes.forEach(r => {
  r.all = r.dates.slice().sort().map(info); r.up = r.all.filter(x => x.diff >= 0); r.next = r.up[0] || null;
  r.name = r.from + ' – ' + r.to; R[r.key] = r;
});
const keysOf = el => (el.dataset.routes || ORDER.join(',')).split(',').filter(k => R[k]);
const soonest = keys => keys.map(k => R[k]).filter(r => r.next).sort((a, b) => a.next.diff - b.next.diff || ORDER.indexOf(a.key) - ORDER.indexOf(b.key))[0] || null;
const aria = r => r.name + ': ' + (r.up.length ? joinDates(r.up) : 'grafikas atnaujinamas.') + ' Skambinti ' + r.tel_label;
const times = r => r.up.map((x, i) => `<time datetime="${x.iso}"${i === 0 ? ' class="is-next"' : ''}>${full(x, true)}</time>`).join('');
const EMPTY = 'Grafikas atnaujinamas – skambinkite';
const V = {
  board(keys) {
    const s = soonest(keys);
    return keys.map(k => {
      const r = R[k], n = r.next, isS = s && r === s, later = r.up.slice(1);
      return `<a class="sgp-bcell${isS ? ' is-soonest' : ''}" href="tel:${r.tel}" aria-label="${esc(aria(r))}">` +
        `<p class="sgp-bcell__dir sgp-mono" aria-hidden="true">${isS ? '<span class="sgp-dot"></span>Artimiausias' : (r.dir === 'out' ? 'Iš Lietuvos' : 'Į Lietuvą')}</p>` +
        `<p class="sgp-bcell__name" aria-hidden="true">${r.from} → ${r.to} ${PH}</p>` +
        `<p class="sgp-bnext" aria-hidden="true"><span class="sgp-flap" data-flap>${n ? tile(n) : '— —'}</span></p>` +
        `<p class="sgp-bdate" aria-hidden="true">${n ? `<time datetime="${n.iso}">${full(n, true)}</time> <span>· ${rel(n.diff)}</span>` : EMPTY}</p>` +
        (later.length ? `<p class="sgp-blater" aria-hidden="true">Vėliau: ${joinDates(later)}</p>` : '') + '</a>';
    }).join('');
  },
  timetable(keys) {
    const outs = keys.filter(k => R[k].dir === 'out').length;
    return keys.map(k => {
      const r = R[k];
      const lbl = r.dir === 'in' ? 'Iš ' + r.from_gen : (outs > 1 ? 'Į ' + r.to_acc : 'Iš Lietuvos');
      return `<li><a class="sgp-tt__row" href="tel:${r.tel}" aria-label="${esc(aria(r))}"><span class="sgp-tt__k sgp-mono" aria-hidden="true">${lbl}</span>` +
        `<span class="sgp-tt__v" aria-hidden="true">${r.up.length ? times(r) : '<span>' + EMPTY + '</span>'}</span><span class="sgp-tt__call" aria-hidden="true">${PH}</span></a></li>`;
    }).join('');
  },
  table(keys) {
    const s = soonest(keys);
    return [['Iš Lietuvos', 'out'], ['Į Lietuvą', 'in']].map(([title, dir]) => {
      const ks = keys.filter(k => R[k].dir === dir);
      if (!ks.length) return '';
      return `<div class="sgp-sched__grp"><p class="sgp-sched__h sgp-mono">${title}</p>` + ks.map(k => {
        const r = R[k], isS = s && r === s;
        const st = r.next ? (isS ? '<span class="sgp-dot"></span>Artimiausias · ' + rel(r.next.diff) : rel(r.next.diff)) : '—';
        return `<a class="sgp-sched__row${isS ? ' is-soonest' : ''}" href="tel:${r.tel}" aria-label="${esc(aria(r))}">` +
          `<span class="sgp-sched__name" aria-hidden="true">${r.from} → ${r.to}<span class="sgp-mono sgp-flap" data-flap>${r.code}</span></span>` +
          `<span class="sgp-sched__dates" aria-hidden="true">${r.up.length ? times(r) : '<span>' + EMPTY + '</span>'}</span>` +
          `<span class="sgp-sched__st sgp-mono" aria-hidden="true">${st}</span>` +
          `<span class="sgp-sched__tel" aria-hidden="true">${r.tel_label}${PH}</span></a>`;
      }).join('') + '</div>';
    }).join('');
  },
  ticker(keys, el) {
    const items = keys.map(k => R[k]).filter(r => r.next).sort((a, b) => a.next.diff - b.next.diff || ORDER.indexOf(a.key) - ORDER.indexOf(b.key)).slice(0, +(el.dataset.limit || 3));
    return items.length ? items.map((r, i) => `<li${i === 0 ? ' class="is-soon"' : ''}><b>${r.from} → ${r.to}</b> ${full(r.next)} · ${rel(r.next.diff)}</li>`).join('')
      : '<li><b>Grafikas atnaujinamas</b> · skambinkite</li>';
  },
  stub(keys, el) {
    const r = R[el.dataset.route]; if (!r) return el.innerHTML;
    const n = r.next;
    /* short label (never wraps in the 200 px stub); the direction moves to the mono meta line */
    return `<p class="sgp-mono">Kitas išvykimas</p><p class="sgp-ticket__date">${n ? `<time datetime="${n.iso}">${full(n, true)}</time>` : 'Grafikas atnaujinamas'}</p>` +
      `<p class="sgp-ticket__rel sgp-mono">${n ? 'iš LT · ' + rel(n.diff) : 'Skambinkite'}</p><a class="sgp-lnk" href="tel:${r.tel}" aria-label="Pervežimai į ${r.to_acc} – skambinti ${r.tel_label}">Skambinti${AR}</a>`;
  },
  lane(keys) {
    /* optional [sgp_grafikas variant="lane"] (/pervezimu-grafikas/ „Laiko juosta“; gr- classes are page-owned) */
    const routes = keys.map(k => R[k]);
    const maxDiff = Math.max(0, ...routes.map(r => (r.up.length ? r.up[r.up.length - 1].diff : 0)));
    const span = Math.max(21, Math.ceil((maxDiff + 4) / 7) * 7), X = d => Math.min(1, Math.max(0, d / span));
    const s = soonest(keys), weeks = [];
    for (let d = 7; d < span; d += 7) weeks.push(d);
    const axis = '<div class="gr-lane__axis sgp-mono"><span class="gr-lane__tick gr-lane__tick--0" style="--x:0">Šiandien</span>' +
      weeks.map(d => `<span class="gr-lane__tick" data-wk="${d}" style="--x:${X(d).toFixed(4)}">po ${d} d.</span>`).join('') + '</div>';
    const rows = routes.map((r, ri) => {
      const isS = s && r === s, last = r.up.length ? X(r.up[r.up.length - 1].diff) : 0;
      const wk = weeks.map(d => `<i class="gr-lane__wk" style="--x:${X(d).toFixed(4)}"></i>`).join('');
      const stops = r.up.map((x, i) => {
        const p = X(x.diff), cls = (i === 0 ? ' is-next' : '') + (isS && i === 0 ? ' is-soon' : '');
        return `<span class="gr-lane__stop${cls}" style="--x:${p.toFixed(4)};--dl:${(ri * 0.12 + 0.2 + p * 1.25).toFixed(2)}s"><i class="gr-ring"></i>` +
          `<span class="gr-lane__lbl"><span class="gr-lane__d">${full(x, true)}</span><span class="gr-lane__r sgp-mono">${rel(x.diff)}</span></span></span>`;
      }).join('');
      return `<div class="gr-lane__row${isS ? ' is-soonest' : ''}" style="--r:${ri}"><p class="gr-lane__name">${esc(r.from)} → ${esc(r.to)}<span class="sgp-mono">${esc(r.code)}</span></p>` +
        `<div class="gr-lane__track">${wk}<i class="gr-lane__base"></i><i class="gr-lane__line" style="--end:${last.toFixed(4)}"></i><i class="gr-lane__origin"></i>${stops}` +
        (r.up.length ? '' : '<span class="gr-lane__empty">' + EMPTY + '</span>') + '</div></div>';
    }).join('');
    return axis + '<div class="gr-lane__rows">' + rows + '</div>';
  },
  next(keys) {
    const s = soonest(keys);
    return '<span class="sgp-next__k sgp-mono"><span class="sgp-dot"></span>Artimiausias išvykimas</span><span class="sgp-next__v">' +
      (s ? `<b>${s.from} → ${s.to}</b> ${full(s.next)} <span class="sgp-next__rel">· ${rel(s.next.diff)}</span>` : EMPTY) + '</span>';
  }
};
/* the static build rendered the schedule for data-today; re-render only when the visitor's date differs */
if (SCH.routes.length && todayISO !== root.dataset.today) {
  $$('[data-sched]').forEach(el => { const fn = V[el.dataset.sched]; if (fn) el.innerHTML = fn(keysOf(el), el); });
}
SGP.schedule = { today: todayISO, routes: R, full, rel, joinDates, render: V };
/* ticker: items that do not fit are hidden (never truncated) */
function fitTicker() {
  $$('.sgp-tk .sgp-tk__list').forEach(tk => {
    const lis = $$('li', tk); lis.forEach(li => { li.hidden = false; });
    for (let i = lis.length - 1; i > 0 && tk.scrollWidth > tk.clientWidth + 1; i--) lis[i].hidden = true;
  });
}
fitTicker();
resizeFns.push(fitTicker);

/* =========== 2 · split-flap (§3.5, M14) — tiles everywhere, animation desktop-only, once, never phone numbers =========== */
const CH = 'ABCDEFGHIJKLMNOPRSTUVZĄČĘĖĮŠŲŪŽ0123456789';
function flapify(el) {
  if (el.classList.contains('is-tiled')) return;
  const txt = el.textContent.trim(); el.textContent = '';
  const sr = d.createElement('span'); sr.className = 'sgp-sr'; sr.textContent = txt; el.append(sr);
  [...txt].forEach(ch => {
    const s = d.createElement('span'); s.setAttribute('aria-hidden', 'true');
    if (ch === ' ') { s.className = 'sgp-fc sp'; s.textContent = ' '; } else { s.className = 'sgp-fc'; s.textContent = ch; s.dataset.c = ch; }
    el.append(s);
  });
  el.classList.add('is-tiled');
}
function flapRun(el) {
  if (reduce || !deskMQ.matches || el._ran) return; el._ran = true;
  $$('.sgp-fc:not(.sp)', el).forEach((s, i) => {
    const fin = s.dataset.c; let n = 4 + Math.floor(Math.random() * 4);
    setTimeout(function tick() {
      if (n-- > 0) { s.textContent = CH[Math.floor(Math.random() * CH.length)]; s.classList.remove('t'); void s.offsetWidth; s.classList.add('t'); setTimeout(tick, 55); }
      else s.textContent = fin;
    }, i * 42);
  });
}
$$('[data-flap]').forEach(flapify);
SGP.flap = { flapify, run: flapRun };

/* =========== 3 · text prep: word split (M22) · blur words (M52) · odometer reels (M26) =========== */
$$('[data-split]').forEach(el => {
  if (el.querySelector('.sgp-w,.sgp-bw')) return;
  const t = el.textContent.replace(/[ \t\r\n]+/g, ' ').trim();   /* U+00A0 stays inside its word */
  const blur = el.dataset.split === 'blur';
  /* a lone dash („ – “) never starts a line: it joins the previous word with a no-break space */
  const words = t.split(' ').reduce((a, w) => { if (/^[–—-]$/.test(w) && a.length) a[a.length - 1] += '\u00a0' + w; else a.push(w); return a; }, []);
  /* the text stays in the DOM once for screen readers (an sr-only span works on any element — aria-label is
     ignored on <p>); the animated word spans are aria-hidden */
  el.innerHTML = '<span class="sgp-sr">' + esc(t) + '</span>' + words.map((w, i) => blur
    ? `<span class="sgp-bw" aria-hidden="true" style="--i:${i}">${esc(w)}</span>`
    : `<span class="sgp-w" aria-hidden="true"><span style="--i:${i}">${esc(w)}</span></span>`).join(' ');
});
$$('[data-reel]').forEach(el => {
  const v = el.dataset.reel; el.setAttribute('role', 'img'); el.setAttribute('aria-label', v);
  el.innerHTML = [...v].map(ch => /\d/.test(ch)
    ? `<span class="sgp-reel" aria-hidden="true"><span style="--d:${ch}">${'0123456789'.split('').map(x => '<b>' + x + '</b>').join('')}</span></span>`
    : `<span aria-hidden="true">${esc(ch)}</span>`).join('');
});

/* =========== 4 · reveal — one IntersectionObserver adds .in (stand-in for Salient entrance animations) =========== */
$$('[data-stagger]').forEach(p => {
  const step = (+p.dataset.stagger || 120) / 1000;
  $$(':scope > [data-reveal], :scope > * > [data-reveal]', p).forEach((c, i) => { if (!c.style.getPropertyValue('--dl')) c.style.setProperty('--dl', (i * step).toFixed(3) + 's'); });
});
function revealNow(t) {
  t.classList.add('in');
  if (t.matches('[data-flap]')) flapRun(t);
  if (t.matches('[data-reveal]')) {
    const done = ev => { if (ev.target === t && ev.propertyName === 'opacity') { t.classList.add('is-done'); t.removeEventListener('transitionend', done); } };
    t.addEventListener('transitionend', done);
    setTimeout(() => t.classList.add('is-done'), 2600);
  }
}
const revealIO = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  revealNow(e.target); revealIO.unobserve(e.target);
}), { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });
function observeReveal(scope) {
  $$('[data-reveal],[data-split],[data-reel],[data-draw],.sgp-stations,.sgp-lane', scope || d).forEach(el => revealIO.observe(el));
  $$('[data-flap]', scope || d).forEach(el => { if (!el.closest('[data-hero]')) revealIO.observe(el); });
}
observeReveal();
/* masks observe their parent (clip-path hides the element itself) */
const maskIO = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  $$(':scope > [data-mask], :scope > * > [data-mask]', e.target).forEach(m => m.classList.add('in'));
  maskIO.unobserve(e.target);
}), { rootMargin: '0px 0px -12% 0px' });
new Set($$('[data-mask]').map(m => m.parentElement)).forEach(p => maskIO.observe(p));
SGP.reveal = observeReveal;
/* print: every reveal target reaches its end state (motion.css @media print does the same for shared classes) */
addEventListener('beforeprint', () => {
  $$('[data-reveal],[data-split],[data-reel],[data-draw],[data-mask],.sgp-stations,.sgp-lane').forEach(el => {
    el.classList.add('in'); if (el.matches('[data-reveal]')) el.classList.add('is-done'); revealIO.unobserve(el);
  });
});
requestAnimationFrame(() => requestAnimationFrame(() => {
  root.classList.add('ready');
  /* everything already inside the first viewport enters on load (the -12 % margin is for scrolling only) */
  $$('[data-reveal],[data-split],[data-reel],[data-draw],.sgp-stations,.sgp-lane').forEach(el => {
    if (el.classList.contains('in')) return;
    const r = el.getBoundingClientRect();
    if (r.top < innerHeight && r.bottom > 0 && getComputedStyle(el).display !== 'none') { revealNow(el); revealIO.unobserve(el); }
  });
  setTimeout(() => $$('[data-hero] [data-flap]').forEach(el => { el.classList.add('in'); flapRun(el); }), 700);
}));

/* =========== 5 · background videos (M16) — lazy, desktop only, pause off-screen, pause control (WCAG 2.2.2) =========== */
function srcFor(v) { if (!v.getAttribute('src')) v.src = (vw < 1280 && v.dataset.sd) ? v.dataset.sd : v.dataset.hd; }
/* no video bytes before window load: the poster, fonts and LCP come first (an eager hero video waits too) */
let pageLoaded = d.readyState === 'complete';
const afterLoad = [];
if (!pageLoaded) addEventListener('load', () => { pageLoaded = true; afterLoad.splice(0).forEach(fn => fn()); }, { once: true });
$$('video[data-bgvideo]').forEach(v => {
  const btns = v.id ? $$(`[data-video-toggle="${v.id}"]`) : [];
  const st = { paused: reduce || saveData, vis: false };
  const allowed = () => deskMQ.matches;
  const sync = () => btns.forEach(b => {
    b.setAttribute('aria-pressed', String(st.paused));
    const l = $('span', b); if (l) l.textContent = st.paused ? 'Leisti' : 'Pauzė';
    const u = $('use', b); if (u) u.setAttribute('href', st.paused ? '#i-play' : '#i-pause');
  });
  const play = () => {
    if (st.paused || !st.vis || !allowed()) return;
    if (!pageLoaded) { if (!afterLoad.includes(play)) afterLoad.push(play); return; }
    srcFor(v); const p = v.play(); if (p) p.catch(() => {});
  };
  v.addEventListener('playing', () => v.classList.add('is-playing'));
  btns.forEach(b => b.addEventListener('click', () => { st.paused = !st.paused; if (st.paused) v.pause(); else { st.vis = true; play(); } sync(); }));
  /* observe the video's own box (not its section): a video deep inside a tall section loads only near the
     viewport and pauses as soon as it has been scrolled past */
  new IntersectionObserver(([e]) => { st.vis = e.isIntersecting; if (st.vis) play(); else v.pause(); }, { rootMargin: '250px 0px' })
    .observe(v);
  deskMQ.addEventListener('change', () => { if (!allowed()) v.pause(); else play(); });
  sync();
});

/* =========== 6 · hover video (M33) — fine pointers, loaded on first hover =========== */
if (fine && !reduce && !saveData) {
  $$('[data-hover-video]').forEach(c => {
    const v = $('video', c); if (!v) return;
    c.addEventListener('pointerenter', () => {
      if (!deskMQ.matches) return;
      if (!v.getAttribute('src')) v.src = c.dataset.hoverVideo;
      const p = v.play(); if (p) p.then(() => c.classList.add('playing')).catch(() => {});
    });
    c.addEventListener('pointerleave', () => { v.pause(); c.classList.remove('playing'); });
  });
}

/* =========== 7 · header (M02–M05): glass on scroll, hide on scroll-down, recolour over light rows =========== */
const hdr = $('#sgp-hdr');
const callpanel = $('#sgp-call');
const menu = $('#sgp-menu'), burger = $('[data-menu-toggle]');
let lastY = scrollY, menuOpen = false, themed = [];
function collectThemed() { themed = $$('main > section, main > div > section, main > [data-theme], .sgp-ftr').filter(el => !el.closest('.sgp-menu')); }
collectThemed();
const callOpen = () => { try { return callpanel && callpanel.matches(':popover-open'); } catch (e) { return false; } };
/* read phase (rects, :focus-within) and write phase (classes, data-on — only on change) are split so the
   frame loop can batch every read before any write (§7.3) */
function readHeader(y) {
  if (!hdr) return null;
  let on = 'dark';
  if (!menuOpen) {
    const probe = y > 40 ? 32 : 60;
    for (const s of themed) {
      const b = s.getBoundingClientRect();
      if (b.top <= probe && b.bottom > probe) { on = s.dataset.theme || (s.classList.contains('on-light') ? 'light' : 'dark'); break; }
    }
  }
  return { y, on, keep: callOpen() || menuOpen || hdr.matches(':focus-within') };
}
function writeHeader(s) {
  if (!s) return;
  const { y } = s;
  hdr.classList.toggle('is-scrolled', y > 40);
  if (Math.abs(y - lastY) > 5) { hdr.classList.toggle('is-hidden', y > lastY && y > 360 && !s.keep); lastY = y; }
  if (hdr.dataset.on !== s.on) hdr.dataset.on = s.on;
}
function updHeader(y) { writeHeader(readHeader(y)); }
SGP.header = { update: () => updHeader(scrollY), recollect: collectThemed };

/* mega menu (§6.3): opens on :hover / :focus-within (CSS); Esc dismisses it (WCAG 1.4.13) until the pointer
   leaves or focus moves out of the menu item */
$$('.sgp-nav__mm').forEach(mm => {
  const top = $(':scope > a', mm);
  mm.addEventListener('keydown', e => {
    if (e.key !== 'Escape' || mm.classList.contains('is-closed')) return;
    mm.classList.add('is-closed');
    if (top && d.activeElement !== top) top.focus();
  });
  mm.addEventListener('pointerleave', () => mm.classList.remove('is-closed'));
  mm.addEventListener('focusout', e => { if (!mm.contains(e.relatedTarget)) mm.classList.remove('is-closed'); });
});

/* =========== 8 · switchboard popover (§4.2, M07) =========== */
if (callpanel) {
  callpanel.addEventListener('beforetoggle', e => {
    if (e.newState === 'open') { callpanel.style.top = deskMQ.matches && hdr ? (Math.round(hdr.getBoundingClientRect().bottom) + 8) + 'px' : ''; if (menuOpen) setMenu(false); }
  });
  /* production hook: any link to #sgp-call opens the popover */
  $$('a[href="#sgp-call"]').forEach(a => a.addEventListener('click', e => { e.preventDefault(); try { callpanel.togglePopover(); } catch (x) {} }));
  if (!HTMLElement.prototype.hasOwnProperty('popover')) {
    callpanel.style.display = 'none';
    $$('[popovertarget="sgp-call"]').forEach(b => b.addEventListener('click', () => {
      const o = callpanel.style.display === 'block';
      Object.assign(callpanel.style, { display: o ? 'none' : 'block', opacity: o ? 0 : 1, transform: 'none', zIndex: 1000 });
    }));
  }
}

/* =========== 9 · off-canvas menu (§4.3, M08) — focus trap, Esc, Lenis paused =========== */
function setMenu(o) {
  if (!menu || !burger) return;
  menuOpen = o;
  if (SGP.lenis) { o ? SGP.lenis.stop() : SGP.lenis.start(); }
  /* scroll lock on the root: html has overflow-x:clip, so body's overflow never reaches the viewport */
  root.classList.toggle('menu-open', o);
  d.body.classList.toggle('menu-open', o);
  menu.setAttribute('aria-hidden', String(!o));
  if (o) menu.removeAttribute('inert'); else menu.setAttribute('inert', '');
  burger.setAttribute('aria-expanded', String(o));
  burger.setAttribute('aria-label', o ? 'Uždaryti meniu' : 'Meniu');
  const u = $('use', burger); if (u) u.setAttribute('href', o ? '#i-close' : '#i-menu');
  if (o) { try { callpanel && callpanel.hidePopover(); } catch (e) {} setTimeout(() => { const a = $('.sgp-menu__nav a', menu); if (a) a.focus(); }, 60); }
  updHeader(scrollY);
}
if (menu && burger) {
  menu.setAttribute('inert', '');
  burger.addEventListener('click', () => setMenu(!menuOpen));
  $$('a', menu).forEach(a => a.addEventListener('click', () => setMenu(false)));
  d.addEventListener('keydown', e => {
    if (!menuOpen) return;
    if (e.key === 'Escape') { setMenu(false); burger.focus(); return; }
    if (e.key === 'Tab') {
      const f = [burger].concat($$('a,button', menu)).filter(x => x.offsetParent !== null || x === burger);
      const i = f.indexOf(d.activeElement);
      if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
    }
  });
}
SGP.menu = { open: () => setMenu(true), close: () => setMenu(false), isOpen: () => menuOpen };

/* =========== 10 · rail stops (§3.4, M31, M34) — [data-stops] > [data-stop] get .is-reached; [data-stop-count] counts =========== */
$$('[data-stops]').forEach(box => { const io = stopObserver(box); $$('[data-stop]', box).forEach(x => io.observe(x)); });
function stopObserver(box) {
  if (box._io) return box._io;
  const stops = $$('[data-stop]', box), counter = $('[data-stop-count]', box);
  box._io = new IntersectionObserver(es => {
    es.forEach(e => { const r = e.boundingClientRect, Rb = e.rootBounds || { left: 0, top: 0 }; e.target.classList.toggle('is-reached', e.isIntersecting || r.right < Rb.left || r.bottom < Rb.top); });
    if (counter) counter.textContent = String(Math.max(1, stops.filter(s => s.classList.contains('is-reached')).length)).padStart(2, '0');
  }, { rootMargin: '0px -30% -30% 0px' });
  return box._io;
}

/* =========== 11 · tabs (Salient Tabs emulation, M40) — [data-tabs] with role=tablist/tab/tabpanel =========== */
$$('[data-tabs]').forEach(box => {
  const tabs = $$('[role=tab]', box);
  const panel = t => d.getElementById(t.getAttribute('aria-controls'));
  function select(t, focus, fromHash) {
    tabs.forEach(x => {
      const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1;
      const p = panel(x); if (p) { p.hidden = !on; if (on) { p.classList.remove('is-shown'); void p.offsetWidth; p.classList.add('is-shown'); } }
    });
    if (focus) t.focus();
    if (t.dataset.hash && !fromHash && history.replaceState) history.replaceState(null, '', '#' + t.dataset.hash);
    box.dispatchEvent(new CustomEvent('sgp:tab', { detail: { tab: t } }));
  }
  tabs.forEach((t, i) => {
    t.addEventListener('click', () => select(t));
    t.addEventListener('keydown', e => {
      let n = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') n = tabs[(i + 1) % tabs.length];
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') n = tabs[(i - 1 + tabs.length) % tabs.length];
      else if (e.key === 'Home') n = tabs[0]; else if (e.key === 'End') n = tabs[tabs.length - 1];
      if (n) { e.preventDefault(); select(n, true); }
    });
  });
  const h = location.hash.slice(1), hit = h && tabs.find(t => t.dataset.hash === h);
  if (hit) select(hit, false, true);
});

/* =========== 12 · accordion = Toggle Panels (M60, M62) — [data-acc] (single open) / [data-acc="multi"] =========== */
$$('[data-acc]').forEach(box => {
  const multi = box.dataset.acc === 'multi';
  const items = $$('.sgp-acc__item', box);
  function set(item, open) {
    const b = $('.sgp-acc__btn', item); item.classList.toggle('is-open', open); if (b) b.setAttribute('aria-expanded', String(open));
    /* inert, not aria-hidden: a collapsed panel (0fr + overflow hidden) must also leave the Tab order */
    const p = $('.sgp-acc__panel', item); if (p) { p.inert = !open; p.removeAttribute('aria-hidden'); }
  }
  items.forEach(item => {
    $$('.sgp-xlist li', item).forEach((li, i) => li.style.setProperty('--xi', i));
    set(item, item.classList.contains('is-open'));
    const b = $('.sgp-acc__btn', item);
    if (b) b.addEventListener('click', () => {
      const open = !item.classList.contains('is-open');
      if (!multi && open) items.forEach(x => x !== item && set(x, false));
      set(item, open);
    });
  });
  const h = location.hash.slice(1);
  if (h) { const t = d.getElementById(h); const it = t && t.closest('.sgp-acc__item'); if (it && box.contains(it)) { if (!multi) items.forEach(x => set(x, false)); set(it, true); } }
});

/* =========== 13 · scroll spy — submenu / sticky index / sticky media (M61, M63, M64, M83) ===========
   data-spy           IntersectionObserver band 45–50 % of the viewport; nothing is active while the first
                      target is still below the band (visitor scrolled back up to the hero)
   data-spy="scroll"  the last target whose top is above the viewport middle, computed in the rAF loop —
                      for sticky / stacked targets (IO never re-fires for a stuck element)
   Active link: aria-current + li.is-active; earlier links: li.is-past; [data-spy-for="<id>"]: .is-active;
   [data-spy-count] inside the nav shows the 01-based position of the active target. */
const spies = [];
$$('[data-spy]').forEach(nav => {
  const links = $$('a[href^="#"]', nav).filter(a => a.getAttribute('href').length > 1);
  const idOf = a => decodeURIComponent(a.getAttribute('href').slice(1));
  const targets = links.map(a => d.getElementById(idOf(a))).filter(Boolean);
  if (!targets.length) return;
  const ids = targets.map(t => t.id), media = $$('[data-spy-for]').filter(el => ids.includes(el.dataset.spyFor));
  const count = $('[data-spy-count]', nav);
  let cur;
  const setActive = id => {
    if (id === cur) return; cur = id;
    const ai = id ? ids.indexOf(id) : -1;
    links.forEach(a => {
      const k = ids.indexOf(idOf(a)), on = id !== null && k === ai;
      if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
      const li = a.closest('li'); if (li) { li.classList.toggle('is-active', on); li.classList.toggle('is-past', k > -1 && k < ai); }
      if (on && nav.scrollWidth > nav.clientWidth) { const sc = a.closest('ul,ol') || nav; sc.scrollTo({ left: a.offsetLeft - 24, behavior: reduce ? 'auto' : 'smooth' }); }
    });
    media.forEach(el => el.classList.toggle('is-active', el.dataset.spyFor === id));
    if (count) count.textContent = String(Math.max(1, ai + 1)).padStart(2, '0');
  };
  if (nav.dataset.spy === 'scroll') { spies.push({ targets, setActive, all: true }); return; }
  /* IO mode: the band picks the active target; the frame loop only clears it above the first chapter
     (IO alone misses that after a jump to the top — the first target never crosses the band) */
  spies.push({ targets, setActive, all: false });
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) setActive(e.target.id); }), { rootMargin: '-45% 0px -50% 0px' });
  targets.forEach(t => io.observe(t));
});
/* read phase → returns the write phase (setActive only writes when the active target changes) */
function spyRead() {
  const line = vh * 0.5, out = [];
  spies.forEach(sp => {
    if (!sp.all) { if (sp.targets[0].getBoundingClientRect().top > line) out.push([sp, null]); return; }
    let id = null; for (const t of sp.targets) if (t.getBoundingClientRect().top < line) id = t.id;
    out.push([sp, id]);
  });
  return () => out.forEach(([sp, id]) => sp.setActive(id));
}

/* =========== 14 · forms (§4.14, M71, M72) — demo: validate, never submit, no network =========== */
/* Name = the .sgp-field__l span only (aria-labelledby), so the <em> error inside the <label> never joins it.
   The error is referenced by aria-describedby only while the field is in error (a display:none element
   referenced by aria-describedby is still announced). */
let uid = 0;
const refs = (i, attr) => (i.getAttribute(attr) || '').split(/\s+/).filter(Boolean);
function fieldError(f, bad) {
  const i = f && $('input,select,textarea', f), er = f && $('.sgp-field__err', f);
  if (f) f.classList.toggle('is-err', bad);
  if (!i) return;
  i.setAttribute('aria-invalid', String(bad));
  if (!er) return;
  const ids = refs(i, 'aria-describedby').filter(x => x !== er.id);
  if (bad) ids.push(er.id);
  if (ids.length) i.setAttribute('aria-describedby', ids.join(' ')); else i.removeAttribute('aria-describedby');
}
$$('form[data-demo-form], form[data-track]').forEach(form => $$('.sgp-field', form).forEach(f => {
  const i = $('input,select,textarea', f), er = $('.sgp-field__err', f), l = $('.sgp-field__l', f);
  if (i && er) er.id = er.id || 'sgp-err-' + (++uid);
  if (i && l && !i.hasAttribute('aria-labelledby')) { l.id = l.id || 'sgp-lbl-' + (++uid); i.setAttribute('aria-labelledby', l.id); }
}));
$$('form[data-demo-form]').forEach(form => {
  $$('.sgp-field', form).forEach(f => {
    const i = $('input,select,textarea', f);
    if (i) i.addEventListener('input', () => { if (i.checkValidity()) fieldError(f, false); });
  });
  const pre = params.get('domina'), sel = $('select[data-domina]', form);
  if (pre && sel) { const o = [...sel.options].find(x => x.text === pre); sel.value = o ? o.text : 'Kita'; }
  form.addEventListener('submit', e => {
    e.preventDefault(); let ok = true;
    $$('.sgp-field', form).forEach(f => {
      const i = $('input,select,textarea', f); if (!i) return;
      const bad = !i.checkValidity(); fieldError(f, bad);
      if (bad && ok) { ok = false; i.focus(); }
    });
    form.classList.toggle('is-sent', ok);
    if (ok) { const box = $('.sgp-form__ok', form); if (box) box.focus(); form.dispatchEvent(new CustomEvent('sgp:sent')); }
  });
});
/* copy e-mail (M73) */
$$('[data-copy]').forEach(b => b.addEventListener('click', () => {
  const t = b.dataset.copy, s = b.parentElement && $('[data-copy-status]', b.parentElement), l = $('span', b);
  const done = () => {
    b.classList.add('is-done'); if (l) l.textContent = 'Nukopijuota'; if (s) s.textContent = 'El. pašto adresas nukopijuotas';
    setTimeout(() => { b.classList.remove('is-done'); if (l) l.textContent = 'Kopijuoti'; }, 2400);
  };
  (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(done).catch(() => { if (s) s.textContent = t; });
}));
/* tracking field (§4.15): empty submit → verbatim tool error; otherwise GET to our own /siuntos-sekimas/?kodas=
   Every submit dispatches `sgp:track` (detail.code) on the form; a page that calls preventDefault() on a non-empty
   code takes over (the tracking page runs its demo lookup) and the GET is cancelled. */
const trackParts = form => ({ f: $('.sgp-field', form), i: $('input', form), er: $('.sgp-field__err', form) });
function trackError(form, msg) {
  const { f, i, er } = trackParts(form);
  if (er) { if (!er.dataset.msg) er.dataset.msg = er.textContent; er.textContent = msg || er.dataset.msg; }
  if (f) fieldError(f, true); else if (i) i.setAttribute('aria-invalid', 'true');
}
function trackClear(form) {
  const { f, i, er } = trackParts(form);
  if (f) fieldError(f, false); else if (i) i.setAttribute('aria-invalid', 'false');
  if (er && er.dataset.msg) er.textContent = er.dataset.msg;
}
SGP.track = { error: trackError, clear: trackClear };
$$('form[data-track]').forEach(form => {
  const i = $('input', form);
  form.addEventListener('submit', e => {
    const code = i ? i.value.trim() : '';
    if (!code) { e.preventDefault(); trackError(form); if (i) i.focus(); }
    const ev = new CustomEvent('sgp:track', { cancelable: true, detail: { code } });
    if (!form.dispatchEvent(ev) && code) e.preventDefault();
  });
  if (i) i.addEventListener('input', () => trackClear(form));
});

/* =========== 15 · rail end (§3.1): the lane stops at the terminus ring =========== */
function sizeRailEnd() {
  $$('.sgp-rail-end').forEach(sec => { const wp = $('[data-rail-end]', sec); if (!wp) return;
    sec.style.setProperty('--rail-end', Math.round(wp.getBoundingClientRect().top - sec.getBoundingClientRect().top + wp.offsetHeight / 2) + 'px'); });
}

/* =========== 16 · cookie bar (§4.24) — remembered per browser (try/catch) =========== */
const cookie = $('#sgp-cookie');
if (cookie) {
  let seen = null; try { seen = localStorage.getItem('sgp-cookie'); } catch (e) {}
  /* demo: shown after the first real scroll so the hero + departure board stay clear on first view */
  if (!seen) { const show = () => { if (scrollY > innerHeight * 0.5) { cookie.hidden = false; removeEventListener('scroll', show); } }; addEventListener('scroll', show, { passive: true }); }
  $$('[data-cookie]', cookie).forEach(b => b.addEventListener('click', () => { try { localStorage.setItem('sgp-cookie', b.dataset.cookie); } catch (e) {} cookie.hidden = true; }));
}
SGP.cookie = {
  open() { if (!cookie) return; try { localStorage.removeItem('sgp-cookie'); } catch (e) {} cookie.hidden = false; const b = $('button', cookie); if (b) b.focus(); }
};

/* =========== 17 · developer overlay „Salient žymės“ (§4.27) ===========
   Tags live in ONE fixed layer (body > .sgp-stags), placed from each element's rect in the frame loop (read phase
   → write phase) and every 400 ms while on: never clipped by an overflow:hidden host, readable width, clamped to
   the viewport; a tall element's tag sticks to the top while the element is on screen; a tag that would cover an
   earlier one moves down below it. */
const tagBtn = $('#sgp-tagbtn');
const tags = { on: false, layer: null, list: [], timer: 0 };
const shown = el => el.checkVisibility ? el.checkVisibility({ opacityProperty: true, visibilityProperty: true })
  : (getComputedStyle(el).visibility !== 'hidden' && (el.offsetParent !== null || getComputedStyle(el).position === 'fixed'));
function tagsMeasure() { tags.list.forEach(t => { t.w = t.s.offsetWidth; t.h = t.s.offsetHeight; }); }
function tagsBuild() {
  const layer = tags.layer = d.createElement('div');
  layer.className = 'sgp-stags'; layer.setAttribute('aria-hidden', 'true');
  tags.list = $$('[data-salient]').filter(el => !el.matches('[popover]') && !el.closest('.sgp-menu')).map(el => {
    const s = d.createElement('span'); s.className = 'sgp-stag'; s.textContent = el.dataset.salient; layer.append(s);
    return { el, s, w: 0, h: 0, vis: null };
  });
  d.body.append(layer);
  tagsMeasure();
}
function tagsRead() {
  if (!tags.on || !tags.layer) return null;
  const cw = root.clientWidth, M = 8;
  const rects = tags.list.map(t => (shown(t.el) ? t.el.getBoundingClientRect() : null));
  return () => {
    const placed = [];
    tags.list.forEach((t, k) => {
      const r = rects[k], on = !!r && (r.width > 0 || r.height > 0) && r.bottom > 0 && r.top < vh;
      if (on !== t.vis) { t.s.style.visibility = on ? '' : 'hidden'; t.vis = on; }
      if (!on) return;
      const x = Math.max(M, Math.min(r.left + M, cw - t.w - M));
      let y = r.top + M;
      if (y < M) y = Math.min(M, r.bottom - t.h - M);          /* sticky label while a tall element is on screen */
      for (let n = 0; n < 60; n++) {
        const hit = placed.find(p => x < p.x + p.w && x + t.w > p.x && y < p.y + p.h && y + t.h > p.y);
        if (!hit) break;
        y = hit.y + hit.h + 4;
      }
      placed.push({ x, y, w: t.w, h: t.h });
      t.s.style.transform = `translate(${Math.round(x)}px,${Math.round(y)}px)`;
    });
  };
}
function tagsUpdate() { const w = tagsRead(); if (w) w(); }
if (tagBtn) tagBtn.addEventListener('click', () => {
  tags.on = tagBtn.getAttribute('aria-pressed') !== 'true'; tagBtn.setAttribute('aria-pressed', String(tags.on));
  clearInterval(tags.timer);
  if (tags.layer) { tags.layer.remove(); tags.layer = null; tags.list = []; }
  if (!tags.on) return;
  tagsBuild(); tagsUpdate();
  tags.timer = setInterval(tagsUpdate, 400);
});
SGP.tags = { update: tagsUpdate };

/* =========== 18 · scroll-linked motion — ONE rAF loop (≥1000 px, motion allowed) =========== */
/* data-parallax="0.18": translateY = −(distance of the parent's centre from the viewport centre) × speed
   data-scroll-scale: scale .88 → 1 and y 40 → 0 px while the parent enters (M66)
   data-stack: .sgp-stack__item i gets --sp 0 → 1 while item i+1 slides over it (M63) */
const motionOK = () => deskMQ.matches && !reduce;
const movers = [];
$$('[data-parallax]').forEach(el => movers.push({ el, ref: el.parentElement, s: parseFloat(el.dataset.parallax) || 0.15, on: false }));
$$('[data-scroll-scale]').forEach(el => movers.push({ el, ref: el.parentElement, scale: true, on: false }));
const visIO = new IntersectionObserver(es => es.forEach(e => { (e.target._sgpMovers || []).forEach(o => { o.on = e.isIntersecting; }); }), { rootMargin: '30% 0px' });
movers.forEach(o => { (o.ref._sgpMovers = o.ref._sgpMovers || []).push(o); visIO.observe(o.ref); });
const stacks = $$('[data-stack]').map(box => ({ box, items: $$('.sgp-stack__item', box), tops: [] }));
function measureStacks() {
  stacks.forEach(s => { s.items.forEach((it, i) => { it.style.setProperty('--i', i); }); s.tops = s.items.map(it => parseFloat(getComputedStyle(it).top) || 0); });
}
/* read phase → returns the write phase */
function motionRead() {
  if (!motionOK()) return null;
  const reads = [];
  for (const o of movers) if (o.on) reads.push([o, o.ref.getBoundingClientRect()]);
  const sreads = stacks.map(s => s.items.map(it => it.getBoundingClientRect().top));
  return () => motionWrite(reads, sreads);
}
function motionWrite(reads, sreads) {
  for (const [o, r] of reads) {
    if (o.scale) {
      const p = clamp((vh - r.top) / (vh * 0.7));
      o.el.style.transform = `translate3d(0,${(40 * (1 - p)).toFixed(1)}px,0) scale(${(0.88 + 0.12 * p).toFixed(4)})`;
    } else {
      const off = (r.top + r.height / 2) - vh / 2;
      o.el.style.transform = `translate3d(0,${(-off * o.s).toFixed(1)}px,0)`;
    }
  }
  stacks.forEach((s, si) => s.items.forEach((it, i) => {
    if (i === s.items.length - 1) return;
    const nextTop = sreads[si][i + 1], stick = s.tops[i + 1], start = vh * 0.9;
    it.style.setProperty('--sp', clamp((start - nextTop) / Math.max(1, start - stick)).toFixed(3));
  }));
}

/* =========== 19 · the loop: header + motion + page hooks (SGP.onFrame) =========== */
/* Reads first, writes last (§7.3): shared reads (header probe, movers, stacks, spies) → page hooks → shared
   writes → deferred page writes. A page hook may return a function: it runs in the write phase, after every
   hook has read (hooks that still read + write inline keep working, they just cost their own layout). */
let ticking = false;
function frame() {
  ticking = false; const y = scrollY;
  const hs = readHeader(y), mw = motionRead(), sw = spyRead(), tw = tagsRead();
  const later = [];
  frameFns.forEach(fn => { const w = fn(y); if (typeof w === 'function') later.push(w); });
  writeHeader(hs); if (mw) mw(); sw(); if (tw) tw();
  later.forEach(w => w());
}
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }, { passive: true });
function onResize() { vh = innerHeight; vw = innerWidth; collectThemed(); sizeRailEnd(); measureStacks(); if (tags.on) tagsMeasure(); resizeFns.forEach(fn => fn()); frame(); }
let rT = 0;
addEventListener('resize', () => { clearTimeout(rT); rT = setTimeout(onResize, 120); });
addEventListener('load', onResize);
if (d.fonts && d.fonts.ready) d.fonts.ready.then(onResize);
deskMQ.addEventListener('change', onResize);
SGP.refresh = onResize;

/* =========== 20 · Lenis smooth scroll (M01) + in-page anchors =========== */
/* fine pointers only: on touch devices Lenis would add non-passive touch listeners to window and, while stopped
   (menu open), preventDefault every touchmove — phones and tablets keep native scrolling */
function initLenis() {
  if (reduce || !fine || !window.Lenis || SGP.lenis) return;
  const l = new window.Lenis({ lerp: 0.1, smoothWheel: true });
  SGP.lenis = l;
  (function raf(t) { l.raf(t); requestAnimationFrame(raf); })(performance.now());
}
initLenis();
/* a stuck card (.sgp-stack__item, position:sticky) reports its stuck position: jump to where it sticks in the natural flow */
function naturalY(t) {
  const it = t.closest && t.closest('.sgp-stack__item');
  if (!it || getComputedStyle(it).position !== 'sticky') return null;
  const box = it.parentElement, gap = parseFloat(getComputedStyle(box).rowGap) || 0;
  let y = box.getBoundingClientRect().top + scrollY;
  for (const c of box.children) { if (c === it) break; y += c.offsetHeight + gap; }
  const inner = t === it ? 0 : t.getBoundingClientRect().top - it.getBoundingClientRect().top;
  return Math.max(0, Math.round(y + inner - (parseFloat(getComputedStyle(it).top) || 0)));
}
d.addEventListener('click', e => {
  const a = e.target.closest && e.target.closest('a[href^="#"]');
  if (!a || e.defaultPrevented) return;
  const id = a.getAttribute('href'); if (id.length < 2 || id === '#sgp-call') return;
  const t = d.getElementById(decodeURIComponent(id.slice(1))); if (!t) return;
  e.preventDefault();
  const it = t.closest('.sgp-acc__item'); if (it && !it.classList.contains('is-open')) { const b = $('.sgp-acc__btn', it); if (b) b.click(); }
  const off = -((hdr ? hdr.querySelector('.sgp-bar').offsetHeight : 64) + 12), ny = naturalY(t);
  if (ny !== null) { if (SGP.lenis) SGP.lenis.scrollTo(ny, { duration: 1.2 }); else scrollTo({ top: ny, behavior: reduce ? 'auto' : 'smooth' }); }
  else if (SGP.lenis) SGP.lenis.scrollTo(t, { offset: off, duration: 1.2 });
  else scrollTo({ top: t.getBoundingClientRect().top + scrollY + off, behavior: reduce ? 'auto' : 'smooth' });
  if (!t.hasAttribute('tabindex') && !/^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(t.tagName)) t.setAttribute('tabindex', '-1');
  t.focus({ preventScroll: true });
  if (history.replaceState && id !== '#main') history.replaceState(null, '', id);
});

sizeRailEnd(); measureStacks(); frame();
})();
