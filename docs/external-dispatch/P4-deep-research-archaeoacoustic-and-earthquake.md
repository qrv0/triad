# Deep research query frame: archaeoacoustic + earthquake-cycle data collation

**Target:** Deep research agent (Anthropic, Perplexity, or similar literature-mining tool with strong primary-source retrieval). Two independent queries; can be dispatched in parallel.

**Output integration:** the returned data will be integrated into the repository by the structural-research-mode-active main agent, who will write or update specific interface and result documents per the structural-realist methodology. The deep research output should be primary-source data with provenance, not interpretation.

---

## Query 1: Archaeoacoustic spectra at non-Hypogeum megalithic chambers

### Context for the search

The interface [`interfaces/05-archaeoacoustic-resonance.md`](../../interfaces/05-archaeoacoustic-resonance.md) claims a structural correspondence between the equation's two-mode vibrational structure (median 0.6 cycles per unit time, secondary 1.0) and the band the rigorous-floor archaeoacoustic literature measures at megalithic stone chambers. Under one defensible calibration (L = 20 m, dt = 9 ms), the two modes map to 66 Hz and 111 Hz physical.

The rigorous-floor sources currently cited:
- Till (2017) *Antiquity* 91(355): 74-89, Hypogeum of Ħal-Saflieni swept-sine ISO 3382-1 measurements (Oracle Chamber primary resonances at 41, 72, 76, 134, 161, 186, 196 Hz)
- Wolfe, Swanson, Till (2020) *Journal of Archaeological Science: Reports* 34: 102623, 3D wave-equation simulation of Hypogeum
- Jahn, Devereux, Ibison (1996) *Journal of the Acoustical Society of America* 99(2): 649-658, cross-site survey of six British/Irish chambered tombs (Newgrange ~110 Hz, Wayland's Smithy ~119 Hz, Chun Quoit ~110 Hz, Cairn Euny ~110 Hz, Cairn L ~114 Hz, Cairn I unspecified; 25 Hz spread across sites)
- Watson, Keating (1999) *Antiquity* 73: 325-336, Newgrange and Maeshowe Helmholtz and standing-wave measurements (1-7 Hz Helmholtz modes tracking inversely with chamber volume)
- Cox, Fazenda, Greaney (2020) *Journal of Archaeological Science*, Stonehenge scale-model simulation

The relevant prediction P5.3 (whole-tone scale) was assigned **partial** status in [`results/23-hypogeum-spectrum-audit.md`](../../results/23-hypogeum-spectrum-audit.md): the Hypogeum spectrum from Wolfe-Swanson-Till 2020 (9 peaks at 37.2, 41.0, 46.1, 50.4, 57.1, 64.3, 72.7, 81.8, 92.5 Hz with consecutive ratio ~1.122 = whole-tone scale) is partially consistent with the equation's two-mode prediction but not cleanly reproduced.

The current 3D vibrational extension at d=3 ([`results/25-vibrational-modes-3d.md`](../../results/25-vibrational-modes-3d.md)) yields a cascade structure (dominant 0.125, 0.225, 0.325, 0.425, 0.525 cycles per unit time) that does not cleanly produce the whole-tone-scale either.

To advance P5.3 from **partial** to a testable cross-chamber prediction, we need higher-resolution acoustic spectra from non-Hypogeum chambers measured with methodology comparable to the Wolfe-Swanson-Till 2020 standard (3D wave-equation simulation OR ISO 3382-1 swept-sine impulse-response with peer-reviewed publication).

### The data needed

For each of the following sites (or others fitting the same methodological floor), retrieve from peer-reviewed primary sources:

(a) Resonance frequencies (peaks in the impulse-response spectrum, or computed room-mode eigenfrequencies from laser-scanned geometry), with sufficient resolution to identify consecutive-ratio structure (target: 9 or more peaks listed individually below 200 Hz, OR a structured spectrum from which 9 peaks can be extracted).

(b) Measurement methodology (swept-sine impulse-response, vocal excitation, scale-model wave-equation simulation, computed room-mode eigenvalues from laser-scanned geometry).

(c) Chamber geometry (volume, dimensions, lining material if relevant).

(d) Publication venue (peer-reviewed tier-1 preferred; conference proceedings acceptable if methodology meets the swept-sine ISO standard; predatory/single-laboratory venues flagged).

### Specific sites to retrieve (in order of priority):

1. **Mnajdra Temples, Malta** (companion to Hypogeum; same period; same builder culture; should be a clean test of the cross-chamber prediction)
2. **Tarxien Temples, Malta** (same culture)
3. **Maeshowe, Orkney** (Watson-Keating 1999 has some data; check for higher-resolution follow-up)
4. **West Kennet Long Barrow, England**
5. **Camster Cairns, Scotland**
6. **Carbane West cairns, Ireland**
7. **Knowth and Dowth passage tombs, Ireland** (companion to Newgrange in the Brú na Bóinne complex)
8. **Bryn Celli Ddu, Wales**
9. **La Hougue Bie, Jersey**
10. **Cueva de Menga, Spain**

For each: does a peer-reviewed acoustic measurement exist? With what resolution? Is the geometry-driven room-mode prediction available (laser-scanned or photogrammetric)? Can we extract a 9-or-more-peak spectrum below 200 Hz?

### Specific question to answer

Does the consecutive-ratio whole-tone-scale pattern (1.122 ratio between consecutive peaks) appear at any non-Hypogeum chamber, or is it specific to the Hypogeum geometry?

If it appears across multiple chambers: the equation's structural claim (two-mode ratio in 0.6:1.0 range, dimension-independent) is strengthened by the cross-chamber invariance of the ratio structure.

If it appears only at the Hypogeum: the whole-tone-scale is a chamber-specific artifact of the Hypogeum geometry; the equation's prediction is the two-mode-ratio structure, which is dimension-independent, not the specific whole-tone consecutive-ratio pattern.

Either finding is structurally informative; the question is empirical.

### Format of expected output

Per site, return:
- Site name and location
- Primary source (full citation; DOI if available)
- Methodology (one-line description)
- Spectrum (list of frequency peaks in Hz, ideally below 200 Hz)
- Chamber geometry (volume in m³, dominant dimensions, lining material)
- Quality flag (rigorous floor / acceptable / methodologically weak / not retrievable)

If a site has no peer-reviewed acoustic measurement: state so. Do not invent or extrapolate.

If multiple measurements exist for one site: list all, with priority to the more rigorous methodology.

---

## Query 2: Earthquake-cycle recurrence variance vs Maxwell-time dataset

### Context for the search

The interface [`interfaces/22-earthquake-cycle.md`](../../interfaces/22-earthquake-cycle.md) (added 2026-05-16) places the seismic cycle as a nonlinear-relaxation-oscillation instance of the equation's P1+P2+P3 triangle at geophysical scale.

The relevant prediction P22.1: **Recurrence-interval distributions scale with the Maxwell-time / recurrence-time ratio in the predicted way.** The equation's structural form predicts that the variance in recurrence intervals decreases as the slow-memory timescale (mantle Maxwell time) approaches the recurrence interval. Fault systems with $T_{\text{Maxwell}} \ll T_{\text{rec}}$ should have more variable recurrence; systems with $T_{\text{Maxwell}} \sim T_{\text{rec}}$ should have more regular recurrence.

The relevant rigorous-floor literature:
- Erickson, Birnir, Lavallée (2008) on relaxation oscillations in earthquake cycles
- Heimisson, Segall (2018) on rate-state-friction cycles
- Cattania, McGuire, Collins (2019) on multi-patch fault complexity
- Pollitz (1997) on viscoelastic postseismic relaxation
- Bürgmann, Dresen (2008) review of mantle Maxwell times

The status of P22.1 is **not_yet_tested**: the test would require a cross-fault dataset of (recurrence-interval distribution, mantle Maxwell time) pairs for a sufficient number of fault systems to detect the predicted scaling.

### The data needed

For each major fault system with documented recurrence history, retrieve from peer-reviewed primary sources:

(a) Recurrence interval distribution (mean, std, coefficient of variation; OR full distribution if available; OR paleoseismic event list with dated event sequence).

(b) Mantle Maxwell time estimate for the region (from geodetic postseismic relaxation modeling, or from regional rheological models, or from inferred lower-crust/upper-mantle viscosity).

(c) Loading rate (tectonic strain accumulation rate, mm/yr).

(d) Fault system type (subduction zone megathrust, continental transform, normal/extensional, complex network).

### Specific fault systems to retrieve (in order of priority):

1. **Cascadia subduction zone** (~500 yr recurrence; mantle Maxwell time well-characterized by GPS postseismic)
2. **San Andreas Fault, California** (~150-200 yr recurrence for Big Bend section)
3. **North Anatolian Fault, Turkey** (~250 yr recurrence; well-documented sequence of 20th-century events)
4. **Sumatra-Andaman megathrust** (~500-1000 yr recurrence; recent 2004 event well-characterized)
5. **Nankai Trough, Japan** (~100-150 yr recurrence; multi-segment with documented historical events back to 684 CE)
6. **Wasatch Fault, Utah** (continental normal fault, ~1000-2000 yr recurrence)
7. **Hayward Fault, California** (~140-170 yr recurrence)
8. **Alpine Fault, New Zealand** (~330 yr recurrence)
9. **Dead Sea Transform, Israel-Jordan** (paleoseismic record)
10. **Andaman Sea / Sagaing Fault, Myanmar** (continental transform with Maxwell-time variability across the strike)

For each: does a peer-reviewed recurrence interval distribution exist (paleoseismic dataset)? Does a peer-reviewed Maxwell-time estimate exist (geodetic postseismic modeling)? Are both for the SAME fault segment?

### Specific question to answer

For the fault systems where both (recurrence-interval distribution) and (Maxwell-time estimate) are available, what is the relationship between the coefficient of variation of recurrence intervals and the ratio $T_{\text{Maxwell}} / T_{\text{rec}}$?

The equation's structural prediction is monotonic: as $T_{\text{Maxwell}} / T_{\text{rec}} \to 1$, the coefficient of variation of recurrence intervals should decrease (memory carries over, recurrence is more regular). As $T_{\text{Maxwell}} / T_{\text{rec}} \to 0$, the coefficient of variation should increase (memory has fully relaxed, recurrence is more variable, Poisson-like).

If the data shows the predicted monotonic trend across the available fault systems: P22.1 is evaluated as tested_consistent under criterion 4.

If the data shows no relationship or the opposite trend: P22.1 is evaluated as partial (variance dominates effect at the available cross-fault N) or tested_inconsistent (effect > variance in the wrong direction).

### Format of expected output

Per fault system, return:
- Fault name and location
- Recurrence interval data: mean (yr), std (yr), coefficient of variation, source citation, methodology (paleoseismic / instrumental / historical)
- Mantle Maxwell time: value (yr), source citation, methodology (geodetic / petrologic / inferred)
- Loading rate (mm/yr) and source
- Quality flag (rigorous floor / acceptable / methodologically weak / not retrievable)
- The ratio $T_{\text{Maxwell}} / T_{\text{rec}}$ computed from the cited values

If a fault has no peer-reviewed recurrence distribution: state so. Do not invent or extrapolate.

If multiple Maxwell-time estimates exist for one region: list with priority to geodetic-postseismic-modeling-derived values (most direct measurement of the relaxation timescale).

---

## Output format note

The deep research output for both queries should be primary-source data with provenance. The repository will integrate the results by:

- Query 1 output → updates to [`interfaces/05-archaeoacoustic-resonance.md`](../../interfaces/05-archaeoacoustic-resonance.md) and a new [`results/29-cross-chamber-spectrum-audit.md`](../../results/29-cross-chamber-spectrum-audit.md) or similar
- Query 2 output → updates to [`interfaces/22-earthquake-cycle.md`](../../interfaces/22-earthquake-cycle.md) and a new [`results/30-recurrence-variance-vs-maxwell-time.md`](../../results/30-recurrence-variance-vs-maxwell-time.md) or similar

The deep research should NOT write methodology framing or interpretive language; that integration is the main agent's job. The deep research should return the data with provenance and the quality flag, no more.
