# Open problem 01: Analytical derivation of the anti-collapse mechanism

**Status:** Open. Numerical evidence exists; analytical derivation does not.

## Precise statement

For the equation
$$
i\hbar\, \partial_t \Psi = \left[-\tfrac{\hbar^2}{2m}\nabla^2 + \Lambda |\Psi|^2 + V_{\text{mem}}\right]\Psi
$$
with $V_{\text{mem}} = \sum_j \lambda_j y_j$ and $\partial_t y_j = \nu_j(\rho - y_j)$, $\rho = |\Psi|^2$, derive the condition under which the memory potential overshoot $V_{\text{mem}}$ exceeds the cubic attraction $|\Lambda| \rho$ at the collapse focal region, releasing the field outward.

The derivation should yield: (a) an analytical bound on the peak density separation ratio between memoried and unmemoried runs as a function of $(\Lambda, \Sigma\lambda, \nu_{\text{slow}}, d)$; (b) the dimensional rescaling relation $\Sigma\lambda / |\Lambda| \sim 1/d$ as a derived consequence rather than a numerical observation; (c) the boundary in parameter space between regimes where anti-collapse operates and where it does not.

## What is known

- Numerical evidence at 2D ([`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md)) shows three-orders-of-magnitude peak-density separation between memoried and unmemoried runs at $\Lambda = -8$, $\Sigma\lambda \sim 0.4$.
- Numerical evidence at 3D ([`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md)) shows $10^5\times$ separation at $\Lambda = -8$, $\Sigma\lambda \sim 4$.
- The dimensional rescaling $\Sigma\lambda / |\Lambda| \sim 1/d$ is documented numerically in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md), with the structural argument that 2D focal volume scales as $\xi^2$ and 3D as $\xi^3$.
- The mechanism is qualitatively understood: $y_j$ relaxes toward $\rho$ at rate $\nu_j$, so $V_{\text{mem}}$ peaks after the focal density does; in the overshoot window $V_{\text{mem}} > |\Lambda|\rho$ and the field is released. The slow mode ($\nu = 0.5$, $\tau = 2$) is structurally essential; the fast mode alone cannot produce the lag.

## What is missing

- A derivation that starts from the equation and ends with a closed-form expression for the separation ratio (or a rigorous bound on it) as a function of the parameters.
- A characterization of the boundary between the anti-collapse and collapse regimes in $(\Lambda, \Sigma\lambda, \nu_j, d)$ space that does not depend on numerical sweeps.
- An analytical version of the dimensional rescaling relation.

## What would constitute progress

- A perturbative derivation linearizing around the collapse focal region that yields the leading-order overshoot magnitude as a function of $(\Lambda, \Sigma\lambda, \nu_{\text{slow}}, d)$.
- A rigorous (non-perturbative) bound on the separation ratio, even if the bound is loose.
- A clear identification of the small parameter that the perturbative expansion is in (most likely $\nu_{\text{slow}} / |\Lambda \rho_{\text{peak}}|$, the ratio of the memory relaxation rate to the focal nonlinear timescale).
- Numerical validation of the analytical prediction against the existing results at 2D and 3D, with stated tolerance.
- A reformulation showing the dimensional rescaling $\Sigma\lambda / |\Lambda| \sim 1/d$ as a corollary of the analytical derivation.

## Suggested approaches

- **Townes profile linearization.** The 2D L²-critical collapse is well-studied (Sulem & Sulem 1999); near the Townes profile the radial concentration $\rho(r, t) \approx |\Psi_T(\xi)|^2 / L(t)^2$ where $L(t) \to 0$ at finite time and $\xi = r/L$ is the rescaled radial coordinate. Compute $V_{\text{mem}}$ at the focal region using this approximation and the OU dynamics of $y_j$. The overshoot condition then becomes a relation between $L(t)$ and $\nu_{\text{slow}}$.
- **WKB-type analysis.** Treat the memory dynamics in the WKB regime where the field evolution is rapid compared to $\nu_{\text{slow}}$ but slow compared to $\nu_{\text{fast}}$. Expand around the moment of maximum density.
- **Variational ansatz.** Parameterize the field with a Gaussian-of-Gaussians ansatz of varying width; derive ODEs for the width parameters; analyze the fixed-point structure of the augmented system including the auxiliary fields.
- **Multiple-scale analysis.** Separate timescales: the fast (collapse) dynamics from the slow (memory equilibration) dynamics; apply method of multiple scales to derive an effective equation for the slow envelope.

