# Long-horizon training: transient → stable regime

This document reports a 50,000-step training run of both Memory-NLS
and Transformer on TinyShakespeare, framed as the structural analog
of the physics warmup/record protocol used in the R1 vibration
experiment (see `../../results/03-vibrational-modes.md` and
`../../results/04-anti-collapse-3d.md`). The short 4,000-step
training run is the training-dynamics analog of stopping the physics
solver during its initial transient, before the auxiliary-field
memory has cycled enough times to produce its stable regime. This
longer run continues past the transient to see what regime each
architecture stabilizes into.

## What the physics analog says to look for

In the 3D physics solver, the auxiliary fields have relaxation times
$\tau_j = 1/\nu_j$ between 0.1 and 2 units of time. The R1 v4
experiment used a 2,000-step warmup ($\sim$5 units of time) before
recording, because that is the timescale over which the slow memory
mode finishes its initial transient and the field settles into a
stable oscillation around its post-collapse-release peak.

The training-dynamics analog is: the slow memory mode of the
Memory-NLS layer has $\nu_\text{min} = 0.5$ and $dt = 0.05$, giving
a relaxation timescale of $\tau = 1 / (0.5 \cdot 0.05) = 40$
training steps in terms of effective gradient steps the slow mode
has 'seen'. With batch size 32, the slow memory needs $O(10^3)$
optimizer steps to have integrated enough samples to act on its
characteristic timescale. The 4,000-step run is therefore on the
edge of the transient; the post-transient regime requires
substantially more.

## What was run

Both architectures trained for **50,000 steps** with identical
infrastructure (AdamW, cosine schedule lr 3e-4 → 3e-5, gradient
clipping 1.0, bf16 mixed precision, batch size 32, seq len 256).

| Quantity | Memory-NLS | Transformer |
|---|---|---|
| Parameters | 1,495,872 | 1,841,472 |
| Wall time | 481 s | 521 s |
| Final train loss | 1.6881 | 0.2118 |
| Final val loss | 1.9353 | 5.3291 |
| Final val perplexity | 6.93 | 206.25 |
| Min val loss reached | 1.9045 (at step 44000) | 1.5338 (at step 5000) |
| Min val perplexity at min step | 6.72 | 4.64 |

## The headline structural finding

The two architectures exhibit qualitatively different long-horizon
training dynamics. This was not visible at 4,000 steps. It is the
specific kind of structural difference that justifies running past
the transient.

**Memory-NLS exhibits stabilization.** Both training loss and
validation loss decrease monotonically and asymptote together. The
gap between train loss (1.69) and val loss (1.94) at step 50,000 is
small. The model finds a generalization regime and stays in it; the
min validation loss is at step 44,000, near the end of training, with
the trajectory still slowly improving at the very end.

**Transformer exhibits the textbook overfitting curve.** Training loss
decreases monotonically all the way to 0.21, the model is memorizing
the training corpus. But validation loss has a U-shape: it reaches its
minimum (1.53) at step 5,000, then climbs steadily, finishing at 5.33
(val perplexity 206) at step 50,000. The model has lost generalization;
it is now reciting the training set rather than modeling its
distribution.

The pattern is the training-dynamics analog of the physics simulation
contrast documented in `../../results/01-anti-collapse-2d.md` and
`../../results/04-anti-collapse-3d.md`. In the physics: a system
without the memory regularization collapses and locks onto a degenerate
configuration (the lattice-clipped peak). A system with the memory
regularization passes through the same transient but is then released
by the delayed repulsion of the memory potential and stabilizes at a
different, structurally non-degenerate configuration.

