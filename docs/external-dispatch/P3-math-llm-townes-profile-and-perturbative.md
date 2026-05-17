# Problem statement for math LLM: Townes-profile volume average + perturbative anti-collapse derivation

**Target:** specialist analytical / symbolic math LLM with strength in PDE perturbation theory, asymptotic analysis, and finite-time singularity (Townes / blow-up) analysis.

**Context format:** paste the full equation, the existing derivation, and the explicit question. Do NOT paste the methodology files; the math LLM should engage analytically, not methodologically. The math LLM is not subject to the structural-research-mode constraints because its output will be integrated into the repository BY the structural-research-mode-active main agent, who will apply Rule B framing then. The math LLM should produce raw math.

---

## The equation

Consider the memory-augmented nonlinear Schrödinger equation in $d$ spatial dimensions:

$$
i\hbar\, \partial_t \Psi(\mathbf{r}, t) \;=\; \left[-\frac{\hbar^2}{2m}\nabla^2 \;+\; \Lambda |\Psi|^2 \;+\; V_{\text{mem}}\right] \Psi
$$

with auxiliary-field memory potential
$$
V_{\text{mem}}(\mathbf{r}, t) \;=\; \sum_j \lambda_j\, y_j(\mathbf{r}, t),
$$
where each auxiliary field satisfies a first-order linear relaxation toward the density $\rho = |\Psi|^2$:
$$
\partial_t y_j(\mathbf{r}, t) \;=\; \nu_j \left(\rho(\mathbf{r}, t) - y_j(\mathbf{r}, t)\right).
$$

Take $\Lambda < 0$ (focusing nonlinearity), $\lambda_j > 0$ (repulsive memory contribution), $\nu_j > 0$ (positive relaxation rates), and write $|\Lambda|$, $\Sigma\lambda = \sum_j \lambda_j$ as the relevant amplitudes. Set $\hbar = m = 1$.

The relevant memory hierarchy uses two timescales:
- fast mode: $\nu_{\text{fast}} = 10$, $\lambda_{\text{fast}}$
- slow mode: $\nu_{\text{slow}} = 0.5$, $\lambda_{\text{slow}}$
- $\Sigma\lambda = \lambda_{\text{fast}} + \lambda_{\text{slow}}$, with $\lambda_{\text{fast}} = 0.75\, \Sigma\lambda$, $\lambda_{\text{slow}} = 0.25\, \Sigma\lambda$

In the focal-collapse regime ($\Lambda < 0$, supercritical for $d \geq 3$), the field develops a focal density peak that, without memory, blows up in finite time according to the standard Townes profile in $d=2$ (L²-critical, log-log correction) or the strong-collapse self-similar profile in $d \geq 3$ (power-law $L(t) \sim (t_* - t)^{1/2}$).

## What is already derived (in `open-problems/01-analytical-anti-collapse.md`)

### Small parameter

The natural expansion parameter is
$$
\varepsilon \;=\; \frac{\nu_{\text{slow}}}{|\Lambda|\, \rho_{\text{peak}}},
$$
the ratio of the slow memory relaxation rate to the nonlinear timescale at the focal peak. Anti-collapse operates in the regime $\varepsilon \ll 1$ (memory lags during focal collapse).

### Auxiliary-field lag at the focal peak (scalar / single-point analysis)

The auxiliary field at the focal point $\mathbf{r} = 0$ satisfies $\dot y = \nu(\rho - y)$, with formal solution
$$
y(t) \;=\; \nu \int_0^{\infty} e^{-\nu s}\, \rho(t - s)\, ds.
$$
Expanding $\rho(t_* - s) = \rho_{\text{peak}} - \tfrac{1}{2}|\ddot\rho|_* s^2 + O(s^3)$ around the focal-peak time $t_*$ and integrating gives
$$
y(t_*) \;=\; \rho_{\text{peak}} \;-\; \frac{|\ddot\rho|_*}{\nu^2} \;+\; O(1/\nu^3).
$$
Defining the focal-peak curvature timescale $\tau_{\text{fast}}^2 = \rho_{\text{peak}} / |\ddot\rho|_*$:
$$
\rho_{\text{peak}} - y(t_*) \;=\; \rho_{\text{peak}} \cdot \varepsilon^2 \;+\; O(\varepsilon^3).
$$

### Variational Gaussian ansatz (equilibrium-tracking limit)