## Partial derivation: leading-order lag analysis

This section is a draft sketch advancing the open problem from "qualitatively understood, no analytical content" to "leading-order skeleton in place, dimensional rescaling still open." It is not a finished derivation; the gaps are flagged explicitly.

### The small parameter

The natural small parameter is
$$
\varepsilon \;=\; \frac{\nu_{\text{slow}}}{|\Lambda|\, \rho_{\text{peak}}},
$$
the ratio of the slow-mode memory relaxation rate to the nonlinear timescale at the focal peak. Anti-collapse operates in the regime $\varepsilon \ll 1$ (memory lags significantly during focal collapse); the opposite regime $\varepsilon \gtrsim 1$ corresponds to no effective lag and reduces to the bare NLS without anti-collapse.

### Auxiliary-field lag at the focal peak

The auxiliary field $y(t)$ at the focal point $\mathbf{r} = 0$ satisfies $\dot y = \nu(\rho - y)$ with formal solution
$$
y(t) \;=\; \nu \int_0^{\infty} e^{-\nu s}\, \rho(t - s)\, ds.
$$
Expand $\rho$ around the focal-peak time $t_*$, where $\rho(t_*) = \rho_{\text{peak}}$, $\dot\rho(t_*) = 0$, $\ddot\rho(t_*) = -|\ddot\rho|_* < 0$:
$$
\rho(t_* - s) \;=\; \rho_{\text{peak}} \;-\; \tfrac{1}{2} |\ddot\rho|_*\, s^2 \;+\; O(s^3).
$$
Inserting this into the convolution and integrating against $\nu e^{-\nu s}$:
$$
y(t_*) \;=\; \rho_{\text{peak}} \;-\; \frac{|\ddot\rho|_*}{\nu^2} \;+\; O\!\left(\frac{1}{\nu^3}\right).
$$
Define the focal-peak curvature timescale $\tau_{\text{fast}}^2 = \rho_{\text{peak}} / |\ddot\rho|_*$. The lag at the focal peak becomes
$$
\rho_{\text{peak}} - y(t_*) \;=\; \rho_{\text{peak}} \cdot \frac{1}{(\nu \tau_{\text{fast}})^2} \;+\; O(\varepsilon^3) \;\equiv\; \rho_{\text{peak}} \cdot \varepsilon^2.
$$
The lag at the focal peak is of order $\varepsilon^2 \rho_{\text{peak}}$, which is small in the slow-memory regime but nonzero.

### Post-peak overshoot

For $\Delta t > 0$ small (just after the focal peak), $\rho$ decreases approximately quadratically:
$$
\rho(t_* + \Delta t) \;\approx\; \rho_{\text{peak}} \left(1 - \tfrac{1}{2}\, \frac{\Delta t^2}{\tau_{\text{fast}}^2}\right).
$$
The auxiliary field continues evolving with $\dot y = \nu(\rho - y)$. At $t_*$, $\dot y(t_*) = \nu \cdot \varepsilon^2 \rho_{\text{peak}} > 0$. The auxiliary field still rises briefly after the focal peak.

Solving the linear ODE for $y$ near $t_*$ with initial condition $y(t_*) = \rho_{\text{peak}}(1 - \varepsilon^2)$:
$$
y(t_* + \Delta t) \;=\; \rho(t_* + \Delta t) \;+\; \varepsilon^2 \rho_{\text{peak}} \, e^{-\nu \Delta t} \;+\; O(\varepsilon^3).
$$
For $\Delta t \lesssim 1/\nu$, the exponential is order unity, so
$$
y(t_* + \Delta t) \;\approx\; \rho(t_* + \Delta t) \;+\; \varepsilon^2 \rho_{\text{peak}}.
$$
The auxiliary field exceeds the field density by approximately $\varepsilon^2 \rho_{\text{peak}}$ for a window of duration $\tau_{\text{persist}} \sim 1/\nu$ after the peak.

### Leading-order release condition

