---
title: "Compare two interfaces"
description: >-
  Side-by-side comparison of any two cross-domain interfaces:
  contrast their P1 / P2 / P3 instantiations, mappings, and
  predictions to make the cross-domain unification concrete.
hide:
  - toc
---

# Compare two interfaces

This page is the cross-domain unification made tangible. Pick any two
interfaces from the dropdowns below; the page renders their
structural-prediction triangles, mappings, and locally-testable
predictions side by side. The work's central claim is that the same
form (P1 + P2 + P3) appears across the documented substrates; this
comparison view is what lets you see that directly for any pair you
choose.

The comparison view is hydrated client-side from
`/assets/data/interfaces-index.json` (built by `hooks/build_index.py`
from the YAML frontmatter of each interface page). Default pair on
page load: interface 01 (other NLS systems) versus interface 10
(Kuramoto synchronization), the canonical mathematical-equivalence
plus structural-prediction-convergence example.

<div id="compare-app" class="compare-app">
  <div class="compare-app__controls">
    <label>
      <span class="compare-app__label">Interface A</span>
      <select id="compare-a"></select>
    </label>
    <label>
      <span class="compare-app__label">Interface B</span>
      <select id="compare-b"></select>
    </label>
  </div>
  <div class="compare-app__body" id="compare-body">
    <p class="compare-app__loading">Loading interface index...</p>
  </div>
</div>

??? note "What this view is for"
    The site has a wheel showing all interfaces and a dashboard
    showing the locally-testable predictions. The wheel surfaces a node at a time;
    the dashboard surfaces predictions individually. This view is the
    in-between: pick two substrates and see what the structural form
    looks like in each, side by side.

    The constructive use: if you have a substrate in mind and want to
    see how its instantiation contrasts with another, this is the
    page. The triangles align row by row (P1 across both, P2 across
    both, P3 across both); the mapping tables sit alongside; the
    locally-testable predictions stack with status chips. The same
    form, two substrates.

[Browse all interfaces in the wheel](../#cross-domain-coherence-the-same-equation-in-many-substrates){ .md-button } &nbsp; [See the predictions status board](predictions.md){ .md-button }
