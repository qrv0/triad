/* ============================================================
   Plotly loader : lazy-load Plotly CDN only on pages with a
   .plotly-hero div. Each .plotly-hero div has data-spec="<name>"
   that resolves to _docs_assets/plotly/<name>.json. The loader
   fetches the spec, fetches Plotly if not already loaded, and
   renders the chart. Plotly is loaded ONCE per page.
   ============================================================ */

(function () {
  'use strict';

  const PLOTLY_CDN = 'https://cdn.plot.ly/plotly-2.27.0.min.js';
  let PLOTLY_PROMISE = null;

  function loadPlotly() {
    if (window.Plotly) return Promise.resolve(window.Plotly);
    if (PLOTLY_PROMISE) return PLOTLY_PROMISE;
    PLOTLY_PROMISE = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = PLOTLY_CDN;
      script.async = true;
      script.onload = () => resolve(window.Plotly);
      script.onerror = () => reject(new Error('Plotly CDN failed to load'));
      document.head.appendChild(script);
    });
    return PLOTLY_PROMISE;
  }

  function init() {
    const heroes = document.querySelectorAll('.plotly-hero[data-spec]');
    if (heroes.length === 0) return;

    heroes.forEach((node) => {
      if (node.dataset.rendered === '1') return;
      const spec = node.dataset.spec;
      if (!spec) return;
      const url = getSpecUrl(spec);

      fetch(url)
        .then((r) => r.ok ? r.json() : Promise.reject(r.status))
        .then((data) => {
          if (data.embed_image) {
            // Tier-A interface that uses a static image instead of Plotly
            node.innerHTML = (
              '<img class="plotly-hero__img" src="' + escape(data.embed_image) +
              '" alt="' + escape(data.alt || '') + '" loading="lazy" />' +
              (data.caption ? '<p class="plotly-hero__caption">' + escape(data.caption) + '</p>' : '')
            );
            node.dataset.rendered = '1';
            return;
          }
          loadPlotly().then((Plotly) => {
            const layout = applyTheme(data.layout || {});
            Plotly.newPlot(node, data.data || [], layout, data.config || {});
            node.dataset.rendered = '1';
            wireThemeListener(node, data);
          }).catch(() => {
            node.innerHTML = '<p class="plotly-hero__error">Plotly failed to load.</p>';
          });
        })
        .catch(() => {
          node.innerHTML = '<p class="plotly-hero__error">Could not load visualization data.</p>';
        });
    });
  }

  function getSpecUrl(spec) {
    return new URL('../../_docs_assets/plotly/' + spec + '.json', window.location.href).pathname;
  }

  function applyTheme(layout) {
    const dark = document.body.getAttribute('data-md-color-scheme') === 'slate';
    const cloned = JSON.parse(JSON.stringify(layout));
    if (dark) {
      cloned.font = Object.assign({}, cloned.font || {}, { color: '#EAE6DE' });
      cloned.xaxis = Object.assign({}, cloned.xaxis || {}, {
        gridcolor: 'rgba(232, 230, 227, 0.08)',
        zerolinecolor: 'rgba(232, 230, 227, 0.18)',
      });
      cloned.yaxis = Object.assign({}, cloned.yaxis || {}, {
        gridcolor: 'rgba(232, 230, 227, 0.08)',
        zerolinecolor: 'rgba(232, 230, 227, 0.18)',
      });
    } else {
      cloned.xaxis = Object.assign({}, cloned.xaxis || {}, {
        gridcolor: 'rgba(46, 44, 42, 0.08)',
      });
      cloned.yaxis = Object.assign({}, cloned.yaxis || {}, {
        gridcolor: 'rgba(46, 44, 42, 0.08)',
      });
    }
    return cloned;
  }

  function wireThemeListener(node, data) {
    if (!window.MutationObserver) return;
    const observer = new MutationObserver(() => {
      if (window.Plotly && data.data) {
        const layout = applyTheme(data.layout || {});
        window.Plotly.relayout(node, layout);
      }
    });
    observer.observe(document.body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });
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

  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(init);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
