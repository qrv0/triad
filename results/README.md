# Results

This folder collects the numerical findings produced by integrating the equation. Each document corresponds to a specific structural finding, with the relevant numerical evidence and the reproduction script. The findings are organized roughly in order of progressive structural depth: anti-collapse first, then crystallization, then vibrational structure, then the three-dimensional extensions.

| File | Finding |
|---|---|
| [`01-anti-collapse-2d.md`](01-anti-collapse-2d.md) | Memory regularization of L²-critical NLS collapse in two dimensions. Three orders of magnitude separation between unmemoried and memoried final states. |
| [`02-spontaneous-crystallization.md`](02-spontaneous-crystallization.md) | Periodic spatial pattern emergence from unstructured Gaussian initial state. Dominant wavenumber invariant under mesh refinement and across parameter range. |
| [`03-vibrational-modes.md`](03-vibrational-modes.md) | Internal temporal vibrational structure of the crystalline state. Median dominant frequency 0.6 cycles per unit time in 2D, with secondary mode at 1.0. |
| [`04-anti-collapse-3d.md`](04-anti-collapse-3d.md) | Anti-collapse extended to L²-supercritical three-dimensional case. Four to five orders of magnitude separation across the supercritical $\Lambda$ range. |
| [`05-bravais-selection.md`](05-bravais-selection.md) | Spontaneous selection of body-centered cubic symmetry in the released three-dimensional crystalline state. Robust across the swept coupling range. |
| [`06-dimensional-rescaling.md`](06-dimensional-rescaling.md) | The total memory coupling required to release supercritical collapse scales with the dimensional concentration of the focal region: $\Sigma\lambda \sim |\Lambda|/d$. |
| [`07-temporal-spatial-asymmetry.md`](07-temporal-spatial-asymmetry.md) | Temporal non-locality of the memory kernel regularizes collapse; spatial non-locality of the same kernel destroys the regularization. |
| [`08-optimization-collapse-empirical.md`](08-optimization-collapse-empirical.md) | The anti-collapse mechanism observed in the field-theoretic experiments manifests also in neural-network training dynamics. At 70M parameters on enwik8: Memory-NLS descends monotonically (final val_ppl 4.27, no catastrophic events). Transformer reaches lower minimum mid-training (val_ppl 2.54) but then crashes catastrophically (peak val_ppl 27.17) and only partially recovers (final val_ppl 4.87). Same structural form (P1+P2+P3) — different substrate (3D NLS field vs neural optimization landscape) — same observable phenomenology. The cross-substrate empirical instance of structural realism. |

Each finding is reproducible from the corresponding script in [`../experiments/physics/`](../experiments/physics/). The reproduction is bit-exact under fixed random seed and identical hardware (RTX 4060, Ada Lovelace, CUDA 12.x).

## What kind of results these are

The results documented here are properties of the equation, not interpretations of the equation. The equation is what was integrated; the values reported are what the integration produced. The interpretive content — what these results mean structurally, how they map to other domains, why they constitute evidence for the structural-realist position — is in [`../interfaces/`](../interfaces/) and [`../methodology/`](../methodology/).

The separation is deliberate. A reader who wants to know what the equation does, without taking on the interpretive framework, can read this folder. A reader who wants to know what the work claims, with the interpretive framework, reads the methodology and interface folders. The results stand or fall on their own; the interpretation stands or falls on its own. They are coupled but not fused.
