---
title: "Predictions status board"
description: >-
  Unified dashboard of all locally-testable predictions across the 17
  cross-domain interfaces; filterable by domain and status; linked to
  source interface and result document.
hide:
  - toc
---

# Predictions status board

This page lists every locally-testable prediction across the 17
cross-domain interfaces in one place. Each row shows the prediction
ID, the source interface, the substrate domain, the one-line claim,
the current status, and a link to the result document where a
coupled-regime test exists.

The status taxonomy follows the methodology (see
[`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md)
and [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md)
for the structural reason): predictions are evaluated by coupled-
regime numerical reproduction (per Rule A of the
structural-research-mode skill), and a prediction's status reflects
whether such a test has run and what the evidence under criterion 4
of [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md)
points to. There is no aggregate "passing rate" because the global
structural claim is not evaluated by per-prediction accumulation;
the six criteria are.

<div id="predictions-app" class="predictions-app">
  <div class="predictions-app__controls">
    <fieldset class="predictions-app__filter">
      <legend>Filter by domain</legend>
      <div class="predictions-app__chips" id="predictions-domain-chips"></div>
    </fieldset>
    <fieldset class="predictions-app__filter">
      <legend>Filter by status</legend>
      <div class="predictions-app__chips" id="predictions-status-chips"></div>
    </fieldset>
  </div>
  <div class="predictions-app__body" id="predictions-body">
    <p class="predictions-app__loading">Loading predictions index...</p>
  </div>
</div>

??? note "Status vocabulary"
    The status terms used in this board follow the
    `structural-research-mode` skill's taxonomy. None of them use the
    word "falsified" because the methodology rejects Popperian
    falsificationism as the evaluation method for this work; see
    [`../methodology/02-limits-of-falsification.md`](../methodology/02-limits-of-falsification.md)
    for the structural argument.

    - **not yet tested** : no coupled-regime test has been run.
    - **tested in coupled regime, consistent** : the coupled-regime
      test ran and the observed quantity matches the prediction.
      Contributes evidence under criterion 4 (cross-domain coherence)
      and criterion 2 (reproducibility).
    - **tested in coupled regime, inconsistent** : the coupled-regime
      test ran and the observed quantity does not match. Prompts
      investigation of calibration, auxiliary numerical assumptions
      (Duhem-Quine), or implementation; does not falsify the
      structural claim.
    - **partially tested** : a related experiment exists but does
      not directly target this prediction.

[Browse interfaces by domain](README.md){ .md-button } &nbsp; [Compare two interfaces](compare.md){ .md-button }
