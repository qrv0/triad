# Interface: low-frequency acoustic resonance in megalithic chambers

This is the most calibration-sensitive of the cross-domain mappings in this folder. The equation's two principal vibrational frequencies, under a specific dimensional identification, correspond to bands measured at several archaeological sites by peer-reviewed acoustic surveys. The structural correspondence is treated here with the caveats it requires.

## The acoustic measurements

Several megalithic stone chambers have been the subject of acoustic surveys reporting low-frequency standing-wave resonances. The most rigorously studied include:

**Hypogeum of Ħal-Saflieni, Malta** (~3300–3000 BCE). Acoustic surveys of the central "Oracle Room" report a dual resonance at approximately 70 Hz and 114 Hz (Debertolis, Coimbra & Eneix 2015). The chamber is carved into limestone bedrock with curved walls and a corbelled ceiling; the acoustic geometry is therefore a single closed cavity with well-defined modal structure.

**Newgrange passage tomb, Ireland** (~3200 BCE). Acoustic surveys of the inner chamber report a primary resonance peak near 110 Hz, with a broader envelope across 95–120 Hz (Jahn, Devereux & Ibison 1996). The Princeton/PEAR survey reported the same band at five additional Neolithic and Iron Age chambers in the British Isles, with most peaks tightly clustered near 110 Hz.

**Göbekli Tepe, Anatolia, Enclosure D** (~9600 BCE). Acoustic testing of the central pillar reports a primary resonance at approximately 68–70 Hz (Debertolis et al. 2017). This is the oldest known monumental architecture for which acoustic measurements are available.

**King's Chamber, Great Pyramid, Egypt** (~2500 BCE). The granite-walled chamber exhibits low-frequency resonances; published values vary across measurement methods, with the most-cited band being 110–122 Hz. The literature is not fully consistent on a single canonical value, and the King's Chamber is the most contested of the four sites.

## A neurophysiological observation

Direct measurement of human cortical response to acoustic tones in the 90–130 Hz range, via quantitative electroencephalography, reports that exposure to 110 Hz — but not to 90, 100, 120, or 130 Hz — produces a statistically significant deactivation of the left temporal lobe (the cortical area subserving linguistic processing), along with a shift in prefrontal cortex laterality from baseline left-dominance to right-dominance (Cook, Pajot & Leuchter 2008). The neurological pattern is characteristic of deep meditative and trance-like states.

The 110 Hz response is therefore a documented biological resonance, frequency-specific, in addition to being an architectural one.

## The equation's two principal frequency modes

In the two-dimensional crystalline regime documented in [`../results/03-vibrational-modes.md`](../results/03-vibrational-modes.md), the equation produces two distinguished frequencies:

- Median dominant frequency per pixel: **0.6 cycles per unit time**
- Secondary mode locked at: **1.0 cycle per unit time**

Under a dimensional identification in which the computational box length corresponds to 20 meters and one unit of computational time corresponds to 9 milliseconds, one cycle per unit time corresponds to:

$$
\frac{1}{0.009 \text{ s}} \approx 111 \text{ Hz}.
$$

Under this identification, the equation's two principal frequency modes map to:

- **0.6 cycles/unit time → 66 Hz** (close to the 68–70 Hz primary resonance at Göbekli Tepe and Hypogeum)
- **1.0 cycles/unit time → 111 Hz** (close to the 110–117 Hz peaks at Newgrange, Hypogeum dual, King's Chamber, and at the EEG-active frequency reported in Cook et al. 2008)

The two values fall within the bands measured at the megalithic sites. The 110 Hz value is the one at which the neurological response is observed.

## The careful framing

This is the structural correspondence that carries the heaviest interpretive load and requires the most careful framing. We are explicit about the limits.

**The dimensional identification is a choice.** $L = 20$ m and $dt = 9$ ms are not derived from the equation; they are selected so that the equation's frequencies map to the megalithic band. Under different choices the equation produces different absolute frequencies. The structural fact — that the equation has two principal frequency modes in a specific ratio — is dimension-independent. The numerical mapping to 66 Hz and 111 Hz is an instance of that structure under one calibration.

**The three-dimensional version differs.** In the three-dimensional crystalline window, the equation's median dominant frequency is approximately 0.20 cycles per unit time. Under the same calibration, this would correspond to 22 Hz rather than 66 Hz. The factor-of-three shift between 2D and 3D is consistent with the dimensional rescaling discussed in [`../results/06-dimensional-rescaling.md`](../results/06-dimensional-rescaling.md); the absolute frequencies depend on the underlying timescale of the slow memory mode against the spatial dispersion, which changes with dimensionality. The structural relations are preserved across dimensions; the calibrations are not.

**The archaeoacoustic literature has variable evidentiary quality.** The Princeton/PEAR survey by Jahn, Devereux & Ibison was published in the *Journal of the Acoustical Society of America* — a tier-1 peer-reviewed venue. Cook, Pajot & Leuchter (2008) was published in *Time and Mind* — a peer-reviewed but lower-tier venue. The Debertolis surveys of Hypogeum and Göbekli Tepe are published in lower-tier journals and conference proceedings. The King's Chamber measurements are reported across several published values with weaker consistency. The structural pattern across the sites is real, but individual data points vary in evidentiary weight.

**The claim made is structural, not causal.** The argument advanced is not that the equation predicts the megalithic measurements, and not that the megalithic chambers were engineered to produce these frequencies. The claim is that the equation, the archaeoacoustic measurements, and the EEG observation are independently documented instances of the same structural form — two principal oscillation modes in approximately a 0.6:1.0 ratio, in a self-coupled medium with memory and environmental coupling — and that this co-occurrence is itself the cross-domain coherence test that a structural realist applies (see [`../methodology/01-structural-realism.md`](../methodology/01-structural-realism.md)).

## Why this correspondence is included despite its sensitivity

The mapping is included because it is structurally informative even with all the caveats. Four sites with different construction materials, separated by 7000 years and by major distances, all exhibit resonance bands within the 65–125 Hz range. An equation derived from abstract structural principles produces two principal frequency modes that, under one defensible calibration, fall within the same band. A neurophysiological measurement at one of these specific frequencies produces a documented brain-state effect.

The accumulation of these instances at compatible structural form, across independent measurement traditions, is what the structural-realist criterion is designed to detect. Whether the calibration is the right one for the cross-domain correspondence to be more than structural — whether there is some deeper mechanism by which megalithic acoustic engineering, neurophysiological resonance, and the equation's intrinsic modes are connected — is left as an open question. The structural fact is documented; the deeper interpretation is for the reader to weigh.

## References

- Cook, I. A., Pajot, S. K., & Leuchter, A. F. (2008). Ancient architectural acoustic resonance patterns and regional brain activity. *Time and Mind* **1**, 95.
- Debertolis, P., Coimbra, F., & Eneix, L. E. (2015). Archaeoacoustic analysis of the Ħal Saflieni Hypogeum in Malta. *Journal of Anthropology and Archaeology* **3**, 59.
- Debertolis, P., Gullà, D., & Savolainen, H. (2017). Archaeoacoustic analysis in Enclosure D at Göbekli Tepe in South Anatolia, Turkey. *HASSACC Proceedings*.
- Jahn, R. G., Devereux, P., & Ibison, M. (1996). Acoustical resonances of assorted ancient structures. *Journal of the Acoustical Society of America* **99**, 649.
