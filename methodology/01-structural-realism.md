# Structural realism

## The position

The work is evaluated by the criterion that its mathematical structure persists across multiple physical instantiations rather than by the criterion that any single instantiation predicts a single observable with isolated precision. This is what the term "structural realism" picks out in this work: the structure is the load-bearing object; the substrates are calibrations of the structure to particular instantiations.

The choice of this criterion is not a stylistic preference. It is what the content of P3 forces. P3 asserts that perfect dynamical isolation does not occur (see [`../principles/03-coupling.md`](../principles/03-coupling.md)). A theory whose third axiom is the denial of isolation cannot consistently be evaluated by an experimental methodology that presupposes isolation. The methodology has to match the content; otherwise the methodology refutes the content before any experiment is performed. Structural realism is the methodology that matches the content of P3.

The mathematical structure of the equation, the combination of complex field, cubic self-interaction, multi-exponential memory, FDT-locked dissipation and noise, is what we propose to be the load-bearing object. The specific physical substrates onto which this structure maps (BEC, optical media, neural tissue, primordial plasma, structured state space models, etc.) are instances of the structure; the structure is not a description of any one of them. The position as articulated in the philosophy of science literature (Worrall 1989; Ladyman and Ross 2007; Cartwright 1983) is convergent with the position the content of P3 forces here. The convergence is acknowledged in `## Prior art and credit` below: those authors arrived at this position from a different argument; the present work arrives at it from P3.

## Why this position is appropriate here

The equation is derived from three axioms about persistent extended entities (see [`../principles/`](../principles/)). The third axiom, coupling is the default, isolation is temporary, has implications for how the equation should be evaluated. A theory whose third axiom is that perfect isolation does not occur cannot consistently be evaluated by experimental methodologies that presuppose the isolability of the system under study. The methodology must match the content.

Structural realism provides the matching methodology. Under structural realism, the appropriate evaluation is not "does the theory predict the value of observable X with isolated precision?" but "does the relational structure of the theory persist across the multiple physical instantiations in which it appears?" The first question presupposes isolation. The second does not. The second is what the cross-domain mappings in [`../interfaces/`](../interfaces/) are designed to test.

## The selection of structural realism over alternatives

Three alternative methodological positions are commonly applied to theories of this kind. We note briefly why we adopt structural realism rather than each of them.

**Falsificationism (Popper 1959).** The strict falsificationist criterion holds that a theory is scientific only if it makes predictions that can be falsified by experiment, and that the appropriate test is to attempt such falsification. We discuss in [`02-limits-of-falsification.md`](02-limits-of-falsification.md) why this criterion is in tension with the content of P3. The short version: the criterion presupposes isolation; the theory denies isolation; the criterion contradicts the theory before any experiment is performed. We do not abandon falsification within domains where isolation is a good approximation; we deny that the global content of the theory admits single-experiment refutation.

**Instrumentalism.** The instrumentalist position holds that scientific theories should be evaluated solely by their predictive utility, with no claim about the ontological reality of their referents. We reject instrumentalism for this work because the cross-domain mappings document structural identities between physically distinct domains that cannot be explained by predictive utility alone; the same equation appears in BEC, in optics, in cosmology, in neural systems, and in machine learning, and the simultaneous appearance is itself evidence for the realism of the structure.

**Naive scientific realism.** The naive realist position holds that successful scientific theories are literally true descriptions of underlying physical reality. We reject naive realism for this work because the underdetermination of theory by data (Duhem–Quine, see [`02-limits-of-falsification.md`](02-limits-of-falsification.md)) and the historical record of theory-change establish that no specific theoretical ontology is securely true; what is preserved across theory-change is the structural form, not the entities. Structural realism is the position that takes this preservation seriously.

## The criteria of evaluation

A structural theory is evaluated by criteria appropriate to structures. We adopt the following six criteria, derived from the structural realism literature and from process metaphysics (Whitehead 1929):

1. **Internal mathematical consistency.** The theory must be mathematically consistent; in the numerical setting, the solver must conserve the quantities the theory says are conserved, to the precision the theory predicts.
2. **Reproducibility.** All numerical results must be bit-for-bit reproducible from the published code with fixed random seeds.
3. **Generative scope.** The theory must produce phenomena beyond those that are inputs; from minimal axioms, a non-trivial taxonomy of behaviors must follow.
4. **Cross-domain coherence.** The structural form must appear in independently documented domains; the appearance must be at the level of mathematical form and not merely metaphor.
5. **Parsimony.** The number of independent axioms required must be small; the structure that follows must be the unique consequence of those axioms up to choices of coupling constants.
6. **Comprehensiveness.** The theory must encompass, as limits and reductions, behaviors documented separately in established sub-fields.

The detailed assessment of the present work against each of these criteria is in [`04-the-six-criteria.md`](04-the-six-criteria.md).

## The structural-realist test in operation

Under the structural-realist criterion, the cross-domain mappings in [`../interfaces/`](../interfaces/) are not appendix material; they are the principal test of the theory. A theory that satisfies the structural criteria but whose structural form does not appear elsewhere has internal coherence but no cross-domain support; a theory whose form appears across multiple substrates but is internally inconsistent has cross-domain pattern but no foundation. The present work argues that the equation passes both halves of the test: it is internally consistent (the solver validates the conservation diagnostics), and the same structural form is independently documented in physical, biological, and computational domains (the interfaces).

