"""One-shot helper script (NOT a mkdocs hook): writes YAML frontmatter
to each interface markdown file. Run once per file-set; subsequent
edits to frontmatter are made directly in the interface files.

Usage:
    cd <repo-root>
    python hooks/_apply_frontmatter.py
"""

from pathlib import Path

# Per-interface frontmatter content. The triangle phrases compress each
# interface's P1/P2/P3 instantiation into one short clause. Status fields
# reflect the state as of the methodology-cleanup completion (commit
# 34a1765, 2026-05-16); pending predictions remain "not_yet_tested".

FRONTMATTER = {
    "01-other-nls-systems": {
        "title": "Interface 01: Other instances of NLS dynamics",
        "description": (
            "Optical solitons, BECs, surface gravity waves, plasma "
            "Langmuir oscillations all instantiate the memory-augmented "
            "NLS form."
        ),
        "domain": "physics",
        "triangle": {
            "p1": "envelope oscillation of the underlying carrier wave",
            "p2": "nonlinear self-interaction plus dispersive / memory kernel",
            "p3": "loss + gain (Raman, thermal cloud, bottom friction, "
                  "electron-ion collisions)",
        },
        "signature_icon": "wave",
        "hero_tier": "B",
        "related": [2, 3, 7],
        "predictions": [
            {"id": "P1.1", "short": "Memory-augmented soliton stability "
             "scales with Raman timescale ratio",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P1.2", "short": "BEC anti-collapse threshold scales "
             "with non-condensate-cloud temperature",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P1.3", "short": "Surface-wave Benjamin-Feir threshold "
             "shifts with bottom-friction memory",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "02-baryon-acoustic": {
        "title": "Interface 02: Baryon acoustic oscillations",
        "description": (
            "Pre-recombination plasma acoustic waves froze a 150 Mpc "
            "characteristic scale into matter distribution; the "
            "equation's memory-modulated wave dynamics predicts "
            "specific corrections."
        ),
        "domain": "cosmology",
        "triangle": {
            "p1": "photon-baryon plasma sound waves",
            "p2": "baryon inertia plus radiation pressure memory",
            "p3": "photon-baryon Thomson scattering coupling",
        },
        "signature_icon": "horizon",
        "hero_tier": "B",
        "related": [7, 1, 3],
        "predictions": [
            {"id": "P2.1", "short": "BAO peak position correction "
             "scales with memory-kernel timescale at recombination",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P2.2", "short": "Secondary BAO peaks show "
             "memory-modulated harmonic structure",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P2.3", "short": "Phase shift in BAO ringing "
             "detectable in DESI/LSST data",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "03-chladni-cymatics": {
        "title": "Interface 03: Chladni cymatics and Faraday waves",
        "description": (
            "Sand-on-plate nodal patterns and Faraday-wave surface "
            "patterns instantiate the equation's spontaneous "
            "symmetry selection."
        ),
        "domain": "acoustics",
        "triangle": {
            "p1": "driven elastic plate or fluid-surface oscillation",
            "p2": "nonlinear mode-coupling plus pattern memory",
            "p3": "driving piston + air damping + viscous dissipation",
        },
        "signature_icon": "pattern",
        "hero_tier": "B",
        "related": [5, 2, 1],
        "predictions": [
            {"id": "P3.1", "short": "Symmetry selection probability "
             "scales with memory timescale at fixed drive",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P3.2", "short": "Pattern stability scales with "
             "drive amplitude in the predicted regime",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P3.3", "short": "Multiple symmetries coexist in "
             "the bistable regime predicted by memory hysteresis",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "04-gamma-entrainment": {
        "title": "Interface 04: Gamma entrainment and broadband absorption",
        "description": (
            "Cortical 40 Hz GENUS protocol and broadband neural "
            "absorption match the equation's released crystalline "
            "regime with multi-timescale memory."
        ),
        "domain": "neuro",
        "triangle": {
            "p1": "neuronal-population gamma-band oscillation",
            "p2": "multi-timescale synaptic + glial memory hierarchy",
            "p3": "thalamocortical + vascular + glial environmental coupling",
        },
        "signature_icon": "brain-wave",
        "hero_tier": "B",
        "related": [9, 8, 12],
        "predictions": [
            {"id": "P4.1", "short": "Broadband absorption bandwidth "
             "scales with memory-mode hierarchy depth",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P4.2", "short": "Cortical regions with "
             "multi-timescale glia show stronger GENUS response",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P4.3", "short": "GENUS amyloid-clearance kinetics "
             "follows the predicted memory-coupling pattern",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "05-archaeoacoustic-resonance": {
        "title": "Interface 05: Archaeoacoustic resonance at megalithic sites",
        "description": (
            "110 Hz and 70 Hz resonance across Hypogeum, Newgrange, "
            "Gobekli Tepe and the Pyramid King's Chamber match the "
            "equation's two principal vibrational modes."
        ),
        "domain": "archaeo",
        "triangle": {
            "p1": "chamber-mode acoustic oscillation",
            "p2": "stone-fluid resonance memory + acoustic boundary impedance",
            "p3": "air absorption + ground coupling + voice / drum drive",
        },
        "signature_icon": "chamber",
        "hero_tier": "C",
        "related": [3, 4, 9],
        "predictions": [
            {"id": "P5.1", "short": "Additional megalithic chambers "
             "resonate in the predicted 70-110 Hz band",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P5.2", "short": "EEG response outside 110 Hz "
             "predicted by the second principal mode at 66 Hz",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P5.3", "short": "Ratio of the two principal "
             "frequencies stays in the predicted band across chambers",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "06-state-space-models": {
        "title": "Interface 06: State space models (Mamba, RWKV, S4)",
        "description": (
            "The diagonal SSM update of S4 / Mamba / RWKV is term-by-"
            "term identical to the equation's auxiliary-field "
            "memory; the equation adds cubic + anti-collapse + "
            "FDT-locked noise."
        ),
        "domain": "engineering",
        "triangle": {
            "p1": "hidden-state oscillation across timesteps",
            "p2": "auxiliary-field memory hierarchy (diagonal SSM update)",
            "p3": "input projection + FDT-locked training noise",
        },
        "signature_icon": "ssm",
        "hero_tier": "A",
        "related": [8, 10, 9],
        "predictions": [
            {"id": "P6.1", "short": "FDT-locked noise reduces training "
             "trajectory variance vs ad-hoc noise schedules",
             "status": "not_yet_tested",
             "result_doc": "results/16-fdt-locked-noise-empirical-p3.md"},
            {"id": "P6.2", "short": "Optimization collapse boundary "
             "scales with model size as the cubic term predicts",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P6.3", "short": "Cubic state nonlinearity prevents "
             "SimSiam collapse without stop-gradient",
             "status": "not_yet_tested",
             "result_doc": "results/17-cubic-ssm-simsiam-fdt.md"},
        ],
    },
    "07-cosmological-expansion": {
        "title": "Interface 07: Cosmological expansion as mechanism-shape",
        "description": (
            "The full cosmic expansion trajectory (inflation, release, "
            "structure formation, late acceleration) instantiates the "
            "equation's anti-collapse mechanism shape."
        ),
        "domain": "cosmology",
        "triangle": {
            "p1": "scale-factor oscillation around expansion trajectory",
            "p2": "vacuum-energy / dark-energy memory of inflationary state",
            "p3": "radiation + matter coupling to the metric",
        },
        "signature_icon": "expansion",
        "hero_tier": "B",
        "related": [2, 1, 14],
        "predictions": [
            {"id": "P7.1", "short": "Late-time dark-energy equation of "
             "state shows V_mem-induced deviation from cosmological constant",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P7.2", "short": "Small-scale BAO substructure "
             "follows the equation's memory-modulated spectrum",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P7.3", "short": "Inflationary-era residual signal "
             "in tensor-to-scalar ratio matches anti-collapse profile",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "08-mechanistic-interpretability": {
        "title": "Interface 08: Mechanistic interpretability (attention)",
        "description": (
            "The empirical observation that attention-only architectures "
            "encode categorical structure as linear superpositions "
            "requiring post-hoc dictionary learning is what the equation "
            "predicts for an architecture instantiating P1 and P3 but "
            "missing P2's memory hierarchy."
        ),
        "domain": "engineering",
        "triangle": {
            "p1": "token-position attention oscillation",
            "p2": "MISSING in attention-only: no auxiliary-field memory hierarchy",
            "p3": "input embedding + residual stream coupling",
        },
        "signature_icon": "attention",
        "hero_tier": "C",
        "related": [6, 9, 4],
        "predictions": [
            {"id": "P8.1", "short": "Sparse autoencoder recovery rate "
             "scales with auxiliary-field count in modified architectures",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P8.2", "short": "Superposition density correlates "
             "inversely with explicit memory hierarchy depth",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P8.3", "short": "Polysemanticity decreases when "
             "Memory-NLS auxiliary fields are added to attention layers",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "09-critical-brain": {
        "title": "Interface 09: Critical brain (neuronal avalanches, 1/f)",
        "description": (
            "Cortical phase-transition phenomenology (power-law "
            "avalanches, 1/f spectra, broadband sensitivity) matches "
            "the equation's released crystalline regime."
        ),
        "domain": "neuro",
        "triangle": {
            "p1": "neuronal-population spiking oscillation",
            "p2": "multi-timescale synaptic / cellular / network memory",
            "p3": "sensory input + neuromodulatory + vascular coupling",
        },
        "signature_icon": "avalanche",
        "hero_tier": "B",
        "related": [14, 4, 8],
        "predictions": [
            {"id": "P14.1", "short": "Cortex shows multi-timescale "
             "memory hierarchy matching equation predictions",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P14.2", "short": "Neuronal avalanche statistics "
             "match equation predictions in matched-drive conditions",
             "status": "tested_consistent",
             "result_doc": "results/18-soc-vs-mnsm-matched-drive.md"},
            {"id": "P14.3", "short": "VIP-AQP4 cortical regions show "
             "predicted broadband absorption signature",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "10-kuramoto-synchronization": {
        "title": "Interface 10: Kuramoto synchronization with memory",
        "description": (
            "Memory-coupled phase oscillator ensembles instantiate "
            "the equation in its phase-only sector; chimera-state "
            "stability tracks the memory-timescale ratio."
        ),
        "domain": "complex-systems",
        "triangle": {
            "p1": "individual phase oscillator dynamics",
            "p2": "coupling-history memory kernel between oscillators",
            "p3": "FDT-locked phase noise + external drive",
        },
        "signature_icon": "phase-circle",
        "hero_tier": "A",
        "related": [13, 15, 12],
        "predictions": [
            {"id": "P10.1", "short": "Chimera-state lifetime peaks at "
             "tau_mem / tau_sync ~ 1",
             "status": "tested_consistent",
             "result_doc": "results/14-kuramoto-chimera-fdt.md"},
            {"id": "P10.2", "short": "Cardiac arrhythmia onset "
             "corresponds to the triangle's structural breakdown",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P10.3", "short": "Power-grid stability correlates "
             "with effective coupling memory in the predicted regime",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "11-immune-affinity-maturation": {
        "title": "Interface 11: Immune affinity maturation",
        "description": (
            "B-cell affinity maturation in germinal centers instantiates "
            "the triangle in a discrete-cell biological substrate with "
            "somatic hypermutation as the memory trace."
        ),
        "domain": "biology",
        "triangle": {
            "p1": "B-cell division-cycle plus clonal dynamics",
            "p2": "somatic hypermutation + clonal selection memory",
            "p3": "antigen environment + T-cell help coupling",
        },
        "signature_icon": "antibody",
        "hero_tier": "B",
        "related": [15, 16, 17],
        "predictions": [
            {"id": "P11.1", "short": "Memory-B-cell response amplitude "
             "scales with predicted timing of antigen exposure",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P11.2", "short": "Autoimmune disease classification "
             "maps to the triangle's structural failure modes",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P11.3", "short": "Affinity maturation kinetics "
             "correlates with memory-kernel timescale predictions",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "12-friston-free-energy": {
        "title": "Interface 12: Friston free-energy and active inference",
        "description": (
            "Predictive coding / free-energy minimization instantiates "
            "the triangle in a variational-dynamics substrate; the "
            "hierarchical generative model is P2's memory hierarchy."
        ),
        "domain": "complex-systems",
        "triangle": {
            "p1": "internal-state inferential dynamics",
            "p2": "hierarchical generative model + precision weights memory",
            "p3": "sensory observation + motor action coupling",
        },
        "signature_icon": "nested",
        "hero_tier": "C",
        "related": [4, 8, 10],
        "predictions": [
            {"id": "P12.1", "short": "Predictive-coding hierarchy depth "
             "correlates with structural memory-mode count",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P12.2", "short": "Hierarchical active-inference "
             "agent more stable than non-hierarchical equivalent",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P12.3", "short": "Cortical hierarchy structurally "
             "aligns with the equation's auxiliary-field hierarchy",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "13-active-matter": {
        "title": "Interface 13: Active matter (self-propelled particles, flocks)",
        "description": (
            "Self-propelled ensembles maintained by external energy "
            "injection instantiate the triangle; orientation memory "
            "is P2, energy injection is P3."
        ),
        "domain": "complex-systems",
        "triangle": {
            "p1": "individual particle motility-orientation dynamics",
            "p2": "alignment / orientation memory across particles",
            "p3": "external energy injection compensating dissipation",
        },
        "signature_icon": "flock",
        "hero_tier": "B",
        "related": [10, 14, 17],
        "predictions": [
            {"id": "P13.1", "short": "Active-crystal symmetry selection "
             "follows the equation's BCC pattern in the predicted regime",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P13.2", "short": "Flock-correlation length scales "
             "with predicted memory-coupling strength",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P13.3", "short": "Motility-induced phase separation "
             "shows broadband-absorption response",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "14-self-organized-criticality": {
        "title": "Interface 14: Self-organized criticality (avalanches)",
        "description": (
            "Drive-and-release systems organizing to a critical state "
            "instantiate the triangle; MNSM produces matching "
            "avalanche-statistics exponents in the coupled regime."
        ),
        "domain": "complex-systems",
        "triangle": {
            "p1": "stress / activity field accumulating toward threshold",
            "p2": "memory of past events tuning local stability",
            "p3": "external drive + dissipative release coupling",
        },
        "signature_icon": "avalanche-tumble",
        "hero_tier": "A",
        "related": [9, 13, 10],
        "predictions": [
            {"id": "P14.1", "short": "BTW-style critical exponents "
             "emerge in MNSM coupled-regime sweeps",
             "status": "tested_consistent",
             "result_doc": "results/18-soc-vs-mnsm-matched-drive.md"},
            {"id": "P14.2", "short": "MNSM avalanche-size distribution "
             "matches BTW reference under matched drive",
             "status": "tested_consistent",
             "result_doc": "results/18-soc-vs-mnsm-matched-drive.md"},
            {"id": "P14.3", "short": "Neuronal-avalanche universality "
             "class shared between cortex and MNSM critical regime",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "15-cardiac-dynamics": {
        "title": "Interface 15: Cardiac dynamics (pacemaker, alternans)",
        "description": (
            "Sustained cardiac rhythm instantiates the triangle; "
            "refractory-state memory is P2, autonomic + metabolic "
            "input is P3."
        ),
        "domain": "biology",
        "triangle": {
            "p1": "intrinsic depolarization-repolarization oscillation",
            "p2": "refractory-state and ion-channel memory",
            "p3": "ANS + hormonal + metabolic environmental coupling",
        },
        "signature_icon": "ecg",
        "hero_tier": "C",
        "related": [10, 11, 16],
        "predictions": [
            {"id": "P15.1", "short": "Cardiac alternans threshold "
             "scales with predicted memory-hierarchy depth",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P15.2", "short": "Clinical arrhythmia categories "
             "map to triangle structural failure modes",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P15.3", "short": "Heart rate variability spectrum "
             "matches the predicted multi-timescale decomposition",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "16-gene-regulation-circadian": {
        "title": "Interface 16: Gene regulation and circadian clocks",
        "description": (
            "Multi-timescale gene-expression patterns maintaining "
            "identity across cell division instantiate the triangle; "
            "chromatin + autoregulation are P2 memory."
        ),
        "domain": "biology",
        "triangle": {
            "p1": "transcriptional oscillation (circadian + others)",
            "p2": "chromatin-mark and autoregulatory-loop memory",
            "p3": "metabolic + hormonal + neural signaling coupling",
        },
        "signature_icon": "clock-helix",
        "hero_tier": "C",
        "related": [11, 15, 17],
        "predictions": [
            {"id": "P16.1", "short": "Circadian period robustness "
             "scales with regulatory hierarchy depth",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P16.2", "short": "Temperature compensation strength "
             "tracks the predicted memory-kernel pattern",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P16.3", "short": "Cell-cycle-circadian coupling "
             "follows the triangle's two-level integration",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
    "17-ecosystem-dynamics": {
        "title": "Interface 17: Ecosystem dynamics (multi-species)",
        "description": (
            "Sustained multi-species communities instantiate the "
            "triangle; age structure + trait inheritance are P2 memory; "
            "interspecies + abiotic coupling is P3."
        ),
        "domain": "biology",
        "triangle": {
            "p1": "intrinsic population-density dynamics (Lotka-Volterra-like)",
            "p2": "age structure + trait inheritance + ecological memory",
            "p3": "interspecies competition + abiotic environmental forcing",
        },
        "signature_icon": "trophic",
        "hero_tier": "B",
        "related": [13, 11, 16],
        "predictions": [
            {"id": "P17.1", "short": "Ecosystem diversity-stability "
             "tracks the predicted memory-coupling pattern",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P17.2", "short": "Age-structured populations show "
             "predicted memory-modulated stability vs unstructured",
             "status": "not_yet_tested", "result_doc": None},
            {"id": "P17.3", "short": "Regime-shift indicators correlate "
             "with the structural failure-mode predictions",
             "status": "not_yet_tested", "result_doc": None},
        ],
    },
}


def render_frontmatter(meta):
    """Render a YAML frontmatter block for one interface."""
    lines = ["---"]
    lines.append(f'title: "{meta["title"]}"')
    lines.append("description: >-")
    desc_text = meta["description"]
    # Wrap description at ~70 chars for readability in source
    words = desc_text.split()
    current = "  "
    for word in words:
        if len(current) + len(word) + 1 > 72:
            lines.append(current.rstrip())
            current = "  " + word
        else:
            current = current + " " + word if current.strip() else current + word
    if current.strip():
        lines.append(current.rstrip())
    lines.append(f'domain: {meta["domain"]}')
    lines.append("triangle:")
    for k in ("p1", "p2", "p3"):
        v = meta["triangle"][k].replace('"', '\\"')
        lines.append(f'  {k}: "{v}"')
    lines.append(f'signature_icon: {meta["signature_icon"]}')
    lines.append(f'hero_tier: {meta["hero_tier"]}')
    rel_str = ", ".join(str(r) for r in meta["related"])
    lines.append(f"related: [{rel_str}]")
    lines.append("predictions:")
    for p in meta["predictions"]:
        lines.append(f'  - id: {p["id"]}')
        short = p["short"].replace('"', '\\"')
        lines.append(f'    short: "{short}"')
        lines.append(f'    status: {p["status"]}')
        rdoc = p.get("result_doc")
        if rdoc:
            lines.append(f'    result_doc: {rdoc}')
        else:
            lines.append("    result_doc: null")
    lines.append("---")
    return "\n".join(lines) + "\n"


def main():
    repo_root = Path(__file__).resolve().parent.parent
    interfaces_dir = repo_root / "interfaces"
    if not interfaces_dir.is_dir():
        raise SystemExit(f"interfaces directory not found at {interfaces_dir}")

    for slug, meta in FRONTMATTER.items():
        path = interfaces_dir / f"{slug}.md"
        if not path.is_file():
            print(f"SKIP {slug}: file missing")
            continue
        text = path.read_text(encoding="utf-8")
        # Strip existing frontmatter if present
        if text.startswith("---\n"):
            end = text.find("\n---\n", 4)
            if end >= 0:
                text = text[end + 5:]
        new_text = render_frontmatter(meta) + text
        path.write_text(new_text, encoding="utf-8")
        print(f"OK   {slug}")


if __name__ == "__main__":
    main()
