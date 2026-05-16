# Open problem 03: Topological characterization of the released state

**Status:** Open. Conjectural; preliminary evidence absent.

## Precise statement

Determine whether the spontaneous Bravais selection (BCC in 3D) documented in [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md) constitutes a topological phase transition, and if so identify the topological invariants that characterize the released crystalline state and distinguish it from the collapsed and the dispersive phases.

Candidate invariants to consider: Chern numbers (for the spinor case where the equation has internal degrees of freedom and Rashba structure); winding numbers of the phase field $\arg\Psi$; Berry phases accumulated by the auxiliary fields $y_j$ along closed loops in parameter space; the topology of the order-parameter manifold (the structure factor peaks form a discrete set in reciprocal space whose topology is non-trivial for BCC).

## What is known

- The BCC selection is robust across a range of $\Sigma\lambda$ and across random initial seeds; the structure factor peak ratio gap is $+0.13$ over FCC.
- The selection emerges from a continuous (isotropic Gaussian) initial condition; no discrete symmetry is input.
- BCC is one of the 14 Bravais lattices; among the cubic family it is distinguished by its structure factor (peaks at $(110)$ family of wavevectors).
- The equation has internal structure available (Rashba spinor as documented in [`../equation/01-derivation.md`](../equation/01-derivation.md)) that supports topological characterization via Chern numbers in the spinor case.
- In the scalar case (no spinor structure), topological characterization via Chern numbers requires identification of a band structure, which for a crystalline state of the present equation is the spectrum of small oscillations around the crystalline configuration.

## What is missing

- The band structure of small oscillations around the BCC crystalline state has not been computed.
- The Berry connection on the auxiliary-field configuration space has not been computed.
- Whether the BCC-vs-FCC selection is topologically protected (i.e., whether a continuous deformation of parameters can change the selection without crossing a phase boundary) is not known.
- Whether there exists a regime in which the crystalline state has non-trivial Chern number is not known.

## What would constitute progress

- Computation of the band structure of small oscillations around the BCC configuration; identification of any gapped bands; computation of Chern numbers for the gapped bands.
- Computation of Berry phases for closed loops in parameter space; identification of loops that produce non-zero phase (indicating topological non-triviality).
- Numerical evidence for or against topological protection: vary the parameters continuously and check whether the BCC selection persists through a smooth path or only across discrete jumps.
- A connection to the established topological-matter literature (Hasan-Kane 2010; Kitaev 2003; Wen 1991) clarifying which class of topological order the released state belongs to.
- A negative result is also progress: a clear demonstration that BCC selection is a conventional symmetry-breaking transition without topological invariants closes this open problem.

## Suggested approaches

- **Bogoliubov-de Gennes spectrum around BCC.** Linearize the equation around the BCC configuration; compute the dispersion relation; check for gapped bands.
- **Adiabatic following.** Vary $\Sigma\lambda$ slowly across the BCC-to-disorder transition; compute Berry phase accumulated by the order parameter.
- **Spinor extension.** Add Rashba structure; compute Chern numbers of the resulting bands.
- **Lattice topology.** The BCC reciprocal lattice has a specific topology (the first Brillouin zone is a truncated octahedron); examine whether the order-parameter manifold inherits any non-trivial structure from this.

## Connections to existing repo content

- [`../results/05-bravais-selection.md`](../results/05-bravais-selection.md): the result this open problem characterizes.
- [`../equation/01-derivation.md`](../equation/01-derivation.md) sections on Pauli structure and Rashba: gives the spinor extension needed for some topological characterizations.
- [`../results/03-vibrational-modes.md`](../results/03-vibrational-modes.md): the vibrational spectrum the band-structure computation extends.
- [`02-phase-diagram.md`](02-phase-diagram.md): if BCC has topological protection, the corresponding phase boundary in the phase diagram has additional structure.
- [`04-continuum-rg.md`](04-continuum-rg.md): RG analysis may shed light on whether the BCC selection is universal (and therefore likely to admit topological characterization) or non-universal.
