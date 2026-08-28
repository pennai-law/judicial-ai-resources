  const tabs = document.querySelectorAll('.tab-btn');
  const panes = document.querySelectorAll('.tab-pane');
  const paneIds = new Set([...panes].map(p => p.id));

  function activateTab(target) {
    const pane = document.getElementById(target);
    if (!pane || !pane.classList.contains('tab-pane')) return;
    tabs.forEach(t => {
      t.classList.remove('active');
      t.setAttribute('aria-selected', 'false');
      t.setAttribute('tabindex', '-1');
    });
    panes.forEach(p => p.classList.remove('active'));
    const btn = document.querySelector(`.tab-btn[data-tab="${target}"]`);
    if (btn) {
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');
      btn.setAttribute('tabindex', '0');
    }
    pane.classList.add('active');
    document.querySelectorAll('.overview-col').forEach(c => c.classList.toggle('active', c.dataset.nav === target));
  }

  function scrollToTabs() {
    window.scrollTo({ top: document.querySelector('.tab-nav-wrap').offsetTop - 56, behavior: 'smooth' });
  }

  tabs.forEach(btn => {
    btn.addEventListener('click', () => {
      activateTab(btn.dataset.tab);
      scrollToTabs();
    });
  });

  function activateFromHash() {
    const target = location.hash.slice(1);
    if (paneIds.has(target)) activateTab(target);
  }
  activateFromHash();
  window.addEventListener('hashchange', activateFromHash);

  document.querySelectorAll('.overview-col').forEach(col => {
    col.addEventListener('click', () => {
      activateTab(col.dataset.nav);
      scrollToTabs();
    });
  });

  // ── SITE SEARCH ──
  const searchBtn = document.querySelector('.header-search');
  const searchOverlay = document.getElementById('search-overlay');
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  const tabNames = {
    'start': 'Start Here',
    'how-it-works': 'How These Tools Work',
    'use-cases': 'Use Cases',
    'guardrails': 'Guardrails',
    'tools': 'Tools',
    'adapting': 'How the Profession Is Adapting'
  };
  let currentResults = [];
  let focusedIdx = -1;

  function escapeHtml(s) {
    return String(s).replace(/[<>&"]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'}[c]));
  }
  function escapeRegex(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  function openSearch() {
    searchOverlay.classList.add('active');
    searchOverlay.removeAttribute('inert');
    searchOverlay.setAttribute('aria-hidden', 'false');
    setTimeout(() => searchInput.focus(), 50);
  }
  function closeSearch() {
    searchOverlay.classList.remove('active');
    if (searchBtn) searchBtn.focus();
    searchOverlay.setAttribute('inert', '');
    searchOverlay.setAttribute('aria-hidden', 'true');
    searchInput.value = '';
    searchResults.innerHTML = '<div class="search-empty">Type to search across all six tabs.</div>';
    currentResults = [];
    focusedIdx = -1;
  }

  function performSearch(query) {
    query = query.trim();
    if (!query) {
      searchResults.innerHTML = '<div class="search-empty">Type to search across all six tabs.</div>';
      currentResults = [];
      focusedIdx = -1;
      return;
    }
    const lc = query.toLowerCase();
    const re = new RegExp(escapeRegex(query), 'gi');
    const matches = [];
    const seen = new Set();

    document.querySelectorAll('.tab-pane').forEach(tab => {
      const tabId = tab.id;
      const tabName = tabNames[tabId] || tabId;
      tab.querySelectorAll('h2, h3, h4, p, li').forEach(el => {
        if (el.closest('.search-overlay')) return;
        const text = el.textContent.replace(/\s+/g, ' ').trim();
        if (!text || !text.toLowerCase().includes(lc)) return;
        if (seen.has(el)) return;
        seen.add(el);

        // Find a section title (nearest heading above, or this element if it's a heading).
        // Climb ancestors too, so items nested in a <ul>/<div> still resolve to their heading.
        let section = '';
        if (el.tagName === 'H2' || el.tagName === 'H3' || el.tagName === 'H4') {
          section = text;
        } else {
          let node = el;
          while (node && node !== tab && !section) {
            let prev = node;
            while ((prev = prev.previousElementSibling)) {
              if (prev.tagName === 'H2' || prev.tagName === 'H3' || prev.tagName === 'H4') { section = prev.textContent.trim(); break; }
            }
            node = node.parentElement;
          }
          if (!section) {
            const h2 = tab.querySelector('h2.section-title');
            if (h2) section = h2.textContent.trim();
          }
        }

        // Build snippet around the match
        const idx = text.toLowerCase().indexOf(lc);
        const start = Math.max(0, idx - 45);
        const end = Math.min(text.length, idx + query.length + 75);
        let snippet = (start > 0 ? '…' : '') + text.slice(start, end) + (end < text.length ? '…' : '');
        snippet = escapeHtml(snippet).replace(re, m => `<mark>${m}</mark>`);

        matches.push({ tabId, tabName, section, element: el, snippet });
      });
    });

    const capped = matches.slice(0, 30);
    currentResults = capped;
    focusedIdx = capped.length > 0 ? 0 : -1;

    if (capped.length === 0) {
      searchResults.innerHTML = '<div class="search-no-results">No results for &ldquo;' + escapeHtml(query) + '&rdquo;.</div>';
      return;
    }

    searchResults.innerHTML = capped.map((m, i) => `
      <a class="search-result${i === 0 ? ' focused' : ''}" data-idx="${i}" href="#">
        <div class="search-result-tab">${escapeHtml(m.tabName)}</div>
        <div class="search-result-title">${escapeHtml(m.section || 'Match')}</div>
        <div class="search-result-snippet">${m.snippet}</div>
      </a>
    `).join('');
  }

  function jumpToResult(result) {
    closeSearch();
    activateTab(result.tabId);
    setTimeout(() => {
      result.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
      const orig = result.element.style.transition;
      result.element.style.transition = 'background-color 0.6s';
      const origBg = result.element.style.backgroundColor;
      result.element.style.backgroundColor = '#EFE7D3';
      setTimeout(() => {
        result.element.style.backgroundColor = origBg;
        setTimeout(() => { result.element.style.transition = orig; }, 700);
      }, 1200);
    }, 120);
  }

  function updateFocused() {
    searchResults.querySelectorAll('.search-result').forEach((el, i) => {
      el.classList.toggle('focused', i === focusedIdx);
      if (i === focusedIdx) el.scrollIntoView({ block: 'nearest' });
    });
  }

  if (searchBtn) searchBtn.addEventListener('click', openSearch);
  searchOverlay.addEventListener('click', e => { if (e.target === searchOverlay) closeSearch(); });
  searchInput.addEventListener('input', e => performSearch(e.target.value));
  searchResults.addEventListener('click', e => {
    const result = e.target.closest('.search-result');
    if (result) {
      e.preventDefault();
      const idx = parseInt(result.dataset.idx, 10);
      if (currentResults[idx]) jumpToResult(currentResults[idx]);
    }
  });

  document.addEventListener('keydown', e => {
    const isOpen = searchOverlay.classList.contains('active');
    if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) {
      e.preventDefault();
      isOpen ? closeSearch() : openSearch();
      return;
    }
    if (!isOpen) return;
    if (e.key === 'Escape') { closeSearch(); }
    else if (e.key === 'ArrowDown' && currentResults.length) {
      e.preventDefault();
      focusedIdx = (focusedIdx + 1) % currentResults.length;
      updateFocused();
    } else if (e.key === 'ArrowUp' && currentResults.length) {
      e.preventDefault();
      focusedIdx = (focusedIdx - 1 + currentResults.length) % currentResults.length;
      updateFocused();
    } else if (e.key === 'Enter' && focusedIdx >= 0) {
      e.preventDefault();
      jumpToResult(currentResults[focusedIdx]);
    }
  });
