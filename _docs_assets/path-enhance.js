/* ============================================================
   Path-page enhancements:
   1. Scroll progress bar (fixed at top of viewport)
   2. Reading-time computation (word count → minutes)
   3. Active-section scroll-spy on the TOC sidebar
   ============================================================ */

document$.subscribe(() => {
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
  };

  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateProgress, { passive: true });
  updateProgress();

  /* ----- 2. Reading-time for path pages ----- */
  const pathHero = document.querySelector('.path-hero');
  if (pathHero && !pathHero.querySelector('.reading-time')) {
    const body = document.querySelector('.path-body');
    if (body) {
      const text = body.innerText || body.textContent || '';
      // strip code/math heuristically — count alphabetic word tokens only
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
