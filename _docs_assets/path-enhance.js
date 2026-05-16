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
