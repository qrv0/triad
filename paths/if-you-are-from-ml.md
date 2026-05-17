[← Pick another path](../#read-it-your-way)

# For ML researchers

> The Triad equation's auxiliary-field memory is the diagonal-state SSM update (S4, Mamba, RWKV), extended with cubic self-interaction, anti-collapse via memory lag, and FDT-locked stochastic regularization — derived from physical first principles rather than fit empirically.

$$
\partial_t y_j = \nu_j(\rho - y_j) \quad\Longleftrightarrow\quad \partial_t \mathbf{h} = \mathbf{A}\,\mathbf{h} + \mathbf{B}\,u
$$

with $\mathbf{A}$ diagonal, eigenvalues $-\nu_j$, $b_j = \nu_j$. No calibration required — the auxiliary-field update *is* the diagonal SSM update.

---

## What this maps to in your area

The exact equivalence between the Triad equation's auxiliary-field memory and the diagonal SSM update means two communities (memory-augmented field theory and efficient sequence modeling) derived the same structure independently. The full Triad equation embeds this P2 subsystem inside a P1 wave-equation kinetic and a P3 FDT-locked dissipation–noise pair. An optimization-collapse experiment at 70M parameters shows the memory-hierarchical model (MNSM) descending monotonically through 50 000 training steps while the matched-shape attention-only baseline spikes catastrophically at step 28 000, perplexity jumping 3.10 → 27.17. The work treats this as criterion-4 structural evidence, not benchmark competition.

---

## Reading sequence

<table>
<tr>
<td width="120" valign="top"><b>01</b><br><sub>Methodology</sub></td>
<td valign="top"><b><a href="../methodology/04-the-six-criteria.md">The six criteria</a></b><br>The evaluation framework — six structural criteria, not benchmark perplexity. Read before judging the ML findings as "competitive".</td>
</tr>
<tr>
<td width="120" valign="top"><b>02</b><br><sub>Conceptual</sub></td>
<td valign="top"><b><a href="../principles/README.md">The three principles</a></b><br>P1, P2, P3 — the structural axioms from which the equation and the SSM equivalence both derive.</td>
</tr>
<tr>
<td width="120" valign="top"><b>03</b><br><sub>Equation</sub></td>
<td valign="top"><b><a href="../equation/02-markovian-embedding.md">Markovian embedding</a></b><br>The auxiliary-field reduction — the mathematical identity with the diagonal SSM update.</td>
</tr>
<tr>
<td width="120" valign="top"><b>04</b><br><sub>Interface</sub></td>
<td valign="top"><b><a href="https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md">SSM equivalence (mnsm spinoff)</a></b><br>The exact correspondence with S4 / Mamba / RWKV, side by side with the equation.</td>
</tr>
<tr>
<td width="120" valign="top"><b>05</b><br><sub>Empirical</sub></td>
<td valign="top"><b><a href="https://github.com/qrv0/mnsm/blob/main/results/01-optimization-collapse-empirical.md">Optimization-collapse experiment</a></b><br>70M-parameter training — anti-collapse in MNSM, catastrophic spike in the matched attention model.</td>
</tr>
<tr>
<td width="120" valign="top"><b>06</b><br><sub>Cross-substrate</sub></td>
<td valign="top"><b><a href="../results/04-anti-collapse-3d.md">3D anti-collapse</a></b><br>The same mechanism in the physics field equation — the structural-realist prediction that links the two substrates.</td>
</tr>
<tr>
<td width="120" valign="top"><b>07</b><br><sub>Synthesis</sub></td>
<td valign="top"><b><a href="../paper/manuscript.md">Full manuscript</a></b><br>The complete synthesized argument covering both field-theoretic and ML-substrate findings.</td>
</tr>
</table>

---

**Switch path:** [Physics](if-you-are-from-physics.md) · [Neuroscience](if-you-are-from-neuroscience.md) · [Philosophy](if-you-are-from-philosophy.md) · [Newcomer](if-you-are-new.md)
