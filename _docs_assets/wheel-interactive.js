/* ============================================================
   Cross-domain wheel : interactive tooltip + side panel
   Augments the existing static SVG wheel on the landing page. On
   hover or focus of each .node element, renders a tooltip showing
   the structural prediction (P1/P2/P3 triangle) for the interface
   that node links to. On click, opens a side panel with extended
   info; the link itself still navigates after a delay so the
   reader can either click-through or click-to-read.
   Data source: /assets/data/interfaces-index.json built by
   hooks/build_index.py.
   ============================================================ */

(function () {
  'use strict';

  // Cache the fetched index once per page load.
  let INDEX = null;
  let TOOLTIP = null;
  let PANEL = null;

  const TIER_LABEL = { A: 'tier A hero', B: 'tier B hero', C: 'tier C hero' };
  const DOMAIN_LABEL = {
    physics: 'Physics',
    cosmology: 'Cosmology',
    acoustics: 'Acoustics',
    neuro: 'Neuroscience',
    archaeo: 'Archaeoacoustics',
    engineering: 'Engineering / ML',
    'complex-systems': 'Complex systems',
    biology: 'Biology',
  };

  function init() {
    const wheel = document.querySelector('.mnsm-wheel');
    if (!wheel) return;

    fetch(getDataBase() + 'interfaces-index.json')
      .then((r) => r.ok ? r.json() : Promise.reject(r.status))
      .then((data) => { INDEX = data; wireNodes(wheel); })
      .catch(() => { /* silent: wheel still navigates without tooltips */ });
  }

  function getDataBase() {
    // The landing page may be at root, /en/, /pt/, /es/. Resolve relative
    // to current path so the fetch hits the right asset dir.
    const path = window.location.pathname;
    const base = path.endsWith('/') ? path : path.replace(/\/[^/]*$/, '/');
    return base + 'assets/data/';
  }

  function wireNodes(wheel) {
    const nodes = wheel.querySelectorAll('a.node[href*="/interfaces/"]');
    nodes.forEach((node) => {
      const num = extractInterfaceNum(node.getAttribute('href'));
      if (!num || !INDEX[num]) return;
      const data = INDEX[num];
      node.setAttribute('data-interface-num', num);

      node.addEventListener('mouseenter', () => showTooltip(node, data));
      node.addEventListener('mouseleave', hideTooltip);
      node.addEventListener('focus', () => showTooltip(node, data));
      node.addEventListener('blur', hideTooltip);
    });
  }

  function extractInterfaceNum(href) {
    if (!href) return null;
    const m = href.match(/interfaces\/(\d+)-/);
    return m ? m[1] : null;
  }

  function ensureTooltip() {
    if (TOOLTIP) return TOOLTIP;
    TOOLTIP = document.createElement('div');
    TOOLTIP.className = 'wheel-tooltip';
    TOOLTIP.setAttribute('role', 'tooltip');
    TOOLTIP.setAttribute('aria-hidden', 'true');
    document.body.appendChild(TOOLTIP);
    return TOOLTIP;
  }

  function showTooltip(node, data) {
    const tip = ensureTooltip();
    const tri = data.triangle || {};
    const tier = (data.hero_tier || 'B').toUpperCase();
    const domain = DOMAIN_LABEL[data.domain] || data.domain || '';

    tip.innerHTML = (
      '<div class="wheel-tooltip__head">' +
        '<span class="wheel-tooltip__num">' + escape(data.num) + '</span>' +
        '<span class="wheel-tooltip__domain">' + escape(domain) + '</span>' +
        '<span class="wheel-tooltip__tier">' + escape(TIER_LABEL[tier] || '') + '</span>' +
      '</div>' +
      '<div class="wheel-tooltip__title">' + escape(data.title || '') + '</div>' +
      '<p class="wheel-tooltip__desc">' + escape(data.description || '') + '</p>' +
      '<ul class="wheel-tooltip__triangle">' +
        '<li class="t-p1"><strong>P1</strong>' + escape(tri.p1 || '') + '</li>' +
        '<li class="t-p2"><strong>P2</strong>' + escape(tri.p2 || '') + '</li>' +
        '<li class="t-p3"><strong>P3</strong>' + escape(tri.p3 || '') + '</li>' +
      '</ul>'
    );

    // Position near the node, prefer above; flip below if not enough room.
    const rect = node.getBoundingClientRect();
    tip.classList.add('is-visible');
    tip.setAttribute('aria-hidden', 'false');
    const tipRect = tip.getBoundingClientRect();

    let left = rect.left + rect.width / 2 - tipRect.width / 2;
    let top = rect.top + window.scrollY - tipRect.height - 12;
    const flipDown = rect.top < tipRect.height + 30;

    if (flipDown) {
      top = rect.bottom + window.scrollY + 12;
      tip.classList.add('is-below');
    } else {
      tip.classList.remove('is-below');
    }

    // Clamp horizontally to viewport
    const minLeft = 12;
    const maxLeft = window.innerWidth - tipRect.width - 12;
    if (left < minLeft) left = minLeft;
    if (left > maxLeft) left = maxLeft;

    tip.style.left = left + 'px';
    tip.style.top = top + 'px';
  }

  function hideTooltip() {
    if (!TOOLTIP) return;
    TOOLTIP.classList.remove('is-visible', 'is-below');
    TOOLTIP.setAttribute('aria-hidden', 'true');
  }

  function escape(s) {
    if (s == null) return '';
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // mkdocs-material instant-navigation friendly: re-init when DOM changes.
  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(init);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
