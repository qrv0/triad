# Mori-Zwanzig foundation

## What this document grounds

This document grounds the auxiliary-field memory structure of the equation in a rigorous theorem from non-equilibrium statistical mechanics: the Mori-Zwanzig projection-operator formalism. The grounding is not a new mathematical result; it is the recognition that the structure P2 introduces into the equation is the standard reduced-description form that emerges, by theorem, when one projects a high-dimensional Hamiltonian system onto a slow subspace and retains the memory of the eliminated degrees of freedom.

The structural-realist argument of the work does not require Mori-Zwanzig grounding to stand: the equation is derived from P1+P2+P3 as structural axioms, evaluated by the six criteria of [`04-the-six-criteria.md`](04-the-six-criteria.md), and validated by cross-domain coherence across the documented interfaces. The Mori-Zwanzig connection adds an independent layer of rigor: the same auxiliary-variable structure that the equation introduces from physics-philosophy axioms is also the unique reduced description that classical statistical mechanics derives by projection from microscopic Hamiltonian dynamics.

## The Mori-Zwanzig theorem

The Mori-Zwanzig formalism (Mori 1965; Zwanzig 1961; modern treatments in Pavliotis 2014 *Stochastic Processes and Applications*; Chu and Li arXiv:1709.05928) is a projection-operator method for reducing high-dimensional dynamical systems to lower-dimensional descriptions while explicitly retaining the influence of the eliminated degrees of freedom as memory.

The setup. Consider a Hamiltonian system on a high-dimensional phase space, partitioned into slow ("resolved") variables $\mathbf{q}$ and fast ("eliminated") variables $\mathbf{Q}$. Define the projection operator $\mathcal{P}$ that maps any phase-space function onto a function of the slow variables alone (typically via conditional expectation in a chosen ensemble). The complementary projector is $\mathcal{Q} = 1 - \mathcal{P}$.

The exact reduced dynamics for the slow variables, obtained by applying $\mathcal{P}$ to the Liouville equation and rearranging, is the generalized Langevin equation:

$$\dot{\mathbf{q}}(t) \;=\; \mathbf{F}(\mathbf{q}(t)) \;-\; \int_0^t K(t - s)\, \mathbf{q}(s)\, ds \;+\; R(t),$$

where $\mathbf{F}$ is the conservative force in the reduced description, $K(\tau)$ is the memory kernel encoding the eliminated dynamics, and $R(t)$ is the residual stochastic force satisfying the fluctuation-dissipation relation

$$\langle R(t)\, R(t')\rangle \;=\; k_B T\, K(t - t').$$

The theorem statement is that this reduced equation is exact: no approximation has been made in passing from the full Hamiltonian dynamics to the GLE form. The price of exactness is the memory kernel, which encodes the entire history of fast-variable dynamics integrated against the slow-variable trajectory.

## Markovian embedding via auxiliary variables

The GLE in its raw form is computationally intractable: direct evaluation of the memory integral requires storing the full slow-variable history. The Markovian-embedding technique (Ceriotti-Bussi-Parrinello 2009 PRL; Baczewski-Bond 2013 J Chem Phys; Schilling 2022) makes the GLE tractable by representing the memory kernel as a finite sum of decaying exponentials,

$$K(\tau) \;=\; \sum_{j=1}^{N} c_j^2\, e^{-\nu_j \tau}/m_j,$$

and introducing auxiliary variables $s_j$ that obey local first-order linear ODEs:

$$\dot s_j \;=\; -\nu_j s_j \;+\; c_j \dot{\mathbf{q}} \;+\; \xi_j(t).$$

The friction force in the reduced equation is then $-\sum_j c_j s_j$ rather than the full memory integral. The replacement is exact for the multi-exponential kernel; the original integro-differential system becomes a coupled system of local ODEs whose dimensionality is finite (the slow variables plus $N$ auxiliary modes).

The Bernstein representation theorem ensures that any completely monotone memory kernel admits a Laplace-integral representation against a positive measure; Prony or Padé approximation discretizes this measure to arbitrary accuracy with a finite sum of exponentials. The class of memory laws that fall into this scheme includes pure exponential (Debye), multi-exponential (generalized Maxwell), stretched-exponential, power-law (approximated to high precision over many decades), and oscillatory (with complex-conjugate $\nu_j$ pairs implementing damped harmonic auxiliary modes).

## Connection to the equation's auxiliary fields

The auxiliary-field equation of the present work,

$$\partial_t y_j \;=\; \nu_j(\rho - y_j),$$

is structurally identical to the auxiliary-mode equation that the Mori-Zwanzig Markovian embedding produces for a slow variable driven by a multi-exponential memory kernel. The identification is direct: $y_j \leftrightarrow s_j$, $\nu_j \leftrightarrow \nu_j$, $\rho \leftrightarrow$ rescaled driving variable. The difference is in the driving: the GLE auxiliary equation is driven by $\dot{\mathbf{q}}$ plus a noise $\xi_j$, whereas the equation's auxiliary equation is driven by the density $\rho = |\Psi|^2$ without an explicit noise term (the noise $\eta$ enters at the level of the primary field $\Psi$, not at the level of $y_j$). Both reductions produce the same first-order linear contractive equation structure.

The implication for the equation's status. The auxiliary-field memory is not an ad-hoc modeling choice in the equation; it is the unique reduced description that Mori-Zwanzig projection from a high-dimensional Hamiltonian system produces for any slow variable coupled to a bath with multi-exponential autocorrelation. The equation, by introducing this structure as a direct consequence of P2, is consistent with what classical statistical mechanics derives by theorem.

