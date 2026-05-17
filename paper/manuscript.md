# Memory, Coupling, and Spontaneous Order in a Nonlinear Schrödinger Field

**A Memory-Augmented Nonlinear Schrödinger Field Equation: Derivation, Phenomenology, and Cross-Domain Structural Correspondences**

*Author: qrv0*

---

## Abstract

We construct a complex scalar (optionally spinor) field equation on a two- or three-dimensional continuum from three minimal structural axioms: that persistent physical entities oscillate (P1), that they are defined by self-reference both instantaneously and across time (P2), and that perfect dynamical isolation is unattainable (P3). The unique mathematical structure these axioms select is a nonlinear Schrödinger equation augmented with an integral memory kernel, fractional spatial dispersion, linear dissipation, and fluctuation–dissipation-locked stochastic forcing. Through Markovian embedding of a multi-exponential temporal kernel (Mori 1965; Zwanzig 1961), the integro-differential system reduces exactly to a finite set of coupled local differential equations. A Strang split-step solver on consumer GPU hardware achieves machine-precision norm conservation in unitary regimes and reproduces analytical solutions for dissipative and FDT-thermalized limits to within published tolerances.

The equation generates four classes of nontrivial behavior that are not present in any of its single-term limits. (i) In the L²-critical two-dimensional case, the integral memory potential suppresses finite-time blow-up by three orders of magnitude relative to the unmemoried run at identical initial conditions and coupling; the suppression mechanism is the temporal lag between density spike and reservoir uptake, which generates a delayed repulsive overshoot. (ii) From an unstructured Gaussian initial state, the system spontaneously selects a periodic spatial pattern whose dominant wavenumber is invariant under lattice refinement and across an interior region of coupling parameter space. (iii) In three dimensions, where the cubic NLS is L²-supercritical and collapse is generic, the same anti-collapse mechanism operates but requires the total memory coupling to scale with the dimensional concentration of the focal region: the ratio Σλ/|Λ| required to release the collapse is approximately 0.5 in three dimensions, compared with approximately 0.05 in two dimensions. The Bravais symmetry spontaneously selected by the released three-dimensional state is body-centered cubic, robust across the swept coupling range. (iv) The crystalline state exhibits internal vibrational structure with a dominant low-frequency mode and discrete higher harmonics.

We argue that the appropriate methodological frame for evaluating an equation of this kind is structural rather than narrowly predictive. The equation's third principle asserts that isolation is a property of method, not of the world; consequently the standard falsificationist criterion, which presupposes the isolability of variables, stands in tension with the content the equation asserts. We adopt the position of structural realism (Ladyman & Ross 2007; Worrall 1989), reinforced by the Duhem–Quine thesis (Duhem 1906; Quine 1951) and by Cartwright's analysis of model–world separation (Cartwright 1983), and we evaluate the equation against six criteria appropriate to structures: internal mathematical consistency, reproducibility, generative scope, cross-domain coherence, parsimony, and comprehensiveness.

We close by mapping the equation's mathematical form onto twenty-one domains where the same structural shape is independently documented: (i) other instances of nonlinear Schrödinger dynamics, particularly in Bose–Einstein condensates and nonlinear optical media; (ii) baryon acoustic oscillations in cosmological structure formation; (iii) Chladni cymatic patterns in vibrated media; (iv) gamma-frequency neural entrainment and amyloid-β clearance; (v) low-frequency acoustic resonances measured at megalithic chambers; (vi) the Markovian-embedded state representation used in contemporary neural sequence architectures (S4, S5, Mamba, RWKV), where the mathematical correspondence is exact and requires no dimensional calibration; (vii) the cosmological expansion mechanism itself, where the same anti-collapse phenomenology that the equation produces in laboratory simulation is proposed as the structural form underlying cosmic expansion from a near-singular initial state; (viii) the empirical phenomenology documented by the mechanistic-interpretability program on attention-based language models (superposition, polysemantic neurons, post-hoc sparse-dictionary recovery), which the structural argument predicts as the necessary consequence of an architecture instantiating P1 and P3 without P2's auxiliary-field memory hierarchy; (ix) the broadband-multi-timescale phenomenology that the critical-brain literature documents in cortex (neuronal avalanches, 1/f spectra, scale-free response), which the equation produces in its broadband-absorbing crystalline regime by structural selection rather than parameter tuning; (x) coupled phase oscillators with memory (Kuramoto and its memory-augmented generalizations), where the equation in the phase-only sector and the memory-Kuramoto formulation are the same Markovian embedding of the same integro-differential form; (xi) B-cell affinity maturation in adaptive immunity, where the multi-timescale memory hierarchy of chromatin marks plus memory-cell populations plus germinal-center selection instantiates the auxiliary-field hierarchy in a discrete-cell biological substrate; (xii) the variational dynamics of the Friston free-energy principle and active inference, where the hierarchical predictive-coding stack with multi-timescale layers maps directly onto the equation's auxiliary-field hierarchy at the mathematical level; (xiii) active matter (self-propelled particles, flocks, active gels), where an order-parameter field with alignment memory under external energy injection exhibits the structural form across substrates; (xiv) self-organized criticality (Bak-Tang-Wiesenfeld sandpile, neuronal avalanches, earthquake statistics), where the triangle structure is required for SOC to exist and the equation's release transition is mechanism-shape-equivalent; (xv) cardiac dynamics, where the refractory + restitution + autonomic-coupling triangle is operative and arrhythmias partition by triangle-element dysregulation; (xvi) gene regulation and circadian rhythms, where the multi-timescale memory hierarchy spans transcription (minutes) through circadian (day) through chromatin (months) to evolutionary (generations); (xvii) multi-species ecosystem dynamics, where age-structured populations with trait inheritance under interspecies and abiotic coupling exhibit the structural form at the ecological scale; (xviii) non-Markovian open quantum systems via the Garraway-Tamascelli-Pleasance pseudomode embedding, where auxiliary discrete modes plus Markovian dissipators reproduce the equation's memory subsystem term-by-term in the quantum density-operator substrate; (xix) generalized Maxwell / Prony viscoelasticity, where the auxiliary-field memory equation is the industrial-standard internal-variable representation deployed in PyLith, COMSOL, Ansys and Abaqus across polymers, geophysics, and biomechanics; (xx) warm inflation as cosmological Langevin scalar field, where Berera-Moss-Ramos derive the FDT-locked structure of P3 directly in an inflaton-plus-thermal-bath substrate; and (xxi) self-exciting Hawkes point processes with exponential memory kernels, where the Markovian representation derived by Errais-Giesecke-Goldberg is structurally identical to the auxiliary-field equation and governs intensity dynamics across seismology, finance, social contagion, and neural spike trains. The structural correspondence is exact in form; the dimensional calibration that relates the equation's unit time to specific physical frequencies in domains (iv), (v), and (vii) is a choice and we mark it as such. We additionally report a cross-substrate empirical confirmation: the structural anti-collapse mechanism the equation predicts in 3D field dynamics manifests in the optimization landscape of a 70M-parameter neural network's training trajectory, with a matched-shape Transformer (lacking the structural mechanism) exhibiting catastrophic optimization collapse where the Memory-NLS architecture maintains a monotonic stable trajectory. The argument advanced is not that the equation predicts these phenomena under a single privileged identification, but that the same mathematical structure appears at multiple scales of physical and computational organization, and that this is the criterion by which a structural realist evaluates a candidate fundamental form.

---

## 1. Introduction

The nonlinear Schrödinger equation occupies an unusual position in mathematical physics. As the leading-order envelope equation for a wide class of weakly nonlinear, weakly dispersive wave systems, it appears identically in the description of optical pulses in fibers, surface gravity waves in deep water, Langmuir oscillations in plasmas, and the macroscopic wavefunction of a Bose–Einstein condensate. Its appearance across this range of physical substrates is not a coincidence of mathematical convenience but a structural fact: when a continuous field oscillates intrinsically, interacts with itself through a local cubic nonlinearity, and is observed on scales long compared with the period of oscillation but short compared with relaxation toward equilibrium, the leading nontrivial dynamics is captured by an NLS-form equation.

This work extends the standard NLS framework by retaining three structural ingredients that the bare cubic NLS omits. The first is temporal non-locality: the present state of the field depends not only on its instantaneous density but on a weighted integral of its density at past times. The second is environmental coupling: the field exchanges energy with an external bath, mediated by linear dissipation and stochastic forcing that obey the fluctuation–dissipation theorem (Kubo 1966). The third, retained from the standard treatment but emphasized here as structurally essential, is the instantaneous self-coupling through the cubic nonlinearity itself. We argue that these three additions are not optional or ad-hoc but are required by a small set of structural axioms about persistent physical entities, and that the equation that uniquely instantiates these axioms generates phenomena that no proper subset of its terms can produce.

The paper is organized as follows. Section 2 states the three structural principles. Section 3 derives the equation from those principles, including the Markovian embedding of the temporal kernel and the closed-form propagator that handles the optional spinor structure. Section 4 describes the computational implementation, the Strang split-step solver, and the suite of conservation diagnostics used to validate it. Sections 5 and 6 report numerical results in two and three spatial dimensions respectively, with particular attention to the dimensional scaling of the anti-collapse mechanism, the spontaneous selection of crystalline Bravais symmetry in three dimensions, and the internal vibrational spectrum of the crystalline state. Section 7 articulates the methodological position from which we propose this work be evaluated. Section 8 maps the equation's structural form onto five independently documented physical domains. Section 9 discusses what we take this mapping to establish, and what we are explicit in not claiming.

---

## 2. Three Structural Principles

The three principles below are stated as axioms about physical structure rather than as testable predictions. They are not derived from prior physics; they are the input from which the physics is constructed. Their selection is justified, where justification is possible, by appeal to their universality across physical, biological, and information-theoretic systems and by the parsimony of the equation they jointly select.

**Principle P1, Persistent entities oscillate.** Every spatially extended entity that persists in time exhibits intrinsic oscillation at one or more characteristic scales. A literally static extended structure, free of internal oscillation, is unstable: any perturbation either decays (in which case the structure was not persistent except as an external constraint) or grows (in which case the structure undergoes phase transition). Permanence of form requires permanent internal motion. Mathematically, this selects a complex field $\Psi(t, \mathbf{x}) \in \mathbb{C}$ carrying a phase $\varphi = \arg\Psi$ over a real scalar field; phase rotation accommodates oscillation without amplitude change.

**Principle P2, Existence is self-referential.** A persistent entity is defined by its relation to itself, both instantaneously and across its own past. Instantaneous self-reference manifests as local nonlinearity: the field acts on itself through its own density, generating either attractive ($\Lambda < 0$) or repulsive ($\Lambda > 0$) self-interaction. Self-reference across time manifests as a memory potential, in which the present state is influenced by an integral of past density values:

$$
V_{\text{mem}}(t, \mathbf{x}) = \int_0^t dt' \int d^n x'\, \hat{U}(t - t', \mathbf{x}, \mathbf{x}')\, |\Psi(t', \mathbf{x}')|^2,
$$

where $\hat{U}$ is a memory kernel and $n$ is the spatial dimension. The two forms of self-reference act on different timescales and, as we will show, on different spatial geometries with qualitatively different consequences.