The release condition is that the memory potential exceeds the attractive nonlinearity at the focal point during the overshoot window:
$$
\Sigma\lambda \cdot \langle y \rangle \;>\; |\Lambda| \cdot \rho.
$$
At the moment when $y$ has peaked relative to $\rho$ (approximately $\Delta t \sim 1/(2\nu)$ after $t_*$):
$$
\Sigma\lambda \cdot \rho_{\text{peak}}\bigl(1 - O(\varepsilon^2)\bigr) \;>\; |\Lambda| \cdot \rho_{\text{peak}}\bigl(1 - O(\varepsilon^2)\bigr).
$$
At leading order, the release condition reduces to the bare amplitude condition
$$
\Sigma\lambda \;>\; |\Lambda|.
$$
This says that anti-collapse operates if the total memory amplitude exceeds the cubic attraction amplitude, independent of dimension. This is the leading-order scalar (single-point) analysis; the numerical evidence shows something stronger.

### The dimensional-rescaling gap

The numerical observation in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md) is that the threshold scales as
$$
\frac{\Sigma\lambda_{\text{crit}}}{|\Lambda|} \;\sim\; \frac{1}{d},
$$
i.e., the critical memory amplitude DECREASES with dimension. The leading-order analysis above does not produce this behavior; it predicts a dimension-independent threshold $\Sigma\lambda \sim |\Lambda|$.

The gap implies that the dimensional rescaling is a sub-leading effect not captured by the lag analysis at zeroth order in spatial structure. Two candidate sources:

1. **Focal-region geometry.** The lag analysis treats $\rho$ as a scalar at the focal point; the actual focal region has spatial extent. In $d$ dimensions, the focal volume scales as $L^d$ where $L$ is the focal width, and the surface area scales as $L^{d-1}$. The "spread" of the focal region into surrounding bulk depends on $d$, and the memory potential averaged over the focal volume might inherit a $1/d$ factor from this geometry. A careful treatment requires the Townes-profile-like ansatz with $\rho(\mathbf{r}, t) = N L^{-d} f(\mathbf{r}/L)$ and integration of $V_{\text{mem}}$ over the focal volume rather than evaluation at the central point.

2. **Critical-exponent dimensional dependence.** The 2D NLS is $L^2$-critical (collapse is logarithmic in time); the 3D NLS is supercritical (collapse is power-law). The scaling exponent $\alpha$ in $\rho_{\text{peak}}(t) \sim (t_* - t)^{-\alpha}$ depends on dimension. This dimensional dependence enters $\tau_{\text{fast}}$ and hence $\varepsilon$, but in a way that the leading-order analysis above absorbs into $\rho_{\text{peak}}$.

The likely correct treatment combines both: the Townes-profile ansatz integrates the field over its spatial extent, with the $d$-dimensional volume element giving a $1/d$ factor in the appropriate averaging. This is the natural next step and is left open.

### Connection to numerical evidence

The numerical separation ratio between memoried and unmemoried runs is approximately $10^3$ in 2D ([`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md)) and approximately $10^5$ in 3D ([`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md)). The leading-order analysis above does not predict these specific magnitudes; the magnitude prediction requires the spatial-geometry treatment of the focal region (sketched above as the open step). The numerical evidence is consistent with the existence of the overshoot mechanism described here, but the quantitative match between leading-order analysis and numerics has not been established.

### Status of this draft

This sketch establishes:
- The small parameter $\varepsilon = \nu_{\text{slow}} / (|\Lambda| \rho_{\text{peak}})$ as the natural expansion parameter.
- The auxiliary-field lag at the focal peak is of order $\varepsilon^2 \rho_{\text{peak}}$ (not $\varepsilon$); the lag persists for a time $\sim 1/\nu$ after the focal peak.
- At leading order in the scalar (single-point) analysis, the release condition is $\Sigma\lambda > |\Lambda|$, dimension-independent.

This sketch does not establish:
- The dimensional rescaling $\Sigma\lambda_{\text{crit}} / |\Lambda| \sim 1/d$. This requires the spatial-geometry treatment of the focal region (Townes-profile or Gaussian-ansatz volume averaging) which is the natural next analytical step.
- A closed-form expression for the separation ratio between memoried and unmemoried runs. This requires solving the full PDE in the overshoot window, not just analyzing the lag at the focal point.
- A rigorous bound (as opposed to a perturbative leading-order estimate).

### Suggested next analytical steps

