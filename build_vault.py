#!/usr/bin/env python3
"""Build Obsidian interview vault from Archive markdown + attachments."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ARCHIVE = Path("/Users/davdev/Documents/Archive")
VAULT = ARCHIVE / "interview-vault"
ASSETS_SRC = ARCHIVE / "Attachments"
ASSETS_DST = VAULT / "assets"

# Folder key -> display name
FOLDERS = {
    "01-statistics": "01 Statistics & Probability",
    "02-mathematics": "02 Mathematics",
    "03-machine-learning": "03 Machine Learning",
    "04-deep-learning": "04 Deep Learning",
    "05-nlp": "05 NLP & Text Mining",
    "06-llm": "06 LLM & Generative AI",
    "07-rag": "07 RAG & Retrieval",
    "08-computer-vision": "08 Computer Vision",
    "09-knowledge-graphs": "09 Knowledge Graphs",
    "10-transformers": "10 Transformers & Attention",
    "11-bayesian": "11 Bayesian & Causal Inference",
    "12-optimization": "12 Optimization & Simulation",
    "13-software": "13 Software Engineering & Python",
    "14-interview": "14 Interview & Career",
}

# Source file -> default folder for unsplit / whole-file placement
SOURCE_DEFAULT = {
    "Bayesian .md": "11-bayesian",
    "Probability.md": "01-statistics",
    "Semi Senior.md": "03-machine-learning",
    "Senior.md": "04-deep-learning",
    "Globant preparation  Junior.md": "01-statistics",
    "NLP.md": "06-llm",
    "TRansformer.md": "10-transformers",
    "OPENCV.md": "08-computer-vision",
    "Knowledge Graphs.md": "09-knowledge-graphs",
    "Interview Planning.md": "14-interview",
    "Interview  DELVI.md": "14-interview",
    "HL Vocabulary.md": "05-nlp",
    "Que hacer hoy.md": "14-interview",
    "ZOOPLUS.md": "14-interview",
    "Xfarm.md": "14-interview",
    "This position offers an exciting opportunity to participate in an….md": "14-interview",
    "Diez títulos de búsqueda (para LinkedIn, InfoJobs, Indeed, Google….md": "14-interview",
}

# Keyword rules: (folder_key, [keywords]) — first match wins
ROUTING = [
    ("14-interview", ["interview", "education", "industrial experience", "zooplus", "xfarm", "delvi", "career", "que hacer"]),
    ("11-bayesian", ["bayesian", "prior", "posterior", "structure learning", "ancova", "frequentist"]),
    ("10-transformers", ["transformer", "attention", "positional encoding", "multi-head", "encoder-only", "decoder-only"]),
    ("09-knowledge-graphs", ["knowledge graph", "rdf", "sparql", "owl", "rdfs", "turtle", "neo4j", "graphrag", "triple", "ontology"]),
    ("08-computer-vision", ["opencv", "sift", "threshold", "morphological", "hough", "tensorrt", "onnx", "segmentation", "object detection", "yolo"]),
    ("07-rag", ["rag", "retrieval", "vector db", "reag", "chunking", "rerank", "hybrid retrieval", "context precision"]),
    ("06-llm", ["llm", "lora", "peft", "moe", "mixture of experts", "kv cache", "guardrail", "alignment", "g-eval", "llm-as-a-judge", "agentic", "langchain", "langgraph", "prompt", "few-shot", "zero-shot", "chain-of-thought", "token", "fine-tuning", "evaluator-optimizer", "trajectory success", "hallucination", "rouge", "bleu", "comet", "perplexity"]),
    ("05-nlp", ["nlp", "tf-idf", "tfidf", "lda", "bag of words", "text mining", "topic model", "word2vec", "embedding"]),
    ("12-optimization", ["optimization", "mip", "mixed-integer", "heuristic", "simulation", "discrete event", "agent based modelling"]),
    ("04-deep-learning", ["deep learning", "neural network", "cnn", "lstm", "relu", "dropout", "batch norm", "sgd", "adam", "loss function", "bias / variance", "bias-variance", "epoch graph", "shallow nn"]),
    ("13-software", ["python", "git", "sql", "fastapi", "flask", "agile", "oop", "cprofile", "virtual env", "pandas", "numpy", "scikit", "bokeh", "plotly", "rest", "wsgi"]),
    ("02-mathematics", ["matrix", "derivative", "integral", "limit", "convolution", "convexity", "gradient descent"]),
    ("01-statistics", ["statistics", "anova", "p-value", "hypothesis", "distribution", "gaussian", "poisson", "binomial", "clt", "central limit", "cross validation", "data leakage", "confusion matrix", "precision", "recall", "f1", "mae", "rmse", "pca", "factor analysis", "autocorrelation", "sampling", "median", "variance", "kurtosis", "heteroskedastic", "overfitting", "population test"]),
    ("03-machine-learning", ["linear regression", "logistic", "decision tree", "random forest", "k-means", "knn", "svm", "k-means", "feature engineering", "variable selection", "class imbalance"]),
]

SKIP_SOURCES = set()

def slugify(title: str) -> str:
    t = title.strip()
    t = re.sub(r"^#+\s*", "", t)
    t = re.sub(r"[^\w\s\-]", "", t, flags=re.UNICODE)
    t = re.sub(r"\s+", " ", t).strip()
    if not t or t.lower() in {"#", ""}:
        return ""
    return t[:80]

def fix_paths(text: str) -> str:
    text = text.replace("Attachments/", "assets/")
    text = re.sub(r"\+\+\[([^\]]+)\]\(([^)]+)\)\+\+", r"[\1](\2)", text)
    return text

def route(title: str, body: str, default: str) -> str:
    blob = (title + " " + body[:2000]).lower()
    for folder, keywords in ROUTING:
        for kw in keywords:
            if kw in blob:
                return folder
    return default

def split_sections(content: str) -> list[tuple[str, str]]:
    """Split on ## or # headings; return (title, body) pairs."""
    lines = content.splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_title = ""
    current_lines: list[str] = []

    def flush():
        nonlocal current_title, current_lines
        if current_title or current_lines:
            body = "\n".join(current_lines).strip()
            if body or current_title:
                sections.append((current_title, current_lines[:]))
        current_title = ""
        current_lines = []

    for line in lines:
        if re.match(r"^#{1,2}\s+", line) and not line.startswith("###"):
            flush()
            current_title = re.sub(r"^#+\s*", "", line).strip()
            current_lines = []
        else:
            current_lines.append(line)
    flush()

    if len(sections) <= 1:
        # try ### splits for very long single-section files
        sections = []
        current_title = ""
        current_lines = []
        for line in lines:
            if re.match(r"^#{1,3}\s+", line):
                flush()
                current_title = re.sub(r"^#+\s*", "", line).strip()
                current_lines = []
            else:
                current_lines.append(line)
        flush()

    result = []
    for title, blines in sections:
        body = "\n".join(blines).strip()
        if title.lower() in {"semi senior", "senior", "junior", "higher seniorities"}:
            continue
        if not body and not title:
            continue
        result.append((title, body))
    return result

