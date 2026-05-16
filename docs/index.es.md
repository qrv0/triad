---
title: Inicio
description: >-
  Modelos de Estado de Memoria-No-Lineales: tres principios estructurales,
  una ecuación, nueve instanciaciones interdominio. Derivada de la
  observación, no ensamblada a partir de la literatura.
hide:
  - navigation
  - toc
---

<div class="mnsm-hero" markdown>

<div class="mnsm-hero__visual" markdown>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../_docs_assets/cross-domain-wheel-dark.svg">
  <img src="../_docs_assets/cross-domain-wheel-light.svg" alt="Rueda interdominio: una ecuación, nueve substratos" class="mnsm-wheel">
</picture>
</div>

<div class="mnsm-hero__copy" markdown>

<div class="mnsm-eyebrow">Memory-Nonlinear State Models</div>

# Una ecuación. Nueve substratos.

Una extensión no-lineal de modelos de espacio de estados estructurados,
derivada de tres principios sobre entidades extendidas persistentes. La
misma forma matemática aparece en física, cosmología, redes neuronales, y
más allá, derivada de la observación, no ensamblada a partir de la
literatura previa.

<div class="mnsm-eq" markdown>
$$
i\hbar\, \partial_t \Psi
=
\left[\,-\tfrac{\hbar^{2}}{2m} D^{2} + V_{\text{ext}} + \Lambda |\Psi|^{2} + V_{\text{mem}} + \alpha\,(-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$
</div>

<div class="eq-breakdown" markdown>
<div class="eq-term eq-term--p1" markdown>
<span class="eq-term-tag">P1 · Oscilación</span>
<span class="eq-term-math">$-\tfrac{\hbar^{2}}{2m}D^{2}$ ・ $\alpha(-\Delta)^{\sigma/2}$</span>
<span class="eq-term-desc">cinética de ecuación de onda + dispersión fraccionaria</span>
</div>
<div class="eq-term eq-term--p2" markdown>
<span class="eq-term-tag">P2 · Auto-referencia</span>
<span class="eq-term-math">$\Lambda |\Psi|^{2}$ ・ $V_{\text{mem}}$</span>
<span class="eq-term-desc">auto-interacción cúbica + jerarquía de memoria de campo auxiliar</span>
</div>
<div class="eq-term eq-term--p3" markdown>
<span class="eq-term-tag">P3 · Acoplamiento</span>
<span class="eq-term-math">$V_{\text{ext}}$ ・ $-i\Gamma$ ・ $\eta$</span>
<span class="eq-term-desc">potencial externo + par disipación–ruido acoplado por FDT</span>
</div>
</div>

<div class="mnsm-cta" markdown>
[:material-play-circle-outline: Solo observar](#vealo-suceder){ .md-button .md-button--primary }
[:material-book-open-page-variant-outline: Leer el paper](paper/manuscript.md){ .md-button }
[:material-download-outline: Usar el modelo](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8){ .md-button }
</div>

</div>

</div>

<div class="mnsm-section" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Fundamentos</span>
## Los tres principios
La ecuación se deriva de estos. No ensamblada a partir de la literatura previa, derivada de la observación de cómo se comportan las entidades extendidas persistentes.
</div>

<div class="grid cards mnsm-principle-grid" markdown>

-   :material-sine-wave:{ .lg .middle } &nbsp; **P1 · Oscilación**

    ---

    Las entidades extendidas persistentes oscilan. La existencia en régimen
    estacionario requiere un equilibrio entre avance y restauración; el
    operador canónico es diferencial parcial de segundo orden. Esto
    selecciona la forma de Schrödinger.

    [Leer P1 →](principles/01-oscillation.md)

-   :material-reflect-vertical:{ .lg .middle } &nbsp; **P2 · Auto-referencia**

    ---

    Una entidad persistente tiene acceso a sus propios estados pasados. La
    instanciación mínima es una jerarquía de memoria multi-escala indexada
    por las tasas de relajación τ, exactamente la actualización diagonal de SSM.

    [Leer P2 →](principles/02-self-reference.md)

-   :material-link-variant:{ .lg .middle } &nbsp; **P3 · Acoplamiento**

    ---

    El aislamiento es temporal; el acoplamiento es lo predeterminado. Todo
    sistema persistente está conectado a su entorno vía fluctuación–disipación,
    no a pesar de ello. Esto selecciona el término estocástico η.

    [Leer P3 →](principles/03-coupling.md)

</div>

</div>

<div class="mnsm-section mnsm-section--alt" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Interdominio</span>
## Nueve instanciaciones de la misma ecuación
Cada substrato produce independientemente la misma forma matemática. La
afirmación es estructural: la ecuación captura un patrón de comportamiento
persistente invariante bajo cambio de substrato.
</div>

<div class="grid cards mnsm-substrate-grid" markdown>

-   <span class="mnsm-substrate-sig sig--nls">:material-sine-wave:</span>
    <span class="mnsm-substrate-num">01 · Física</span>
    **Campos NLS**

    Condensados de Bose–Einstein, fibras ópticas, envolventes de ondas
    acuáticas: la ecuación de Schrödinger no-lineal aparece dondequiera
    que una envolvente lentamente variable gobierna un portador oscilatorio.

    [→ Leer interfaz](interfaces/01-other-nls-systems.md)

-   <span class="mnsm-substrate-sig sig--bao">:material-star-four-points-outline:</span>
    <span class="mnsm-substrate-num">02 · Cosmología</span>
    **Cosmología BAO**

    Oscilaciones acústicas de bariones: una onda de presión modulada por
    memoria en el plasma primordial. La escala de 150 Mpc es el lock-in de
    un término de memoria.

    [→ Leer interfaz](interfaces/02-baryon-acoustic.md)

-   <span class="mnsm-substrate-sig sig--cym">:material-hexagon-multiple-outline:</span>
    <span class="mnsm-substrate-num">03 · Acústica</span>
    **Cimática de Chladni**

    La arena sobre una placa vibrante se auto-organiza en patrones nodales.
    Cristalización discreta a partir de substrato continuo, el mismo
    mecanismo de selección que el patrón BCC producido por la ecuación en 3D.

    [→ Leer interfaz](interfaces/03-chladni-cymatics.md)

-   <span class="mnsm-substrate-sig sig--neuro">:material-brain:</span>
    <span class="mnsm-substrate-num">04 · Neuro</span>
    **Gamma Neural**

    Entrainment cortical a 40 Hz en el binding cognitivo. La estructura de
    memoria temporal de la ecuación se corresponde con la arquitectura
    multi-escala de las jerarquías de oscilación neural.

    [→ Leer interfaz](interfaces/04-gamma-entrainment.md)

-   <span class="mnsm-substrate-sig sig--archeo">:material-pillar:</span>
    <span class="mnsm-substrate-num">05 · Acústica</span>
    **Arqueoacústica**

    Cámaras megalíticas de piedra (Hipogeo de Hal Saflieni, Newgrange)
    resuenan a frecuencias que coinciden con el espectro vibracional de la
    ecuación. Misma estructura, substrato geológico.

    [→ Leer interfaz](interfaces/05-archaeoacoustic-resonance.md)

-   <span class="mnsm-substrate-sig sig--ssm">:material-grid:</span>
    <span class="mnsm-substrate-num">06 · ML</span>
    **Modelos de Espacio de Estados**

    La actualización de campo auxiliar es matemáticamente idéntica a la
    actualización diagonal de SSM de S4, S5, Mamba, y RWKV. La ecuación
    extiende esa arquitectura con no-linealidad, anti-colapso, y ruido
    acoplado por FDT.

    [→ Leer interfaz](interfaces/06-state-space-models.md)

-   <span class="mnsm-substrate-sig sig--cosmo">:material-orbit-variant:</span>
    <span class="mnsm-substrate-num">07 · Cosmología</span>
    **Expansión Cosmológica**

    Expansión a escala Hubble como una liberación dirigida por memoria
    desde el colapso gravitacional. La constante cosmológica se mapea a
    un acoplamiento de memoria de largo plazo en la formulación de campo
    auxiliar.

    [→ Leer interfaz](interfaces/07-cosmological-expansion.md)

-   <span class="mnsm-substrate-sig sig--interp">:material-magnify-scan:</span>
    <span class="mnsm-substrate-num">08 · ML / Interp</span>
    **Interpretabilidad Mecanística**

    Los sistemas solo de atención no poseen la jerarquía de memoria
    multi-escala de P2; el argumento estructural predice que deben
    codificar estructura categórica como proyecciones superpuestas,
    exactamente lo que el programa de interpretabilidad de Anthropic
    recupera mediante descomposición esparsa.

    [→ Leer interfaz](interfaces/08-mechanistic-interpretability.md)

-   <span class="mnsm-substrate-sig sig--critical">:material-graph-outline:</span>
    <span class="mnsm-substrate-num">09 · Neuro / Criticalidad</span>
    **Cerebro Crítico**

    Avalanchas neuronales, espectros 1/f, respuesta de banda ancha sin
    escala característica: la fenomenología que la literatura del cerebro
    crítico documenta en la corteza es la fenomenología que la ecuación
    produce en su régimen cristalino de absorción de banda ancha, por
    forma estructural y no por ajuste de parámetros.

    [→ Leer interfaz](interfaces/09-critical-brain.md)

</div>

</div>

<div class="mnsm-section" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Empírico</span>
## Qué hace
El mecanismo estructural de anti-colapso predicho por la ecuación ha sido
verificado empíricamente en tres substratos hasta ahora.
</div>

<div class="mnsm-results" markdown>

<div class="mnsm-result" markdown>
<div class="mnsm-result-figure">10<sup>5</sup>×</div>
<div class="mnsm-result-label">Separación anti-colapso</div>
<div class="mnsm-result-desc">Razón de densidad pico entre estados finales sin memoria y con memoria en simulación NLS 3D supercrítica.</div>
<div class="mnsm-result-link"><a href="../results/04-anti-collapse-3d.md">Anti-colapso 3D →</a></div>
</div>

<div class="mnsm-result" markdown>
<div class="mnsm-result-figure">+0.13</div>
<div class="mnsm-result-label">Margen de selección BCC</div>
<div class="mnsm-result-desc">El estado cristalino liberado selecciona espontáneamente simetría cúbica centrada en el cuerpo sobre redes Bravais alternativas.</div>
<div class="mnsm-result-link"><a href="../results/05-bravais-selection.md">Cristalización →</a></div>
</div>

<div class="mnsm-result" markdown>
<div class="mnsm-result-figure">4.27</div>
<div class="mnsm-result-label">Perplejidad estable (70M)</div>
<div class="mnsm-result-desc">Memory-NLS a 70M parámetros en enwik8 desciende monotónicamente a una meseta estable donde el Transformer de escala equivalente colapsa catastróficamente.</div>
<div class="mnsm-result-link"><a href="../results/08-optimization-collapse-empirical.md">Colapso de optimización →</a></div>
</div>

</div>

</div>

<div class="mnsm-section mnsm-section--demo" id="vealo-suceder" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Véalo</span>
## Misma ecuación, dos substratos, mismo resultado
El campo físico 3D arriba, la trayectoria de entrenamiento neural abajo,
sincronizados en el tiempo. Ambos paneles muestran el mecanismo de
anti-colapso predicho por la ecuación, manifestándose en substratos tan
diferentes como una simulación de laboratorio y un modelo de lenguaje de
70M parámetros.
</div>

<div class="mnsm-demo" markdown>
<div class="mnsm-demo-video" markdown>
<video class="mnsm-demo-media" autoplay loop muted playsinline
       poster="../assets/scale_up_val_ppl.png">
  <source src="../assets/cross_substrate_hero.mp4" type="video/mp4">
  <img src="../assets/cross_substrate_hero.gif" alt="Animación de anti-colapso interdominio">
</video>

*<strong>Arriba:</strong> campo NLS 3D supercrítico. Panel izquierdo, sin
memoria, el campo colapsa singularmente. Panel derecho, con memoria, el
campo es liberado y se estabiliza. <strong>Abajo:</strong> entrenamiento
neural, 70M parámetros en enwik8. El Transformer (rojo) colapsa
catastróficamente en el paso 28 000 donde el Memory-NLS (teal) mantiene su
descenso estable. Misma forma estructural, dos substratos, sincronizados
en el tiempo.*
</div>
</div>

</div>

<div class="mnsm-section mnsm-section--alt" markdown>

<div class="mnsm-section-head" markdown>
<span class="mnsm-section-tag">Rutas de lectura</span>
## Elija su punto de entrada
El mismo contenido es abordable desde varios trasfondos. Elija el que tenga.
</div>

<div class="grid cards mnsm-path-grid" markdown>

-   :material-account-outline:{ .middle } &nbsp; **Nuevo en todo esto**

    Recorrido en lenguaje sencillo por los principios y lo que hace la ecuación, sin prerrequisitos.

    [Comience aquí →](paths/if-you-are-new.md)

-   :material-atom:{ .middle } &nbsp; **Desde física**

    Forma de Schrödinger, correspondencias BEC/ópticas, instanciación BAO, la cuestión metodológica.

    [Ruta de física →](paths/if-you-are-from-physics.md)

-   :material-chip:{ .middle } &nbsp; **Desde machine learning**

    Equivalencia con modelos espacio-estado, anti-colapso, convolución FFT, el experimento de 70M.

    [Ruta de ML →](paths/if-you-are-from-ml.md)

-   :material-brain:{ .middle } &nbsp; **Desde neurociencia**

    Entrainment gamma, jerarquías de memoria, la arquitectura multi-escala de la oscilación neural.

    [Ruta neuro →](paths/if-you-are-from-neuroscience.md)

-   :material-book-search-outline:{ .middle } &nbsp; **Desde filosofía de la ciencia**

    Realismo estructural, por qué la falsación no es la lente correcta aquí, los seis criterios.

    [Ruta de filosofía →](paths/if-you-are-from-philosophy.md)

</div>

</div>

<div class="mnsm-section mnsm-section--quiet" markdown>

<div class="mnsm-methodology" markdown>

<span class="mnsm-section-tag">Metodología</span>

Este trabajo se evalúa por **criterios del realismo estructural**, no por
pruebas de falsación de cantidad única. Una teoría cuyo tercer axioma niega
el aislamiento no puede consistentemente ser evaluada por una metodología
que presupone la aislabilidad de las variables. El enmarcado se documenta
de antemano porque el marco estándar de machine learning ("le gana al
benchmark X por Y%") y el marco estándar de física ("predice la cantidad Q
con precisión ε") ambos pierden lo que es este trabajo.

Los seis criterios que gobiernan la evaluación: consistencia matemática
interna, reproducibilidad, alcance generativo, coherencia interdominio,
parsimonia, exhaustividad.

[→ Por qué realismo estructural](methodology/01-structural-realism.md) ・
[→ Límites de la falsación](methodology/02-limits-of-falsification.md) ・
[→ Cómo evaluar esto](methodology/03-how-to-evaluate-this.md) ・
[→ Los seis criterios](methodology/04-the-six-criteria.md)

</div>

</div>

<div class="mnsm-footer-cite" markdown>

```bibtex
@misc{mnsm,
  title  = {Memory-Nonlinear State Models: A Memory-Augmented Nonlinear
            Schr\"odinger Field Equation with State Space Model Correspondence},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, nine cross-domain instantiations.}
}
```

</div>
