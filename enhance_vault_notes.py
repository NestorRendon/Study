#!/usr/bin/env python3
"""Append standard sections to vault notes if missing."""

from pathlib import Path

VAULT = Path("/Users/davdev/Documents/Archive/interview-vault")
SKIP = {"_archive", ".obsidian", "assets"}
CHAPTERS = [p for p in VAULT.iterdir() if p.is_dir() and p.name[0].isdigit()]

TRAPS_BY_CHAPTER = {
    "02 Mathematics": [
        ("Gradient = derivative of loss only", "Gradient is vector of partial derivatives; points uphill"),
        ("Convex = always global minimum in DL", "Deep nets are non-convex; convexity matters more for linear models"),
    ],
    "03 Machine Learning": [
        ("Random Forest reduces bias", "RF reduces **variance** (bagging); boosting reduces **bias**"),
        ("Logistic regression needs linearly separable data", "Separable data can cause huge weights — use **regularization**"),
        ("k-means always finds global optimum", "k-means finds **local** optima; restart with different inits"),
        ("Accuracy on 99% negative class", "Use precision/recall/F1 or ROC-AUC"),
    ],
    "05 NLP & Text Mining": [
        ("TF-IDF captures semantics", "TF-IDF is **lexical**; use embeddings for meaning"),
        ("More topics in LDA = better", "Too many topics → incoherent; tune with coherence/perplexity"),
    ],
    "06 LLM & Generative AI": [
        ("Lower temperature = smarter", "Temperature controls **randomness**, not intelligence"),
        ("Fine-tune full 70B on one GPU without QLoRA", "Use LoRA/QLoRA or API"),
        ("Context window = model memory forever", "Context is **limited**; older tokens may be lost in long chats"),
    ],
    "07 RAG & Retrieval": [
        ("RAG eliminates hallucinations", "Reduces them; still need eval + grounding checks"),
        ("Bigger chunks = better", "Too big → noise; too small → lost context; tune 256–1024 tokens"),
        ("Vector search alone for multi-hop", "Use GraphRAG or agentic multi-step retrieval"),
    ],
    "08 Computer Vision": [
        ("OpenCV and deep learning are interchangeable", "OpenCV = preprocessing; DL = feature learning"),
        ("Higher resolution always helps", "Costs compute; may need resize + augmentation balance"),
    ],
    "09 Knowledge Graphs": [
        ("KG replaces vector DB", "They **complement** each other (GraphRAG)"),
        ("OWL is always needed", "RDFS enough for simple schemas; OWL when logic matters"),
    ],
    "10 Transformers & Attention": [
        ("Attention = remembering long-term memory", "Attention = weighted mix of **current sequence** tokens"),
        ("Q,K,V are embeddings", "They are **learned projections** of embeddings"),
    ],
    "11 Bayesian & Causal Inference": [
        ("Bayesian = subjective only", "Bayesian is **coherent updating**; priors can be weak/informative"),
        ("Correlation implies causation", "Need causal design, DAG, or experiment"),
    ],
    "12 Optimization & Simulation": [
        ("Heuristics always worse", "Heuristics trade optimality for **speed** at scale"),
    ],
    "13 Software Engineering & Python": [
        ("pandas iterrows for speed", "Use vectorized ops or apply; iterrows is slow"),
        ("SQL SELECT * in production", "Select only needed columns; reduces shuffle in Spark too"),
    ],
    "14 Interview & Career": [
        ("List every paper detail", "Lead with **impact** and **your role** in 2 minutes"),
    ],
}


def format_traps(rows):
    lines = ["\n---\n\n## Common traps\n", "| Trap | Correct |", "|------|---------|"]
    for a, b in rows:
        lines.append(f"| {a} | {b} |")
    return "\n".join(lines) + "\n"


def enhance_file(path: Path, chapter_name: str):
    text = path.read_text(encoding="utf-8")
    if path.name.startswith("00 -"):
        return
    changed = False

    if "## In plain English" not in text and "## Interview one-liner" in text:
        # Insert plain English placeholder after first ---
        parts = text.split("---", 2)
        if len(parts) >= 3:
            title_block = parts[0] + "---" + parts[1] + "---"
            rest = parts[2]
            insert = "\n\n## In plain English\n\n*(Read the sections below — each concept builds intuition before formulas.)*\n"
            text = title_block + insert + rest
            changed = True

    if "## Common traps" not in text:
        traps = TRAPS_BY_CHAPTER.get(chapter_name, [])
        if traps:
            # Use first trap only as note-specific is manual; add generic chapter traps shortened
            text = text.rstrip() + format_traps(traps[:3])
            changed = True

    if changed:
        path.write_text(text, encoding="utf-8")


def main():
    for ch in CHAPTERS:
        ch_name = ch.name
        for md in ch.glob("*.md"):
            if md.name.startswith("00 -"):
                continue
            enhance_file(md, ch_name)
    print("Enhanced notes with plain-English header and traps where missing.")


if __name__ == "__main__":
    main()