1. **Townes-profile volume average.** Write $\rho(\mathbf{r}, t) = N_T L(t)^{-d} f(\mathbf{r}/L(t))$. Solve the auxiliary-field equation for $y(\mathbf{r}, t)$ at the focal width $L(t)$. Average the memory potential $\sum_j \lambda_j y_j$ over the focal volume. Re-derive the release condition with the volume-averaging in place. Check whether the $1/d$ dimensional rescaling emerges.

2. **Variational ansatz.** Parametrize the field as a Gaussian of width $\sigma(t)$ with auxiliary fields $y_j(t)$ at the focal point. Derive the coupled ODE system for $(\sigma, y_j)$. Linearize around the focal-peak fixed point. Identify the critical line in $(\Sigma\lambda, |\Lambda|, d)$ space at which the fixed point is no longer attracting.

3. **Multiple-scale analysis.** Separate the field-evolution timescale (rapid, of order $1/|\Lambda \rho_{\text{peak}}|$) from the memory-equilibration timescale (slow, of order $1/\nu$). Apply the method of multiple scales to derive an effective slow equation for the focal density's slow envelope. The resulting equation should be amenable to fixed-point and linear-stability analysis.

The Townes-profile volume average is the most direct path to the dimensional-rescaling result and is the recommended first attempt.

## Continuation: variational-ansatz analysis (partial)

The variational Gaussian ansatz suggested above is the cleanest setup short of the full Townes-profile treatment. This section carries it out and identifies what it does and does not explain.

### The Gaussian ansatz

Parametrize the field as $\Psi(\mathbf{r}, t) = A(t)\, \exp(-r^2 / (2\sigma(t)^2))$ with width $\sigma(t)$ and amplitude $A(t)$ in $d$ dimensions. Norm conservation gives $|A|^2 = N / (\pi^{d/2} \sigma^d)$ where $N$ is the conserved total norm. The peak density at $r = 0$ is $\rho_{\text{peak}}(t) = |A(t)|^2 = N / (\pi^{d/2} \sigma(t)^d)$.

### Kinetic and nonlinear energies

The kinetic energy of the Gaussian is
$$
E_K \;=\; \frac{1}{2m} \int |\nabla\Psi|^2\, d^d r \;=\; \frac{d N}{4 m \sigma^2}.
$$
The cubic nonlinear energy is
$$
E_{\text{NL}} \;=\; \frac{\Lambda}{2} \int |\Psi|^4\, d^d r \;=\; \frac{\Lambda\, N^2}{2 (2\pi)^{d/2}\, \sigma^d}.
$$
$E_K$ grows as $\sigma \to 0$; $E_{\text{NL}}$ also grows in magnitude (with opposite sign for $\Lambda < 0$).

### Fixed-point analysis without memory

Setting $\partial E / \partial \sigma = 0$:
$$
\frac{-d N}{2 m \sigma^3} \;+\; \frac{d |\Lambda| N^2}{2 (2\pi)^{d/2}\, \sigma^{d+1}} \;=\; 0,
$$
giving
$$
\sigma_*^{\,d-2} \;=\; \frac{m\, |\Lambda|\, N}{(2\pi)^{d/2}}.
$$
For $d > 2$ this has a real solution; for $d = 2$ it is critical (no equilibrium width); for $d < 2$ the kinetic dominates always and there is no collapse.

Second-derivative analysis at $\sigma_*$:
$$
\left.\frac{\partial^2 E}{\partial \sigma^2}\right|_{\sigma_*} \;=\; \frac{d N\, (2 - d)}{2 m\, \sigma_*^4}.
$$
This is positive for $d < 2$ (the focal width is a stable minimum), zero at $d = 2$ (critical), and negative for $d > 2$ (the focal width is an unstable maximum). The well-known L^2-supercriticality of the cubic NLS in $d \geq 3$ appears in the Gaussian ansatz as the absence of a stable focal width: any small perturbation either disperses the Gaussian (growing $\sigma$) or collapses it (shrinking $\sigma$).

### Adding memory in the equilibrium-tracking limit

