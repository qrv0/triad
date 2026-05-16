"""mkdocs hook : build interfaces-index.json + predictions-index.json
from interface frontmatter; inject hero block into each interface page.

The hook reads the YAML frontmatter on each `interfaces/NN-*.md` page,
collects the data into two JSON files served from
`docs/assets/data/`, and prepends a hero HTML block to each interface
page's body. The hero is rendered from the same frontmatter, so the
single source of truth is the interface markdown's own frontmatter.

Wave 1 of the site-restructure plan: commit 2 of 8.
"""

import json
import re
from pathlib import Path

INTERFACES_DIR = "interfaces"
SKIP_FILENAMES = {"README.md", "compare.md", "predictions.md"}

# Domain label shown in the hero eyebrow (mkdocs writes the slug; the
# eyebrow displays the prettified label).
DOMAIN_LABELS = {
    "physics": "Physics",
    "cosmology": "Cosmology",
    "acoustics": "Acoustics",
    "neuro": "Neuroscience",
    "archaeo": "Archaeoacoustics",
    "engineering": "Engineering / ML",
    "complex-systems": "Complex systems",
    "biology": "Biology",
}


def on_files(files, config, **kwargs):
    """Build interfaces-index.json + predictions-index.json from
    frontmatter of all interface markdown files. Writes the JSON
    files to `docs_dir/assets/data/` so mkdocs picks them up.
    """
    interfaces_root = Path(config["docs_dir"]).parent / INTERFACES_DIR
    if not interfaces_root.is_dir():
        return files

    interfaces_index = {}
    predictions_index = []

    for path in sorted(interfaces_root.glob("*.md")):
        if path.name in SKIP_FILENAMES:
            continue
        meta = _parse_frontmatter(path)
        if not meta:
            continue

        slug = path.stem
        num_match = re.match(r"^(\d+)", slug)
        if not num_match:
            continue
        num = num_match.group(1)

        entry = dict(meta)
        entry["slug"] = slug
        entry["num"] = num
        interfaces_index[num] = entry

        for pred in meta.get("predictions", []) or []:
            pred_entry = dict(pred)
            pred_entry["interface_num"] = num
            pred_entry["interface_slug"] = slug
            pred_entry["interface_title"] = meta.get("title", "")
            pred_entry["domain"] = meta.get("domain", "")
            predictions_index.append(pred_entry)

    data_dir = Path(config["docs_dir"]) / "assets" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    (data_dir / "interfaces-index.json").write_text(
        json.dumps(interfaces_index, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (data_dir / "predictions-index.json").write_text(
        json.dumps(predictions_index, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return files


def on_page_markdown(markdown, page, config, files, **kwargs):
    """Inject the interface hero block at the top of each interface
    page (after the H1, before the first body section)."""
    src = page.file.src_path
    if not src.startswith(INTERFACES_DIR + "/"):
        return markdown
    name = Path(src).name
    if name in SKIP_FILENAMES:
        return markdown

    meta = page.meta or {}
    triangle = meta.get("triangle") or {}
    if not triangle:
        return markdown

    hero_html = _render_hero(meta)

    lines = markdown.split("\n")
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("##"):
            insert_at = i + 1
            break
    while insert_at < len(lines) and lines[insert_at].strip() == "":
        insert_at += 1

    return "\n".join(lines[:insert_at] + ["", hero_html, ""] + lines[insert_at:])


def _parse_frontmatter(path):
    """Return the YAML frontmatter dict, or None if the file has none.
    Uses PyYAML if available; otherwise a minimal hand-parser sufficient
    for the structured fields this hook reads.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    raw = text[4:end]
    try:
        import yaml
        return yaml.safe_load(raw) or {}
    except ImportError:
        return _minimal_yaml_parse(raw)


def _minimal_yaml_parse(raw):
    """Fallback YAML parser when PyYAML is unavailable. Handles only
    flat scalar fields, simple nested triangle dict, and predictions
    list of dicts."""
    result = {}
    current_block = None
    current_pred = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("triangle:"):
            current_block = "triangle"
            result["triangle"] = {}
            continue
        if line.startswith("predictions:"):
            current_block = "predictions"
            result["predictions"] = []
            continue
        if line.startswith("related:"):
            current_block = "related"
            tail = line.split(":", 1)[1].strip()
            if tail.startswith("[") and tail.endswith("]"):
                items = [s.strip() for s in tail[1:-1].split(",") if s.strip()]
                result["related"] = [int(s) for s in items if s.isdigit()]
            else:
                result["related"] = []
            continue
        if current_block == "triangle" and line.startswith("  "):
            key, _, val = line.strip().partition(":")
            result["triangle"][key.strip()] = val.strip().strip('"')
            continue
        if current_block == "predictions":
            if line.startswith("  - "):
                current_pred = {}
                result["predictions"].append(current_pred)
                rest = line[4:].strip()
                if rest:
                    key, _, val = rest.partition(":")
                    current_pred[key.strip()] = val.strip().strip('"')
                continue
            if current_pred is not None and line.startswith("    "):
                key, _, val = line.strip().partition(":")
                current_pred[key.strip()] = val.strip().strip('"')
                continue
        # Top-level scalar
        if ":" in line and not line.startswith(" "):
            current_block = None
            current_pred = None
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip().strip('"')
    return result


def _render_hero(meta):
    """Return the HTML block for the interface hero."""
    description = _escape(meta.get("description", ""))
    domain_key = meta.get("domain", "")
    domain_label = DOMAIN_LABELS.get(domain_key, domain_key.replace("-", " "))
    tri = meta.get("triangle") or {}
    p1 = _escape(tri.get("p1", ""))
    p2 = _escape(tri.get("p2", ""))
    p3 = _escape(tri.get("p3", ""))
    tier = meta.get("hero_tier", "B").upper()
    signature = _escape(meta.get("signature_icon", ""))

    return (
        '<div class="interface-hero" markdown="0">\n'
        '  <div class="interface-hero__visual">\n'
        f'    <div class="interface-hero__placeholder" aria-hidden="true"'
        f' data-signature="{signature}">&#x2B22;</div>\n'
        '  </div>\n'
        '  <div class="interface-hero__copy">\n'
        f'    <span class="interface-hero__eyebrow">{domain_label}'
        f' &middot; <span class="interface-hero__tier">tier {tier} hero</span></span>\n'
        f'    <p class="interface-hero__desc">{description}</p>\n'
        '    <ul class="interface-hero__triangle">\n'
        f'      <li class="t-p1"><strong>P1 oscillation</strong>{p1}</li>\n'
        f'      <li class="t-p2"><strong>P2 self-reference</strong>{p2}</li>\n'
        f'      <li class="t-p3"><strong>P3 coupling</strong>{p3}</li>\n'
        '    </ul>\n'
        '  </div>\n'
        '</div>'
    )


def _escape(text):
    if not isinstance(text, str):
        text = str(text)
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )
