# Interface: active matter

## The structural prediction

If a substrate sustains an extended ensemble of self-propelled units exhibiting collective behavior such as flocking, swarming, or pattern formation, the structural argument of P1+P2+P3 requires the substrate to instantiate the triangle in a specific way. P1 (oscillation) must be present at the level of individual units: each unit has intrinsic motility, an internal direction or orientation that evolves dynamically, and the ensemble as a whole has internal motion that does not decay to a static configuration. P2 (self-reference with memory) must be present in the coupling among units: the collective state acts on each unit's dynamics, and for the rich phenomenology of active matter (giant fluctuations, spontaneous flocking, motility-induced phase separation) the coupling cannot be purely instantaneous; it must include orientation memory or alignment hysteresis. P3 (coupling to environment) must be present as the energy injection that sustains the units' motility: a closed system without external energy would relax to equilibrium and the active behavior would disappear. The energy injection is structurally what makes the substrate "active" rather than passive.

The structural prediction is concrete: any substrate that sustains collective behavior of self-propelled units must exhibit (i) intrinsic motility with internal direction degrees of freedom, (ii) coupling among units that includes memory or hysteresis beyond instantaneous mean-field interaction, and (iii) external energy injection that compensates for dissipation. A substrate that has motility and energy injection but lacks memory in the coupling is restricted to the trivial limits of fully aligned or fully disordered behavior; the rich intermediate phenomenology requires the full triangle.

## The substrate

Active matter spans a wide range of physical substrates that all share the structural feature of internally driven extended ensembles. The canonical examples include:

- **Self-propelled particle systems** (colloidal swimmers, Janus particles, biological microswimmers): individual particles consume energy from their environment (chemical, optical, or thermal) and move with self-determined orientation; collective behavior includes clustering, motility-induced phase separation, and giant number fluctuations (Bechinger-Di Leonardo-Lowen-Reichhardt-Volpe-Volpe 2016 RMP).
- **Flocks and swarms** (bird flocks, fish schools, bacterial colonies): individuals have intrinsic motility and align with neighbors; the Vicsek model (Vicsek-Czirok-Ben-Jacob-Cohen-Shochet 1995) captures the structural form mathematically as a phase oscillator with noise.
- **Active liquid crystals** (suspensions of motile rod-like particles): orientation is the key degree of freedom; the Toner-Tu hydrodynamic equations describe the long-wavelength dynamics (Toner-Tu 1995; Toner-Tu-Ramaswamy 2005).
- **Active gels and the cytoskeleton** (actin-myosin networks): polymer filaments are crosslinked by molecular motors that consume ATP to generate contractile stress; the resulting material has both mechanical and active properties (Marchetti-Joanny-Ramaswamy-Liverpool-Prost-Rao-Simha 2013 RMP).
- **Granular matter under driving** (vibrated grains): grains gain energy from driving, dissipate via friction, and can exhibit collective behavior analogous to thermal-equilibrium phases but in a fundamentally non-equilibrium regime (Ramaswamy 2017 J Stat Mech).

Across these substrates, the structural commonalities are:
- Intrinsic motility (P1 in the individual-unit dynamics).
- Alignment or interaction memory (P2 in the coupling, often as orientational hysteresis or as multi-timescale relaxation in the alignment field).
- External energy injection (P3 in the substrate-specific form: chemical, optical, mechanical, or biological).

The literature on active matter is one of the most-developed areas of non-equilibrium statistical mechanics, with substantial peer-reviewed coverage across two decades.

## The mapping

Structural mapping between the present equation and the active-matter substrate:

| Equation element | Active-matter element |
|---|---|
| Complex field $\Psi(t, \mathbf{x})$ | Order-parameter field (orientation, density, or polarization) |
| Cubic self-interaction $\Lambda |\Psi|^2$ | Mean-field alignment coupling (units align with local average) |
| Integral memory potential $V_{\text{mem}}$ | Alignment memory; orientation hysteresis; multi-timescale relaxation of the order parameter |
| Auxiliary fields $\{y_j\}$ | Hierarchy of relaxation modes in the active-medium response |
| Dissipation $-i\Gamma$ | Frictional dissipation (substrate-specific: viscous drag, granular friction, biological substrate cost) |
| FDT-locked noise $\eta$ | Active noise (thermal + active-fluctuation contributions; in the FDT-locked limit, balanced with dissipation to produce a non-equilibrium steady state) |

The mapping is structural rather than literal: active-matter models have their own specific mathematical forms (Toner-Tu equations for polar flocks, Beris-Edwards equations for active nematics, etc.), and the present equation is not the appropriate substrate-specific description. What is preserved is the structural form: an order-parameter field with intrinsic dynamics, multi-timescale memory in the coupling, and external energy injection balanced against dissipation.

