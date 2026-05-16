/* ============================================================
   Comparison view : side-by-side rendering of two interfaces
   Hydrates the #compare-app on interfaces/compare.md from
   /assets/data/interfaces-index.json (built by build_index.py).
   Reader picks two interfaces via dropdowns; the body renders
   their P1/P2/P3 triangles + descriptions + predictions stacked.
   ============================================================ */

(function () {
  'use strict';

  const DEFAULT_A = '06';
  const DEFAULT_B = '10';

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

  const STATUS_LABEL = {
    not_yet_tested: 'not yet tested',
    tested_consistent: 'tested in coupled regime, consistent',
    tested_inconsistent: 'tested in coupled regime, inconsistent',
    partial: 'partially tested',
  };

  const STATUS_CLASS = {
    not_yet_tested: 'pred-status--untested',
    tested_consistent: 'pred-status--consistent',
    tested_inconsistent: 'pred-status--inconsistent',
    partial: 'pred-status--partial',
  };

  function init() {
    const root = document.getElementById('compare-app');
    if (!root) return;

    fetch(getDataBase() + 'interfaces-index.json')
      .then((r) => r.ok ? r.json() : Promise.reject(r.status))
      .then((data) => render(root, data))
      .catch(() => {
        const body = document.getElementById('compare-body');
        if (body) body.innerHTML = '<p class="compare-app__error">Could not load interfaces index. Reload the page to retry.</p>';
      });
  }

  function getDataBase() {
    // From /interfaces/compare/, the data dir is at ../../assets/data/
    return new URL('../../assets/data/', window.location.href).pathname;
  }

  function render(root, data) {
    const selA = document.getElementById('compare-a');
    const selB = document.getElementById('compare-b');
    if (!selA || !selB) return;

    const nums = Object.keys(data).sort((a, b) => parseInt(a, 10) - parseInt(b, 10));

    function populateSelect(sel, defaultNum) {
      sel.innerHTML = '';
      nums.forEach((num) => {
        const opt = document.createElement('option');
        opt.value = num;
        opt.textContent = `${num} : ${data[num].title.replace(/^Interface \d+:\s*/, '')}`;
        if (num === defaultNum) opt.selected = true;
        sel.appendChild(opt);
      });
    }

    populateSelect(selA, DEFAULT_A);
    populateSelect(selB, DEFAULT_B);

    const update = () => renderBody(data[selA.value], data[selB.value]);
    selA.addEventListener('change', update);
    selB.addEventListener('change', update);
    update();
  }

  function renderBody(a, b) {
    const body = document.getElementById('compare-body');
    if (!body || !a || !b) return;

    body.innerHTML = (
      '<div class="compare-app__grid">' +
        renderCard(a, 'a') +
        renderCard(b, 'b') +
      '</div>' +
      '<h2 class="compare-app__section-title">Triangle contrast</h2>' +
      renderTriangleContrast(a, b) +
      '<h2 class="compare-app__section-title">Locally-testable predictions</h2>' +
      renderPredictions(a, b)
    );
  }

  function renderCard(meta, slot) {
    const tri = meta.triangle || {};
    const domain = DOMAIN_LABEL[meta.domain] || meta.domain || '';
    const tier = (meta.hero_tier || 'B').toUpperCase();
    const titleClean = (meta.title || '').replace(/^Interface \d+:\s*/, '');
    return (
      '<article class="compare-card compare-card--' + slot + '">' +
        '<header class="compare-card__head">' +
          '<span class="compare-card__num">' + escape(meta.num) + '</span>' +
          '<span class="compare-card__domain">' + escape(domain) + '</span>' +
          '<span class="compare-card__tier">tier ' + escape(tier) + '</span>' +
        '</header>' +
        '<h3 class="compare-card__title"><a href="../' + escape(meta.slug) + '/">' + escape(titleClean) + '</a></h3>' +
        '<p class="compare-card__desc">' + escape(meta.description || '') + '</p>' +
      '</article>'
    );
  }

  function renderTriangleContrast(a, b) {
    const triA = a.triangle || {};
    const triB = b.triangle || {};
    const rows = ['p1', 'p2', 'p3'];
    const labels = {
      p1: 'P1 oscillation',
      p2: 'P2 self-reference',
      p3: 'P3 coupling',
    };
    let html = '<table class="compare-app__triangle"><tbody>';
    rows.forEach((p) => {
      html += (
        '<tr class="t-' + p + '">' +
          '<th>' + escape(labels[p]) + '</th>' +
          '<td>' + escape(triA[p] || '') + '</td>' +
          '<td>' + escape(triB[p] || '') + '</td>' +
        '</tr>'
      );
    });
    html += '</tbody></table>';
    return html;
  }

  function renderPredictions(a, b) {
    const all = []
      .concat((a.predictions || []).map((p) => ({ p, src: a })))
      .concat((b.predictions || []).map((p) => ({ p, src: b })));

    if (all.length === 0) {
      return '<p class="compare-app__empty">No predictions cataloged for either interface.</p>';
    }

    let html = '<ul class="compare-app__predictions">';
    all.forEach(({ p, src }) => {
      const cls = STATUS_CLASS[p.status] || 'pred-status--untested';
      const lbl = STATUS_LABEL[p.status] || 'not yet tested';
      const link = p.result_doc
        ? '<a class="compare-app__pred-link" href="../../' + escape(p.result_doc) + '">result &rarr;</a>'
        : '';
      html += (
        '<li class="compare-app__pred">' +
          '<div class="compare-app__pred-head">' +
            '<span class="compare-app__pred-id">' + escape(p.id) + '</span>' +
            '<span class="compare-app__pred-src">interface ' + escape(src.num) + '</span>' +
            '<span class="pred-status ' + cls + '">' + escape(lbl) + '</span>' +
          '</div>' +
          '<p class="compare-app__pred-short">' + escape(p.short) + '</p>' +
          link +
        '</li>'
      );
    });
    html += '</ul>';
    return html;
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
