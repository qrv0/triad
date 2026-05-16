/* ============================================================
   Predictions status board : unified dashboard for all ~51
   locally-testable predictions. Hydrates #predictions-app from
   /assets/data/predictions-index.json (built by build_index.py).
   Filter by substrate domain, filter by status. No aggregate
   metrics (no "passing rate"; status reporting is row-level).
   ============================================================ */

(function () {
  'use strict';

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

  let PREDICTIONS = [];
  const activeDomains = new Set();
  const activeStatuses = new Set();

  function init() {
    const root = document.getElementById('predictions-app');
    if (!root) return;

    fetch(getDataBase() + 'predictions-index.json')
      .then((r) => r.ok ? r.json() : Promise.reject(r.status))
      .then((data) => {
        PREDICTIONS = data;
        setupChips();
        renderBody();
      })
      .catch(() => {
        const body = document.getElementById('predictions-body');
        if (body) body.innerHTML = '<p class="predictions-app__error">Could not load predictions index. Reload the page to retry.</p>';
      });
  }

  function getDataBase() {
    return new URL('../../assets/data/', window.location.href).pathname;
  }

  function setupChips() {
    const domains = unique(PREDICTIONS.map((p) => p.domain)).sort();
    const statuses = unique(PREDICTIONS.map((p) => p.status)).sort();
    domains.forEach((d) => activeDomains.add(d));
    statuses.forEach((s) => activeStatuses.add(s));

    const domainHolder = document.getElementById('predictions-domain-chips');
    const statusHolder = document.getElementById('predictions-status-chips');

    if (domainHolder) {
      domainHolder.innerHTML = '';
      domains.forEach((d) => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'predictions-app__chip is-active';
        chip.textContent = DOMAIN_LABEL[d] || d;
        chip.dataset.value = d;
        chip.addEventListener('click', () => {
          chip.classList.toggle('is-active');
          if (activeDomains.has(d)) activeDomains.delete(d);
          else activeDomains.add(d);
          renderBody();
        });
        domainHolder.appendChild(chip);
      });
    }

    if (statusHolder) {
      statusHolder.innerHTML = '';
      statuses.forEach((s) => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'predictions-app__chip is-active ' + (STATUS_CLASS[s] || '');
        chip.textContent = STATUS_LABEL[s] || s;
        chip.dataset.value = s;
        chip.addEventListener('click', () => {
          chip.classList.toggle('is-active');
          if (activeStatuses.has(s)) activeStatuses.delete(s);
          else activeStatuses.add(s);
          renderBody();
        });
        statusHolder.appendChild(chip);
      });
    }
  }

  function renderBody() {
    const body = document.getElementById('predictions-body');
    if (!body) return;

    const filtered = PREDICTIONS.filter((p) =>
      activeDomains.has(p.domain) && activeStatuses.has(p.status)
    );

    if (filtered.length === 0) {
      body.innerHTML = '<p class="predictions-app__empty">No predictions match the current filter. Toggle a chip to broaden.</p>';
      return;
    }

    filtered.sort((a, b) => {
      // Sort by interface number, then prediction id
      const na = parseInt(a.interface_num, 10);
      const nb = parseInt(b.interface_num, 10);
      if (na !== nb) return na - nb;
      return (a.id || '').localeCompare(b.id || '');
    });

    let html = (
      '<p class="predictions-app__count">' + filtered.length +
      ' of ' + PREDICTIONS.length + ' predictions shown</p>' +
      '<ul class="predictions-app__list">'
    );

    filtered.forEach((p) => {
      const cls = STATUS_CLASS[p.status] || 'pred-status--untested';
      const lbl = STATUS_LABEL[p.status] || 'not yet tested';
      const domain = DOMAIN_LABEL[p.domain] || p.domain || '';
      const link = p.result_doc
        ? '<a class="predictions-app__result-link" href="../../' + escape(p.result_doc) + '">result &rarr;</a>'
        : '';
      const titleClean = (p.interface_title || '').replace(/^Interface \d+:\s*/, '');
      html += (
        '<li class="predictions-app__row">' +
          '<div class="predictions-app__row-head">' +
            '<span class="predictions-app__id">' + escape(p.id) + '</span>' +
            '<a class="predictions-app__src" href="../' + escape(p.interface_slug) + '/">' +
              'interface ' + escape(p.interface_num) +
              '<span class="predictions-app__src-title">: ' + escape(titleClean) + '</span>' +
            '</a>' +
            '<span class="predictions-app__domain">' + escape(domain) + '</span>' +
            '<span class="pred-status ' + cls + '">' + escape(lbl) + '</span>' +
          '</div>' +
          '<p class="predictions-app__short">' + escape(p.short) + '</p>' +
          link +
        '</li>'
      );
    });
    html += '</ul>';
    body.innerHTML = html;
  }

  function unique(arr) {
    const seen = new Set();
    const out = [];
    arr.forEach((x) => {
      if (x != null && !seen.has(x)) {
        seen.add(x);
        out.push(x);
      }
    });
    return out;
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
