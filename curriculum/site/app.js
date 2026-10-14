(() => {
  'use strict';

  const $ = (sel, el = document) => el.querySelector(sel);
  const LEVELS = ['Foundation', 'Core: Cloud Foundry', 'Developer: CAP / Fiori focus', 'Advanced / Admin', 'Optional / Reference-only'];
  const STATUS_CLASS = { 'not started': 'notstarted', 'in progress': 'inprogress', 'done': 'done' };
  const DARK = window.matchMedia('(prefers-color-scheme: dark)').matches;

  let state = { modules: [], done: 0, total: 0 };
  let renderedPath = null;   // path of the document currently on screen ('' = home)

  marked.use({ gfm: true });
  mermaid.initialize({
    startOnLoad: false,
    theme: DARK ? 'dark' : 'default',
    securityLevel: 'strict',
    flowchart: { htmlLabels: true, curve: 'basis' },
  });

  // ---------- helpers ----------
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);
  const slug = (s) => s.toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu, '').trim().replace(/\s+/g, '-').replace(/-+/g, '-');

  function splitOnce(s, ch) {
    const i = s.indexOf(ch);
    return i < 0 ? [s, ''] : [s.slice(0, i), s.slice(i + 1)];
  }

  function resolvePath(baseDir, rel) {
    const parts = rel.startsWith('/') ? [] : baseDir.split('/').filter(Boolean);
    for (const p of rel.split('/')) {
      if (!p || p === '.') continue;
      if (p === '..') parts.pop(); else parts.push(p);
    }
    return parts.join('/');
  }

  function currentRoute() {
    const raw = decodeURIComponent(location.hash.replace(/^#\/?/, ''));
    const [path, frag] = splitOnce(raw, '#');
    return { path, frag };
  }

  const moduleFor = (path) => state.modules.find((m) => m.lesson === path);

  function toast(msg) {
    const t = $('#toast');
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(toast._t);
    toast._t = setTimeout(() => t.classList.remove('show'), 2200);
  }

  // ---------- status / progress ----------
  async function loadStatus() {
    try {
      const r = await fetch('/api/status', { cache: 'no-store' });
      if (!r.ok) throw new Error(String(r.status));
      state = await r.json();
    } catch (e) {
      state = { modules: [], done: 0, total: 0, error: true };
    }
    renderNav();
    renderOverall();
  }

  async function setStatus(id, status) {
    try {
      const r = await fetch('/api/progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'X-Requested-With': 'btp-study' },
        body: JSON.stringify({ id, status }),
      });
      if (!r.ok) throw new Error((await r.json().catch(() => ({}))).error || r.status);
    } catch (e) {
      toast('Could not save: ' + e.message);
      return;
    }
    await loadStatus();
    toast(status === 'done' ? `${id} marked as done` : `${id} is now ${status}`);
    if (renderedPath === 'curriculum/progress.md') { renderedPath = null; route(); }
    else if (renderedPath !== null) { renderBanner(renderedPath); }
  }

  function renderOverall() {
    const pct = state.total ? Math.round((100 * state.done) / state.total) : 0;
    $('#overall').innerHTML = `<span>${state.done} / ${state.total} done</span><div class="bar"><span style="width:${pct}%"></span></div>`;
  }

  // ---------- sidebar ----------
  function renderNav() {
    if (state.error) {
      $('#moduleNav').innerHTML = '<p class="tips">Could not load progress. Start the site with <code>serve.py</code>.</p>';
      return;
    }
    const q = $('#filter').value.trim().toLowerCase();
    const byLevel = {};
    for (const m of state.modules) (byLevel[m.level] ||= []).push(m);
    const levels = [...LEVELS.filter((l) => byLevel[l]), ...Object.keys(byLevel).filter((l) => !LEVELS.includes(l))];
    let html = '';
    levels.forEach((lvl, i) => {
      const all = byLevel[lvl];
      const mods = all.filter((m) => !q || `${m.id} ${m.title}`.toLowerCase().includes(q));
      if (!mods.length) return;
      const d = all.filter((m) => m.status === 'done').length;
      html += `<div class="level-title"><span>L${i + 1} · ${esc(lvl)}</span><span>${d}/${all.length}</span></div>`;
      for (const m of mods) {
        const tip = m.exists ? m.title : `${m.title} (lesson not written yet)`;
        html += `<a class="mod-link${m.exists ? '' : ' missing'}" data-route="${esc(m.lesson)}" href="#/${esc(m.lesson)}" title="${esc(tip)}">`
          + `<span class="dot ${STATUS_CLASS[m.status] || ''}"></span>`
          + `<span class="mod-id">${esc(m.id.slice(1))}</span><span class="mod-title">${esc(m.title)}</span></a>`;
      }
    });
    $('#moduleNav').innerHTML = html || '<p class="tips">No modules match.</p>';
    markActive();
  }

  function markActive() {
    const { path } = currentRoute();
    document.querySelectorAll('[data-route]').forEach((a) => a.classList.toggle('active', a.dataset.route === path));
    const act = $('#moduleNav .active');
    if (act) act.scrollIntoView({ block: 'nearest' });
  }

  // ---------- home ----------
  function renderHome() {
    renderedPath = '';
    document.title = 'BTP Study';
    $('#crumb').textContent = 'Home';
    $('#banner').innerHTML = '';
    $('#pager').innerHTML = '';
    $('#toc').innerHTML = '';
    const mods = state.modules;
    const written = mods.filter((m) => m.exists).length;
    const next = mods.find((m) => m.status === 'in progress') || mods.find((m) => m.status !== 'done');

    let html = `<div class="hero"><h1>SAP BTP learning path</h1>`
      + `<p>${state.done} of ${state.total} modules done · ${written} lesson${written === 1 ? '' : 's'} written so far</p></div>`;

    if (next) {
      html += `<div class="continue"><div class="grow">`
        + `<div class="label">${next.status === 'in progress' ? 'Continue' : 'Up next'}</div>`
        + `<div class="title">${esc(next.id)} · ${esc(next.title)}</div>`
        + `<div class="tips">${esc(next.level)}${next.exists ? '' : ' · lesson not written yet (say “next” to Claude)'}</div>`
        + `</div><a class="btn primary" href="#/${esc(next.lesson)}">${next.exists ? 'Open lesson' : 'View'}</a></div>`;
    } else if (mods.length) {
      html += `<div class="continue"><div class="grow"><div class="label">Finished</div><div class="title">All modules done. Well done!</div></div></div>`;
    }

    html += '<h2>Levels</h2><div class="cards">';
    const byLevel = {};
    for (const m of mods) (byLevel[m.level] ||= []).push(m);
    LEVELS.filter((l) => byLevel[l]).forEach((lvl, i) => {
      const all = byLevel[lvl];
      const d = all.filter((m) => m.status === 'done').length;
      const first = all.find((m) => m.status !== 'done') || all[0];
      html += `<div class="card"><h3>L${i + 1} · ${esc(lvl)}</h3>`
        + `<div class="meta">${d} / ${all.length} done · ${esc(all[0].id)}–${esc(all[all.length - 1].id)}</div>`
        + `<div class="bar"><span style="width:${Math.round((100 * d) / all.length)}%"></span></div>`
        + `<p style="margin:12px 0 0;font-size:14px"><a href="#/${esc(first.lesson)}">${esc(first.id)} · ${esc(first.title)}</a></p></div>`;
    });
    html += '</div>';

    html += `<h2>How to use this site</h2><ul class="tips">`
      + `<li>Work through modules in order. Each lesson ends with interview Q&amp;A, customer questions and a quiz.</li>`
      + `<li>Use <strong>Start module</strong> and <strong>Mark as done</strong> at the top of a lesson. They update <code>curriculum/progress.md</code>.</li>`
      + `<li>Source links open the original SAP documentation inside this site. Use <strong>← Back</strong> to return.</li>`
      + `<li>Legend in lessons: 📄 from the SAP docs · 🌐 general knowledge to verify · 🔁 analogy.</li>`
      + `<li>Write your notes in <code>curriculum/progress.md</code> in your editor, then reload this page.</li></ul>`;

    $('#doc').innerHTML = html;
    markActive();
    window.scrollTo(0, 0);
  }

  // ---------- documents ----------
  async function renderDoc(path, frag) {
    const doc = $('#doc');
    const isNew = path !== renderedPath;
    if (isNew) {
      doc.innerHTML = '<div class="skeleton" style="width:55%;height:28px"></div>' + '<div class="skeleton"></div>'.repeat(6);
      $('#banner').innerHTML = '';
      $('#pager').innerHTML = '';
      $('#toc').innerHTML = '';
      let text;
      try {
        const r = await fetch('/' + path.split('/').map(encodeURIComponent).join('/'), { cache: 'no-store' });
        if (!r.ok) throw new Error(String(r.status));
        text = await r.text();
      } catch (e) {
        renderMissing(path);
        return;
      }
      doc.innerHTML = marked.parse(text);
      postProcess(doc, path, path.split('/').slice(0, -1).join('/'));
      renderedPath = path;
      const h1 = doc.querySelector('h1');
      document.title = (h1 ? h1.textContent.trim() + ' · ' : '') + 'BTP Study';
      $('#crumb').textContent = crumbFor(path, h1);
      renderBanner(path);
      renderPager(path);
      buildToc(doc, path);
      if (!frag) window.scrollTo(0, 0);
      await renderMermaid(doc);
    }
    markActive();
    if (frag) scrollToFrag(frag);
  }

  function crumbFor(path, h1) {
    const m = moduleFor(path);
    if (m) return `${m.id} · ${m.level}`;
    if (path.startsWith('btp-cloud-platform/')) return 'SAP documentation';
    return h1 ? h1.textContent.trim() : path;
  }

  function postProcess(doc, path, baseDir) {
    const used = new Set();
    doc.querySelectorAll('h1, h2, h3, h4').forEach((h) => {
      const base = slug(h.textContent) || 'section';
      let id = base, n = 2;
      while (used.has(id)) id = `${base}-${n++}`;
      used.add(id);
      h.id = id;
    });

    doc.querySelectorAll('a[href]').forEach((a) => {
      const href = a.getAttribute('href');
      if (/^[a-z][a-z0-9+.-]*:/i.test(href)) { a.target = '_blank'; a.rel = 'noopener noreferrer'; return; }
      if (href.startsWith('#')) { a.setAttribute('href', `#/${path}${href}`); return; }
      const [p, f] = splitOnce(href, '#');
      let target;
      try { target = resolvePath(baseDir, decodeURIComponent(p)); } catch (e) { target = resolvePath(baseDir, p); }
      if (/\.md$/i.test(target)) {
        a.setAttribute('href', `#/${target}${f ? '#' + f : ''}`);
      } else {
        a.setAttribute('href', `/${target}${f ? '#' + f : ''}`);
        a.target = '_blank';
      }
    });

    doc.querySelectorAll('img[src]').forEach((img) => {
      const s = img.getAttribute('src');
      if (!/^[a-z][a-z0-9+.-]*:/i.test(s) && !s.startsWith('/')) img.src = '/' + resolvePath(baseDir, s);
      img.loading = 'lazy';
    });

    doc.querySelectorAll('table').forEach((t) => {
      const w = document.createElement('div');
      w.className = 'table-wrap';
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });

    doc.querySelectorAll('pre > code').forEach((code) => {
      if (code.classList.contains('language-mermaid')) {
        const div = document.createElement('div');
        div.className = 'mermaid';
        div.textContent = code.textContent;
        code.parentElement.replaceWith(div);
        return;
      }
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'copy-btn';
      btn.textContent = 'Copy';
      btn.addEventListener('click', async () => {
        try { await navigator.clipboard.writeText(code.textContent.replace(/\n$/, '')); btn.textContent = 'Copied'; }
        catch (e) { btn.textContent = 'Select + Ctrl+C'; }
        setTimeout(() => { btn.textContent = 'Copy'; }, 1500);
      });
      code.parentElement.appendChild(btn);
    });
  }

  async function renderMermaid(doc) {
    const nodes = [...doc.querySelectorAll('.mermaid')];
    for (const node of nodes) {
      try {
        await mermaid.run({ nodes: [node] });
        // Big diagrams: show at natural size and let the box scroll, instead of shrinking text to unreadable.
        const svg = node.querySelector('svg');
        const vb = svg && svg.viewBox && svg.viewBox.baseVal;
        if (vb && vb.width > node.clientWidth * 1.15) {
          svg.style.maxWidth = 'none';
          svg.style.width = `${Math.round(vb.width)}px`;
          svg.style.height = 'auto';
          node.classList.add('wide');
          const hint = document.createElement('div');
          hint.className = 'wide-hint';
          hint.textContent = 'Wide diagram: scroll sideways →';
          node.before(hint);
        }
      } catch (e) {
        if (!node.querySelector('svg')) {
          const err = document.createElement('div');
          err.className = 'mermaid-error';
          err.textContent = 'This diagram could not be rendered: ' + (e && e.message ? e.message : e);
          node.appendChild(err);
        }
      }
    }
  }

  function scrollToFrag(frag) {
    const el = document.getElementById(frag) || document.querySelector(`[name="${CSS.escape(frag)}"]`);
    if (el) el.scrollIntoView({ block: 'start' });
  }

  function renderMissing(path) {
    renderedPath = path;
    const m = moduleFor(path);
    $('#toc').innerHTML = '';
    if (m) {
      const anchor = slug(`${m.id} · ${m.title}`);
      document.title = `${m.id} · BTP Study`;
      $('#crumb').textContent = `${m.id} · ${m.level}`;
      $('#doc').innerHTML = `<h1>${esc(m.id)} · ${esc(m.title)}</h1>`
        + `<div class="continue"><div class="grow"><div class="label">Not written yet</div>`
        + `<p style="margin:6px 0 0">Lessons are written one at a time. In Claude, say <strong>next</strong> to get this lesson, then reload this page.</p></div>`
        + `<a class="btn" href="#/curriculum/01-syllabus.md#${anchor}">See objectives in the syllabus</a></div>`;
      renderBanner(path);
      renderPager(path);
    } else {
      $('#banner').innerHTML = '';
      $('#pager').innerHTML = '';
      $('#doc').innerHTML = `<h1>Page not found</h1><p><code>${esc(path)}</code></p><p><a href="#/">Go to Home</a></p>`;
    }
    markActive();
    window.scrollTo(0, 0);
  }

  function renderBanner(path) {
    const b = $('#banner');
    const m = moduleFor(path);
    if (m) {
      const cls = STATUS_CLASS[m.status] || 'notstarted';
      let buttons = '';
      if (m.status === 'not started') buttons += '<button class="btn" data-set="in progress">Start module</button>';
      if (m.status !== 'done') buttons += '<button class="btn primary" data-set="done">Mark as done</button>';
      else buttons += '<button class="btn" data-set="in progress">Reopen</button>';
      b.innerHTML = `<div class="banner"><span class="pill ${cls}">${esc(cap(m.status))}</span>`
        + `<span class="grow">${esc(m.id)} · ${esc(m.level)}${m.tag ? ' · ' + esc(m.tag) : ''}</span>${buttons}</div>`;
      b.querySelectorAll('[data-set]').forEach((btn) => btn.addEventListener('click', () => setStatus(m.id, btn.dataset.set)));
    } else if (path.startsWith('btp-cloud-platform/')) {
      b.innerHTML = `<div class="banner"><span class="pill source">SAP source doc</span>`
        + `<span class="grow">${esc(path.replace('btp-cloud-platform/docs/', ''))}</span>`
        + `<button class="btn" id="backBtn">← Back</button></div>`;
      $('#backBtn').addEventListener('click', () => history.back());
    } else {
      b.innerHTML = '';
    }
  }

  function renderPager(path) {
    const i = state.modules.findIndex((m) => m.lesson === path);
    const p = $('#pager');
    if (i < 0) { p.innerHTML = ''; return; }
    const prev = state.modules[i - 1], next = state.modules[i + 1];
    p.innerHTML = (prev ? `<a class="prev" href="#/${esc(prev.lesson)}"><span class="dir">← Previous</span>${esc(prev.id)} · ${esc(prev.title)}</a>` : '<span></span>')
      + (next ? `<a class="next" href="#/${esc(next.lesson)}"><span class="dir">Next →</span>${esc(next.id)} · ${esc(next.title)}${next.exists ? '' : ' (not written yet)'}</a>` : '');
  }

  // ---------- table of contents ----------
  let tocLinks = [];
  function buildToc(doc, path) {
    const hs = [...doc.querySelectorAll('h2, h3')];
    const toc = $('#toc');
    if (hs.length < 2) { toc.innerHTML = ''; tocLinks = []; return; }
    toc.innerHTML = '<p class="toc-title">On this page</p>' + hs.map((h) =>
      `<a class="${h.tagName.toLowerCase()}" href="#/${esc(path)}#${esc(h.id)}" data-id="${esc(h.id)}">${esc(h.textContent)}</a>`).join('');
    tocLinks = [...toc.querySelectorAll('a')].map((a) => ({ a, h: document.getElementById(a.dataset.id) }));
    updateTocActive();
  }

  function updateTocActive() {
    if (!tocLinks.length) return;
    let current = tocLinks[0];
    for (const t of tocLinks) { if (t.h && t.h.getBoundingClientRect().top < 120) current = t; }
    tocLinks.forEach((t) => t.a.classList.toggle('active', t === current));
  }
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { updateTocActive(); ticking = false; });
  }, { passive: true });

  // ---------- routing & chrome ----------
  function closeNav() {
    document.body.classList.remove('nav-open');
    $('#menuBtn').setAttribute('aria-expanded', 'false');
  }

  async function route() {
    closeNav();
    const { path, frag } = currentRoute();
    if (!path) { renderHome(); return; }
    await renderDoc(path, frag);
  }

  $('#menuBtn').addEventListener('click', () => {
    const open = document.body.classList.toggle('nav-open');
    $('#menuBtn').setAttribute('aria-expanded', String(open));
  });
  $('#scrim').addEventListener('click', closeNav);
  $('#filter').addEventListener('input', renderNav);
  window.addEventListener('hashchange', route);
  window.addEventListener('focus', async () => {
    // Pick up edits made in your editor (progress.md, new lessons) when you come back to the tab.
    await loadStatus();
    if (renderedPath === '') renderHome();
    else if (renderedPath) { renderBanner(renderedPath); renderPager(renderedPath); }
  });

  (async () => {
    await loadStatus();
    await route();
  })();
})();