Take $\Psi(\mathbf{r}, t) = A(t) \exp(-r^2 / (2\sigma(t)^2))$ in $d$ dimensions. With norm conservation $|A|^2 = N / (\pi^{d/2} \sigma^d)$ and peak density $\rho_{\text{peak}} = N / (\pi^{d/2} \sigma^d)$. The energy functional is
$$
E[\sigma] \;=\; \frac{d N}{4 \sigma^2} \;+\; \frac{\Lambda\, N^2}{2 (2\pi)^{d/2}\, \sigma^d}.
$$
The fixed-point condition $\partial E / \partial \sigma = 0$ yields $\sigma_*^{d-2} = |\Lambda| N / (2\pi)^{d/2}$. The second-derivative analysis shows $d > 2$ is unstable (collapse), $d = 2$ critical, $d < 2$ stable (no collapse).

In the equilibrium-tracking limit ($y_j = \rho$ at all times), the effective nonlinearity is $\Lambda_{\text{eff}} = \Lambda + \Sigma\lambda$, and the release condition is
$$
\Sigma\lambda \;>\; |\Lambda|.
$$
**This is dimension-independent.**

### The gap: numerical observation

The numerical observation (results/06 + results/10 + results/26 phase diagram at d=3 and forthcoming d=2, d=4 slices) is that the critical $\Sigma\lambda$ scales as
$$
\frac{\Sigma\lambda_{\text{crit}}}{|\Lambda|} \;\sim\; \frac{1}{d},
$$
i.e., the critical memory amplitude DECREASES with dimension (at d=2 it's ~0.05, d=3 it's ~0.5 in some references but in the d=3 anti-collapse normalized convention the released regime occurs at $\Sigma\lambda$ in the 0.5-4 range, d=4 is ~0.125, d=5 not on the boxed formula, d=6 dispersive).

The equilibrium-tracking leading-order analysis above does NOT recover this $1/d$ scaling. The dimensional rescaling must come from a sub-leading effect not captured by the scalar analysis.

### Two candidate sources for the dimensional rescaling

**(a) Focal-region geometry.** The scalar analysis treats $\rho$ as a single-point quantity. The actual focal region has spatial extent. In $d$ dimensions, the focal volume scales as $L^d$ where $L$ is the focal width. The memory potential averaged over the focal volume might inherit a $1/d$ factor from this geometry. The natural treatment uses the Townes-profile (or Gaussian) ansatz with $\rho(\mathbf{r}, t) = N_T L(t)^{-d} f(\mathbf{r}/L(t))$ and integration of $V_{\text{mem}}$ over the focal volume.

**(b) Self-similar collapse divergence.** In the strict self-similar regime, $L(t) \to 0$ at finite time, so $\rho_{\text{peak}}(t) = L(t)^{-d}$ diverges. The auxiliary field at the focal center
$$
y(0, t_*) \;=\; \nu f(0)^2 \int_0^\infty e^{-\nu s}\, L(t_* - s)^{-d}\, ds
$$
has an integrand with a non-integrable singularity at the collapse time. The integral must be regularized self-consistently by the back-reaction the memory itself produces.

---

## The specific analytical questions

### Question 1: Townes-profile volume average derivation

Carry out the spatial-volume averaging of the auxiliary-field equation around the self-similar collapse profile. Specifically:

Take the field in the focal-collapse self-similar regime: $\Psi(\mathbf{r}, t) = L(t)^{-d/2}\, f(\xi)\, e^{i\phi(\xi, t)}$ with $\xi = r/L(t)$, where $f(\xi)$ is the Townes (or strong-collapse) profile in $d$ dimensions and $L(t)$ is the width function. The density is $\rho(\mathbf{r}, t) = L(t)^{-d}\, f(\xi)^2$.

Solve the auxiliary-field equation $\partial_t y(\mathbf{r}, t) = \nu(\rho - y)$ for $y(\mathbf{r}, t)$ in this self-similar regime. The auxiliary field will also have a self-similar structure, but with a lag relative to $\rho$.

Compute the spatial average of the memory potential $V_{\text{mem}}(\mathbf{r}, t) = \Sigma\lambda \cdot y(\mathbf{r}, t)$ over the focal volume (defined as the volume where $f(\xi)^2 > \alpha f(0)^2$ for some threshold $\alpha$, e.g., $\alpha = 1/e$).

Show whether the spatial-volume-averaged release condition
$$
\langle V_{\text{mem}} \rangle_{\text{focal volume}} \;>\; |\Lambda|\, \langle \rho \rangle_{\text{focal volume}}
$$
reduces to a $d$-dependent condition. Specifically, derive whether the $d$-dependence enters as $1/d$ or some other functional form.

### Question 2: Self-consistent regularization of the self-similar divergence