## Why this grounding matters for the structural-realist case

Three structural consequences follow from the Mori-Zwanzig grounding.

**Criterion 1 reinforcement (internal mathematical consistency).** The auxiliary-field structure is not a phenomenological invention; it is a rigorous reduced description that follows from projection of any high-dimensional system with multi-exponential bath autocorrelation. The equation's choice of structure is consistent with the standard theorem.

**Criterion 5 reinforcement (parsimony).** The Mori-Zwanzig theorem identifies the auxiliary-mode form as the unique finite-rank representation of fading memory in completely monotone kernels. The equation, by adopting this form, makes the structurally minimal choice for representing memory at finite computational cost.

**Cross-domain coherence at the meta-level (criterion 4).** The structural correspondences documented across the interfaces are not merely coincidental shared forms; they are the consequence of the underlying mathematical fact that Mori-Zwanzig projection produces the same auxiliary-mode structure regardless of substrate. This is why the auxiliary-field equation appears in:
- Open quantum systems (interface 18 pseudomode embedding) as a quantum-version Mori-Zwanzig reduction
- Viscoelasticity (interface 19 generalized Maxwell) as a continuum-mechanics MZ reduction with stress as the slow variable
- Diagonal SSMs (see the [`mnsm`](https://github.com/qrv0/mnsm) spinoff) as a machine-learning instantiation of the same reduced description
- Hawkes processes (interface 21) as a stochastic-process Markovian lift
- Kuramoto with memory (interface 10) as a phase-only sector MZ reduction
- Warm inflation Langevin (interface 20) as a cosmological-field MZ reduction in expanding-spacetime background

The cross-domain coherence the equation exhibits is, at the foundational level, the Mori-Zwanzig theorem operating across substrates. The structural-realist position is reinforced: the form recurs because the underlying mathematical theorem applies universally.

## What this document does not claim

It does not claim that the present equation can be rigorously derived from a specific microscopic Hamiltonian via Mori-Zwanzig projection. Such a derivation would be a substantial mathematical undertaking and is open work. What this document claims is the weaker structural statement: the auxiliary-field memory form the equation introduces matches the form Mori-Zwanzig projection produces in principle, and this match is non-accidental.

It does not claim that all memory in nature is multi-exponential. The Mori-Zwanzig formalism applies most cleanly to systems with completely monotone (Bernstein-representable) autocorrelation; pathological memory kernels (oscillatory non-decaying, sign-indefinite, fractal) require generalizations. The equation's multi-exponential auxiliary-field structure is the most economical form consistent with both P2 and the standard MZ Markovian embedding; substrates with more exotic memory may require structural extensions.

It does not claim that Mori-Zwanzig grounding makes the structural-realist case independent of cross-domain evidence. The cross-domain interfaces remain the principal evidence under criterion 4; the MZ grounding adds a foundational layer that explains why those cross-domain matches exist mathematically, not a substitute for the matches themselves.

## Cross-references

- [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md): the technical derivation of the auxiliary-field structure from the integral memory kernel.
- [`../principles/02-self-reference.md`](../principles/02-self-reference.md): P2 as the structural axiom from which the auxiliary-field structure follows.
- [`01-structural-realism.md`](01-structural-realism.md): the methodology under which Mori-Zwanzig grounding is read as foundational reinforcement of cross-domain coherence.
- [`04-the-six-criteria.md`](04-the-six-criteria.md): the criteria the MZ grounding strengthens (1 consistency, 4 cross-domain coherence, 5 parsimony).
- [`../interfaces/18-pseudomode-quantum.md`](../interfaces/18-pseudomode-quantum.md), [`../interfaces/19-viscoelasticity-prony.md`](../interfaces/19-viscoelasticity-prony.md), [`mnsm/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md), [`../interfaces/21-hawkes-intensity.md`](../interfaces/21-hawkes-intensity.md): substrate-specific instantiations of the MZ auxiliary-mode reduction.

## References

- Baczewski, A. D., & Bond, S. D. (2013). Numerical integration of the extended variable generalized Langevin equation. *Journal of Chemical Physics* **139**, 044107.
- Ceriotti, M., Bussi, G., & Parrinello, M. (2009). Langevin equation with colored noise for constant-temperature molecular dynamics simulations. *Physical Review Letters* **102**, 020601.
- Chu, W., & Li, X. (2017). Mori-Zwanzig reduced models for uncertainty quantification. arXiv:1709.05928.
- Hijon, C., Espanol, P., Vanden-Eijnden, E., & Delgado-Buscalioni, R. (2010). Mori-Zwanzig formalism as a practical computational tool. *Faraday Discussions* **144**, 301.
- Lei, H., Baker, N. A., & Li, X. (2016). Data-driven parameterization of the generalized Langevin equation. *Proceedings of the National Academy of Sciences* **113**, 14183.
- Mori, H. (1965). Transport, collective motion, and Brownian motion. *Progress of Theoretical Physics* **33**, 423.
- Pavliotis, G. A. (2014). *Stochastic Processes and Applications*. Springer.
- Schilling, R. L. (2022). Generalised Langevin equation and the Markovian embedding. Lecture notes on stochastic processes.
- Zwanzig, R. (1961). Memory effects in irreversible thermodynamics. *Physical Review* **124**, 983.