def write_note(folder_key: str, filename: str, title: str, body: str, tags: list[str] | None = None):
    folder = VAULT / FOLDERS[folder_key]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / filename
    if path.exists():
        # avoid overwrite: append counter
        stem = path.stem
        n = 2
        while path.exists():
            path = folder / f"{stem} ({n}).md"
            n += 1

    tag_line = ""
    if tags:
        tag_line = "\n" + " ".join(f"#{t.replace(' ', '-')}" for t in tags) + "\n"

    front = f"---\ntags: [{', '.join(tags or [])}]\nsource: interview-prep\n---\n" if tags else ""

    content = f"# {title}\n{tag_line}\n{fix_paths(body)}\n"
    if front:
        content = front + "\n" + content
    path.write_text(content, encoding="utf-8")
    return path

def process_source(name: str, default_folder: str):
    src = ARCHIVE / name
    if not src.exists():
        return []
    text = src.read_text(encoding="utf-8", errors="replace")
    created = []

    # Special: Classical Algorithms block in Semi Senior — extract as ML index
    if name == "Semi Senior.md":
        # Write classical algorithms composite note
        m = re.search(
            r"Classical Algorithms.*?(\n##\s+Central Limit)",
            text,
            re.DOTALL | re.IGNORECASE,
        )
        if m:
            block = m.group(0)
            block = re.sub(r"\n##\s+Central Limit.*", "", block, flags=re.DOTALL)
            p = write_note(
                "03-machine-learning",
                "Classical ML Algorithms.md",
                "Classical ML Algorithms",
                block,
                ["machine-learning", "algorithms"],
            )
            created.append(p)

    sections = split_sections(text)
    if len(sections) <= 1:
        title = slugify(name.replace(".md", "")) or name.replace(".md", "")
        folder = route(title, text, default_folder)
        fname = re.sub(r"[^\w\s\-]", "", title) + ".md"
        fname = re.sub(r"\s+", " ", fname).strip() + ".md"
        p = write_note(folder, fname, title, text)
        created.append(p)
        return created

    for title, body in sections:
        slug = slugify(title)
        if not slug:
            continue
        if len(body) < 30 and "!" not in body:
            continue
        folder = route(title, body, default_folder)
        safe = re.sub(r"[^\w\s\-]", "", slug)
        safe = re.sub(r"\s+", " ", safe).strip() + ".md"
        p = write_note(folder, safe, title or slug, body)
        created.append(p)
    return created