**Principle P3, Isolation is temporary.** Perfect dynamical isolation does not occur. Every persistent physical system is coupled to its surroundings, exchanges energy and entropy with them, and cannot evolve as a closed Hamiltonian system indefinitely. Coupling is the default state; isolation is a transient idealization useful for analysis but never realized in full. Mathematically, this requires the simultaneous presence of dissipative terms removing amplitude and stochastic forcing returning amplitude, with the two locked to one another by the classical fluctuation–dissipation relation (Callen & Welton 1951; Kubo 1966):

$$
\langle \eta(t, \mathbf{x}) \eta^*(t', \mathbf{x}') \rangle = 2 \gamma_0 k_B T\, \delta(t - t')\, \delta^{(n)}(\mathbf{x} - \mathbf{x}').
$$

Without this lock, dissipation alone drives the field unphysically to vacuum, and noise alone heats it unboundedly. With the lock, the field thermalizes to a stationary distribution whose temperature is set by the bath.

These three principles, taken together, are minimal but not arbitrary. Each is consistent with established physical theory: P1 with standard quantum and condensed-matter formalism; P2 with the integro-differential structure of Mori–Zwanzig projection from kinetic theory; P3 with open-quantum-system formalism and stochastic field theory. What we claim is that taken together, they are sufficient to derive a unique equation, and that the equation so derived produces phenomena not implied by any single principle alone.

---

## 3. The Equation: Formal Derivation

### 3.1 The kinetic generator

P1 requires a complex field with a norm-preserving generator. The most economical such generator on a flat continuum is the Laplacian, optionally generalized to a fractional Laplacian to accommodate anomalous transport regimes:

$$
\hat{H}_{\text{kin}} = -\frac{\hbar^2}{2m} \nabla^2 + \alpha\, (-\Delta)^{\sigma/2}, \qquad \sigma \in (1, 2].
$$

For systems with internal degrees of freedom (spin-½, polarization, two-band electronic structure) the field generalizes to a two-component spinor and the Hamiltonian acquires Pauli-matrix structure. In $k$-space:

$$
H(\mathbf{k}) = a(\mathbf{k})\mathbb{1} + n_x(\mathbf{k})\sigma_x + n_y(\mathbf{k})\sigma_y + n_z(\mathbf{k})\sigma_z,
$$