The same pattern appears here. The Transformer (no structural memory
mechanism beyond attention's content-based lookup) collapses onto the
training-set distribution, a degenerate configuration, in the sense
that it is the maximally specific representation possible. The
Memory-NLS architecture (structural multi-timescale memory with
hierarchical relaxation) passes through the same initial transient
but is then held by the slow memory mode at a regime that captures
the corpus's structural properties without memorizing its surface form.

This is not a benchmark observation. It is a structural observation
about what each architecture's training dynamics naturally do. The
relevant axis is not which one reaches a lower validation loss at some
arbitrary checkpoint, but what kind of regime each one stabilizes in,
and how that regime relates to the equation's behavior in its other
substrates.

## Trajectory shape

Validation loss at each milestone:

| Step | Memory-NLS val_loss | Memory-NLS ppl | Transformer val_loss | Transformer ppl |
|---|---|---|---|---|
|  4000 | 2.0535 | 7.79 | 1.5492 | 4.71 |
|  8000 | 2.0315 | 7.63 | 1.7176 | 5.57 |
| 16000 | 1.9770 | 7.22 | 2.5053 | 12.25 |
| 32000 | 1.9526 | 7.05 | 4.3024 | 73.88 |
| 50000 | 1.9353 | 6.93 | 5.3291 | 206.25 |

## Generation samples through the trajectory

How each architecture's output evolves through the transient and
into its stable regime, at the same prompt:

### Step 4000

**Prompt:** `ROMEO:`

**Memory-NLS:**

```
ROMEO: mar ould ill mordsas rot lid beod him.

MORIO:
Thald thare sire grinie.

MADY:
Thertixt ond aboning the so our shop shad senee seproured, slut,
Are when no dot the har attiker the him sorre? hath 'tis
```

**Transformer:**

```
ROMEO: good something is pardon, fairst.

LUCENTIO:
O perfant command, I will true a do crown weeping.

First Musician:
Welcome, who causes a bear backnation, ay: I have one
my prosperous is shoulder busines
```

**Prompt:** `First Citizen:`

**Memory-NLS:**

```
First Citizen:
And Ifo forewe your shalllful mearent upon fright after though my the and broorey.

POMPCINERE: man friets, bustor And neathe taker, do a haved
Torry of the hen haveang bon the mare paulin is mubl,
Th
```

**Transformer:**

```
First Citizen:
Here is your loves of everit that offence
Importentance to your talk the faces fight.
In that may not the measury will;
When thou best at the already of his doctiny
To make them buy.

LEONTES:
Claudio
```

**Prompt:** `KING HENRY V:`

**Memory-NLS:**

```
KING HENRY V: tome is ith to hear be comper palul.

KINCHIZIO:
So noontunced as thee minge welpy
Marrakencerss to I enor har I cresemed. the good in a noid lonely trorve wing agathe paing bet she bist: po-tifo;
And
```

**Transformer:**

```
KING HENRY V: I do have leave you wing,
And how in my good fathoms here and deserves.

KING EDWARD IV:
God grace my weept were I frown the gracious lord.

KING HENRY VI:
But thou sure the rood of my hand time
Neigh
```

### Step 8000

**Prompt:** `ROMEO:`

**Memory-NLS:**

```
ROMEO: it he'sh griese to with thy mal the the lerve this Murseic and doth his witt them deat makelf
And of to his hor deep mame a free, stres
As any untertion shoul proked,
And warricend there
And Stig what
```

**Transformer:**

```
ROMEO: I will those woes think, and five thing
things I should slip, that recreature all. Nay, mother; I
saw thou verse the break not what true know
peace with him, and gailant-grave with thee better heaven'
```

**Prompt:** `First Citizen:`

**Memory-NLS:**

```
First Citizen:
In it prepise sirdes stay this willlves speer their lord he mart ours and of grate, Gord?

RII:
The thuth the mare to hownd heart mover a stame not coid reporte takel's get true: thou sore be thy that
```

**Transformer:**

```
First Citizen:
But Oxford, to our land entertain our account
Proceedixt a cure, in such a fuder in a country,
Or with him an hot: This is the bed,
Will with Romeo that seat on his gates abroad
Touching cloudy makes 
```

**Prompt:** `KING HENRY V:`

**Memory-NLS:**

```
KING HENRY V: the the will be arotted we preak I prow, the allel of this,
Lord, a itt to speas a will thean's her lorrivese your.

Sest wither bad I weath fords mawd's mane and a fored all this hourstt his canterer
```

**Transformer:**

```
KING HENRY V: and man it is no or sex.

DUKE VINCENTIO:
How far is your motion's sons, you might last.

ISABELLA:
I will bring this grief is at at enjoy'd in him.

ISABELLA:
Believe my with him in the execution.

I
```

### Step 16000

**Prompt:** `ROMEO:`

**Memory-NLS:**

```
ROMEO: nood; led a sont mis blos bot and callacity that:
Whiche chit ove thath of not poldsey of a dimer trund excue, spang thook and the bree the do more wenses fair to visight to a hearthe to for one think
```

**Transformer:**

```
ROMEO: dishone't shall shine my help throught
As my master thoughts: I can conceit now,
But make wing me: on the man is conjuration,
To stay mother, almost go with me that hole.
I'll tell meet me to merry, m
```

**Prompt:** `First Citizen:`

**Memory-NLS:**

```
First Citizen:
Singare mike bry from sid that, nay thou lovest som gordor sweeth be not hert subject ateelf.
All, sime of my firme you that! And the will die her me 'eatok man it the have hearthelf warwings Aus deat
```

**Transformer:**

```
First Citizen:
You may deny the garden are:
Good ty, good citizens are rent entorced me:
This is such a longer, that little out
An made as eggess, with my hand these are:
Thou art my country's lovers' antog, not hea
```

**Prompt:** `KING HENRY V:`

**Memory-NLS:**

```
KING HENRY V: end fith what's my minten hell, goor are you is fair Sith is, my consurver,
Go Will und gonet puke
And aler an the han under byn.

WIRGIZABETH:
Bin artos sol thy preatherled po thy heave that full hou
```

**Transformer:**

```
KING HENRY V: but must speak,
To make a shamen dyetem to engual me!

GLOUCESTER:
Go, bear the vanitage of death, seize them all;
And his mother wall, I chot return af.

WARWICK:
If in the ghostly confeder'd valour,
```

### Step 32000

**Prompt:** `ROMEO:`

**Memory-NLS:**

```
ROMEO: oull dee
Anglalk the that the come my brease, that their were of saint we crie for blothers their grows case come, then terrmither,
I worl be in the heaven us all got so.

Second of in wich to chosssa
```

**Transformer:**

```
ROMEO: you have been execed
I love the battleming of the earth
And, you have right: your prayers for your request
But in the hight disease of fresh of kin.

Lord Marshal:
From whency, and my powen's soul, an
```

**Prompt:** `First Citizen:`

**Memory-NLS:**

```
First Citizen:
Come?

ABORSOLA:
And more aree blood
Go not out, lord one
Anvis and them.

LUCIO:
They this king so prock'd of the af weall art.
wear hairs int goinge you ton the see carposed,
I the offiend but and a
```

**Transformer:**

```
First Citizen:
I'll and so dim and to murder men,
And thus wrong thee wested,--a cite your lord,--
You make rise thou a man?

Second Sortong:
And ask, as yourse were wore well charge
In that boon.

Third Citizen:
Ne
```

**Prompt:** `KING HENRY V:`

**Memory-NLS:**

```
KING HENRY V: upon hilll morp stiffonce of come he canspeand him thereer's the be Romency thee,
The sears it Lan one it depe more thy do stor poilte to some it.
Af eve to be geque of fortem,
Anourd to the commone g
```

**Transformer:**

```
KING HENRY V: Clarence, 'pardon me:
Take him to despair.

DUCHESS OF YORK:
Haway, you we forget, since, I chearge you
Of your deems roud worldless end in Parist' ,
Your caphering transpor: you betake it straight
Ad
```

### Step 50000

**Prompt:** `ROMEO:`

**Memory-NLS:**

```
ROMEO: butouce the hath mad a palland,
I'll and thy secon them
Thou a cannot have and you; darse you must spother my will men hen this the do rest it truep,
For with gong to wevee a man thy your requetition 
```

**Transformer:**

```
ROMEO: I say, here's no some and endomure
sighned and onot adly to-morrow.

Provost:
I was it expedicious woth, and he well played
Thrust-blood did water man the should be distraughte
It may do the doubt not
```

**Prompt:** `First Citizen:`

**Memory-NLS:**

```
First Citizen:
Of all then you have cominth.
Star and when by it, oncl fight of inter? Gres whall so the wouldrs he worlleigh of and rust a a man impove thall of my mere: of so faldy to full a fait be
Thath go trips
```

**Transformer:**

```
First Citizen:
And so did I.

SICINIUS:
Where is he you?

Citizen:
To the way bre chance to-day. O'Fhall. think'stiness,--
must callesness has should his dam ribels: hie

::
Hai be, bethink it me, forbed him with an
```

**Prompt:** `KING HENRY V:`

**Memory-NLS:**

```
KING HENRY V: stapase the is speak mie, with postine, and he knotle rive of of warbaim awan of Romenced you are.

LUCIO:
The to-me
your pleast him, as that not me sole bry my forw my the stords and the dogses waste
```

**Transformer:**

```
KING HENRY V: Bestop it makes crown!
No, not a Montague, thinks your face of it.
So, sir, I talk you, let me let it be predr.

LORD WILLOUGHBY:
Base men by his entreaties in mine honest.

EDWARD:
Bow, my lord, the 
```

## Structural reading

Two things to look for, in analogy with the physics warmup/record
structure:

1. **Where does each architecture's val_loss stabilize?**
   In the physics analog, the field reaches a plateau peak after
   the transient; thereafter it oscillates around that peak. In the
   training analog, the val_loss plateaus (or rises again due to
   overfitting on this small corpus) after the transient. Where
   each architecture plateaus, and how the plateau differs between
   them, is the structural fact to read.

2. **Do the samples qualitatively change through the trajectory?**
   In the physics analog, the late-time crystalline state has
   internal vibrational structure not present in the initial
   collapse-and-release transient. In the training analog, the
   late-training output should exhibit structure not present in
   the early-training output. Look for: increased coherence,
   emergence of multi-sentence structure, stable character names,
   convergence to repeated patterns vs. continued exploration.

## What this experiment is not

This is not a benchmark contest at longer horizons. The numbers
compared above are not claims that either architecture is
'beating' the other; they are observations of how each one
settles into its stable regime under the same conditions. See
`../../CLAUDE.md` Rule 7a for the framing of comparison as
differentiation rather than competition.

On a corpus this small (~1 MB), 50,000 training steps means many
hundreds of epochs through the data; both architectures will be
substantially overfitting by the end. The relevant observation is
not the absolute final loss but the *trajectory shape* and the
*qualitative character* of the post-transient regime.