def build_mocs(note_paths: dict[str, list[Path]]):
    for key, display in FOLDERS.items():
        folder = VAULT / display
        notes = sorted(folder.glob("*.md")) if folder.exists() else []
        notes = [n for n in notes if not n.name.startswith("MOC")]
        if not notes:
            continue
        lines = [
            f"# MOC — {display.split(' ', 1)[1]}",
            "",
            f"[[Home|← Back to Home]]",
            "",
            "## Topics",
            "",
        ]
        for n in notes:
            title = n.stem
            lines.append(f"- [[{title}]]")
        lines.append("")
        moc_path = folder / f"MOC - {display.split(' ', 1)[1]}.md"
        moc_path.write_text("\n".join(lines), encoding="utf-8")

def build_home():
    lines = [
        "# Interview Knowledge Base",
        "",
        "Quick navigation by **field of science** — tap a section, then a topic.",
        "",
        "> Open this vault in Obsidian: **File → Open vault →** `interview-vault`",
        "",
        "## Fields",
        "",
    ]
    for key, display in FOLDERS.items():
        name = display.split(" ", 1)[1]
        lines.append(f"- [[MOC - {name}|{display}]]")
    lines.extend(
        [
            "",
            "## Original PDFs",
            "",
            "PDF copies live in `../pdfs/` (same content as these notes).",
            "",
            "## Tips for interviews",
            "",
            "- Use **Cmd+O** (Quick switcher) to jump to any concept (e.g. `ANOVA`, `Linear Regression`)",
            "- Pin **Home** during the interview",
            "- Add new notes in the folder that matches the science field",
            "",
        ]
    )
    (VAULT / "Home.md").write_text("\n".join(lines), encoding="utf-8")

def setup_obsidian():
    obs = VAULT / ".obsidian"
    obs.mkdir(parents=True, exist_ok=True)
    (obs / "app.json").write_text(
        '{\n  "alwaysUpdateLinks": true,\n  "newFileLocation": "folder",\n  "attachmentFolderPath": "assets",\n  "showInlineTitle": true,\n  "defaultViewMode": "preview"\n}\n'
    )
    (obs / "appearance.json").write_text(
        '{\n  "theme": "moonstone",\n  "baseFontSize": 16\n}\n'
    )
    (obs / "core-plugins.json").write_text(
        '["file-explorer","global-search","switcher","graph","outgoing-link","tag-pane","page-preview","note-composer","outline","backlink"]\n'
    )

def main():
    if VAULT.exists():
        shutil.rmtree(VAULT)
    VAULT.mkdir(parents=True)
    ASSETS_DST.mkdir(parents=True)
    if ASSETS_SRC.exists():
        shutil.copytree(ASSETS_SRC, ASSETS_DST, dirs_exist_ok=True)

    for key, display in FOLDERS.items():
        (VAULT / display).mkdir(parents=True, exist_ok=True)

    all_created: dict[str, list[Path]] = {k: [] for k in FOLDERS}
    for name, default in SOURCE_DEFAULT.items():
        created = process_source(name, default)
        for p in created:
            for key, display in FOLDERS.items():
                if str(p).startswith(str(VAULT / display)):
                    all_created[key].append(p)

    build_mocs(all_created)
    build_home()
    setup_obsidian()

    total = sum(len(list((VAULT / d).glob("*.md"))) for d in FOLDERS.values())
    print(f"Vault created at: {VAULT}")
    print(f"Notes: {total}")
    print(f"Assets: {len(list(ASSETS_DST.iterdir()))} files")

if __name__ == "__main__":
    main()
