#!/usr/bin/env python3
"""Reorganize chapter order and fix cross-links."""

import shutil
from pathlib import Path

VAULT = Path("/Users/davdev/Documents/Archive/interview-vault")

# old folder name -> new folder name
RENAMES = [
    ("14 Interview & Career", "15 Interview & Career"),
    ("11 Bayesian & Causal Inference", "_t02 Bayesian & Causal Inference"),
    ("08 Computer Vision", "_t11 Computer Vision"),
    ("07 RAG & Retrieval", "_t08 RAG & Retrieval"),
    ("06 LLM & Generative AI", "_t07 LLM & Generative AI"),
    ("05 NLP & Text Mining", "_t06 NLP & Text Mining"),
    ("04 Deep Learning", "_t05 Deep Learning"),
    ("03 Machine Learning", "_t04 Machine Learning"),
    ("02 Mathematics", "_t03 Mathematics"),
    ("_t02 Bayesian & Causal Inference", "02 Bayesian & Causal Inference"),
    ("_t03 Mathematics", "03 Mathematics"),
    ("_t04 Machine Learning", "04 Machine Learning"),
    ("_t05 Deep Learning", "05 Deep Learning"),
    ("_t06 NLP & Text Mining", "06 NLP & Text Mining"),
    ("_t07 LLM & Generative AI", "07 LLM & Generative AI"),
    ("_t08 RAG & Retrieval", "08 RAG & Retrieval"),
    ("_t11 Computer Vision", "11 Computer Vision"),
]

LINK_REPLACEMENTS = [
    ("14 Interview & Career", "15 Interview & Career"),
    ("11 Bayesian & Causal Inference", "02 Bayesian & Causal Inference"),
    ("08 Computer Vision", "11 Computer Vision"),
    ("07 RAG & Retrieval", "08 RAG & Retrieval"),
    ("06 LLM & Generative AI", "07 LLM & Generative AI"),
    ("05 NLP & Text Mining", "06 NLP & Text Mining"),
    ("04 Deep Learning", "05 Deep Learning"),
    ("03 Machine Learning", "04 Machine Learning"),
    ("02 Mathematics", "03 Mathematics"),
    # Chapter progression text
    ("Chapter 2 — Mathematics", "Chapter 3 — Mathematics"),
    ("Chapter 3 — Machine Learning", "Chapter 4 — Machine Learning"),
    ("Chapter 4 — Deep Learning", "Chapter 5 — Deep Learning"),
    ("Chapter 5 — NLP", "Chapter 6 — NLP"),
    ("Chapter 6 — LLM", "Chapter 7 — LLM"),
    ("Chapter 7 — RAG", "Chapter 8 — RAG"),
    ("Chapter 8 — Computer Vision", "Chapter 11 — Computer Vision"),
    ("Chapter 11 — Bayesian", "Chapter 2 — Bayesian"),
    ("Chapter 5 — NLP & Text Mining", "Chapter 6 — NLP & Text Mining"),
    ("Ch 4 DL", "Ch 5 DL"),
    ("Ch 3 ML", "Ch 4 ML"),
]

def reorganize_folders():
    for old, new in RENAMES:
        src = VAULT / old
        dst = VAULT / new
        if src.exists():
            shutil.move(str(src), str(dst))
            print(f"  {old} -> {new}")


def fix_links():
    for md in VAULT.rglob("*.md"):
        if "_archive" in str(md):
            continue
        text = md.read_text(encoding="utf-8")
        orig = text
        for old, new in LINK_REPLACEMENTS:
            text = text.replace(old, new)
        if text != orig:
            md.write_text(text, encoding="utf-8")
    print("Links updated.")


if __name__ == "__main__":
    print("Reorganizing folders...")
    reorganize_folders()
    print("Fixing links...")
    fix_links()
    print("Done.")
