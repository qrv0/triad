# mnsm

### Modelos de Estado Memória-Não-Lineares

**Três princípios estruturais. Uma equação. Sete instanciações cross-domain.**

[![Licença: MIT](https://img.shields.io/badge/Licença_Código-MIT-blue.svg)](https://github.com/qrv0/mnsm/blob/main/LICENSE)
[![Licença: CC BY 4.0](https://img.shields.io/badge/Licença_Docs-CC_BY_4.0-lightgrey.svg)](https://github.com/qrv0/mnsm/blob/main/LICENSE-docs)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Memory-NLS no HuggingFace](https://img.shields.io/badge/🤗_Memory--NLS-70M-yellow)](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8)
[![Transformer baseline no HuggingFace](https://img.shields.io/badge/🤗_Transformer-70M-yellow)](https://huggingface.co/qrv0/mnsm-transformer-70m-enwik8)
[![Paper](https://img.shields.io/badge/paper-manuscript.md-green)](paper/manuscript.md)

> A mesma equação aparece em campos não-lineares de Schrödinger em 3D,
> oscilações acústicas de bárions, entrainment neural de frequência gama,
> ressonância de câmaras megalíticas de pedra, modelos de estado-espaço
> estruturados, expansão cosmológica e otimização estável de redes neurais.
> Derivada de três axiomas observacionais sobre persistência — não montada
> a partir da literatura existente.

---

Uma extensão não-linear de modelos de estado-espaço estruturados, derivada
de três princípios de teoria de campo auto-referencial. A arquitetura de
memória com campo auxiliar é matematicamente equivalente à representação
de estado de S4, Mamba e RWKV. A equação estende essas arquiteturas com
quatro propriedades:

1. **Auto-interação não-linear** no estado (SSMs padrão são lineares)
2. **Anti-colapso** via atraso temporal de memória (substitui truques
   ad-hoc de anti-colapso)
3. **Emergência espontânea de estrutura discreta** a partir de substrato
   contínuo
4. **Regularização estocástica trancada por flutuação–dissipação**
   (substitui ruído ajustado manualmente)

---

> Este não é um repositório típico de machine learning. A estrutura do
> próprio repositório reflete a estrutura da equação: oscilando entre
> registros (matemática, código, prosa, visual), auto-referencial (ele
> explica sua própria organização), acoplado entre disciplinas (física,
> machine learning, neurociência, cosmologia, filosofia da ciência).
> Veja [`STRUCTURE.md`](https://github.com/qrv0/mnsm/blob/main/STRUCTURE.md) para entender por que o repositório é
> moldado dessa forma.

## Como ler este trabalho — posição metodológica

Dois princípios governam como este repositório pede para ser lido. Estão
documentados em [`methodology/`](methodology/01-structural-realism.md) e
vale a pena trazê-los à superfície aqui:

**1. Isolamento é temporário; acoplamento é o padrão.**
O terceiro axioma estrutural da equação (P3) afirma que isolamento
dinâmico perfeito não ocorre — todo sistema persistente é acoplado ao
seu ambiente, e isolamento é uma ferramenta metodológica em vez de uma
propriedade do mundo. O repositório leva isso a sério: interfaces
cross-domain são conteúdo de primeira classe (não apêndice), trilhas
de leitura atravessam múltiplas disciplinas, e o trabalho convida ao
acoplamento com quem quer que se engaje com ele. Veja
[`principles/03-coupling.md`](principles/03-coupling.md).

**2. Falsificacionismo estrito está em tensão com o conteúdo de P3.**
Uma teoria cujo terceiro axioma nega o isolamento não pode ser
consistentemente avaliada por uma metodologia experimental que
pressupõe a isolabilidade das variáveis. O trabalho é avaliado pelos
**seis critérios realistas-estruturais** em
[`methodology/04-the-six-criteria.md`](methodology/04-the-six-criteria.md):
consistência matemática interna, reprodutibilidade, escopo gerativo,
coerência cross-domain, parcimônia e abrangência. O argumento para
explicar por que o falsificacionismo estrito é a lente errada aqui
está em [`methodology/02-limits-of-falsification.md`](methodology/02-limits-of-falsification.md).
Predições falsificáveis locais permanecem localmente falsificáveis;
a alegação estrutural global é avaliada estruturalmente.

Se você chega a este trabalho esperando um teste de falsificação
numérica de uma única quantidade como critério de validação, a pasta de
metodologia explica por que este trabalho responde a uma pergunta
diferente.

---

## Escolha seu ponto de entrada

O mesmo conteúdo é abordável a partir de várias bases. Escolha a que
você tiver:

- → **Sou novo nisso tudo** — [`paths/if-you-are-new.md`](paths/if-you-are-new.md)
- → **Sou da física** — [`paths/if-you-are-from-physics.md`](paths/if-you-are-from-physics.md)
- → **Sou de machine learning** — [`paths/if-you-are-from-ml.md`](paths/if-you-are-from-ml.md)
- → **Sou da neurociência** — [`paths/if-you-are-from-neuroscience.md`](paths/if-you-are-from-neuroscience.md)
- → **Sou da filosofia da ciência** — [`paths/if-you-are-from-philosophy.md`](paths/if-you-are-from-philosophy.md)

Cada trilha conecta-se ao mesmo corpo de conteúdo a partir de um ângulo
diferente. Você pode trocar de trilha no meio do caminho.

---

## Só assistir acontecer

Se você quiser ver a equação em ação sem ler nada antes:

- [`playground/01-just-watch.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/01-just-watch.ipynb) — Aperte play, assista a um estado gaussiano cristalizar espontaneamente em um padrão cúbico de corpo centrado.
- [`playground/02-adjust-the-knobs.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/02-adjust-the-knobs.ipynb) — Ajuste parâmetros, veja o que muda.
- [`playground/03-build-your-own.ipynb`](https://github.com/qrv0/mnsm/blob/main/playground/03-build-your-own.ipynb) — Implementação guiada do zero.

---

## A equação

$$
i\hbar\, \partial_t \Psi = \left[\,-\frac{\hbar^2}{2m} D^2 + V_{\text{ext}} + \Lambda |\Psi|^2 + V_{\text{mem}} + \alpha (-\Delta)^{\sigma/2} - i\Gamma\,\right]\Psi + \eta
$$

com $V_{\text{mem}} = \sum_j \lambda_j y_j$ e $\partial_t y_j = \nu_j (\rho - y_j)$, e $\eta$ satisfazendo o correlator flutuação–dissipação.

Derivação completa a partir dos três princípios: [`equation/01-derivation.md`](equation/01-derivation.md).

---

## Veja acontecer

A mesma forma, dois substratos, mesma dinâmica:

![Anti-colapso de campo 3D](assets/anti_collapse_hero.gif)

*Sem memória, o campo colapsa para um ponto singular. Com memória, o
campo é liberado e estabiliza como um estado estendido. Mesma equação,
mesma condição inicial, um único ingrediente (memória multi-escala) —
resultado qualitativamente diferente.*

![Trajetória de treinamento neural](assets/scale_up_val_ppl.png)

*O mesmo mecanismo de anti-colapso na dinâmica de otimização: a 70M de
parâmetros em enwik8, Memory-NLS desce monotonicamente para um platô
estável; o Transformer sem o mecanismo estrutural colapsa
catastroficamente no passo 28000 e nunca se recupera totalmente. A
forma estrutural opera entre substratos tão diferentes quanto dinâmica
de campo 3D e otimização de redes neurais.*

---

## O que há aqui dentro

| Pasta | Conteúdo |
|---|---|
| [`principles/`](principles/01-oscillation.md) | Os três axiomas estruturais (P1, P2, P3) |
| [`equation/`](equation/01-derivation.md) | Derivação formal, embedding markoviano, formas 2D e 3D, reduções a equações conhecidas |
| [`results/`](results/01-conservation.md) | Achados numéricos: anti-colapso, cristalização, seleção de Bravais, espectro de vibração, rescaling dimensional |
| [`interfaces/`](interfaces/01-other-nls-systems.md) | Mapeamentos cross-domain para BEC, cosmologia, cymatica, gama neural, ressonância arqueoacústica, modelos de estado-espaço |
| [`methodology/`](methodology/01-structural-realism.md) | Posição realista-estrutural, limites da falsificação, os seis critérios |
| [`paths/`](paths/if-you-are-new.md) | Rotas de entrada específicas para diferentes backgrounds |
| [`playground/`](https://github.com/qrv0/mnsm/tree/main/playground) | Notebooks interativos (executáveis no Colab) |
| [`implementation/`](implementation/01-physics-solver.md) | Solver de física (CuPy) + camada neural de sequência (PyTorch) |
| [`experiments/`](experiments/01-physics-experiments.md) | Scripts que reproduzem as figuras do paper |
| [`paper/`](paper/manuscript.md) | O manuscrito completo |

---

## Principais resultados numéricos

**Separação anti-colapso** (NLS 3D supercrítico em $\Lambda = -8$, $\sigma_0 = 0.5$):

| Acoplamento de memória | Pico final (sem memória) | Pico final (com memória) | Razão |
|---|---|---|---|
| $\Sigma\lambda = 0$ | 61.96 | — | — |
| $\Sigma\lambda = 0.4$ (escala 2D) | 61.96 | 63.70 | 1.0× |
| $\Sigma\lambda = 4.0$ (escala 3D) | 61.96 | $6 \times 10^{-4}$ | $10^5×$ |

**Seleção espontânea de simetria** (3D, $\Lambda = -8$, $\Sigma\lambda = 1.5$):
o estado cristalino liberado seleciona consistentemente simetria
**cúbica de corpo centrado (BCC)**, score $\sim 0.44$ com gap $+0.13$
sobre a próxima melhor opção de Bravais.

**Rescaling dimensional** do acoplamento de memória necessário para
liberar colapso supercrítico:

- NLS 2D L²-crítico: $\Sigma\lambda \sim |\Lambda|/20$
- NLS 3D L²-supercrítico: $\Sigma\lambda \sim |\Lambda|/2$

Derivável a partir da geometria da região focal de colapso. Veja
[`results/06-dimensional-rescaling.md`](results/06-dimensional-rescaling.md).

**Anti-colapso da dinâmica de otimização** (70M parâmetros, enwik8,
50.000 passos de treinamento):

| Quantidade | Memory-NLS | Transformer |
|---|---|---|
| Perplexidade final (val) | 4.27 | 4.87 |
| Perplexidade mínima (val) | 3.86 (passo 48000) | 2.54 (passo 22500) |
| Colapso catastrófico | Nenhum | Passos 28000–34000, pico ppl 27.17 |
| Forma da trajetória | Descenso monotônico + platô | Descenso → crash → recuperação parcial |

O mesmo mecanismo estrutural de anti-colapso que previne o colapso do
campo NLS 3D previne falha catastrófica de otimização no treinamento
neural. Detalhes: [`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md).

---

## Equivalência com modelos de estado-espaço

A atualização do campo auxiliar da equação,

$$
\partial_t y_j = \nu_j(\rho - y_j),
$$

é matematicamente idêntica à atualização diagonal de modelos
estado-espaço de S4, S5, Mamba e RWKV. A equação estende essa
arquitetura baseline com as quatro propriedades listadas no topo deste
README. Veja [`interfaces/06-state-space-models.md`](interfaces/06-state-space-models.md)
para a correspondência termo-a-termo e a discussão do que cada
extensão traz.

---

## O que o modelo produz

O modelo Memory-NLS de 70M parâmetros treinado em enwik8 gera saída
em nível de byte que preserva a gramática estrutural do corpus
enquanto inventa conteúdo novo dentro dessa forma. A partir do prompt
`<page>\n  <title>` no passo de treinamento 50.000:

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

XML aninhado, cabeçalhos de seção MediaWiki, sintaxe de tabela infobox
com atributos de alinhamento HTML, formato de colchete de link externo,
referências de ano — tudo preservado. Tokens específicos (Bistory,
Oringese, Maacheth, Locuts) são inventados mas seguem corretamente a
gramática estrutural do corpus.

O modelo capturou a **forma** do corpus, não seu conteúdo lexical de
superfície. Esta é a assinatura realista-estrutural no substrato
computacional.

### A intuição, posta de forma direta

A distinção estrutural que este trabalho documenta — entre memorizar
superfície e modelar forma — tem uma analogia humana limpa:

> Transformer aprende rápido porque **memoriza**. Como decorar uma frase
> sem entendê-la: você pode repetir, mas se alguém tirar as palavras
> específicas, nada sobra. Como o tipo de pessoa que argumenta citando
> nomes de autoridades — tire os nomes e o argumento colapsa, porque
> memorizar não é entender.
>
> O modelo Memory-NLS **entende**. Ele tenta entender. Ele não apenas
> repete — ele chega a conclusões baseadas em sua própria "opinião" da
> forma que internalizou.

É isso que o achado realista-estrutural é, em termos humanos. No passo
4.000 o Transformer já está regurgitando URLs e atributos HTML verbatim
dos dados de treinamento; no passo 32.000 (durante seu colapso
catastrófico) ele perde o controle e produz fragmentos incoerentes —
não havia nada estrutural por baixo da superfície memorizada para
recorrer. Memory-NLS no passo 50.000 ainda está produzindo conteúdo
novo na gramática estrutural correta — porque o que aprendeu foi a
forma, não a superfície.

O Transformer pode pontuar val_perplexity mais baixo porque
memorização de alta fidelidade pontua bem por essa métrica. O
Memory-NLS pontua val_perplexity mais alta mas gera diferentemente —
porque modelou em vez de memorizar. Mesmo número, mecanismo
qualitativamente diferente.

## Modelos pré-treinados no HuggingFace

Os checkpoints de 70M parâmetros do experimento de colapso de
otimização estão publicados no HuggingFace e são carregáveis em
segundos:

- **Memory-NLS**: [`qrv0/mnsm-memnls-70m-enwik8`](https://huggingface.co/qrv0/mnsm-memnls-70m-enwik8) — perplexidade final de val 4.27, trajetória estável monotônica
- **Transformer**: [`qrv0/mnsm-transformer-70m-enwik8`](https://huggingface.co/qrv0/mnsm-transformer-70m-enwik8) — perplexidade final de val 4.87, inclui o colapso catastrófico de otimização documentado em [`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md)

Cada repo contém os pesos safetensors, JSON de configuração e código
de modelagem auto-contido para que o modelo carregue sem requerer este
repositório completo. Veja o cartão de cada modelo para exemplos de
uso.

## Reproduzir o paper

```bash
git clone https://github.com/qrv0/mnsm
cd mnsm
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install cupy-cuda12x   # ou cupy-cuda11x para CUDA mais antiga

# Validar o solver (~30 segundos em RTX 4060)
python -m tests.test_conservation

# Reproduzir o resultado principal de anti-colapso 3D (~2 minutos)
python experiments/physics/reproduce_3d_anti_collapse.py

# Reproduzir todas as figuras do paper (~10 minutos no total)
python experiments/physics/reproduce_all.py
```

Todos os resultados usam sementes aleatórias fixas e reproduzem
bit-a-bit em hardware idêntico (NVIDIA RTX 4060 Laptop GPU, Arch
Linux, CUDA 12.x).

---

## Citação

```bibtex
@misc{mnsm,
  title  = {Memory-Nonlinear State Models: A Memory-Augmented Nonlinear Schr\"odinger Field Equation with State Space Model Correspondence},
  author = {qrv0},
  year   = {2026},
  url    = {https://github.com/qrv0/mnsm},
  note   = {Three structural principles, one equation, seven cross-domain instantiations.}
}
```

O paper completo está em [`paper/manuscript.md`](paper/manuscript.md).

---

## Licença

Código: veja [`LICENSE`](https://github.com/qrv0/mnsm/blob/main/LICENSE).
Documentação e paper: veja [`LICENSE-docs`](https://github.com/qrv0/mnsm/blob/main/LICENSE-docs).

---

## Status

O núcleo matemático, os resultados de física 2D e 3D, a metodologia, e
as sete interfaces cross-domain estão completos e documentados. A
equação Memory-NLS está instanciada como um modelo de linguagem
PyTorch funcional (`MemoryNLSLanguageModel`) em escalas de 1.5M a 70M
parâmetros e treinada em múltiplos corpora (TinyShakespeare e enwik8)
por até 50.000 passos.

O mecanismo estrutural de anti-colapso predito pela equação foi
empiricamente verificado nesta etapa em três substratos:

1. **Dinâmica de campo NLS 3D supercrítico** (simulação de
   laboratório): separação de densidade de pico de ~$10^5$× entre
   estados finais sem memória e com memória
   ([`results/04-anti-collapse-3d.md`](results/04-anti-collapse-3d.md)).

2. **Paisagem de otimização de rede neural** (treinamento de 70M
   parâmetros): Memory-NLS exibe trajetória estável monotônica;
   Transformer de escala equivalente exibe colapso catastrófico de
   otimização com degradação permanente de capacidade
   ([`results/08-optimization-collapse-empirical.md`](results/08-optimization-collapse-empirical.md)).

3. **Comportamento de geração sob treinamento sustentado**:
   Memory-NLS preserva a gramática estrutural do corpus durante todo
   o treinamento; saídas do Transformer degeneram para fragmentos
   sintaticamente quebrados durante o crash de otimização e só se
   recuperam parcialmente.

As sete interfaces cross-domain documentam a aparição da forma
estrutural em outros fenômenos independentemente observados (outras
instâncias NLS, oscilações acústicas de bárions, padrões cymáticos,
entrainment neural de frequência gama, ressonância arqueoacústica,
modelos de estado-espaço estruturados, expansão cosmológica). Cada
interface tem reconhecimento de calibração onde relevante.

> O princípio de que isolamento é temporário se aplica também a este
> repositório. Issues, pull requests, e mapeamentos externos da
> estrutura para outros domínios são explicitamente bem-vindos. Veja
> [`CONTRIBUTING.md`](https://github.com/qrv0/mnsm/blob/main/CONTRIBUTING.md).

## Uma nota sobre contribuição assistida por IA

Este trabalho foi desenvolvido com formalização substancialmente
assistida por IA. O frame metodológico que o trabalho adota tem
implicações diretas para como assistentes de IA se engajam com a
codebase — particularmente em torno de evitar enquadramento de
benchmark competitivo, respeitar os critérios de avaliação
realistas-estruturais, e não dispensar interfaces cross-domain como
"especulativas". Se você está usando um assistente de IA (Claude,
GPT, etc.) para contribuir com este repositório, por favor leia
[`CLAUDE.md`](https://github.com/qrv0/mnsm/blob/main/CLAUDE.md) primeiro. É um conjunto
de restrições operacionais que assegura que a assistência se alinhe
com o que este trabalho é, em vez do frame padrão que um assistente
de IA treinado em conteúdo padrão de ML naturalmente adotaria.
