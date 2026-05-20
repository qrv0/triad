[← Pick another path](../#read-it-your-way)

# For physicists

> Memory-augmented NLS with FDT-locked dissipation and L²-supercritical anti-collapse via auxiliary-field Mori–Zwanzig embedding. Three structural axioms about persistent extended entities select the form — and produce phenomena no single-term reduction captures.

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

with $V_{\text{mem}} = \sum_j \lambda_j y_j$, $\partial_t y_j = \nu_j(\rho - y_j)$, $\rho = |\Psi|^2$, and $\eta$ Gaussian-white satisfying the classical FDT correlator $\langle \eta(\mathbf{x},t)\,\eta^*(\mathbf{x}',t')\rangle = 4\Gamma T\,\delta(\mathbf{x}-\mathbf{x}')\,\delta(t-t')$.

---

## What this maps to in your area

The cubic NLS is augmented with three structural additions: (i) an auxiliary-field Mori–Zwanzig memory $V_{\text{mem}}$ — a Markovian embedding of an integro-differential kernel, standard in projection-operator reduction but here treated as structurally required by P2; (ii) an FDT-locked dissipation–noise pair $(-i\Gamma, \eta)$ as in stochastic field theory for open systems; and (iii) an optional fractional Laplacian for anomalous dispersion. In 2D at the L²-critical threshold the memory lag prevents focal collapse by three orders of magnitude in peak density; in 3D (supercritical) the same mechanism operates with a geometrically predicted rescaling $\Sigma\lambda/|\Lambda|\big|_{3D} \sim 10\times\Sigma\lambda/|\Lambda|\big|_{2D}$. The released crystalline state spontaneously selects BCC from a continuous isotropic initial condition.

---

## Reading sequence

<table>
<tr>
<td width="120" valign="top"><b>01</b><br><sub>Derivation</sub></td>
<td valign="top"><b><a href="../equation/01-derivation.md">Equation derivation</a></b><br>How the three axioms (P1 kinetic, P2 cubic + memory, P3 dissipation + FDT noise) select the form.</td>
</tr>
<tr>
<td width="120" valign="top"><b>02</b><br><sub>Reduction</sub></td>
<td valign="top"><b><a href="../equation/02-markovian-embedding.md">Markovian embedding</a></b><br>Mori–Zwanzig projection of the integral kernel into auxiliary fields with diagonal dynamics — the form physicists already use.</td>
</tr>
<tr>
<td width="120" valign="top"><b>03</b><br><sub>Result</sub></td>
<td valign="top"><b><a href="../results/01-anti-collapse-2d.md">2D anti-collapse</a></b><br>L²-critical NLS at Λ=−8 — three orders of magnitude peak-density separation between memoried and unmemoried runs.</td>
</tr>
<tr>
<td width="120" valign="top"><b>04</b><br><sub>Result</sub></td>
<td valign="top"><b><a href="../results/04-anti-collapse-3d.md">3D anti-collapse</a></b><br>L²-supercritical regime — 10⁵× separation. Mechanism survives the harder regime where bare NLS collapse is generic.</td>
</tr>
<tr>
<td width="120" valign="top"><b>05</b><br><sub>Result</sub></td>
<td valign="top"><b><a href="../results/06-dimensional-rescaling.md">Dimensional rescaling</a></b><br>$\Sigma\lambda/|\Lambda| \sim 1/d$ derived from focal-region geometry — predicted from structure, confirmed numerically.</td>
</tr>
<tr>
<td width="120" valign="top"><b>06</b><br><sub>Result</sub></td>
<td valign="top"><b><a href="../results/05-bravais-selection.md">Bravais selection</a></b><br>Spontaneous BCC selection from isotropic Gaussian initial state — no symmetry input.</td>
</tr>
<tr>
<td width="120" valign="top"><b>07</b><br><sub>Interface</sub></td>
<td valign="top"><b><a href="../interfaces/07-cosmological-expansion.md">Cosmological expansion</a></b><br>The anti-collapse mechanism at cosmic scale — memory-coupled Friedmann.</td>
</tr>
<tr>
<td width="120" valign="top"><b>08</b><br><sub>Methodology</sub></td>
<td valign="top"><b><a href="../methodology/01-structural-realism.md">Why structural realism</a></b><br>The position the work commits to and why falsification is the wrong lens for evaluating P3-bearing theories.</td>
</tr>
<tr>
<td width="120" valign="top"><b>09</b><br><sub>Synthesis</sub></td>
<td valign="top"><b><a href="../paper/manuscript.md">Full paper</a></b><br>The complete synthesized manuscript covering all of the above.</td>
</tr>
</table>

To reproduce: scripts in [`../experiments/physics/`](../experiments/physics/README.md). Wall-clock on RTX 4060 Laptop is minutes per experiment.

---

**Switch path:** [ML](if-you-are-from-ml.md) · [Neuroscience](if-you-are-from-neuroscience.md) · [Philosophy](if-you-are-from-philosophy.md) · [Newcomer](if-you-are-new.md)