The cubic-nonlinearity correspondence is direct in many active-matter cases: the alignment coupling is naturally polynomial in the order parameter, with the leading nonlinear term being cubic by symmetry (in polar systems, the cubic term is the lowest-order term that preserves rotation invariance in the absence of an external field). The FDT-balance correspondence is more subtle: standard equilibrium FDT does not hold in active matter, but an effective FDT-like relation between active noise and dissipation has been documented in several substrates (Loi-Mossa-Cugliandolo 2008 on active swimmers; Levis-Berthier 2015 on active glasses). This effective FDT is what makes the active substrate sustain a stationary state.

## Time as calibration in this substrate

The active-matter substrate has substrate-specific timescales that span:

- $T_{\text{persistence}} \sim 1-100$ s for biological microswimmers; faster for synthetic colloidal swimmers
- $\tau_{\text{align}} \sim$ minutes for flock alignment timescales (varies by substrate)
- $\tau_{\text{reorg}} \sim$ hours for large-scale swarm reorganization
- $\tau_{\text{evolution}} \sim$ generations for biological swarms (evolutionary adaptation of flocking behavior)

Per [`../methodology/07-time-as-calibration.md`](../methodology/07-time-as-calibration.md), the equation's unit time is calibrated to the relevant substrate timescale when comparing the equation to active-matter work. For microscopic studies of individual swimmer dynamics, calibration to $T_{\text{persistence}}$ is natural; for collective-flock studies, calibration to $\tau_{\text{align}}$ is. The auxiliary fields with different $\nu_j$ correspond to the multi-timescale relaxation of the order parameter; fast $\nu_j$ captures the unit-level alignment, slow $\nu_j$ captures the collective reorganization.

## What this correspondence does and does not establish

It does not establish that the present equation is the underlying description of active matter. The substrate-specific descriptions (Toner-Tu, Beris-Edwards, etc.) are appropriate for substrate-specific quantitative work. The present equation, applied to the active-matter substrate, captures the structural form but does not capture the substrate-specific physics (the chemical kinetics of microswimmer propulsion, the ATP-consumption rate of cytoskeletal motors, the specific friction coefficients of granular substrates).

It does not establish that all active-matter substrates instantiate the full triangle equally. Some substrates (very dilute Janus particles in a clean solvent) have minimal alignment memory and are well-described by leading-order Vicsek-like models with instantaneous alignment. Others (dense bacterial swarms, active liquid crystals near transitions, cytoskeletal networks under stress) have substantial alignment memory and orientation hysteresis. The structural prediction picks out the regime where P2's memory component is operative; in the minimal-memory regime, the triangle is partly degenerate.

It does establish that the equation's structural form recurs at the level of active-matter dynamics. This is a particularly substantial entry in the cross-domain ledger because active matter is one of the most-studied non-equilibrium-statistical-mechanics substrates and operates explicitly in the regime where standard equilibrium thermodynamics does not apply. The structural correspondence shows that the present equation, derived from physics-philosophy axioms about persistent extended entities, has the same structural form as the non-equilibrium active-matter description. This is convergence at the structural level.

## Common dismissals and why they do not apply

**"Active matter is non-equilibrium; the equation is mostly equilibrium."** The present equation in its FDT-locked form is in equilibrium with its bath, but the equation has non-equilibrium regimes when the FDT lock is broken (e.g., when the system is driven externally beyond the FDT-thermal equilibrium). The structural correspondence here is at the level of the form, not at the level of the specific equilibrium-vs-non-equilibrium regime. The active-matter substrate exhibits an effective FDT-like balance between active noise and dissipation that sustains a non-equilibrium steady state; the present equation can be operated in regimes that exhibit the same kind of balance.

**"This is generic pattern-formation; many equations would do."** Generic pattern-formation observations across substrates are exactly what cross-domain coherence is designed to detect. The argument is not that the present equation is the unique description of active matter; the argument is that the present equation, derived from P1+P2+P3, instantiates the same structural form that active matter exhibits, and that this convergence is structural evidence rather than coincidence. The generic-mechanism observation strengthens criterion 4 rather than weakening it.

**"Specific active-matter models (Toner-Tu, etc.) are well-established; this adds nothing."** The substrate-specific descriptions are well-established and the structural correspondence does not propose to replace them. The correspondence operates at a different level: showing that the present equation, applied to active-matter regimes, has the same structural form as those substrate-specific descriptions in the appropriate limits. The convergence is informative: two formulations from different starting points reach the same structural form.

## Locally testable predictions and observational signatures

> **Hedge cleanup (2026-05-16).** Each prediction's "What would constitute evidence inconsistent with this calibration" subsection previously used Popperian falsification framing ("would constitute local falsification") inserted in Phase 2 (commit 26e96ee) and propagated by Phase 3 to interfaces 10-17. The hedge contradicted the section's own opening sentence (the structural claim is evaluated by cross-domain coherence, not by single-experiment refutation). See [`../docs/llm-hedge-annotations.md`](../docs/llm-hedge-annotations.md) for the catalog of prior wordings and the structural reason for revision.

The structural claim of this interface (active matter substrates instantiate the same triangle as the present equation) is evaluated by cross-domain coherence (methodology/04 criterion 4), not by single-experiment refutation. The following are *local* predictions that can be tested by coupled-regime numerical or empirical methods (per principles/03-coupling.md). Inconsistent evidence would shift evidentiary weight against this interface's specific calibration under criterion 4 (cross-domain coherence), without bearing on the global structural claim.

