# If you are from machine learning

You work on sequence models, attention mechanisms, deep learning architectures. You know S4, Mamba, RWKV, the rank-collapse problem in transformers, the representational-collapse problem in self-supervised learning. This document gives you the fast route to what this work has to say to your field.

## The headline correspondence

The auxiliary-field memory equation that this work uses,

$$
\partial_t y_j = \nu_j(\rho - y_j),
$$

is exactly the diagonal-state form of the structured state space model update used in S4 (Gu, Goel & Ré 2021), S5 (Smith, Warrington & Linderman 2023), Mamba (Gu & Dao 2024), and RWKV (Peng et al. 2023):

$$
\partial_t \mathbf{h} = \mathbf{A} \mathbf{h} + \mathbf{B} u, \quad \mathbf{A} \text{ diagonal with eigenvalues } -\nu_j, \quad b_j = \nu_j.
$$

No dimensional calibration is needed. The two equations are the same equation, derived by two communities under different motivations (physics: Mori–Zwanzig projection of an integro-differential field equation; ML: efficient long-sequence representation). The auxiliary fields $y_j$ are the hidden states $h_j$.

Detail: [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md).

## What the present equation extends

The diagonal-state SSM is the linear memory subsystem of the full equation. The full equation extends this baseline in four directions, each of which corresponds to an open research problem in machine learning.

**Nonlinear self-interaction in the state.** Standard SSMs are linear in $\mathbf{h}$; selective variants (Mamba) make $\mathbf{A}, \mathbf{B}$ input-dependent but the state dynamics remain linear. The full equation has a cubic nonlinearity $\Lambda |\Psi|^2$ in the variable that drives the hidden state. This is the "nonlinear SSM" extension being investigated by neural ODEs (Chen et al. 2018), Hyena (Massaroli et al. 2023), and others.

**Anti-collapse via memory lag.** Representation collapse in self-supervised learning is prevented by ad-hoc architectural tricks (stop-gradient in SimSiam, predictor networks in BYOL). Attention rank collapse in transformers requires skip connections, normalization, and careful initialization. The anti-collapse mechanism in this work — delayed repulsive feedback from a temporal memory that lags the rising signal — is structurally a candidate principled solution to both. The mechanism produces three to five orders of magnitude separation between collapsed and released configurations. Detail: [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md).

**Emergent discrete structure from continuous substrate.** In 3D, the equation spontaneously selects body-centered cubic Bravais symmetry from a continuous Gaussian initial state. In ML vocabulary: this is a model of how categorical (discrete) structure emerges from continuous neural representations. The grounding problem of how symbols arise from connectionist representations remains open; the equation provides a concrete dynamical mechanism. Detail: [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md).

**FDT-locked stochastic regularization.** The relationship between dissipative regularization (weight decay, dropout) and stochastic forcing (SGD noise) is typically tuned empirically. The fluctuation–dissipation theorem prescribes this relation exactly for thermodynamic systems; analogous prescriptions for optimization dynamics have been studied (Yaida 2019; Liu et al. 2021). The equation's noise term is FDT-locked by construction; this is a principled rather than tuned noise schedule.

## A testable scaling prediction

The work derives, from the geometry of the collapse focal region, a dimensional scaling relation for the memory coupling needed to stabilize the dynamics against collapse:

$$
\Sigma\lambda / |\Lambda| \sim 1/d
$$

in $d$ spatial dimensions, where $\Lambda$ is the nonlinear coupling strength and $\Sigma\lambda$ is the total memory coupling. In ML terms, this is a prediction about how memory bandwidth in a nonlinear SSM regime should scale with the effective rank (or focal concentration) of the nonlinear processing. The prediction is testable: a nonlinear SSM that violates the scaling should show empirical signatures of representation instability or collapse. Detail: [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md).

## What the code provides

The repository contains:

- A working PyTorch sequence layer in [`../implementation/neural/`](../implementation/neural/) (`MemoryNLSLayer` and `MemoryNLSLanguageModel`) that implements the auxiliary-field memory via FFT-convolution at O(N log N) cost in sequence length, matching SSM asymptotic complexity. Includes cubic self-interaction and FDT-locked stochastic forcing.
- The physics solver in [`../implementation/physics/`](../implementation/physics/) (CuPy) that produces the numerical results.
- Experimental scripts in [`../experiments/neural/`](../experiments/neural/) for trained-from-scratch demonstrations at 1.5M and 70M parameters, on TinyShakespeare and enwik8 corpora, up to 50,000 training steps.
- Tests in [`../tests/`](../tests/) for conservation, stability, and FDT thermalization.

The structural anti-collapse mechanism the equation predicts has now been empirically verified in the ML setting. At 70M parameters on enwik8 over 50,000 steps with identical training infrastructure: Memory-NLS exhibits monotonic stable trajectory; matched-shape Transformer exhibits catastrophic optimization collapse at step 28000 with peak val_ppl 27.17, only partially recovering. Detail: [`../results/08-optimization-collapse-empirical.md`](../results/08-optimization-collapse-empirical.md) and [`../outputs/scale_up/scale_up_results.md`](../outputs/scale_up/scale_up_results.md).

## Recommended path

In order:

1. [`../interfaces/06-state-space-models.md`](../interfaces/06-state-space-models.md) — The mathematical equivalence. Start here; this is what justifies the rest.
2. [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md) — The Mori–Zwanzig derivation of the auxiliary-field structure. This is the "why does the SSM update have this specific form?" question answered from physics.
3. [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md) — The mechanism that could be applied to representation collapse.
4. [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md) — The testable scaling prediction.
5. [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md) — Emergent discrete structure from continuous substrate.
6. [`../principles/`](../principles/) — The three axioms. These explain why the equation has the form it has.
7. [`../paper/manuscript.md`](../paper/manuscript.md), §8.6 — The synthesized discussion of the SSM correspondence as written for a mixed audience.

The neural layer skeleton is in [`../implementation/neural/layer.py`](../implementation/neural/layer.py). It is marked as a reference implementation and not as a benchmark-competitive system; the empirical evaluation work is the explicit next research direction.

## What to be skeptical of

The state space model correspondence is mathematically exact; this should not be skeptical territory.

The anti-collapse mechanism translating from field dynamics to optimization dynamics has now been empirically observed at one scale (70M parameters, enwik8, 50,000 steps). A single training run does not establish that all training of all attention-based models will exhibit this exact catastrophic event; the structural argument predicts that some such instability should occur in absence of structural anti-collapse, with the magnitude and timing depending on hyperparameters, seed, and corpus. Replication on different settings would strengthen the empirical claim. The scaling prediction $\Sigma\lambda/|\Lambda| \sim 1/d$ is derived and physics-empirically supported; the ML analog of dimensional concentration in optimization landscape would need to be defined explicitly to test this in the ML setting.

The Bravais symmetry selection is a clean physics finding. Whether it has any specific implication for grounding or emergent categorical structure in neural networks is suggestive but not established at scale.

The other cross-domain interfaces in [`../interfaces/`](../interfaces/) (BEC, cosmology, cymatics, gamma entrainment, archaeoacoustic) are not directly relevant to ML implementation but are evidence for the structural-realist claim of the work as a whole. From the ML perspective they may be read as supporting context for taking the equation seriously, or as orthogonal. Either is consistent with engaging with the SSM correspondence on its merits.