The integral
$$
y(0, t_*) \;=\; \nu \int_0^\infty e^{-\nu s}\, L(t_* - s)^{-d}\, ds
$$
diverges at $s \to 0$ for $d \geq 2$ assuming the strict self-similar scaling $L(t) \propto (t_* - t)^{1/2}$ (or the log-log corrected version at $d = 2$).

The physical interpretation: the memory cannot indefinitely track an actually-collapsing density; once $y$ becomes large enough, $V_{\text{mem}} > |\Lambda|\rho$ locally, and the field is pushed back, regularizing the would-be singularity.

Derive the self-consistent solution: replace the bare self-similar $L(t)$ with the $L(t)$ that satisfies the regularization condition, i.e., the $L(t)$ at which the memory back-reaction just balances the focal attraction. Show whether this self-consistent $L(t)$ has a minimum (the regularization timescale and minimum focal width as functions of $\Sigma\lambda$, $|\Lambda|$, $\nu$, $d$).

### Question 3: Closed-form $\Sigma\lambda_{\text{crit}}(d)$

Combining Questions 1 and 2, derive (perturbatively or rigorously, whichever is feasible) the closed-form expression for $\Sigma\lambda_{\text{crit}}/|\Lambda|$ as a function of $d$, $\nu_{\text{slow}}$, and the initial condition $\sigma_{\text{init}}$ (or normalization $N$).

The numerical observations to match (within the focal-collapse regime, $d = 2, 3, 4, 5$):
- $d = 2$: $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 0.05$
- $d = 3$: $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 0.5$ (in dimensional-rescaling convention, sigma=0.4 non-normalized) or $\sim 0.2$ (in canonical anti-collapse normalized convention, sigma=0.5 normalized, where Sigma_lambda=1.5 is the crystalline window)
- $d = 4$: $\Sigma\lambda_{\text{crit}}/|\Lambda| \sim 0.125$
- $d = 5$: not on the boxed $1/d$ formula
- $d = 6$: dispersive-dominated (focal-collapse regime ends)

The analytical formula need not match the numerical fits at any specific $d$ within the focal-collapse regime, but should:
(i) recover the right qualitative scaling (decreasing in $d$ for the focal-collapse regime);
(ii) identify the boundary where the focal-collapse regime ends (and the formula no longer applies);
(iii) be derivable from the equation, the variational ansatz, the Townes-profile structure, and the lag analysis, without empirical fitting.

### Question 4: Closed-form separation ratio between memoried and unmemoried runs

The numerical observations (results/01 at $d=2$, results/04 at $d=3$):
- $d = 2$: separation ratio $\sim 10^3$ at $\Lambda = -8$, $\Sigma\lambda \sim 0.4$
- $d = 3$: separation ratio $\sim 10^5$ at $\Lambda = -8$, $\Sigma\lambda \sim 4$

The separation ratio is $\rho_{\text{peak}}^{\text{no-memory}} / \rho_{\text{peak}}^{\text{memory}}$ evaluated at the same time after collapse onset.

Derive (perturbatively) the separation ratio as a function of $\Sigma\lambda / |\Lambda|$, $\nu_{\text{slow}}$, and $d$.

---

## Format of expected output

Mathematical derivation in LaTeX or plain notation. For each question:

1. State the integral / equation / ansatz that you are working with.
2. Show the key steps of the manipulation.
3. State the result (formula).
4. State the validity range (the parameter regime where the derivation is valid).
5. If the derivation is incomplete or requires further assumptions, state explicitly which assumption and what would be needed to remove it.

Do NOT include hedge or methodological framing. The user (a structural-research-mode-active assistant) will integrate the result into the repository with the appropriate framing.

---

## Why this matters

Open-problems/01 status today: "leading-order skeleton + variational ansatz + regime constraints, closed-form $\Sigma\lambda_{\text{crit}}(d)$ open."

A successful resolution of Questions 1-3 would advance this to: "analytical $\Sigma\lambda_{\text{crit}}(d)$ derived, numerically validated against d=2,3,4,5 data, with the focal-collapse-vs-dispersive boundary characterized." This is criterion 1 (internal mathematical consistency) progress at substrate-foundational level.

A successful resolution of Question 4 closes the criterion 2 (reproducibility) loop: the analytical separation ratio is a quantitative prediction the existing numerical data evaluates directly.

The cross-domain interfaces feed back: BAO, archaeoacoustic, cymatic, gamma-entrainment, SSM, etc. all rely on the equation having well-characterized anti-collapse behavior at the relevant $d$ in the relevant regime. The analytical theory tightens the structural claim across all 22 interfaces.