Suppose the auxiliary fields track the density perfectly: $y_j(t) = \rho(t)$ at all times. Then the memory potential is $V_{\text{mem}} = \sum_j \lambda_j y_j = \Sigma\lambda \cdot \rho$, and the effective nonlinearity becomes
$$
\Lambda_{\text{eff}} \;=\; \Lambda + \Sigma\lambda.
$$
The fixed-point condition becomes $\sigma_*^{\,d-2} = m |\Lambda_{\text{eff}}| N / (2\pi)^{d/2}$ when $\Lambda_{\text{eff}} < 0$, and disappears (no collapse) when $\Lambda_{\text{eff}} > 0$.

The release condition in the equilibrium-tracking limit is therefore
$$
\Sigma\lambda \;>\; |\Lambda|.
$$
This is the same condition as the leading-order scalar analysis. It is dimension-independent and does not recover the numerical $\Sigma\lambda_{\text{crit}} / |\Lambda| \sim 1/d$ for $d = 2, 3$.

### Where the dimensional rescaling must come from

The equilibrium-tracking limit assumes $y_j = \rho$ at all times. In reality $y_j$ lags $\rho$ during focal collapse, with the lag analyzed in the leading-order section above. The lag at the focal peak is of order $\varepsilon^2 \rho_{\text{peak}}$ where $\varepsilon = \nu / |\Lambda \rho_{\text{peak}}|$.

For the equilibrium-tracking release condition $\Sigma\lambda > |\Lambda|$ to be SUFFICIENT during the actual lag dynamics, the lag must be small enough not to push the system past the focal-peak before $y_j$ has caught up. The lag analysis quantifies "small enough" as $\varepsilon \ll 1$.

The dimensional dependence enters via $\varepsilon$, which depends on $\rho_{\text{peak}}$ via $\rho_{\text{peak}} \sim N / \sigma^d$. At the focal peak in $d$ dimensions, $\sigma$ scales as $\sigma_* \sim (m |\Lambda| N)^{1/(d-2)}$, so $\rho_{\text{peak}} \sim (m |\Lambda|)^{d/(d-2)} N^{-2/(d-2)}$. The exponent on $|\Lambda|$ depends on $d$.

For $d = 3$: $\rho_{\text{peak}} \sim (m|\Lambda|)^3 N^{-2}$. For $d = 4$: $\rho_{\text{peak}} \sim (m|\Lambda|)^2 N^{-1}$. The two are not simply related.

This is where the gap in the analytical derivation stands: the equilibrium-tracking condition $\Sigma\lambda > |\Lambda|$ is dimension-independent, but the SUFFICIENCY of this condition during the actual lag dynamics depends on $\varepsilon$, which depends on $d$ through $\rho_{\text{peak}}$. The detailed treatment of how this affects the critical $\Sigma\lambda$ would require solving the coupled system $(\sigma(t), y_j(t))$ self-consistently and identifying the boundary in $(\Sigma\lambda, |\Lambda|, d)$ space where the lag-dynamics breaks the equilibrium-tracking sufficiency.

### Self-similar collapse and memory divergence

A further complication: in the self-similar regime, $\rho(\mathbf{r}, t) = L(t)^{-d} f(\mathbf{r}/L(t))^2$ with $L(t) \to 0$ at finite time $t_*$. The auxiliary field at the focal center is
$$
y(0, t_*) \;=\; \nu f(0)^2 \int_0^\infty e^{-\nu s}\, L(t_* - s)^{-d}\, ds.
$$
For 2D critical, $L \propto \sqrt{(t_* - t)/\log\log}$, so $L^{-d} = L^{-2} \propto 1/(t_* - t)\log\log$. The integral diverges logarithmically at $s \to 0$.

For 3D supercritical, $L \propto (t_* - t)^{1/2}$ in the strong-collapse self-similar regime, so $L^{-3} \propto (t_* - t)^{-3/2}$. The integral diverges as $\int s^{-3/2} ds$.

The interpretation: in the strict self-similar collapse, the memory cannot track the focal-point density because the integrand has a non-integrable singularity at the collapse time. In reality the memory regularizes its own collapse by producing the back-reaction that the lag analysis identifies; once $y$ becomes large enough, the effective potential turns repulsive and the focal density stops growing. The self-similar form is therefore only valid until the memory regularization kicks in.

This is the structural mechanism but the closed-form expression for the critical $\Sigma\lambda$ requires self-consistent treatment of the coupled $(\sigma(t), y(t))$ system, which the variational ansatz above does not provide.

