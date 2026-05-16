# Cross-domain interfaces

This folder is where the structural-realist claim of the work is operationalized. Each document maps the equation's mathematical form onto a separate independently-documented domain where the same structural form appears. The mappings use only peer-reviewed sources; speculative or contested mappings are not included.

| File | Domain | Type of correspondence |
|---|---|---|
| [`01-other-nls-systems.md`](01-other-nls-systems.md) | Bose–Einstein condensates, optical solitons, deep-water waves | Established physical instantiations of NLS-class dynamics |
| [`02-baryon-acoustic.md`](02-baryon-acoustic.md) | Cosmological structure formation via baryon acoustic oscillations | Acoustic dynamics in a self-interacting coupled medium |
| [`03-chladni-cymatics.md`](03-chladni-cymatics.md) | Vibrated continuous media producing geometric patterns | Periodic spatial structure from sustained oscillation |
| [`04-gamma-entrainment.md`](04-gamma-entrainment.md) | 40 Hz neural entrainment and amyloid-β clearance | Broadband absorption regime intersecting documented neural resonance |
| [`05-archaeoacoustic-resonance.md`](05-archaeoacoustic-resonance.md) | Low-frequency acoustic resonance in megalithic chambers | Calibrated frequency correspondence at 66 Hz and 110 Hz |
| [`06-state-space-models.md`](06-state-space-models.md) | Structured state space models in machine learning (S4, Mamba, RWKV) | **Mathematically exact equivalence with no calibration required** |
| [`07-cosmological-expansion.md`](07-cosmological-expansion.md) | Cosmological expansion as anti-collapse release at cosmic scale | Mechanism-shape correspondence between lab anti-collapse and cosmic expansion |

## Two classes of correspondence

The six mappings divide into two structurally distinct classes.

**Mathematical equivalence (no calibration).** This is the strongest possible type of cross-domain correspondence: the formal mathematical structures are identical. Two examples in this folder fall into this class. The first is the family of NLS instantiations (BEC, optics, oceanography): the equation derived here is the same equation that already describes those systems, with the addition of memory and FDT-locked noise as structural extensions. The second is the state space model correspondence: the auxiliary-field memory $\partial_t y_j = \nu_j(\rho - y_j)$ is literally the diagonal-state SSM update used in machine learning. No physical units bridge the two formulations; the equations are the same equation.

**Structural correspondence (calibration-dependent).** This is the weaker but still substantive type: the mathematical structure is the same form, but the absolute scales at which the form appears in each domain are set by domain-specific dimensional choices. The remaining four mappings (BAO, cymatics, gamma entrainment, archaeoacoustic) fall into this class. The structural fact — that oscillation, nonlinear coupling, and environmental coupling produce specific patterns — is preserved across the domains. The absolute frequencies, wavelengths, and coupling strengths are calibrated separately in each domain to its specific physical scale.

The distinction between these two classes matters for evaluation. A mathematical equivalence is harder to dismiss than a calibrated structural correspondence: the latter can always be questioned on the choice of calibration; the former cannot. Both classes are evidence for the structural-realist position, but they are evidence of different weights.

## Why this folder is the structural argument

A standard machine-learning repository or physics paper buries cross-domain content in an introduction or a discussion section. This work places it at the same hierarchical level as the equation itself. The decision reflects the methodological position documented in [`../methodology/`](../methodology/): a structural theory is evaluated not by single-quantity predictive precision in one domain but by the coherence of its form across multiple domains. The cross-domain mappings are not appendix material; they are first-class content equal in weight to the mathematical derivation and the numerical results.

A reader who has reached this folder has the right context to evaluate the work as it asks to be evaluated: not "does this equation predict X with isolated precision?" but "does the same structural form appear in independently documented physical, biological, and computational systems, and if so what does that imply?" Each document in this folder is one piece of evidence for the answer.
