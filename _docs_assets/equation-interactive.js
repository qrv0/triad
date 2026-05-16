/* ============================================================
   Equation showpiece : interactive term-click reveals which of
   the 17 cross-domain interfaces instantiate each principle.
   Hydrates equation/01-derivation.md from
   /assets/data/interfaces-index.json.
   ============================================================ */

(function () {
  'use strict';

  const PRINCIPLE_LABEL = {
    p1: 'P1 oscillation',
    p2: 'P2 self-reference',
    p3: 'P3 coupling',
  };

  const PRINCIPLE_CLASS = {
    p1: 't-p1',
    p2: 't-p2',
    p3: 't-p3',
  };

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

  let INDEX = null;

  function init() {
    const showpiece = document.querySelector('.equation-showpiece');
    if (!showpiece) return;

    fetch(getDataBase() + 'interfaces-index.json')
      .then((r) => r.ok ? r.json() : Promise.reject(r.status))
      .then((data) => { INDEX = data; wireTerms(showpiece); })
      .catch(() => { /* silent: page still renders the equation statically */ });
  }

  function getDataBase() {
    return new URL('../../assets/data/', window.location.href).pathname;
  }

  function wireTerms(showpiece) {
    const panel = showpiece.querySelector('#eq-panel');
    const terms = showpiece.querySelectorAll('.eq-term-interactive');
    let activeTerm = null;

    terms.forEach((term) => {
      const principle = term.dataset.principle;

      const activate = () => {
        if (activeTerm === term) {
          term.classList.remove('is-active');
          panel.hidden = true;
          activeTerm = null;
          return;
        }
        terms.forEach((t) => t.classList.remove('is-active'));
        term.classList.add('is-active');
        activeTerm = term;
        renderPanel(panel, principle);
      };

      term.addEventListener('click', activate);
      term.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          activate();
        }
      });
    });
  }

  function renderPanel(panel, principle) {
    panel.hidden = false;
    const cls = PRINCIPLE_CLASS[principle];
    const label = PRINCIPLE_LABEL[principle];

    let html = (
      '<div class="eq-panel__head ' + cls + '">' +
        '<strong>' + escape(label) + '</strong>' +
        '<span>17 substrate instantiations</span>' +
      '</div>'
    );
    html += '<ul class="eq-panel__list">';

    const nums = Object.keys(INDEX).sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
    nums.forEach((num) => {
      const meta = INDEX[num];
      const phrase = (meta.triangle || {})[principle] || '';
      const titleClean = (meta.title || '').replace(/^Interface \d+:\s*/, '');
      const domain = DOMAIN_LABEL[meta.domain] || meta.domain || '';
      html += (
        '<li class="eq-panel__item">' +
          '<a class="eq-panel__link" href="../../interfaces/' + escape(meta.slug) + '/">' +
            '<span class="eq-panel__num">' + escape(num) + '</span>' +
            '<span class="eq-panel__title">' + escape(titleClean) + '</span>' +
            '<span class="eq-panel__domain">' + escape(domain) + '</span>' +
          '</a>' +
          '<p class="eq-panel__phrase">' + escape(phrase) + '</p>' +
        '</li>'
      );
    });
    html += '</ul>';
    panel.innerHTML = html;
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