### The d=6 finding as constraint on the analytical theory

The Phase 9 wave-3 d=6 result ([`../results/24-dimensional-rescaling-d6.md`](../results/24-dimensional-rescaling-d6.md)) showed that at d=6 with the chosen configuration, the field does not collapse even without memory. The dispersive kinetic operator dominates the cubic attraction at the field amplitudes accessible in numerical simulation. The 1/d formula extrapolated from d=2,3 does not apply because the regime is no longer focal-collapse.

This means the analytical theory must characterize:
1. The boundary in $(d, |\Lambda|, N, \sigma_{\text{init}})$ space between the focal-collapse regime (where anti-collapse is the relevant question) and the dispersive-dominated regime (where no collapse occurs).
2. Within the focal-collapse regime, the dimensional dependence of $\Sigma\lambda_{\text{crit}}$.
3. The transition between these regimes as one increases $d$.

The current numerical data:
- d=2 ratio ~0.05 (focal-collapse, anti-collapse active)
- d=3 ratio ~0.5 (focal-collapse, anti-collapse active)
- d=4 ratio ~0.125 (focal-collapse, anti-collapse active, off 1/d)
- d=5: not on boxed 1/d (focal-collapse degrading)
- d=6: dispersive-dominated, anti-collapse not the relevant phenomenology

is consistent with a transition between regimes near $d \sim 4$ or $5$, with the boxed 1/d formula being a partial fit valid only in the focal-collapse regime where the dimensional scaling of the focal volume is the dominant geometric effect.

### Status of the analytical theory

The leading-order scalar analysis (above) plus the variational Gaussian ansatz (this section) plus the self-similar collapse argument (this section) together establish:

- The small parameter for the lag dynamics is $\varepsilon = \nu / (|\Lambda| \rho_{\text{peak}})$.
- The auxiliary-field lag at the focal peak is $O(\varepsilon^2 \rho_{\text{peak}})$.
- In the equilibrium-tracking limit (no lag), the release condition is $\Sigma\lambda > |\Lambda|$, dimension-independent.
- The dimensional dependence of $\Sigma\lambda_{\text{crit}}$ enters via the lag-dynamics correction to the equilibrium-tracking sufficiency, which depends on $\rho_{\text{peak}}$ via $\sigma_*$ and hence on $d$.
- The d=6 result places a constraint: above some critical dimension the dispersive operator dominates and the focal-collapse phenomenology is absent, regardless of memory.

The remaining gaps:
- A closed-form expression for the critical $\Sigma\lambda(d)$ within the focal-collapse regime.
- The exact form of the focal-collapse-vs-dispersive-dominated regime boundary as a function of $(d, |\Lambda|, N, \sigma_{\text{init}})$.
- The Townes-profile volume-averaging treatment carried out rigorously to extract the leading non-equilibrium correction to the release condition.
- Numerical validation of any analytical formula against the existing d=2,3,4,5,6 data.

The variational Gaussian ansatz of this section advances Phase 4 in identifying the structural mechanism by which dimensional dependence enters (via the lag-dynamics correction to the equilibrium-tracking sufficiency), but does not produce a clean closed-form expression for the critical $\Sigma\lambda(d)$. The 1/d formula extracted from results/06 at d=2,3 should be treated as an empirical fit within the focal-collapse regime, not a fundamental analytical result.

## Connections to existing repo content

- [`../principles/02-self-reference.md`](../principles/02-self-reference.md) section "A structural observation about the two parts": the qualitative argument is here; the open problem is to make it quantitative.
- [`../equation/02-markovian-embedding.md`](../equation/02-markovian-embedding.md): the auxiliary-field embedding gives the form of the memory dynamics; the open problem uses this form.
- [`../results/01-anti-collapse-2d.md`](../results/01-anti-collapse-2d.md), [`../results/04-anti-collapse-3d.md`](../results/04-anti-collapse-3d.md), [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md): numerical results the derivation must reproduce.
- [`../methodology/04-the-six-criteria.md`](../methodology/04-the-six-criteria.md) criterion 1 (internal mathematical consistency): a successful analytical derivation strengthens criterion 1 substantially.
- [`02-phase-diagram.md`](02-phase-diagram.md): the boundary characterized analytically here would feed directly into the phase-diagram open problem.