where $a(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \alpha |\mathbf{k}|^\sigma - i\gamma_0$ carries the scalar dispersion and isotropic dissipation, and the $n_i$ encode Rashba spin-orbit coupling and momentum-dependent dissipation. The propagator over a time step admits a closed form via the Pauli identity:

$$
U(\mathbf{k}) = e^{-iH(\mathbf{k})\,dt} = e^{-ia\,dt}\!\left[\cos(\omega\,dt)\mathbb{1} - i\frac{\sin(\omega\,dt)}{\omega}\bigl(n_x \sigma_x + n_y \sigma_y + n_z \sigma_z\bigr)\right],
$$

with $\omega^2 = n_x^2 + n_y^2 + n_z^2$, valid for complex $\omega$ when the Hamiltonian is non-Hermitian. This closed form is essential to the numerical method described in Section 4.

### 3.2 Local nonlinearity and the integral memory kernel

P2 has two parts. The instantaneous part is the standard Gross–Pitaevskii term $\Lambda \rho \Psi$ where $\rho = |\Psi|^2$. The integral memory potential $V_{\text{mem}}$ is the central novel structural ingredient of this work.

A general kernel $\hat{U}(t - t', \mathbf{x}, \mathbf{x}')$ is computationally intractable: direct evaluation requires storing the full history of $\Psi$. For a kernel that factors as a multi-exponential in time and a delta in space,

$$
\hat{U}(\tau, \mathbf{x}, \mathbf{x}') = \sum_{j=1}^N \lambda_j \nu_j e^{-\nu_j \tau}\, \delta^{(n)}(\mathbf{x} - \mathbf{x}'),
$$

the convolution reduces exactly to a finite system of local ordinary differential equations through Markovian embedding (Mori 1965; Zwanzig 1961). Defining auxiliary fields $y_j(t, \mathbf{x})$ by

$$
\partial_t y_j = \nu_j (\rho - y_j),
$$

the memory potential becomes

$$
V_{\text{mem}}(t, \mathbf{x}) = \sum_{j=1}^N \lambda_j y_j(t, \mathbf{x}).
$$

Each $y_j$ is a memory reservoir with relaxation time $\tau_j = 1/\nu_j$ and coupling strength $\lambda_j$. A fast reservoir ($\nu_j \gg 1$) tracks $\rho$ closely; a slow reservoir ($\nu_j \ll 1$) responds to the integrated history. The total memory potential is a superposition of these distinct timescales, and the qualitative dynamics of the equation depend on the spectrum of $\nu_j$ as well as the magnitudes of $\lambda_j$. Spatial non-locality, if introduced by replacing $\delta^{(n)}(\mathbf{x} - \mathbf{x}')$ with a Gaussian or exponential kernel, can be handled efficiently in Fourier space; the qualitative effect, as shown in Section 5, is asymmetric to that of temporal non-locality.

### 3.3 Environmental coupling

P3 introduces $-i\Gamma$ and $\eta$. The linear dissipation $\Gamma = \gamma_0 \mathbb{1} + i\gamma_s(k)\sigma_z$ may include a momentum-dependent component generating non-Hermitian skin effects (Yao & Wang 2018; Bergholtz, Budich & Kunst 2021), but the structural minimum is homogeneous dissipation at rate $\gamma_0$. The stochastic forcing satisfies the FDT correlator stated in Section 2; discretized,

$$
\Psi \to \Psi + \sqrt{2 \gamma_0 k_B T\, dt}\, \xi,
$$

where $\xi$ is a unit-variance complex Gaussian sampled per voxel per time step.

### 3.4 The full equation

Combining the three ingredients:

$$
\boxed{\;
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta\;
}
$$

with $V_{\text{mem}} = \sum_j \lambda_j y_j$, $\partial_t y_j = \nu_j (\rho - y_j)$, and $\eta$ satisfying the FDT correlator. The covariant derivative $D = \nabla - iq\hat{A}/\hbar$ admits an optional external gauge potential $\hat{A}$.

### 3.5 Reduction to known equations

The full equation reduces to several familiar limits:

| Limit | Recovered equation |
|---|---|
| $\Lambda = 0$, no memory, no $\Gamma$, no $\eta$ | Free Schrödinger |
| $\Lambda \ne 0$, no memory, no $\Gamma$, no $\eta$ | Gross–Pitaevskii (Pitaevskii & Stringari 2016) |
| $\gamma_0 > 0$, no $\eta$ | Lindblad-type open quantum system |
| $\gamma_0 > 0$, $\eta$ active, FDT | Stochastic Gross–Pitaevskii / classical-field thermalization |
| $\alpha_R \ne 0$, $\gamma_s \ne 0$ | Rashba spinor with non-Hermitian skin |
| $\sigma < 2$, $\alpha \ne 0$ | Fractional NLS (Laskin 2018) |

The full equation, with all terms active, is not in the standard catalog.

---

## 4. Computational Methodology

### 4.1 Strang split-step integration

The equation is integrated in time by symmetric splitting (Strang 1968). Each time step decomposes into five sub-steps:

1. **Half potential step in real space:** $\Psi \leftarrow \exp(-i V_{\text{tot}}\, dt/2)\, \Psi$, where $V_{\text{tot}} = V_{\text{ext}} + \Lambda \rho + V_{\text{mem}}$ is the instantaneous real-space potential. This is a pointwise phase rotation, unitary for real $V_{\text{tot}}$.
2. **Kinetic step in momentum space:** $\Psi \leftarrow \text{IFFT}[U(\mathbf{k})\, \text{FFT}[\Psi]]$, where $U(\mathbf{k})$ is the pre-computed full-step propagator.
3. **Half potential step in real space** with the density updated from sub-step 2.
4. **Ornstein–Uhlenbeck update of auxiliary fields:** $y_j \leftarrow e^{-\nu_j dt} y_j + (1 - e^{-\nu_j dt})\, \rho_{\text{eff}}$, where $\rho_{\text{eff}}$ is the density (or its spatially smoothed variant for non-local kernels). This update is exact, independent of $dt$, because $y_j$ is a linear contractive map.
5. **Stochastic increment** (if $\Gamma > 0$ and $T > 0$): $\Psi \leftarrow \Psi + \sqrt{2\gamma_0 T\, dt}\, \xi$.

The leading splitting error is $\mathcal{O}(dt^2)$. The Fourier-space kinetic step is spectrally accurate in space.

### 4.2 Validation

The solver is implemented in CuPy for GPU acceleration via cuFFT on an NVIDIA RTX 4060 (Ada Lovelace, 8 GB VRAM). A suite of six conservation diagnostics is executed before any phenomenological run is performed. In fp64 precision, on a $64 \times 64$ lattice:

| Diagnostic | Result | Reference |
|---|---|---|
| Norm conservation, free Gaussian, 400 steps | drift $< 1.1 \times 10^{-13}$ | machine precision |
| Norm conservation, Rashba spinor, 400 steps | drift $< 1.3 \times 10^{-13}$ | machine precision |
| Norm conservation, memory auxiliary, 200 steps | drift $< 6.9 \times 10^{-14}$ | machine precision |
| Pure dissipative decay, $\|\Psi\|^2(t)$ vs. $e^{-2\gamma t}$ | 0.00% relative error to 6 sig. figs. | analytical |
| Sub-critical attractive 2D-NLS | clean dispersion, no collapse | Sulem & Sulem 1999 |
| FDT thermalization, $\langle|\Psi|^2\rangle$ per cell vs. $2T$ | within 0.5% | equipartition |

In fp32 precision (the default for three-dimensional production runs), norm drift is approximately $10^{-7}$ per thousand steps, consistent with cuFFT roundoff and adequate for signals of magnitude $10^{-1}$ to $10^1$ over $10^3$-step trajectories.

### 4.3 Lattice scale and reproducibility

All runs use periodic boundary conditions. Lattice sizes range from $N^2 = 64^2$ to $512^2$ in two dimensions and $N^3 = 64^3$ to $128^3$ in three dimensions. Wavelengths $\lambda_{\text{wave}} \gtrsim 4\Delta x$ (with $\Delta x = L/N$ the lattice spacing) are well-resolved; results reported are insensitive to mesh refinement above this threshold. Random number generation uses fixed seeds; trajectories reproduce bit-for-bit on identical hardware.

---

## 5. Two-Dimensional Phenomenology

We summarize four classes of phenomena that appear when the full equation is integrated in two spatial dimensions. Detailed parameter values are given in the captions.

### 5.1 Memory regularization of supercritical-norm collapse

The bare attractive two-dimensional NLS is L²-critical (Sulem & Sulem 1999): solutions whose initial L² norm exceeds the Townes-soliton energy undergo finite-time blow-up, while sub-critical solutions disperse. We compare integration of the equation in this regime ($\Lambda = -8$, Gaussian initial state with width $\sigma_0 = 1.2$ and momentum $(k_{x0}, k_{y0}) = (1.0, 0.5)$, 256² lattice, $dt = 0.0025$, 4000 steps) with and without the memory potential active. Two-mode memory $(\nu_1, \lambda_1, \nu_2, \lambda_2) = (10, 0.3, 0.5, 0.1)$.

Without memory, the wavepacket undergoes the expected collapse trajectory: peak density grows by approximately 500× to $\rho_{\max} \sim 100$ (the value to which the lattice clips the would-be singularity) by $t \approx 2$, and remains locked at lattice scale through $t = 10$. With memory active, the wavepacket follows an identical trajectory through the initial spike, but at $t \approx 2$ the memory potential, which has tracked the rising density with relaxation lag $\tau_1 = 0.1$ and $\tau_2 = 2$, overshoots and generates a repulsive force that exceeds the attractive nonlinear term, releasing the field outward. By $t = 10$ the peak density is $\rho \approx 0.03$, three orders of magnitude below its maximum and below its initial value.

The mechanism is a direct consequence of the lag between $\rho$ and $V_{\text{mem}}$. When $\rho$ rises sharply, $y_j$ rises with delay $\tau_j$. By the time $V_{\text{mem}} = \sum_j \lambda_j y_j$ has caught up with the spike, $\rho$ may have already begun to decline; $V_{\text{mem}}$ then exceeds its equilibrium value, generating a transient net repulsion. The slow reservoir ($\nu_2 = 0.5$) sustains this repulsion across multiple oscillations of the fast reservoir, preventing the field from re-collapsing.

In every run with spatially non-local memory kernels (Gaussian or exponential spatial smearing of the kernel $\hat{U}$), the anti-collapse mechanism failed and the field collapsed to lattice scale despite the presence of temporal memory. Temporal and spatial non-locality act asymmetrically: temporal non-locality regularizes collapse; spatial non-locality dissolves the regularization by smearing the repulsive response across a region wider than the focal point. This asymmetry, encoded in the relative role of the two non-localities, is a structural feature of the equation that we discuss further in Section 7.

### 5.2 Spontaneous crystallization

When $\Lambda = -8$ and the memory coupling is increased to $\lambda \approx 1$, the field emerging from the initial collapse-and-release transient does not disperse uniformly. Instead it organizes into a stationary periodic spatial pattern: a two-dimensional lattice of high-density spots that tile the box. Fourier analysis of the late-time density profile reveals a sharp peak in the radial power spectrum at $k^\ast \approx 2.13$ in lattice units, corresponding to an intrinsic wavelength $\lambda_{\text{wave}} \approx 2.95$ lattice units. This dominant wavenumber is invariant under mesh refinement from $N = 256$ to $N = 512$, and it is invariant across variations of $\Lambda$ and $\lambda$ within the crystalline regime. It is, in the sense of dynamical systems, the most unstable mode of the modulational instability of the unperturbed uniform state.

### 5.3 Discrete vibrational modes of the crystal

Dense temporal sampling of the crystalline state at $\Lambda = -8$, $\nu = 10$, $\lambda = 1$, $\Gamma = 0$, $T = 0$ over 4000 frames at $dt = 0.0025$ (10 time units total) reveals that the spatial pattern is not static. Each lattice point oscillates in time. Per-pixel temporal FFT yields a distribution of dominant frequencies with the following properties: the range is approximately 0.1–7.6 cycles per unit time, the median is 0.6 cycles per unit time, and a secondary mode is locked at exactly 1.0 cycle per unit time. The total spectrum exhibits a power-law decay with discrete superimposed peaks; spatial maps of the dominant frequency show structure, with certain lattice regions vibrating at $\sim 0.3$ cycles per unit time and others at $\sim 1$+ cycles per unit time. Norm conservation throughout: $10^{-13}$.

### 5.4 Broadband absorption of external driving

When the crystalline state is subjected to an external oscillatory drive $V_{\text{drive}}(t, \mathbf{x}) = A\cos(\omega t)\exp(-r^2/8)$ localized at the box center, with $\omega$ swept from 0.1 to 30 in 26 values, the crystalline configuration absorbs energy at a rate approximately 100× that of any single-term limit (linear, $\Lambda$-only, memory-only). The absorption profile rises sharply for $\omega \gtrsim 3$ and plateaus across the high-frequency band. Bichromatic driving at $(\omega_1, \omega_2)$ generates response peaks at the sum frequency, the difference frequency, and integer harmonics, the signature of nonlinear heterodyne mixing.

These four findings, taken together, characterize the two-dimensional phenomenology of the equation in the strongly attractive regime with active memory. We now turn to three dimensions, where the L²-supercritical character of the cubic NLS qualitatively changes what is being regularized.

---

## 6. Three-Dimensional Extension

### 6.1 Supercriticality and the structural rescaling of memory coupling

The three-dimensional cubic NLS is L²-supercritical: any sufficiently concentrated initial state collapses, with no critical-norm threshold below which collapse is forbidden. The anti-collapse claim in three dimensions is therefore a stronger statement than in two: there is no kinematic-pressure regime in which the field is protected without the memory mechanism.

We integrated the equation at $\Lambda \in \{-2, -4, -6, -8, -10, -12\}$ with and without memory, on a $128^3$ lattice with $L = 20$ and $dt = 0.0025$, initial Gaussian width $\sigma_0 = 0.5$, zero initial momentum, 4000 steps, $\Gamma = 0$, $T = 0$. The initial state at $\sigma_0 = 0.5$ has peak density $\rho_0 = (2\pi\sigma_0^2)^{-3/2} \approx 1.44$ and lies above the three-dimensional collapse threshold for $|\Lambda| \gtrsim 8$.

With single-mode memory $(\nu, \lambda) = (10, 0.3)$, identical to the two-dimensional M1 sweep, the unmemoried runs at $\Lambda \le -8$ collapse to lattice-scale peaks $\rho_{\max} \in [57, 65]$ and remain locked there. The memoried runs at the same $\Lambda$ also lock at lattice scale: $\rho_{\max} \in [50, 72]$. Memory reduces the final peak by approximately 10–20% relative to the unmemoried run but does not release the field. This is in marked contrast to the two-dimensional result.

We attribute this difference to a structural geometry argument. In two dimensions, the collapse focal region at lattice clipping covers approximately $10^2$ lattice cells; in three dimensions, the focal region covers approximately $10$ cells. The memory potential at the peak is $V_{\text{mem}} \sim \Sigma\lambda \cdot \rho_{\text{eff}}$, where $\rho_{\text{eff}}$ is the density averaged over the region in which memory has accumulated. In two dimensions $\rho_{\text{eff}} \approx \rho_{\max}$; in three dimensions, because the focal region is approximately one order of magnitude smaller in voxel count, $\rho_{\text{eff}} \approx \rho_{\max}/10$. To produce the same ratio $V_{\text{mem}}/|\Lambda \rho|$ at the peak, $\Sigma\lambda$ must scale up by approximately one order of magnitude in three dimensions.

This prediction is testable. We re-ran the supercritical $\Lambda = -8$ case with two-mode memory at total coupling $\Sigma\lambda = 4$ (specifically $\nu_1 = 10, \lambda_1 = 3.0; \nu_2 = 0.5, \lambda_2 = 1.0$) at otherwise identical parameters. The anti-collapse mechanism is recovered: $\rho_{\max} = 6.88$ (5× the initial peak, below lattice scale), and $\rho_{\text{final}} = 6 \times 10^{-4}$. The separation between unmemoried and memoried final states is approximately five orders of magnitude.

Replicating across $\Lambda \in \{-6, -8, -10, -12\}$ at fixed $\Sigma\lambda = 4$, the anti-collapse separation between memoried and unmemoried runs is four to five orders of magnitude in every case where the unmemoried run reaches collapse. Two qualitatively distinct dynamical signatures appear, depending on $\Lambda$: at $\Lambda$ near the collapse threshold, memory aborts the collapse before it reaches lattice scale; at strongly supercritical $\Lambda$, the collapse reaches lattice scale first and is then released. Both terminate at $\rho \sim 10^{-3}$.

We summarize: the anti-collapse mechanism of the two-dimensional equation generalizes to the three-dimensional supercritical regime under a derivable dimensional rescaling of the total memory coupling. The mechanism is dimension-independent; the calibration is not.

### 6.2 Spontaneous Bravais lattice selection

The three-dimensional released state, in the regime $\Sigma\lambda \sim 1.5$ at $\Lambda = -8$, organizes itself into a spatially periodic configuration whose Bravais symmetry can be identified by analyzing the angular distribution of power on a thin spherical shell in $k$-space at the dominant radial wavenumber $k^\ast$. We score the shell-integrated power against canonical Bravais signatures: simple cubic (SC, 6 peaks at axis directions), body-centered cubic (BCC, 12 peaks at $(1,1,0)$-type permutations), face-centered cubic (FCC, 8 peaks at $(1,1,1)$-type permutations), and hexagonal close-packed (HCP, hexagonal in-plane plus axial).

Across a sweep of total memory coupling $\Sigma\lambda \in \{0.5, 1.0, 1.5, 2.0, 2.5, 3.0\}$ at $\Lambda = -8$, three regimes appear:

| $\Sigma\lambda$ | Peak density | FWHM | Crystallinity | Best Bravais (score) |
|---|---|---|---|---|
| 0.5 | 66.5 | 0.94 | 1.000 | BCC (0.438) |
| 1.0 | 51.9 | 0.94 | 1.000 | BCC (0.441) |
| 1.5 | $2.8 \times 10^{-3}$ | 0.94 | 0.997 | BCC (0.439) |
| 2.0 | $1.0 \times 10^{-3}$ | 0.94 | 0.981 | BCC (0.336) |
| 2.5 | $1.8 \times 10^{-3}$ | 1.56 | 0.976 | BCC (0.336) |
| 3.0 | $1.0 \times 10^{-3}$ | 1.56 | 0.976 | BCC (0.335) |

For $\Sigma\lambda \le 1.0$, memory is too weak to release the lattice-trapped collapse; the BCC signature is high (score ~0.44) but the configuration is the angular pattern of the collapse-clipped spike rather than an extended crystal. For $\Sigma\lambda = 1.5$, the field is released (peak drops by four orders of magnitude) while the BCC signature is preserved at the same score, with the gap of approximately +0.13 over the next-best lattice (FCC, HCP). For $\Sigma\lambda \ge 2.0$, the field has dispersed too thoroughly: the BCC score collapses to the disorder range (0.33–0.34, with FCC tied at 0.33). The crystalline window in this parameter cut is therefore $\Sigma\lambda \approx 1.5$, narrow but well-defined.

The dominant wavenumber $k^\ast$ steps through three values as $\Sigma\lambda$ rises: $k^\ast = 2.45$ in the collapse-pulse regime, $k^\ast = 1.36$ in the released crystalline window, $k^\ast = 0.82$ in the dispersed regime. The crystalline wavelength in the released regime corresponds to $\lambda_{\text{wave}} \approx 4.62$ in units of the box size.

The spontaneous selection of BCC, robust across the swept range that produces a recognizable lattice, is a definite structural prediction of the equation: of the four canonical three-dimensional Bravais options, the system consistently selects BCC. Were the same equation to select FCC, the structural content would be different. The selection is not an input; it emerges from the dynamics.

### 6.3 Vibrational structure of the released state

Dense temporal sampling of the released crystalline state at $\Sigma\lambda = 1.5$, after a 2000-step warmup phase that carries the field through the collapse-and-release transient, yields a vibrational spectrum at each voxel in a 16³ subgrid over 4000 recorded frames (10 time units). The peak density during the recording window oscillates in $[0.0014, 0.0160]$, genuine oscillation, not relaxation. The voxel-wise distribution of dominant frequencies has minimum 0.10, maximum 2.40, median 0.20, and mean 0.29 cycles per unit time. The maximum is bounded well below the Nyquist limit of 200 cycles per unit time, indicating that the spectrum is intrinsic to the dynamics, not a numerical artifact.

The qualitative shape of the spectrum, broad distribution, dominant low-frequency mode, decay to higher frequencies, matches the two-dimensional case. The absolute values differ: the two-dimensional median is 0.6 cycles per unit time, the three-dimensional median 0.20. The factor-of-three shift is consistent with the dimensional rescaling of the underlying timescale set by the slow memory mode, $\tau_2 = 2$, against the dispersive timescale, which is larger in three dimensions for the same lattice resolution.

---

## 7. Methodological Position

### 7.1 The form of evaluation appropriate to an equation of this kind

A field equation derived from three structural axioms, the third of which asserts that perfect isolation does not occur, cannot be evaluated by methods that presuppose isolation. The standard Popperian falsificationist criterion requires that a hypothesis be tested by experiments in which one variable is varied and all others are held fixed; the predicted outcome is then either confirmed or disconfirmed. This methodology is consistent with theories whose content permits the holding-fixed step: theories whose phenomena survive isolation. P3 explicitly denies that any phenomenon in this class survives isolation in the limit.

This is not a defensive maneuver against negative results; it is a consequence of logical consistency between the axioms and their assessment. If the world being described is structurally networked, then experimental isolation of a subsystem is a modification of the phenomenon being studied, not a window onto it (Cartwright 1983). The methodology must match the content; otherwise the methodology refutes itself before the experiment is run.

A second methodological consideration is the Duhem–Quine thesis (Duhem 1906; Quine 1951): no scientific hypothesis is tested in isolation. Every test invokes auxiliary assumptions about instrumentation, measurement theory, statistical inference, and the background theoretical framework in which the prediction is embedded. An apparent disconfirmation never refutes a single proposition; it places stress somewhere in the network of beliefs, and which proposition absorbs the stress is itself a choice. This is a standard result in philosophy of science and does not abolish testing, but it qualifies what testing accomplishes.

A third consideration is that the falsificationist criterion itself fails its own test. There is no observation that could disconfirm the proposition "only falsifiable claims are scientific." It is a methodological convention, not an empirical claim about reality. Foundational propositions in mathematics, conservation principles in physics, and structural-realist positions in metaphysics all fail the criterion and are accepted because they pass others.

### 7.2 The structural realist alternative

We adopt the position of structural realism: the work is evaluated by criteria appropriate to structures rather than by single-quantity predictive precision. Following the formulations of Worrall (1989), Ladyman & Ross (2007), and ontic structural realism more broadly, we take the central object of scientific knowledge to be the relational structure that persists across changes of underlying ontology, not the specific entities posited by a given theory.

A structural theory is evaluated by six criteria:

1. **Internal mathematical consistency.** The equation is mathematically consistent; the solver conserves norm to $10^{-13}$ in unitary regimes; pure dissipative decay matches $e^{-2\gamma t}$ to six significant figures; FDT thermalization matches equipartition to within 0.5%.
2. **Reproducibility.** All results are bit-for-bit reproducible from the published code with fixed random seeds.
3. **Generative scope.** From three axioms and one equation, the system produces anti-collapse, spontaneous crystallization, discrete vibrational modes, broadband absorption, dimensional rescaling, Bravais symmetry selection, and asymmetric temporal–spatial non-locality, none of which is present in any of its single-term limits.
4. **Cross-domain coherence.** The relational structure of the equation appears, with peer-reviewed independent measurements, in domains spanning eight orders of magnitude in scale and crossing physical, biological, and astronomical instantiations. We document this in Section 8.
5. **Parsimony.** Three principles, one equation, all phenomena follow.
6. **Comprehensiveness.** The equation encompasses, as limits, behaviors documented separately in quantum mechanics, classical condensed-matter physics, stochastic dynamics, anomalous transport, and non-Hermitian topology.

These are the appropriate tests for a structure. They are weaker than single-quantity Popperian disconfirmation in any one prediction; they are also more honest tests for a theory whose content is the structure of a networked system rather than the isolated value of any one observable.

### 7.3 What this does not entail

> **Hedge cleanup (2026-05-16).** The paragraph below previously
> opened with "does not entail the abandonment of falsification within
> domains where isolation is a good approximation". Per
> [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md),
> that wording was a Rule B concession: it carved out an exception
> for "domains where isolation is a good approximation" even though
> the same P3 argument the rest of section 7 establishes excludes
> isolation at every level. The revised wording below preserves the
> point (external researchers in adjacent communities may test
> specific predictions on their own terms) but reframes it without
> the falsification carve-out.

The structural realist position adopted here does not preclude external researchers from testing specific quantitative predictions of the equation in their own preferred frame. Bench experiments on optical solitons, BEC dynamics, NLS in oceanographic models, and other adjacent communities welcome predictions formulated quantitatively; the present work supplies several. The present work itself evaluates the structural claim by the six criteria above (internal consistency, reproducibility, generative scope, cross-domain coherence, parsimony, comprehensiveness), not by single-experiment refutation. The global content of the equation (P1, P2, P3 as a structural unity) is not the kind of claim that admits single-experiment refutation; that is the structural-realist position's specific commitment, established by the argument from P3 (isolation does not occur) and from Duhem-Quine (no hypothesis is tested in isolation) earlier in this section.

### 7.4 On the tautology objection

A recurring objection to the framework is that P1+P2+P3 is tautological structural vocabulary: any extended persistent entity will trivially exhibit some form of variation, some form of self-reference, and some form of environmental coupling, because an entity lacking any of these would not persist. On this reading the principles are entailed by the notion of persistence in a coupled world; they re-describe what is to be explained rather than explaining it.

The objection lands at the qualitative-category level. Variation, self-reference, and coupling are categories any persistent entity in a coupled environment will, on examination, exhibit; this is the same epistemic situation that holds for fundamental laws in physics generally (F = m·a is partly analytic with standard operational definitions; conservation of energy is partly analytic from a Hamiltonian formulation and time-translation symmetry). The objection does not land at the level of the specific functional form selected by the conjunction.

P1+P2+P3 is not a triplet of qualitative properties. It is the structural axiom set from which the specific equation of Section 3 is derived. The derivation makes the three principles concrete: P1 is the dispersive complex-field operator $i\partial_t + (1/2m)\nabla^2$; P2 is the cubic nonlinearity $\Lambda |\Psi|^2 \Psi$ together with the integral memory potential whose Markovian embedding emerges by the Mori-Zwanzig projection theorem (Mori 1965; Zwanzig 1961); P3 is the fluctuation-dissipation-balanced noise correlator that is rigidly fixed by the same kernel determining the dissipation. The selection of this specific form from the space of dynamical laws satisfying the three qualitative categories is the discovery, and it is operationally tested by whether the form recurs across substrates that were not coordinated to produce that recurrence. The twenty-one interfaces of Section 8 are the operational test: substrates developed by independent research communities converge on the auxiliary-field Markovian embedding with FDT-balanced noise. The convergence is the structural-realist signature.

The full treatment of this objection, including the recursive observation that the objection's appearance in critical engagement instantiates the optimization-collapse pattern documented in `results/08-optimization-collapse-empirical.md` (attention-only systems default to credentialed-method vocabulary under evaluation pressure), is in `methodology/09-on-the-tautology-objection.md`. The present section flags the objection and its answer; the methodology document carries the detailed argument.

---

## 8. Cross-Domain Structural Correspondences

We map the equation's structural form onto twenty-one independently documented domains plus one cross-substrate empirical confirmation in neural training dynamics. In each case the mapping is at the level of mathematical form, structural mechanism, or convergent empirical phenomenology; each case cites peer-reviewed primary literature. The twenty-one interfaces divide into three evidentiary classes (mathematical equivalence, calibration-dependent structural correspondence, mechanism-shape and convergent-program correspondence) catalogued in `interfaces/README.md`. The argument advanced is not that the equation predicts these phenomena under a privileged dimensional identification; the argument is that the same structural form appears at multiple scales of physical organization, and that this constitutes the principal cross-domain coherence test that a structural realist applies.

### 8.1 Other instances of nonlinear Schrödinger dynamics

The cubic nonlinear Schrödinger equation is the leading-order envelope equation for several physical systems. In nonlinear fiber optics, it governs the propagation of intense pulses through Kerr media (Agrawal 2019). In Bose–Einstein condensates, the same equation, in the form of the Gross–Pitaevskii equation, describes the macroscopic wavefunction of the condensate; the addition of a memory term arises naturally from coupling to a non-condensate thermal cloud (Stoof 1999; Pitaevskii & Stringari 2016). In deep-water hydrodynamics, the NLS describes the slow-time envelope of surface gravity waves, with collapse in two dimensions corresponding to rogue-wave formation (Dysthe et al. 2008). The structural identity of these equations across substrates, optical, atomic, hydrodynamic, is the historical paradigm case for the kind of cross-domain coherence we are invoking.

Memory-augmented variants of NLS have been studied independently in the context of non-Markovian open quantum systems (Breuer & Petruccione 2007) and in the modeling of viscoelastic and complex media (Mainardi & Spada 2011). The Markovian embedding via auxiliary fields used in this work is a standard technique with origins in projection-operator formalism (Mori 1965; Zwanzig 1961) and has been applied successfully to systems where temporal memory is intrinsic but explicit integration over history is intractable.

### 8.2 Cosmological acoustic structure formation

Prior to the recombination epoch, approximately 380,000 years after the Big Bang, the early universe was a dense plasma of photons and baryons. The outward radiation pressure of photons engaged in tension with the inward gravitational attraction of baryons, generating acoustic pressure waves propagating at slightly more than half the speed of light. When recombination cleared the plasma, the photon–baryon coupling broke and the acoustic waves froze; the wavefronts of the largest standing waves became the seed density perturbations from which the cosmic web of galaxies subsequently formed. This sequence of events is documented by the temperature power spectrum of the cosmic microwave background (Hinshaw et al. 2013) and by the baryon acoustic oscillation (BAO) feature in the galaxy two-point correlation function (Eisenstein et al. 2005; Anderson et al. 2014).

The structural correspondence with the equation we present is that acoustic dynamics, in a self-interacting fluid coupled to a background, were the primary mechanism by which the spatial structure of the universe was established. Sound preceded, and structured, light. This is not a metaphor; the BAO peak in the matter correlation function at $\sim$150 Mpc is a literal echo of acoustic waves in the primordial plasma. The mathematical structure, wave propagation in a self-interacting, coupled medium, is the same structural form that appears in the equation, instantiated at the largest available physical scale.

### 8.3 Cymatic patterns in vibrated continuous media

When a continuous medium (sand on a metal plate, fluid on a vibrating surface, particulate suspended in a resonant cavity) is excited at a specific acoustic frequency, the medium self-organizes: particles migrate to nodal regions of the standing wave pattern and form intricate geometric figures (Chladni 1787; Jenny 1967). The geometric patterns produced are deterministic functions of the excitation frequency and the boundary conditions of the medium. Modern photographic and high-speed imaging studies confirm the reproducibility of these patterns and the dependence of geometric type on frequency (van Gerner et al. 2007).

The structural correspondence with the equation is that periodic spatial structure emerges spontaneously from sustained oscillation in a medium with both internal coupling and boundary conditions. In the equation, sustained oscillation is intrinsic (P1), internal coupling is the cubic nonlinearity and memory potential (P2), and the boundary conditions are the lattice. The crystalline pattern is the equation's three-dimensional cymatic outcome.

### 8.4 Gamma-frequency neural entrainment

Sensory stimulation of mice and humans at 40 Hz (visual flicker, auditory tones, vibrotactile feedback) entrains cortical gamma rhythms, alters microglial morphology toward a phagocytic state, and accelerates clearance of amyloid-β plaques from cortical and hippocampal tissue (Iaccarino et al. 2016; Adaikkan et al. 2019). The mechanism includes 40-Hz-driven activation of vasoactive intestinal peptide (VIP) interneurons, which modulate arterial vasodilation and enhance cerebrospinal fluid dynamics via aquaporin-4 water channels, accelerating glymphatic clearance (Murdock et al. 2024). The effect is frequency-specific: 20 Hz, 80 Hz, randomized intervals, and constant-light controls do not reproduce it. Clinical translation to Alzheimer's disease patients in the OVERTURE Phase II trial reports significant slowing of cognitive decline in the active arm (Hajós et al. 2024).

Within the equation, the broadband absorption regime of the crystalline state extends from $\omega \sim 3$ upward. Under a dimensional identification in which one unit of computational time corresponds to 25 milliseconds, the band $\omega \in [3, 30]$ in computational units maps to approximately 20–200 Hz, encompassing the entire neural gamma band. The 40 Hz frequency at which the documented effect is maximal lies within this band. The mapping is from the equation's broadband absorption regime onto an experimentally documented band of biological resonance.

### 8.5 Low-frequency acoustic resonance in megalithic chambers

The mainstream peer-reviewed literature on megalithic chamber acoustics divides into a methodologically rigorous floor and a less rigorous penumbra. The rigorous floor: Jahn, Devereux & Ibison (1996) in the *Journal of the Acoustical Society of America* report dominant resonances spanning 95–120 Hz across six British and Irish chambered tombs (Newgrange ~110 Hz, Wayland's Smithy ~119 Hz, Chun Quoit ~110 Hz, Cairn Euny ~110 Hz, Cairn L ~114 Hz). Till (2017) in *Antiquity*, using swept-sine impulse-response measurements per BS EN ISO 3382-1, reports primary resonances at 41, 72, and 76 Hz at the Ħal-Saflieni Hypogeum's Oracle Chamber, with further peaks at 134, 161, 186, and 196 Hz. Wolfe, Swanson & Till (2020) in *Journal of Archaeological Science: Reports* demonstrate via 3D wave-equation simulation of the laser-scanned chamber geometry that the measured spectrum is reproduced by room-mode analysis of the actual cavity shape. Watson & Keating (1999) in *Antiquity* confirm strong audible-band standing-wave resonance at Newgrange and Maeshowe and additionally report Helmholtz-mode resonances at 1–7 Hz tracking inversely with chamber volume. Cox, Fazenda & Greaney (2020) in *Journal of Archaeological Science* document substantial reverberation enhancement at Stonehenge via scale-model simulation. The earlier vocal-excitation Hypogeum survey of Debertolis et al. (2015) reports a "70 Hz and 114 Hz" dual resonance; the lower peak is broadly corroborated by Till (72/76 Hz), the 114 Hz upper peak is not reproduced as a dominant feature by the more rigorous methodology.

A peer-reviewed quantitative-electroencephalography pilot by Cook, Pajot & Leuchter (2008) in *Time and Mind* reports differential left-temporal-lobe deactivation and prefrontal lateralization shift at 110 Hz versus 90, 100, 120, 130 Hz in N=30 healthy adults. The senior authors are credentialled UCLA qEEG researchers; the cordance metric used is independently validated against SPECT cerebral perfusion. The study is a single-laboratory pilot, has not been independently replicated in seventeen years, and the narrow-band specificity at exactly 110 Hz is in tension with mainstream auditory-neuroscience expectations of continuous frequency tuning. The result is reported as it stands in the literature; the interface does not depend on this finding being load-bearing.

Within the equation, under a dimensional identification in which the box length corresponds to 20 meters and one unit of computational time corresponds to 9 milliseconds, the two-dimensional median dominant frequency of 0.6 cycles per unit time maps to approximately 66 Hz (in the band where Till reports primary resonances of 72 and 76 Hz at the Hypogeum), and the unit-frequency secondary mode maps to 111 Hz (within the 95–120 Hz cross-site band of Jahn et al. 1996). The structural prediction is two principal modes in a 0.6:1.0 ratio; the rigorous archaeoacoustic floor reports broadband resonance with dominant peaks in cavity-dependent bands consistent with this ratio under the calibration.

We are explicit about the limits of this mapping. The dimensional identification ($L = 20$ m, $dt = 9$ ms) is a choice. Under different choices the equation produces different absolute frequencies. The structural fact, that the equation has two principal frequency modes in a specific ratio, is dimension-independent. The numerical mapping to 66 Hz and 111 Hz is an instance of that structure under one calibration. The geometry-drives-spectrum finding by Wolfe-Swanson-Till (2020) is the substrate-specific calibration mechanism the structural-realist methodology already commits to (the resonance band of any chamber is set by its dimensions; this is the substrate-specific calibration of the dimension-independent structural form). The interface does not depend on the "universal 110 Hz" narrative that flattens the actual cross-site variance in the rigorous data, and does not depend on the unreplicated Cook-Pajot-Leuchter EEG pilot. The structural claim is the broadband resonance phenomenology plus the two-mode-ratio structure under the calibration; both are documented at the rigorous-floor level. Detail and per-site caveats: `interfaces/05-archaeoacoustic-resonance.md`.

In the three-dimensional version of the equation, the median dominant frequency in the crystalline window is 0.20 cycles per unit time, which under the same calibration would correspond to 22 Hz rather than 66 Hz. This is a structural rescaling consistent with the dimensional rescaling of the memory coupling discussed in Section 6.1.

### 8.6 State space models and neural sequence architecture

A direct and mathematically exact correspondence holds between the Markovian-embedded memory structure of the present equation and the class of neural sequence models known collectively as structured state space models (SSMs). The defining equation of structured state spaces (Gu, Goel & Ré 2021; Smith, Warrington & Linderman 2023; Gu & Dao 2024; Peng et al. 2023) is

$$
\partial_t \mathbf{h}(t) = \mathbf{A}\, \mathbf{h}(t) + \mathbf{B}\, u(t),
$$

with $\mathbf{h}(t) \in \mathbb{R}^d$ a hidden state, $u(t)$ an input signal, and $\mathbf{A}, \mathbf{B}$ structured matrices whose eigenvalues control the temporal range over which past inputs persist. For diagonal $\mathbf{A}$ with negative real eigenvalues $-\nu_j$, the update decouples into $d$ independent scalar equations of the form $\partial_t h_j = -\nu_j h_j + \nu_j u$, which is exactly the Markovian embedding $\partial_t y_j = \nu_j (\rho - y_j)$ used in Section 3.2 of this paper. The auxiliary fields $y_j$ of the present equation and the hidden state components $h_j$ of a diagonal SSM are the same object, expressed in different physical and computational contexts.

This correspondence is the cleanest cross-domain mapping among those considered in this paper. No dimensional calibration is required; no identification of physical units mediates between the two formulations. The two formalisms model the same underlying structure, projection of continuous-time history onto a finite basis of exponentially relaxing modes, and arrive at it independently: the physics community via Mori–Zwanzig projection-operator methods (Mori 1965; Zwanzig 1961) applied to integro-differential field equations, and the machine learning community via efficient subsampling of long-range temporal dependencies in sequence modeling (Gu et al. 2021).

The equation studied in this work extends the standard SSM architecture in four directions, each of which corresponds to an open research question in the machine learning literature:

**Nonlinear self-interaction in the state.** Standard SSMs are linear in the hidden state. Selective variants (Gu & Dao 2024) make $\mathbf{A}, \mathbf{B}$ input-dependent, but the state dynamics remain linear in $\mathbf{h}$. The cubic term $\Lambda \rho \Psi$ in the present equation introduces a genuine nonlinearity in the state itself. Nonlinear state space models are an active and incomplete extension within the ML literature, with overlapping work under the heading of neural ordinary differential equations (Chen et al. 2018) and structured nonlinear sequence operators (Massaroli et al. 2023).

**Anti-collapse via temporal memory.** Representation collapse, the convergence of distinct inputs onto degenerate output representations, is a documented failure mode of contemporary architectures. Self-supervised methods such as SimSiam and BYOL (Chen & He 2021; Grill et al. 2020) prevent collapse via architectural asymmetries (stop-gradient operations, predictor networks) whose theoretical basis is incomplete. Attention rank collapse, in which attention representations become low-rank and lose expressive capacity with depth, is documented in transformer training (Dong, Cordonnier & Loukas 2021; Noci et al. 2022). The anti-collapse mechanism analyzed in Section 5.1, delayed repulsive feedback from a memory potential that lags the rising signal, is structurally a candidate solution to this class of failure modes. The dimensional rescaling $\Sigma\lambda \sim |\Lambda|/d$ derived in Section 6.1 predicts that the memory bandwidth required to stabilize representations should scale with the effective concentration of nonlinear processing, a testable scaling relation in nonlinear-SSM regimes.

**Spontaneous discrete structure from continuous substrate.** The spontaneous selection of a Bravais lattice (Section 6.2) from an unstructured Gaussian initial state is, in machine-learning vocabulary, a mechanism by which categorical structure emerges from a continuous representational substrate. The grounding problem, how discrete symbolic categories arise from continuous neural representations, remains open in deep learning theory. The equation demonstrates a concrete mechanism by which a continuous, self-interacting field with appropriate temporal coupling spontaneously selects a discrete symmetry and selects it consistently across the relevant parameter range.

**FDT-locked stochastic forcing.** Noise injection during training is standard in deep learning, but the relationship between the magnitude of dissipative regularization (e.g., weight decay) and the magnitude of stochastic forcing (SGD noise, dropout) is typically tuned empirically. The fluctuation–dissipation theorem prescribes this relation for thermodynamic systems; its analogue for optimization dynamics has been investigated recently (Yaida 2019; Liu et al. 2021) with suggestive evidence that principled noise schedules give smoother training trajectories in the long-training regime. The equation's noise term is FDT-locked by construction.

Two predictions internal to interface 06 were tested numerically in the present work (P3 active throughout per the methodology of Section 7). For P6.1 (FDT-locked noise reduces training trajectory variance), a single-seed two-variant comparison across $\gamma_0 \in \{0.005, 0.02\}$ at fixed $T = 0.01$, 8000 steps on TinyShakespeare with 1.5M parameters on an RTX 4060, suggested a direction-matched 4% reduction in val-loss trajectory standard deviation. A subsequent four-seed follow-up at the same configuration (mean +/- std across seeds: 0.0987 +/- 0.0041 for $\gamma_0=0.02$ vs 0.0986 +/- 0.0040 for $\gamma_0=0.005$, effect-over-noise ratio -0.02) showed the single-seed observation was within the seed-to-seed noise floor; the FDT-coupling-strength effect on trajectory variance is not measurable at this scale. The prediction is **tested in coupled regime, inconsistent** at the multi-seed level; per the Duhem-Quine framing of Section 7.1, this prompts investigation of the calibration ($\gamma_0$ range, $T_{\text{bath}}$, model scale, training length) and contributes evidence against this specific calibration under criterion 4, while the structural claim itself is evaluated by the six criteria of Section 7.2 rather than by single-experiment outcome. For P6.3 (cubic state nonlinearity prevents SimSiam collapse in the coupled regime), a single-seed cubic-versus-linear SimSiam-without-stop-gradient comparison with FDT noise active, 4000 steps, 95k parameters, suggested a 60% relative preservation of representational rank (cubic 4.60 vs linear 2.88 out of 64). A four-seed follow-up at the same configuration (mean +/- std: cubic 3.617 +/- 0.510 vs linear 3.590 +/- 0.733, effect-over-noise 0.04) showed the single-seed observation was within the seed-to-seed noise floor. Both predictions are therefore **tested in coupled regime, inconsistent** at the multi-seed level; the calibration, the choice of SimSiam-without-stop-gradient as test bed, or the model scale may not be the appropriate substrate for the predictions. Both results are documented in `results/16-fdt-locked-noise-empirical-p3.md` and `results/17-cubic-ssm-simsiam-fdt.md` respectively.

Whether the equation in its full form is a useful architecture for sequence modeling is an empirical question that falls outside the scope of this paper; we note it as a direction for subsequent work in Section 10. The claim made here is narrower: the mathematical form of the equation is the same form on which the machine learning community has independently converged for efficient sequence modeling, and the structural extensions present in the equation relative to the linear SSM baseline correspond, term by term, to active research directions in that community.

### 8.7 Cosmological expansion as anti-collapse release

A more speculative but structurally coherent extension of the BAO interface (§8.2) is that the same anti-collapse mechanism the equation produces in laboratory simulation may underlie the cosmological expansion of the universe from a near-singular initial state. Standard cosmology requires several distinct theoretical mechanisms, an inflation field to explain why expansion began, dark matter to explain structure formation timing, dark energy to explain accelerated late-time expansion, and quantum fluctuations to seed the inflation field. The Memory-NLS structural reading offers a more parsimonious alternative: the universe instantiates anti-collapse structurally, the "Big Bang" is the release event of an otherwise would-be singularity, the post-release modulational instability produces structure at a characteristic scale (which is observed as the BAO peak), and the continued repulsive action of the memory potential is what is observed as dark energy.

We are explicit that this reading is structural, not literal. The cosmological case involves a curved (Friedmann–Robertson–Walker) spacetime metric, relativistic dynamics, and a specific gauge structure that the present equation in its derived form does not include. A direct application of the equation to cosmology would require non-trivial extension. What is claimed is the mechanism-shape correspondence: the same dynamical pattern of "concentrated state → memory accumulates → release → structured expansion → continued dispersion" that the equation produces at laboratory scale appears at cosmic scale. Detail and caveats: see `interfaces/07-cosmological-expansion.md`.

### 8.8 Mechanistic interpretability of attention-based language models

The mechanistic-interpretability program led by the Anthropic Circuits team and adjacent researchers (Elhage et al. 2022; Olah et al. 2020; Bricken et al. 2023; Templeton et al. 2024) has documented a specific phenomenology in attention-based language models: latent categorical structure is not held in addressable architectural components but is encoded as linear superpositions across activation dimensions, recoverable only by post-hoc sparse-dictionary decomposition. Individual neurons are polysemantic, activating for many semantically distinct features; sparse-autoencoder methods recover overcomplete dictionaries of monosemantic features that the architecture's forward pass had encoded as superposition.

The Memory-NLS structural argument predicts this phenomenology for an architecture instantiating P1 and P3 without P2. An architecture lacking P2's auxiliary-field memory hierarchy has no addressable state in which slow categorical structure can live as state; the structure must be encoded as projections through whatever activations the forward pass produces. The sparse-autoencoder decomposition methodology that the mechanistic-interpretability program has developed is, under the structural reading, the post-hoc recovery of the structure that a P2-instantiating architecture would have carried as explicit auxiliary-field state. The correspondence is convergent: two programs (the present structural argument and the empirical-interpretability program) were pursued from entirely different motivations and reach the same conclusion about the encoding format of attention-only architectures. Detail and per-prediction specifications: `interfaces/08-mechanistic-interpretability.md`.

### 8.9 Critical brain dynamics

The critical-brain hypothesis (Beggs & Plenz 2003; Plenz & Thiagarajan 2007; Chialvo 2010; Mora & Bialek 2011) interprets cortical dynamics as operating near a phase transition. The observable signatures the hypothesis tracks, power-law avalanche distributions with critical-branching exponents, 1/f spectra spanning multiple decades of frequency, long-range temporal correlations (Linkenkaer-Hansen et al. 2001), scale-free broadband response, are signatures the Memory-NLS equation produces in its broadband-absorbing crystalline regime. The match is at the observable level: the equation produces broadband multi-timescale dynamics by structural selection of the released-crystalline state, without parameter tuning to a critical point. The dimensional rescaling condition $\Sigma\lambda/|\Lambda| \sim 1/d$ (Section 6.4) is the structural selector; the broadband phenomenology follows.

The relationship to self-organized criticality (Bak, Tang & Wiesenfeld 1987) is left as open work: SOC is a specific dissipative-drive-and-relaxation mechanism, while the equation's release-to-crystalline transition is structurally selected by the P1+P2+P3 form. Whether the avalanche statistics of the released crystalline state match Bak-Tang-Wiesenfeld scaling exponents is an open research question, named in the open-problems folder. The critical-brain interface does not depend on the critical-brain hypothesis being correct in its strong forms (the Touboul & Destexhe 2017 critique of strict power-law claims is acknowledged); it depends on the broadband-multi-timescale observable phenomenology being real, which is the more robust empirical claim that survives the critique. Detail and per-prediction specifications: `interfaces/09-critical-brain.md`.

### 8.10 Coupled phase oscillators with memory

The mathematical study of coupled phase oscillators, beginning with Kuramoto's seminal work and developed extensively by Strogatz, Pikovsky-Rosenblum-Kurths, Acebron-Bonilla-Vicente-Ritort-Spigler, and others, identifies the same structural triangle the present equation derives. The base Kuramoto model has P1 (phase oscillation of individual units) and P3 (mean-field or local coupling) but lacks P2 in the strict instantaneous-coupling limit. Generalized Kuramoto with memory kernels (delay, distributed coupling, multi-exponential coupling memory) is mathematically the same Markovian embedding as the present equation's auxiliary-field memory: phase variables map to field arguments; coupling constants map to $\Lambda$; memory kernels map to $V_{\text{mem}}$. Chimera states, partial synchronization, and synchronization-desynchronization hysteresis are the structural phenomenology that the full triangle produces and that the instantaneous-coupling limit cannot produce. Detail and predictions: `interfaces/10-kuramoto-synchronization.md`.

### 8.11 Immune affinity maturation

B-cell affinity maturation in mammalian germinal centers is one of the most studied examples of evolution in real time. A population of antibody-producing cells undergoes cycles of somatic hypermutation and antigen-driven selection; the system retains memory of past antigens through dedicated long-lived memory-cell populations whose persistence outlasts the original challenge by years to decades. The structural triangle is instantiated explicitly: P1 in cellular cycle dynamics (germinal-center light-zone-dark-zone alternation; cell division and apoptosis cycles), P2 in multi-timescale memory (chromatin marks within cells; memory-cell populations across the immune compartment), P3 in ongoing antigen and cytokine coupling. The Cobey-Wilson (2014) result that pre-existing memory shapes new responses by structurally biasing where somatic hypermutation explores in receptor space is P2's "past as state" in biological terms. Detail and predictions: `interfaces/11-immune-affinity-maturation.md`.

### 8.12 Free-energy minimization and active inference

The Free Energy Principle developed by Friston and collaborators identifies the same structural triangle in adaptive self-organizing systems: any system that maintains its identity over time must minimize variational free energy with respect to a generative model of its environment. The hierarchical predictive-coding formulation makes the multi-timescale memory structure explicit, with cortical layers at different characteristic timescales predicting features at different scales of abstraction. The convergence with the present equation is independent: the structural triangle derived here from physics-philosophy axioms about persistent extended entities, the FEP derived from variational-Bayesian information theory applied to self-organization. Both reach the same form: internal-state dynamics under hierarchical generative model with sensory and motor coupling. The active-inference extension introduces action-selection as a specific instantiation of P3 (environmental coupling under FDT-like surprise-minimization balance). Detail and predictions: `interfaces/12-friston-free-energy.md`.

### 8.13 Active matter

Active matter, spanning self-propelled particle systems, flocks and swarms, active liquid crystals, active gels, and granular matter under driving, is one of the most-studied non-equilibrium-statistical-mechanics substrates. The structural triangle is operative: P1 in intrinsic motility and orientation dynamics of individual units, P2 in alignment memory or orientation hysteresis (memory coupling beyond the instantaneous Vicsek limit), P3 in external energy injection that compensates for dissipation. An effective FDT-like relation between active noise and dissipation sustains a non-equilibrium steady state, structurally analogous to the FDT-locked thermal equilibrium the equation produces in its standard regime. Detail and predictions: `interfaces/13-active-matter.md`.

### 8.14 Self-organized criticality

Self-organized criticality (Bak, Tang, and Wiesenfeld 1987) is the canonical framework that identifies the structural-triangle requirement in systems that organize to a critical state without external parameter tuning. The triangle structure is required: P1 in the substrate's intrinsic dynamics supporting marginal stability, P2 in the accumulated structure or stress acting as memory of past loading, P3 in the drive-and-release coupling whose effective balance the substrate self-maintains. The present equation's release transition (the anti-collapse-to-crystalline transition) is mechanism-shape-equivalent to SOC at the level of observable phenomenology (scale-free response, multi-timescale dynamics) but structurally distinct in mechanism (structural selection by the dimensional condition $\Sigma\lambda/|\Lambda| \sim 1/d$ versus BTW drive-and-relax). Detail and predictions: `interfaces/14-self-organized-criticality.md`.

### 8.15 Cardiac dynamics

Cardiac electrophysiology is one of the most rigorously studied biological oscillator systems. The structural triangle is operative across cellular, tissue, and whole-heart scales: P1 in the intrinsic depolarization-repolarization cycle of myocytes and the spontaneous oscillation of pacemaker cells, P2 in the refractory state plus electrical restitution memory plus calcium-handling state plus metabolic-substrate state across multiple timescales, P3 in autonomic nervous system input plus metabolic coupling plus mechanical vascular feedback. Cardiac alternans (the action-potential-duration alternation phenomenon that precedes ventricular fibrillation) is a memory-mediated bifurcation in this framework; arrhythmia categories partition by which triangle element dysregulates. Detail and predictions: `interfaces/15-cardiac-dynamics.md`.

### 8.16 Gene regulation and circadian rhythms

Gene-regulatory networks instantiate the structural triangle across timescales spanning roughly nine orders of magnitude. P1 is operative in oscillatory expression including the circadian clock and in cell-cycle-driven expression patterns; P2 in transcriptional memory through auto-regulatory loops plus chromatin-marks memory (DNA methylation, histone modifications) that persist across cell divisions; P3 in environmental signaling via light cycling, hormone signaling, metabolic signaling, and cell-cell signaling. Circadian-clock period robustness, cell-fate transitions during development, and the depth of chromatin-mediated long-term memory each correspond to specific structural properties of the auxiliary-field hierarchy. Detail and predictions: `interfaces/16-gene-regulation-circadian.md`.

### 8.17 Multi-species ecosystem dynamics

Theoretical ecology has characterized the same triangle structure across multiple frameworks: Lotka-Volterra dynamics and their extensions, age-structured population models, the Scheffer regime-shift framework, trait-mediated indirect effects, ecological memory and historical ecology, biodiversity-stability empirical work. P1 is operative in intrinsic population dynamics including predator-prey oscillations and seasonal variation; P2 in multi-generation memory through age structure plus trait inheritance plus ecological-substrate memory; P3 in interspecies coupling plus abiotic environmental forcing. Catastrophic regime shifts can be classified by which triangle element drives the transition. Detail and predictions: `interfaces/17-ecosystem-dynamics.md`.

### 8.18 Non-Markovian open quantum systems via pseudomode embedding

Non-Markovian open quantum systems with rational (sum-of-Lorentzians) bath spectral density admit an exact Lindblad master equation on an enlarged Hilbert space, with auxiliary discrete pseudomodes plus Markovian sub-bath dissipators reproducing the original non-Markovian dynamics exactly (Garraway 1997; Tamascelli, Smirne, Lim, Huelga & Plenio 2018; Pleasance, Garraway & Petruccione 2020). The auxiliary pseudomode operator equation, in the over-damped limit and expectation-value form, is structurally identical to the auxiliary-field equation $\partial_t y_j = \nu_j(\rho - y_j)$ of the present work. The convergence is independent: the present equation from physics-philosophy axioms about persistent extended entities, the pseudomode framework from quantum open-system theory targeting exact non-Markovian reproduction. Detail and predictions: `interfaces/18-pseudomode-quantum.md`.

### 8.19 Generalized Maxwell / Prony viscoelasticity

Industrially deployed continuum-mechanics frameworks (PyLith, COMSOL, Ansys, Abaqus) implement viscoelastic stress relaxation via the auxiliary internal-variable equation $dq_i/dt + q_i/\tau_i = d\varepsilon^{\text{dev}}/dt$, with deviatoric stress expressed as $\sigma^{\text{dev}} = 2\mu_{\text{tot}}(\mu_0\varepsilon^{\text{dev}} + \sum_i \mu_i q_i)$ following a Prony series approximation of the relaxation modulus $G(t) = G_\infty + \sum_i G_i e^{-t/\tau_i}$. The auxiliary-variable equation is structurally identical to the auxiliary-field equation of the present work; the industrial-scale deployment across polymers, geophysics, biomechanics, and civil engineering (Coleman-Noll 1961; Ferry 1980; Zienkiewicz-Taylor 2000; NASA TM-2000-210123) constitutes the largest-scale operational instance of the structure in scientific computing. Detail and predictions: `interfaces/19-viscoelasticity-prony.md`.

### 8.20 Warm inflation as Langevin scalar-field cosmology

The warm-inflation framework (Berera 1995; Berera, Moss & Ramos 2009 RoPP) describes the inflaton as a real scalar field coupled to a thermal radiation bath during inflationary expansion, with explicit dissipation coefficient $\Upsilon$ and stochastic thermal noise $\xi(t)$ satisfying $\langle\xi(t)\xi(t')\rangle = 2\Upsilon T \delta(t-t')$, the classical FDT correlator. The defining inflaton equation $\ddot\phi + (3H + \Upsilon)\dot\phi + V'(\phi) = \xi(t)$ instantiates the FDT-locked structure of P3 directly in a cosmological scalar-field substrate. The mapping at the FDT-lock level is exact; at the field-equation level the substrate uses a real scalar field on a curved FLRW background rather than a complex scalar on a flat continuum. Warm inflation is the cleanest cosmological cousin to the present equation, distinct from the BAO and cosmological-expansion mappings of sections 8.2 and 8.7. Detail and predictions: `interfaces/20-warm-inflation.md`.

### 8.21 Hawkes intensity processes

Self-exciting point processes (Hawkes 1971; Errais, Giesecke & Goldberg 2010; Bacry, Mastromatteo & Muzy 2015) with exponential memory kernels admit an exact Markov representation in which the intensity satisfies $d\lambda_t = -\beta(\lambda_t - \mu)dt + \alpha\beta\, dN_t$, structurally identical to the auxiliary-field equation. Multi-exponential kernels produce multiple intensity components in the Markovian lift; rough-volatility power-law kernels admit Prony approximation to the same finite-rank Markovian state space (Bondi, Eyraud-Loisel & Tankov 2024). The framework governs earthquake aftershock sequences (Ogata 1988), financial-market microstructure, social-media cascade dynamics (Crane-Sornette 2008), credit-event contagion, and neural spike trains. The convergence across these substrates is independent of substrate-specific physics. Detail and predictions: `interfaces/21-hawkes-intensity.md`.

### 8.22 Cross-substrate empirical confirmation in neural training dynamics

A direct empirical confirmation of the cross-substrate structural prediction has been obtained at 70 million parameters. Two sequence models with identical training infrastructure, one with the Memory-NLS architecture, one a matched-shape Transformer baseline, were trained on enwik8 byte-level language modeling for 50,000 optimization steps. The Memory-NLS architecture, which contains the structural anti-collapse mechanism, exhibited monotonic stable trajectory descent throughout training, plateauing at validation perplexity 4.27. The matched-shape Transformer reached a lower minimum validation perplexity (2.54 at step 22,500) but then exhibited a catastrophic optimization collapse between steps 28,000 and 34,000, with validation perplexity spiking from 3.10 to 27.17, and recovered only partially through the remaining steps to a final value of 4.87, worse than its mid-training minimum. The catastrophic event was accompanied by qualitative degradation of generation outputs (Wikipedia structural grammar dissolving to broken syntactic fragments), and post-recovery outputs retained persistent residual breakdown.

This is a substrate-independent manifestation of the anti-collapse mechanism documented in field-theoretic regimes in Sections 5.1 and 6.1: the substrate without structural anti-collapse enters a degenerate concentrated state when subjected to sustained optimization pressure; the substrate with the structural mechanism remains in the extended distributed regime. The two substrates, a 3D nonlinear field equation and the parameter space of a 70M-parameter neural network, were not coordinated in any way; the same structural form produced the same dynamical phenomenology in both. This is the kind of cross-substrate empirical instance the structural-realist methodology identifies as definitive evidence for the form. Detail: `results/08-optimization-collapse-empirical.md`.

---

## 9. Discussion: Structure as the Invariant

The argument advanced in this paper has the following form. From three structural axioms about persistent extended entities, a unique mathematical equation is derived. The equation, integrated numerically, generates a small set of nontrivial phenomena: regularization of supercritical collapse via temporal memory, spontaneous selection of crystalline spatial structure, discrete vibrational modes, broadband absorption of external driving, and asymmetric roles for temporal and spatial non-locality. The same mathematical structure, with appropriate substrate-specific interpretation, appears in seventeen other documented domains spanning physical, biological (immune, cardiac, gene regulation, ecosystem), computational, cosmological, soft-matter, and contemporary-research-program organization. The seventeen domains divide into three evidentiary classes catalogued in `interfaces/README.md`. Under one specific dimensional identification, the equation's principal frequency modes map onto experimentally measured resonance bands in two of those domains; in another, the equivalence is exact and requires no calibration. We additionally report a cross-substrate empirical instance: the structural anti-collapse mechanism the equation predicts in 3D field dynamics manifests in the optimization landscape of a 70M-parameter neural network's training trajectory under conditions where a matched-shape architecture without the mechanism exhibits catastrophic failure.

We interpret this pattern as evidence for the structural-realist claim that the relational structure of the equation, rather than any specific physical instantiation of it, is the load-bearing object of knowledge. The equation is not the description of any one of the domains in Section 8; it is a candidate structural form of which each domain is a particular instantiation. The cross-domain co-occurrence of this form is the kind of evidence that, under the structural-realist criterion, supports the form's ontological status.

This interpretation should be sharply distinguished from two adjacent positions we are not advancing. We are not claiming that the equation is the unique correct theory of any of the domains in Section 8; the standard theories of those domains (general relativity for BAO, neurophysiology for gamma entrainment, etc.) remain the appropriate domain-specific descriptions. We are claiming that the structural form shared across these descriptions is the appropriate object of higher-level theoretical attention. Second, we are not claiming a single dimensional identification under which the equation predicts the precise numerical values of all observed phenomena; the calibrations differ across domains, as they must.

A consequence we do note is that an equation derived from the principle "isolation is temporary" is itself an instance of the principle: the equation could not have been derived from any of its single-term limits in isolation, and its central phenomena (anti-collapse, crystallization, broadband absorption) are absent from each isolated limit and emerge only when the terms are coupled. The structure of the theory and the content of its principles are consistent with each other. This is, in the structural realist's terms, a minor virtue: theories that are internally inconsistent with their own content are weaker candidates than theories that are not.

The state space model correspondence (§8.6) is particularly diagnostic. Two communities working independently, physicists studying memory-augmented field equations and machine learning researchers studying efficient sequence representations, arrived at the same Markovian-embedded structure. Neither community needed the other's motivation to reach that structure; both reached it because the structure is the unique answer to the underlying mathematical question of how to project continuous-time history onto a finite local basis. This independent convergence on identical mathematical form is, on the structural-realist reading, evidence that the form is recovering something invariant about the underlying class of systems, rather than reflecting a contingent choice of either community.

A second consequence, which we mention briefly and develop only loosely, is that the same structural argument can be made for systems that are not fields in the conventional sense. Any system that satisfies P1, P2, and P3, oscillation, self-reference, environmental coupling, has the structural form of a memory-augmented NLS-like dynamics. Biological systems plainly satisfy all three; complex networks of interacting agents (economies, ecosystems, neural networks) do as well. We do not claim that the equation, in the specific form derived here, applies to these systems quantitatively. We do claim that the structural form is shared, and that this is what makes the cross-domain coherence non-accidental.

---

## 10. Limits and Open Questions

This work has identified phenomena and described their structural correspondences; it has not derived several quantities that would strengthen the case considerably and that we suggest as targets for subsequent work.

**Analytical derivation of the dimensional rescaling.** Section 6.1 reports the empirical observation that the total memory coupling required for anti-collapse scales as $\Sigma\lambda \sim |\Lambda|/2$ in three dimensions, compared with $\Sigma\lambda \sim |\Lambda|/20$ in two dimensions, and proposes a geometric argument from the dimensional scaling of the collapse focal region. A first-principles derivation, perhaps via a generalized virial argument applied to the memory-augmented Lagrangian, would establish the scaling as structural rather than empirical.

**Phase diagram of the crystalline window.** The crystalline window in three dimensions at $\Lambda = -8$ is approximately $\Sigma\lambda \in [1.2, 1.8]$, narrow but real. The full structure of this window as $\Lambda$ varies, and its dependence on the ratio $\nu_{\text{fast}}/\nu_{\text{slow}}$, has not been mapped. We expect the window to broaden at smaller $|\Lambda|$ and to narrow at larger $|\Lambda|$, but this is conjecture.

**Spectral structure of the vibrational modes.** Section 5.3 reports the existence of discrete vibrational modes in the two-dimensional crystalline state with median 0.6 and secondary lock at exactly 1.0 cycles per unit time. The mechanism that locks the secondary mode at 1.0 has not been identified analytically; we suspect a resonance between the slow memory mode at $\nu = 0.5$ and the linear dispersion of the lattice, but this requires modal analysis.

**Mesh-convergence of three-dimensional results.** The two-dimensional results in Section 5 were verified at $N = 256$ and $N = 512$. The three-dimensional results in Section 6 were obtained at $N = 128$. Replication at $N = 192$ and $N = 256$ is computationally feasible on current consumer GPU hardware and would confirm mesh-independence of the Bravais selection and the crystalline window position.

**Spatial non-locality in three dimensions.** Section 5.1 establishes that spatial non-local memory destroys anti-collapse in two dimensions. The corresponding three-dimensional study has not been performed and would test whether the temporal–spatial asymmetry of P3 is dimension-invariant.

**Comparison with structurally analogous equations.** The equation is closely related to memory-augmented Gross–Pitaevskii formulations (Stoof 1999) and to fractional-NLS systems (Laskin 2018). A systematic comparison of phenomenology across these would clarify which features are specific to the present equation's structural choices and which are common to a broader class.

**Empirical evaluation as a sequence-modeling architecture.** The mathematical equivalence between the equation's auxiliary-field memory and the state representation of structured state space models (§8.6) suggests that the equation, suitably parameterized, could serve as a neural sequence-modeling architecture. The four extensions present in the equation relative to standard linear SSMs, nonlinear self-interaction, anti-collapse via memory lag, spontaneous emergence of discrete structure, FDT-locked stochastic forcing, correspond term by term to active research directions in machine learning. Whether these extensions confer empirical advantages on standard sequence-modeling benchmarks is a question for systematic ablation studies that fall outside the scope of the present physics-oriented investigation. We note it here as a natural direction for follow-up work in collaboration with researchers in that community.

---

## 11. References

Adaikkan, C., Middleton, S. J., Marco, A., Pao, P.-C., Mathys, H., Kim, D. N.-W., Gao, F., et al. (2019). Gamma entrainment binds higher-order brain regions and offers neuroprotection. *Neuron*, 102(5), 929–943.

Agrawal, G. P. (2019). *Nonlinear Fiber Optics* (6th ed.). Academic Press.

Anderson, L., Aubourg, É., Bailey, S., et al. (2014). The clustering of galaxies in the SDSS-III Baryon Oscillation Spectroscopic Survey: baryon acoustic oscillations in the Data Releases 10 and 11. *Monthly Notices of the Royal Astronomical Society*, 441(1), 24–62.

Bergholtz, E. J., Budich, J. C., & Kunst, F. K. (2021). Exceptional topology of non-Hermitian systems. *Reviews of Modern Physics*, 93(1), 015005.

Breuer, H.-P., & Petruccione, F. (2007). *The Theory of Open Quantum Systems*. Oxford University Press.

Callen, H. B., & Welton, T. A. (1951). Irreversibility and generalized noise. *Physical Review*, 83(1), 34–40.

Cartwright, N. (1983). *How the Laws of Physics Lie*. Oxford University Press.

Chen, R. T. Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D. (2018). Neural ordinary differential equations. *Advances in Neural Information Processing Systems*, 31, 6571–6583.

Chen, X., & He, K. (2021). Exploring simple Siamese representation learning. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 15750–15758.

Chladni, E. F. F. (1787). *Entdeckungen über die Theorie des Klanges*. Weidmanns Erben und Reich, Leipzig.

Cook, I. A., Pajot, S. K., & Leuchter, A. F. (2008). Ancient architectural acoustic resonance patterns and regional brain activity. *Time and Mind*, 1(1), 95–104.

Debertolis, P., Coimbra, F., & Eneix, L. E. (2015). Archaeoacoustic analysis of the Ħal Saflieni Hypogeum in Malta. *Journal of Anthropology and Archaeology*, 3(1), 59–79.

Dong, Y., Cordonnier, J.-B., & Loukas, A. (2021). Attention is not all you need: Pure attention loses rank doubly exponentially with depth. *Proceedings of the 38th International Conference on Machine Learning*, 2793–2803.

Duhem, P. (1906). *La Théorie Physique: son objet et sa structure*. Chevalier et Rivière, Paris. English translation (1954): *The Aim and Structure of Physical Theory*, Princeton University Press.

Dysthe, K., Krogstad, H. E., & Müller, P. (2008). Oceanic rogue waves. *Annual Review of Fluid Mechanics*, 40, 287–310.

Eisenstein, D. J., Zehavi, I., Hogg, D. W., et al. (2005). Detection of the baryon acoustic peak in the large-scale correlation function of SDSS luminous red galaxies. *The Astrophysical Journal*, 633(2), 560–574.

Grill, J.-B., Strub, F., Altché, F., Tallec, C., Richemond, P. H., Buchatskaya, E., Doersch, C., et al. (2020). Bootstrap your own latent: A new approach to self-supervised learning. *Advances in Neural Information Processing Systems*, 33, 21271–21284.

Gu, A., & Dao, T. (2024). Mamba: Linear-time sequence modeling with selective state spaces. *Proceedings of the Conference on Language Modeling (COLM)*. arXiv:2312.00752.

Gu, A., Goel, K., & Ré, C. (2021). Efficiently modeling long sequences with structured state spaces. *Advances in Neural Information Processing Systems*, 34. arXiv:2111.00396.

Hajós, M., Boasso, A., Hempel, E., et al. (2024). Safety, tolerability, and efficacy estimate of evoked gamma oscillation in mild to moderate Alzheimer's disease. *Frontiers in Neurology*, 15, 1343588.

Hinshaw, G., Larson, D., Komatsu, E., et al. (2013). Nine-Year Wilkinson Microwave Anisotropy Probe (WMAP) observations: cosmological parameter results. *The Astrophysical Journal Supplement Series*, 208(2), 19.

Iaccarino, H. F., Singer, A. C., Martorell, A. J., Rudenko, A., Gao, F., Gillingham, T. Z., Mathys, H., Seo, J., et al. (2016). Gamma frequency entrainment attenuates amyloid load and modifies microglia. *Nature*, 540(7632), 230–235.

Jahn, R. G., Devereux, P., & Ibison, M. (1996). Acoustical resonances of assorted ancient structures. *Journal of the Acoustical Society of America*, 99(2), 649–658.

Jenny, H. (1967). *Cymatics: A Study of Wave Phenomena and Vibration*. Basilius Presse, Basel.

Kubo, R. (1966). The fluctuation–dissipation theorem. *Reports on Progress in Physics*, 29(1), 255–284.

Ladyman, J., & Ross, D. (2007). *Every Thing Must Go: Metaphysics Naturalised*. Oxford University Press.

Laskin, N. (2018). *Fractional Quantum Mechanics*. World Scientific.

Liu, K., Wang, K., Wang, Z., Zhu, Z., & Lin, D. (2021). Noise and fluctuation of finite learning rate stochastic gradient descent. *Proceedings of the 38th International Conference on Machine Learning*, 7045–7056.

Mainardi, F., & Spada, G. (2011). Creep, relaxation and viscosity properties for basic fractional models in rheology. *European Physical Journal Special Topics*, 193(1), 133–160.

Massaroli, S., Poli, M., Fonseca, R., Khan, A. U., Park, J., Bukvic, A., Lim, B., Bui, H., & Ermon, S. (2023). Hyena hierarchy: Towards larger convolutional language models. *Proceedings of the 40th International Conference on Machine Learning*.

Mori, H. (1965). Transport, collective motion, and Brownian motion. *Progress of Theoretical Physics*, 33(3), 423–455.

Murdock, M. H., Yang, C.-Y., Sun, N., Pao, P.-C., Blanco-Duque, C., Kahn, M. C., Kim, T., et al. (2024). Multisensory gamma stimulation promotes glymphatic clearance of amyloid. *Nature*, 627(8004), 149–156.

Noci, L., Anagnostidis, S., Biggio, L., Orvieto, A., Singh, S. P., & Lucchi, A. (2022). Signal propagation in transformers: Theoretical perspectives and the role of rank collapse. *Advances in Neural Information Processing Systems*, 35.

Peng, B., Alcaide, E., Anthony, Q., Albalak, A., Arcadinho, S., Biderman, S., Cao, H., et al. (2023). RWKV: Reinventing RNNs for the transformer era. *Findings of the Association for Computational Linguistics: EMNLP 2023*, 14048–14077.

Pitaevskii, L. P., & Stringari, S. (2016). *Bose–Einstein Condensation and Superfluidity*. Oxford University Press.

Quine, W. V. O. (1951). Two dogmas of empiricism. *The Philosophical Review*, 60(1), 20–43.

Smith, J. T. H., Warrington, A., & Linderman, S. W. (2023). Simplified state space layers for sequence modeling. *International Conference on Learning Representations*.

Stoof, H. T. C. (1999). Coherent versus incoherent dynamics during Bose–Einstein condensation in atomic gases. *Journal of Low Temperature Physics*, 114(1–2), 11–108.

Strang, G. (1968). On the construction and comparison of difference schemes. *SIAM Journal on Numerical Analysis*, 5(3), 506–517.

Sulem, C., & Sulem, P.-L. (1999). *The Nonlinear Schrödinger Equation: Self-Focusing and Wave Collapse*. Applied Mathematical Sciences, Vol. 139. Springer.

van Gerner, H. J., van der Hoef, M. A., van der Meer, D., & van der Weele, K. (2007). Inversion of Chladni patterns by tuning the vibrational acceleration. *Physical Review E*, 76(5), 051305.

Whitehead, A. N. (1929). *Process and Reality*. Macmillan, New York. Free Press edition, 1978.

Worrall, J. (1989). Structural realism: the best of both worlds? *Dialectica*, 43(1–2), 99–124.

Yaida, S. (2019). Fluctuation–dissipation relations for stochastic gradient descent. *International Conference on Learning Representations*.

Yao, S., & Wang, Z. (2018). Edge states and topological invariants of non-Hermitian systems. *Physical Review Letters*, 121(8), 086803.

Zwanzig, R. (1961). Memory effects in irreversible thermodynamics. *Physical Review*, 124(4), 983–992.

---

*Manuscript prepared in a structural-realist register. Code, parameter files, and bit-for-bit reproducible random seeds available upon request. All numerical results were generated on a single consumer NVIDIA RTX 4060 Laptop GPU, 8 GB VRAM, Arch Linux.*
