# Compare two interfaces

This page describes how to read two cross-domain interfaces in parallel — how to see the same structural form expressed in two different substrates side by side. Each interface document is self-contained; comparing two of them is what makes the cross-domain coherence claim concrete.

## The three evidentiary classes

Every interface falls into one of three classes by evidentiary type. When you compare two interfaces, the class of each tells you what the comparison can and cannot establish.

<table>
<tr><th>Class</th><th>What it means</th><th>Examples</th></tr>
<tr>
<td><b>🔷 Mathematical equivalence</b></td>
<td>The equations are literally the same — no calibration required. Reading two interfaces in this class side by side shows the same mathematical object in two notations.</td>
<td><a href="01-other-nls-systems.md">01 NLS</a> · <a href="https://github.com/qrv0/mnsm/blob/main/interfaces/01-state-space-models.md">06 SSM</a> · <a href="10-kuramoto-synchronization.md">10 Kuramoto</a></td>
</tr>
<tr>
<td><b>🔶 Calibration-dependent structural correspondence</b></td>
<td>The mathematical structure is the same form, but substrate-specific dimensional choices set the absolute scales. Comparing two reveals how the same form appears at different scales.</td>
<td><a href="02-baryon-acoustic.md">02 BAO</a> · <a href="04-gamma-entrainment.md">04 gamma</a> · <a href="05-archaeoacoustic-resonance.md">05 archaeoacoustic</a> · <a href="11-immune-affinity-maturation.md">11 immune</a> · <a href="15-cardiac-dynamics.md">15 cardiac</a> · <a href="18-pseudomode-quantum.md">18 quantum</a> · <a href="19-viscoelasticity-prony.md">19 viscoelastic</a> · <a href="20-warm-inflation.md">20 warm inflation</a> · <a href="21-hawkes-intensity.md">21 Hawkes</a> · <a href="22-earthquake-cycle.md">22 earthquake</a></td>
</tr>
<tr>
<td><b>🔸 Mechanism-shape / convergent-program correspondence</b></td>
<td>The trajectory shape or convergent observation matches without committing to a specific calibration. Comparing two reveals what the underlying mechanism is doing.</td>
<td><a href="07-cosmological-expansion.md">07 cosmological expansion</a> · <a href="09-critical-brain.md">09 critical brain</a> · <a href="12-friston-free-energy.md">12 Friston FEP</a> · <a href="14-self-organized-criticality.md">14 SOC</a> · <a href="17-ecosystem-dynamics.md">17 ecosystem</a></td>
</tr>
</table>

## How to compare two interfaces

Pick any two interface documents and read these sections side by side:

<table>
<tr>
<td width="40" align="center"><b>1</b></td>
<td><b>The triangle frontmatter</b> — how P1 (oscillation), P2 (self-reference), P3 (coupling) are instantiated in each substrate. This is where the structural identity is most explicit.</td>
</tr>
<tr>
<td width="40" align="center"><b>2</b></td>
<td><b>"The mapping" table</b> — each interface has a term-by-term table mapping the equation onto substrate-specific elements. The two tables read in parallel show what is invariant.</td>
</tr>
<tr>
<td width="40" align="center"><b>3</b></td>
<td><b>"Time as calibration"</b> — each interface fixes a substrate-specific time unit. Comparing the two calibrations shows how the same structure operates across different absolute scales.</td>
</tr>
<tr>
<td width="40" align="center"><b>4</b></td>
<td><b>"Locally testable predictions"</b> (P&lt;N&gt;.1, P&lt;N&gt;.2, P&lt;N&gt;.3) — each interface names predictions specific to its substrate. Comparing the two prediction sets shows what is testable in each.</td>
</tr>
</table>

## Worked example: NLS (01) vs Kuramoto (10)

Both are class **🔷 mathematical equivalence**. Read side by side:

- **P1 in 01**: envelope oscillation of the underlying carrier wave. **P1 in 10**: individual phase oscillator dynamics. Both are oscillation — the substrates differ in whether the oscillating object is a field amplitude or a phase scalar.
- **P2 in 01**: nonlinear self-interaction plus dispersive/memory kernel. **P2 in 10**: coupling-history memory kernel between oscillators. Both are the same auxiliary-field memory $\partial_t y_j = \nu_j(\rho - y_j)$ — only the driving variable differs (density in 01, phase coupling in 10).
- **P3 in 01**: loss + gain (Raman, thermal cloud, friction). **P3 in 10**: FDT-locked phase noise + external drive. Both are FDT-locked coupling — the noise correlator structure is identical.

The mapping is exact at the auxiliary-field level. The substrates differ in what the field describes; the equation does not.

## Worked example: gamma entrainment (04) vs archaeoacoustic resonance (05)

Both are class **🔶 calibration-dependent**, and the calibrations are different — interface 04 uses 1 unit = 25 ms (gamma cycle), interface 05 uses $dt = 9$ ms (110 Hz cycle). The equation's broadband absorption regime maps to **different physical frequencies under each calibration**, but the structural mechanism (broadband absorption by self-organized oscillating medium) is the same. The comparison illustrates that *the structural form is dimension-independent and the calibration is substrate-specific* — exactly what methodology/06 (calibration philosophy) commits to.

---

**See also:** [`README.md`](README.md) for the full interface catalog · [`predictions.md`](predictions.md) for the status board of every prediction