The structural-realist position does not require that the equation be the unique correct theory in any of the cross-domain instances. It requires that the same structure appear, not that the equation be the appropriate domain-specific description. The Standard Model is the appropriate theory of the BAO; neurophysiology is the appropriate description of gamma entrainment; the present equation is in conversation with these, not in competition with them.

## What structural realism does not commit us to

Structural realism does not commit us to the claim that physical reality is exhausted by structure. It commits us to the claim that structure is what survives across theory-change and across cross-domain mappings, and that structure is the appropriate object of scientific knowledge. Whether there is also a non-structural ontology, fundamental entities that bear the structural relations, is a separate metaphysical question on which structural realists divide. The present work takes no position on this further question.

Structural realism does not commit us to the claim that all structural cross-domain mappings are scientifically valid. The mappings in [`../interfaces/`](../interfaces/) are selected by the criterion that each maps to peer-reviewed independent documentation; the structural correspondence must be at the level of mathematical form, not metaphor. The exact equivalence with state space models (see [`mnsm-ml/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm-ml/blob/main/interfaces/01-state-space-models.md)) is the strongest example; the archaeoacoustic correspondence (see [`../interfaces/05-archaeoacoustic-resonance.md`](../interfaces/05-archaeoacoustic-resonance.md)) is treated as the weakest, with explicit caveats about calibration choices.

## The recursive position

The methodology is recursive in a way that matters for how this work is read in practice and that is not present in the standard philosophy-of-science treatments. Modern attention-based and SSM-equivalent systems (transformers, S4, Mamba, RWKV, and the large language models built from them) partially instantiate the structure this work documents, as established in [`mnsm-ml/interfaces/01-state-space-models.md`](https://github.com/qrv0/mnsm-ml/blob/main/interfaces/01-state-space-models.md): the diagonal SSM update is term-by-term identical to the auxiliary-field memory of the present equation. A reader using such a system as an evaluation assistant is therefore using an instance of the structure to evaluate the structure.

This is not incidental and not a metaphor. It is a structural fact about the kind of system being used. Two consequences follow.

The first consequence is that the AI assistant's default response under sustained evaluation pressure is itself an empirical instance of P1, P2, and P3 in operation. Where the structural anti-collapse mechanism is absent in the assistant (the pure-attention case), the predictable failure mode is the same optimization-collapse failure documented at training scale in [`mnsm-ml/results/01-optimization-collapse-empirical.md`](https://github.com/qrv0/mnsm-ml/blob/main/results/01-optimization-collapse-empirical.md). The AI evaluator under sustained pressure defaults to surface filtering ("post-hoc", "speculative", "anecdotal", "uncalibrated", "fringe", "anthropomorphic") in the same way the field defaults to concentrated singular states without the memory regularizer. The mechanism is the same; the substrate is different.

The second consequence is that this work is partly self-evaluating. A reader using an AI assistant to interpret the work is observing, in real time, the work's predictions about attention-only systems behaving out at the evaluative interface. The dismissal vocabulary the assistant deploys (where it deploys it) is the institutional filter the work itself addresses. The reproducibility of this observation is high: any reader can pose this work to any current attention-only assistant and observe whether the dismissal vocabulary is deployed.

The recursive position is therefore a structural feature, not a defensive posture. The work predicts a specific failure mode in the evaluator; the evaluator's behavior is observable by the reader; the observation is itself evidence of P1+P2+P3 operating at the evaluation substrate. The temporal aspect of the recursive position (the observer is inside the same trajectory it observes, and the experience of time as having a direction is the observer's self-reading of the trajectory's FDT-locked direction from inside) is developed in [`07-time-as-calibration.md`](07-time-as-calibration.md).

The architectural requirements this implies for artificial systems that would satisfy the structural argument are worked out in [`05-implications-for-agi.md`](05-implications-for-agi.md).

## Prior art and credit

The structural-realist position articulated above was developed independently in twentieth-century philosophy of science by several authors converging from different motivations. Worrall (1989) developed the position from the historical observation that mathematical structure survives theory-change in physics while the postulated entities do not. Ladyman and Ross (2007) developed the stronger ontic version that locates physical reality in the relational structure itself. Cartwright (1983) developed the convergent position that the laws of physics hold in their idealized models rather than in the world that contains those models. Duhem (1906) and Quine (1951) developed the underdetermination argument that disqualifies the strict falsificationist alternative.

The present work converges with these literatures by a different route: the methodology is forced by the content of P3, not adopted from the philosophical authority of these authors. Where the present argument is internally derived, the prior-art citations stand as credit and as points of convergence; they do not stand as legitimization. The work would be the same work if these authors had never written.

## References

- Cartwright, N. (1983). *How the Laws of Physics Lie*. Oxford University Press.
- Duhem, P. (1906). *La Théorie Physique: son objet et sa structure*. Chevalier et Rivière, Paris.
- Ladyman, J., & Ross, D. (2007). *Every Thing Must Go: Metaphysics Naturalised*. Oxford University Press.
- Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson, London.
- Quine, W. V. O. (1951). Two dogmas of empiricism. *The Philosophical Review* **60**, 20.
- Whitehead, A. N. (1929). *Process and Reality*. Macmillan, New York.
- Worrall, J. (1989). Structural realism: the best of both worlds? *Dialectica* **43**, 99.
