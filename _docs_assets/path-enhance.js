/* ============================================================
   Path-page enhancements:
   0. Long-form serif body class
   1. Scroll progress bar (fixed at top of viewport)
   2. Reading-time computation (word count : minutes)
   3. Active-section scroll-spy on the TOC sidebar
   4. Reveal-on-scroll via IntersectionObserver
   ============================================================ */

document$.subscribe(() => {
  /* ----- 0. Long-form serif body class -----
     Apply .long-form to <body> on pages where Newsreader serif body
     improves long-form reading. Excludes landing index, the playground,
     and the about/STRUCTURE/CONTRIBUTING/CLAUDE pages. */
  const LONG_FORM_PREFIXES = [
    '/methodology/', '/paper/', '/results/', '/interfaces/',
    '/equation/', '/principles/', '/open-problems/',
  ];
  const path = window.location.pathname;
  const isLongForm = LONG_FORM_PREFIXES.some(p => path.includes(p));
  if (isLongForm) {
    document.body.classList.add('long-form');
  } else {
    document.body.classList.remove('long-form');
  }

  /* ----- 1. Scroll progress bar ----- */
  let bar = document.querySelector('.scroll-progress');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'scroll-progress';
    document.body.appendChild(bar);
  }

  const updateProgress = () => {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = `${pct}%`;
    // Bar fades in once user has scrolled past 60px; hides again near top
    if (scrollTop > 60) {
      bar.classList.add('is-active');
    } else {
      bar.classList.remove('is-active');
    }
  };

  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress, { passive: true });
  updateProgress();

  /* ----- 4. Reveal-on-scroll via IntersectionObserver -----
     Targets section headings, large figures, callouts, and cards in
     long-form content. Selection limited to long-form pages so that
     the landing keeps its own bespoke animations. */

  const prefersReducedMotion =
    window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReducedMotion && 'IntersectionObserver' in window && isLongForm) {
    const revealTargets = document.querySelectorAll(
      '.md-content h2, .md-content h3, ' +
      '.md-content .admonition, .md-content details, ' +
      '.md-content blockquote.pull-quote, .md-content .mnsm-card, ' +
      '.md-content .ref-card, .md-content table, ' +
      '.md-content mjx-container[display="true"], ' +
      '.md-content figure'
    );

    revealTargets.forEach((el) => {
      el.classList.add('reveal');
    });

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        rootMargin: '0px 0px -10% 0px',
        threshold: 0.05,
      }
    );

    revealTargets.forEach((el) => observer.observe(el));
  }

  /* ----- 5. Prediction status chips on interface pages ----- */
  if (path.includes('/interfaces/')) {
    // Find every <li> whose text starts with "Status:" and contains a
    // bolded state phrase. Wrap the state in a styled chip span. The
    // status taxonomy follows the structural-research-mode skill:
    //   "tested (consistent in coupled regime)"  -> consistent
    //   "tested (inconsistent in coupled regime)" -> inconsistent
    //   "untested" or "not yet tested" or "pending" -> untested
    //   "partially tested" -> partial
    const STATUS_PATTERNS = [
      { re: /\btested\s*\([^)]*consistent[^)]*\)/i, cls: 'pred-status--consistent' },
      { re: /\btested\s*\([^)]*inconsistent[^)]*\)/i, cls: 'pred-status--inconsistent' },
      { re: /\btested in coupled regime,\s*consistent/i, cls: 'pred-status--consistent' },
      { re: /\btested in coupled regime,\s*inconsistent/i, cls: 'pred-status--inconsistent' },
      { re: /\bpartially tested\b/i, cls: 'pred-status--partial' },
      { re: /\b(?:untested|not yet tested|pending)\b/i, cls: 'pred-status--untested' },
    ];

    const predictionLists = document.querySelectorAll(
      'h2[id^="locally-testable"] + blockquote + p + ul > li'
    );

    predictionLists.forEach((li) => {
      // The status line is a <li> inside the inner <ul> that starts with
      // "Status:". The text after "Status:" carries a bolded state.
      const statusLi = Array.from(li.querySelectorAll('ul > li'))
        .find((sub) => sub.textContent.trim().startsWith('Status:'));
      if (!statusLi) return;

      const strong = statusLi.querySelector('strong');
      if (!strong) return;

      const text = strong.textContent;
      for (const { re, cls } of STATUS_PATTERNS) {
        if (re.test(text)) {
          strong.classList.add('pred-status', cls);
          return;
        }
      }
      strong.classList.add('pred-status', 'pred-status--untested');
    });
  }

  /* ----- 2. Reading-time for path pages ----- */
  const pathHero = document.querySelector('.path-hero');
  if (pathHero && !pathHero.querySelector('.reading-time')) {
    const body = document.querySelector('.path-body');
    if (body) {
      const text = body.innerText || body.textContent || '';
      // strip code/math heuristically: count alphabetic word tokens only
      const words = text.match(/[\p{L}]+/gu) || [];
      const wpm = 230;  // research-reading pace, includes pausing for equations
      const minutes = Math.max(1, Math.round(words.length / wpm));
      const breadcrumb = pathHero.querySelector('.path-breadcrumb');
      if (breadcrumb) {
        const rt = document.createElement('span');
        rt.className = 'reading-time';
        rt.innerHTML = `· <strong>${minutes} min read</strong> · ${words.length.toLocaleString()} words`;
        breadcrumb.appendChild(rt);
      }
    }
  }
});