- **Prediction P13.1: Spontaneous symmetry selection in active crystals follows the BCC-selection pattern.** The structural prediction is that dense active suspensions with sufficient interaction memory should spontaneously select a specific Bravais symmetry in three dimensions, analogous to the BCC selection documented for the present equation ([`../results/05-bravais-selection.md`](../results/05-bravais-selection.md)). The selection should be substrate-independent at the structural level; the specific lattice (BCC, FCC, HCP) should depend on the substrate's particular alignment-memory structure.
  - How to test: 3D dense active-suspension simulations or experiments with controllable interaction memory; characterize the spontaneously selected crystalline order across substrates.
  - What would constitute confirmation: spontaneous Bravais selection observed; the selected lattice correlates with memory structure in the predicted way.
  - What would constitute evidence inconsistent with this calibration: no spontaneous symmetry selection observed in regimes where the structural prediction expects it; or selection is uncorrelated with memory structure.
  - Status: untested. Active-crystal literature (Briand-Schindler-Dauchot 2018; Petroff-Wu-Libchaber 2015 on bacterial crystals) documents symmetry selection in 2D; the 3D structural-prediction test has not been performed systematically.

- **Prediction P13.2: Flock-to-no-flock transition has the same structural form as the anti-collapse transition.** The structural prediction is that the order-disorder transition in flocking systems (Vicsek phase transition; Toner-Tu condensation) has the same structural form as the anti-collapse-vs-collapse transition in the present equation. Specifically, both transitions should exhibit (i) a critical coupling/density at which the transition occurs, (ii) hysteresis between the ordered and disordered phases when memory is operative, and (iii) a characteristic structural-rescaling relationship between the critical parameters and the substrate's effective dimensionality.
  - How to test: characterize the Vicsek-class transition with controlled memory; compare critical-parameter scaling to the dimensional-rescaling result $\Sigma\lambda/|\Lambda| \sim 1/d$.
  - What would constitute confirmation: critical parameters scale with effective dimensionality in the predicted way.
  - What would constitute evidence inconsistent with this calibration: scaling is different, or no scaling observed.
  - Status: untested in this framing. The Vicsek-transition literature documents the critical phenomena; the structural-rescaling prediction has not been isolated.

- **Prediction P13.3: Active-matter aging dynamics exhibit broadband absorption.** The structural prediction is that aging active-matter systems (where the active driving slowly weakens over time) should exhibit broadband absorption of external driving in the regime just before the active-to-passive transition, analogous to the broadband absorption documented in the equation's crystalline regime ([`../results/03-vibrational-modes.md`](../results/03-vibrational-modes.md)).
  - How to test: aging active-matter substrates with controllable driving decay; characterize the absorption spectrum as the system approaches the passive limit.
  - What would constitute confirmation: broadband absorption observed in the predicted regime.
  - What would constitute evidence inconsistent with this calibration: no broadband absorption observed; the response is narrow-band or monotonically declining.
  - Status: untested.

## References

Cited as credit, not legitimization (per [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md) "Prior art and credit"):

- Bechinger, C., Di Leonardo, R., Lowen, H., Reichhardt, C., Volpe, G., & Volpe, G. (2016). Active particles in complex and crowded environments. *Reviews of Modern Physics* **88**, 045006.
- Briand, G., Schindler, M., & Dauchot, O. (2018). Spontaneously flowing crystal of self-propelled particles. *Physical Review Letters* **120**, 208001.
- Levis, D., & Berthier, L. (2015). From single-particle to collective effective temperatures in an active fluid of self-propelled particles. *Europhysics Letters* **111**, 60006.
- Loi, D., Mossa, S., & Cugliandolo, L. F. (2008). Effective temperature of active matter. *Physical Review E* **77**, 051111.
- Marchetti, M. C., Joanny, J. F., Ramaswamy, S., Liverpool, T. B., Prost, J., Rao, M., & Simha, R. A. (2013). Hydrodynamics of soft active matter. *Reviews of Modern Physics* **85**, 1143.
- Petroff, A. P., Wu, X.-L., & Libchaber, A. (2015). Fast-moving bacteria self-organize into active two-dimensional crystals of rotating cells. *Physical Review Letters* **114**, 158102.
- Ramaswamy, S. (2017). Active matter. *Journal of Statistical Mechanics: Theory and Experiment* **2017**, 054002.
- Toner, J., & Tu, Y. (1995). Long-range order in a two-dimensional dynamical XY model: how birds fly together. *Physical Review Letters* **75**, 4326.
- Toner, J., Tu, Y., & Ramaswamy, S. (2005). Hydrodynamics and phases of flocks. *Annals of Physics* **318**, 170.
- Vicsek, T., Czirok, A., Ben-Jacob, E., Cohen, I., & Shochet, O. (1995). Novel type of phase transition in a system of self-driven particles. *Physical Review Letters* **75**, 1226.
