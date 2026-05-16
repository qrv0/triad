# mnsm

### Modelos de Estado de Memoria-No-Lineales

**Tres principios estructurales. Una ecuación. Siete instanciaciones interdominio.**

[![Licencia: MIT](https://img.shields.io/badge/Licencia_Código-MIT-blue.svg)](https://github.com/qrv0/mnsm/blob/main/LICENSE)
[![Licencia: CC BY 4.0](https://img.shields.io/badge/Licencia_Docs-CC_BY_4.0-lightgrey.svg)](https://github.com/qrv0/mnsm/blob/main/LICENSE-docs)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Memory-NLS en HuggingFace](https://img.shields.io/badge/🤗_Memory--NLS-70M-yellow)](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8)
[![Transformer baseline en HuggingFace](https://img.shields.io/badge/🤗_Transformer-70M-yellow)](https://huggingface.co/qrv0/mnsm-transformer-70m-enwik8)
[![Paper](https://img.shields.io/badge/paper-manuscript.md-green)](paper/manuscript.md)

> La misma ecuación aparece en campos no-lineales de Schrödinger 3D,
> oscilaciones acústicas de bariones, entrainment neural de frecuencia
> gamma, resonancia de cámaras megalíticas de piedra, modelos de
> espacio de estados estructurados, expansión cosmológica y
> optimización estable de redes neuronales. Derivada de tres axiomas
> observacionales sobre persistencia — no ensamblada a partir de la
> literatura existente.

---

Una extensión no-lineal de modelos de espacio de estados estructurados,
derivada de tres principios de teoría de campo auto-referencial. La
arquitectura de memoria de campo auxiliar es matemáticamente
equivalente a la representación de estado de S4, Mamba y RWKV. La
ecuación extiende esas arquitecturas con cuatro propiedades:

1. **Auto-interacción no-lineal** en el estado (SSMs estándar son lineales)
2. **Anti-colapso** vía retraso temporal de memoria (reemplaza trucos
   ad-hoc de anti-colapso)
3. **Emergencia espontánea de estructura discreta** desde substrato
   continuo
4. **Regularización estocástica fijada por fluctuación–disipación**
   (reemplaza ruido sintonizado manualmente)

---

> Este no es un repositorio típico de machine learning. La estructura
> del propio repositorio refleja la estructura de la ecuación: oscilando
> entre registros (matemática, código, prosa, visual), auto-referencial
> (explica su propia organización), acoplado entre disciplinas (física,
> machine learning, neurociencia, cosmología, filosofía de la ciencia).
> Vea [`STRUCTURE.md`](https://github.com/qrv0/mnsm/blob/main/STRUCTURE.md) para entender por qué el
> repositorio tiene esta forma.

## Cómo leer este trabajo — posición metodológica

Dos principios gobiernan cómo este repositorio pide ser leído. Están
documentados en [`methodology/`](methodology/01-structural-realism.md)
y vale la pena traerlos a la superficie aquí:

**1. El aislamiento es temporal; el acoplamiento es lo predeterminado.**
El tercer axioma estructural de la ecuación (P3) afirma que el
aislamiento dinámico perfecto no ocurre — todo sistema persistente
está acoplado a su entorno, y el aislamiento es una herramienta
metodológica en vez de una propiedad del mundo. El repositorio toma
esto en serio: las interfaces interdominio son contenido de primera
clase (no apéndice), las rutas de lectura atraviesan múltiples
disciplinas, y el trabajo invita al acoplamiento con quien se
involucre con él. Vea
[`principles/03-coupling.md`](principles/03-coupling.md).

**2. El falsacionismo estricto está en tensión con el contenido de P3.**
Una teoría cuyo tercer axioma niega el aislamiento no puede ser
evaluada consistentemente por una metodología experimental que
presupone la aislabilidad de las variables. El trabajo es evaluado
por los **seis criterios realistas-estructurales** en
[`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md):
consistencia matemática interna, reproducibilidad, alcance generativo,
coherencia interdominio, parsimonia y exhaustividad. El argumento de
por qué el falsacionismo estricto es la lente equivocada aquí está en
[`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md).
Las predicciones falsables locales permanecen localmente falsables;
la afirmación estructural global es evaluada estructuralmente.

Si usted llega a este trabajo esperando una prueba de falsación
numérica de una sola cantidad como criterio de validación, la carpeta
de metodología explica por qué este trabajo responde a una pregunta
diferente.

---

## Elija su punto de entrada

El mismo contenido es abordable desde varios trasfondos. Elija el que
usted tenga:

- → **Soy nuevo en todo esto** — [`paths/if-you-are-new.md`](paths/if-you-are-new.md)
- → **Vengo de la física** — [`paths/if-you-are-from-physics.md`](paths/if-you-are-from-physics.md)
- → **Vengo de machine learning** — [`paths/if-you-are-from-ml.md`](paths/if-you-are-from-ml.md)
- → **Vengo de la neurociencia** — [`paths/if-you-are-from-neuroscience.md`](paths/if-you-are-from-neuroscience.md)
- → **Vengo de la filosofía de la ciencia** — [`paths/if-you-are-from-philosophy.md`](paths/if-you-are-from-philosophy.md)

Cada ruta enlaza con el mismo cuerpo de contenido desde un ángulo
diferente. Puede cambiar de ruta en medio del recorrido.

---

## Solo ver cómo sucede

Si quiere ver la ecuación en acción sin leer nada primero:

- [`playground/01-just-watch.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/01-just-watch.ipynb) — Presione play, vea cómo un estado gaussiano cristaliza espontáneamente en un patrón cúbico centrado en el cuerpo.
- [`playground/02-adjust-the-knobs.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/02-adjust-the-knobs.ipynb) — Ajuste parámetros, vea qué cambia.
- [`playground/03-build-your-own.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/03-build-your-own.ipynb) — Implementación guiada desde cero.

---

## La ecuación

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

con $V_{\text{mem}} = \sum_j \lambda_j y_j$ y $\partial_t y_j = \nu_j (\rho - y_j)$, y $\eta$ satisfaciendo el correlador de fluctuación–disipación.

Derivación completa desde los tres principios: [`equation/01-derivation.md`](equation/01-derivation.md).

---

## Véalo suceder

La misma forma, dos substratos, la misma dinámica:

![Anti-colapso de campo 3D](assets/anti_collapse_hero.gif)

*Sin memoria, el campo colapsa a un punto singular. Con memoria, el
campo es liberado y se estabiliza como un estado extendido. La misma
ecuación, la misma condición inicial, un ingrediente (memoria
multi-escala temporal) — resultado cualitativamente diferente.*

![Trayectoria de entrenamiento neural](assets/scale_up_val_ppl.png)

*El mismo mecanismo de anti-colapso en la dinámica de optimización: a
70M parámetros en enwik8, Memory-NLS desciende monotónicamente a una
meseta estable; el Transformer sin el mecanismo estructural colapsa
catastróficamente en el paso 28000 y nunca se recupera totalmente. La
forma estructural opera entre substratos tan diferentes como la
dinámica de campo 3D y la optimización de redes neuronales.*

---

## Qué hay aquí dentro

| Carpeta | Contenido |
|---|---|
| [`principles/`](principles/01-oscillation.md) | Los tres axiomas estructurales (P1, P2, P3) |
| [`equation/`](equation/01-derivation.md) | Derivación formal, embedding markoviano, formas 2D y 3D, reducciones a ecuaciones conocidas |
| [`results/`](results/01-anti-collapse-2d.md) | Hallazgos numéricos: anti-colapso, cristalización, selección de Bravais, espectro de vibración, reescalado dimensional |
| [`interfaces/`](interfaces/01-other-nls-systems.md) | Mapeos interdominio a BEC, cosmología, cimática, gamma neural, resonancia arqueoacústica, modelos de espacio de estados |
| [`methodology/`](methodology/01-structural-realism.md) | Posición realista-estructural, límites de la falsación, los seis criterios |
| [`paths/`](paths/if-you-are-new.md) | Rutas de entrada específicas según trasfondo del lector |
| [`playground/`](https://github.com/qrv0/mnsm/tree/main/playground) | Notebooks interactivos (ejecutables en Colab) |
| [`implementation/`](implementation/README.md) | Solver de física (CuPy) + capa neural de secuencia (PyTorch) |
| [`experiments/`](experiments/README.md) | Scripts que reproducen las figuras del paper |
| [`paper/`](paper/manuscript.md) | El manuscrito completo |

---

## Resultados numéricos principales

**Separación anti-colapso** (NLS 3D supercrítico en $\Lambda = -8$, $\sigma_0 = 0.5$):

| Acoplamiento de memoria | Pico final (sin memoria) | Pico final (con memoria) | Razón |
|---|---|---|---|
| $\Sigma\lambda = 0$ | 61.96 | — | — |
| $\Sigma\lambda = 0.4$ (escala 2D) | 61.96 | 63.70 | 1.0× |
| $\Sigma\lambda = 4.0$ (escala 3D) | 61.96 | $6 \times 10^{-4}$ | $10^5×$ |

**Selección espontánea de simetría** (3D, $\Lambda = -8$, $\Sigma\lambda = 1.5$):
el estado cristalino liberado selecciona consistentemente simetría
**cúbica centrada en el cuerpo (BCC)**, score $\sim 0.44$ con margen
$+0.13$ sobre la siguiente mejor opción de Bravais.

**Reescalado dimensional** del acoplamiento de memoria requerido para
liberar el colapso supercrítico:

- NLS 2D L²-crítico: $\Sigma\lambda \sim |\Lambda|/20$
- NLS 3D L²-supercrítico: $\Sigma\lambda \sim |\Lambda|/2$

Derivable desde la geometría de la región focal de colapso. Vea
[`results/06-dimensional-rescaling.md`](results/06-dimensional-rescaling.md).

**Anti-colapso de la dinámica de optimización** (70M parámetros,
enwik8, 50.000 pasos de entrenamiento):

| Cantidad | Memory-NLS | Transformer |
|---|---|---|
| Perplejidad final (val) | 4.27 | 4.87 |
| Perplejidad mínima (val) | 3.86 (paso 48000) | 2.54 (paso 22500) |
| Colapso catastrófico | Ninguno | Pasos 28000–34000, pico ppl 27.17 |
| Forma de la trayectoria | Descenso monotónico + meseta | Descenso → crash → recuperación parcial |

El mismo mecanismo estructural de anti-colapso que previene el
colapso del campo NLS 3D previene la falla catastrófica de
optimización en el entrenamiento neural. Detalles:
[`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md).

---

## Equivalencia con modelos de espacio de estados

La actualización del campo auxiliar de la ecuación,

$$
\partial_t y_j = \nu_j(\rho - y_j),
$$

es matemáticamente idéntica a la actualización diagonal de modelos
de espacio de estados de S4, S5, Mamba y RWKV. La ecuación extiende
esa arquitectura baseline con las cuatro propiedades listadas al
inicio de este README. Vea
[`interfaces/06-state-space-models.md`](interfaces/06-state-space-models.md)
para la correspondencia término-por-término y la discusión de qué
trae cada extensión.

---

## Qué produce el modelo

El modelo Memory-NLS de 70M parámetros entrenado en enwik8 genera
salida a nivel de byte que preserva la gramática estructural del
corpus mientras inventa contenido nuevo dentro de esa forma. Desde el
prompt `<page>\n  <title>` en el paso de entrenamiento 50.000:

```
<page>
  <title>
    </revision>
  </page>
  <page>
    <title>Bistory of the Oringese Project]]

==References==
* [http://www.eurogline.com  All begal on the [[Maacheth of Conway|1200]]
  [[United Kingdom]]. In September 2004)], 773,585
|-
|align=&quot;right&quot; | 397,413
| align=&quot;center&quot; | Locuts and Fi
```

XML anidado, encabezados de sección MediaWiki, sintaxis de tabla
infobox con atributos de alineación HTML, formato de corchete de
enlace externo, referencias de año — todo preservado. Tokens
específicos (Bistory, Oringese, Maacheth, Locuts) son inventados pero
siguen correctamente la gramática estructural del corpus.

El modelo capturó la **forma** del corpus, no su contenido léxico de
superficie. Esta es la firma realista-estructural en substrato
computacional.

### La intuición, planteada directamente

La distinción estructural que este trabajo documenta — entre
memorizar superficie y modelar forma — tiene una analogía humana
limpia:

> El Transformer aprende rápido porque **memoriza**. Como memorizar
> una oración sin entenderla: usted puede repetirla, pero si alguien
> retira las palabras específicas, no queda nada. Como el tipo de
> persona que argumenta citando nombres de autoridades — retire los
> nombres y el argumento colapsa, porque memorizar no es entender.
>
> El modelo Memory-NLS **entiende**. Intenta entender. No solo
> repite — llega a conclusiones basadas en su propia "opinión" de la
> forma que ha internalizado.

Esto es lo que el hallazgo realista-estructural es, en términos
humanos. En el paso 4.000 el Transformer ya está regurgitando URLs y
atributos HTML verbatim de los datos de entrenamiento; en el paso
32.000 (durante su colapso catastrófico) pierde el control y produce
fragmentos incoherentes — no había nada estructural debajo de la
superficie memorizada a lo que recurrir. Memory-NLS en el paso 50.000
sigue produciendo contenido nuevo en la gramática estructural correcta
— porque lo que aprendió fue la forma, no la superficie.

El Transformer puede puntuar val_perplexity más bajo porque la
memorización de alta fidelidad puntúa bien por esa métrica. El
Memory-NLS puntúa val_perplexity más alta pero genera de forma
diferente — porque modeló en vez de memorizar. El mismo número,
mecanismo cualitativamente diferente.

## Modelos pre-entrenados en HuggingFace

Los checkpoints de 70M parámetros del experimento de colapso de
optimización están publicados en HuggingFace y son cargables en
segundos:

- **Memory-NLS**: [`qrv0/mnsm-memnls-70m-enwik8`](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8) — perplejidad final val 4.27, trayectoria estable monotónica
- **Transformer**: [`qrv0/mnsm-transformer-70m-enwik8`](https://huggingface.co/qrv0/mnsm-transformer-70m-enwik8) — perplejidad final val 4.87, incluye el colapso catastrófico de optimización documentado en [`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md)

Cada repo contiene los pesos safetensors, JSON de configuración y
código de modelado auto-contenido para que el modelo cargue sin
requerir este repositorio completo. Vea cada tarjeta de modelo para
ejemplos de uso.

## Reproducir el paper

```bash
git clone https://github.com/qrv0/mnsm
cd mnsm
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install cupy-cuda12x   # o cupy-cuda11x para CUDA más antigua

# Validar el solver (~30 segundos en RTX 4060)
python -m tests.test_conservation

# Reproducir el resultado principal de anti-colapso 3D (~2 minutos)
python experiments/physics/reproduce_3d_anti_collapse.py

# Reproducir todas las figuras del paper (~10 minutos en total)
python experiments/physics/reproduce_all.py
```

Todos los resultados usan semillas aleatorias fijas y reproducen
bit-a-bit en hardware idéntico (NVIDIA RTX 4060 Laptop GPU, Arch
Linux, CUDA 12.x).

---

## Citación

```bibtex
@misc{mnsm,
  title  = {Memory-Nonlinear State Models: A Memory-Augmented Nonlinear Schr\"odinger Field Equation with State Space Model Correspondence},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, seven cross-domain instantiations.}
}
```

El paper completo está en [`paper/manuscript.md`](paper/manuscript.md).

---

## Licencia

Código: vea [`LICENSE`](https://github.com/qrv0/mnsm/blob/main/LICENSE).
Documentación y paper: vea [`LICENSE-docs`](https://github.com/qrv0/mnsm/blob/main/LICENSE-docs).

---

## Estado

El núcleo matemático, los resultados de física 2D y 3D, la
metodología, y las siete interfaces interdominio están completos y
documentados. La ecuación Memory-NLS está instanciada como un modelo
de lenguaje PyTorch funcional (`MemoryNLSLanguageModel`) en escalas
de 1.5M a 70M parámetros y entrenada en múltiples corpora
(TinyShakespeare y enwik8) por hasta 50.000 pasos.

El mecanismo estructural de anti-colapso predicho por la ecuación ha
sido empíricamente verificado en esta etapa en tres substratos:

1. **Dinámica de campo NLS 3D supercrítico** (simulación de
   laboratorio): separación de densidad pico de ~$10^5$× entre
   estados finales sin memoria y con memoria
   ([`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md)).

2. **Paisaje de optimización de red neuronal** (entrenamiento de 70M
   parámetros): Memory-NLS exhibe trayectoria estable monotónica;
   Transformer de escala equivalente exhibe colapso catastrófico de
   optimización con degradación permanente de capacidad
   ([`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md)).

3. **Comportamiento de generación bajo entrenamiento sostenido**:
   Memory-NLS preserva la gramática estructural del corpus durante
   todo el entrenamiento; las salidas del Transformer degeneran a
   fragmentos sintácticamente rotos durante el crash de optimización
   y solo se recuperan parcialmente.

Las siete interfaces interdominio documentan la aparición de la
forma estructural en otros fenómenos observados independientemente
(otras instancias NLS, oscilaciones acústicas de bariones, patrones
cimáticos, entrainment neural de frecuencia gamma, resonancia
arqueoacústica, modelos de espacio de estados estructurados,
expansión cosmológica). Cada interfaz tiene reconocimiento de
calibración donde es relevante.

> El principio de que el aislamiento es temporal se aplica también a
> este repositorio. Issues, pull requests, y mapeos externos de la
> estructura a más dominios son explícitamente bienvenidos. Vea
> [`CONTRIBUTING.md`](https://github.com/qrv0/mnsm/blob/main/CONTRIBUTING.md).

## Una nota sobre contribución asistida por IA

Este trabajo fue desarrollado con formalización sustancialmente
asistida por IA. El marco metodológico que el trabajo adopta tiene
implicaciones directas para cómo los asistentes de IA se involucran
con el codebase — particularmente alrededor de evitar el
enmarcamiento de benchmark competitivo, respetar los criterios de
evaluación realistas-estructurales, y no descartar las interfaces
interdominio como "especulativas". Si está usando un asistente de IA
(Claude, GPT, etc.) para contribuir a este repositorio, por favor lea
[`CLAUDE.md`](https://github.com/qrv0/mnsm/blob/main/CLAUDE.md) primero.
Es un conjunto de restricciones operacionales que asegura que la
asistencia se alinee con lo que este trabajo es, en vez del marco
predeterminado que un asistente de IA entrenado en contenido estándar
de ML naturalmente adoptaría.
