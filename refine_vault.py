#!/usr/bin/env python3
"""Archive legacy notes and prepare clean chapter folders."""

import shutil
from pathlib import Path

VAULT = Path("/Users/davdev/Documents/Archive/interview-vault")
ARCHIVE = VAULT / "_archive" / "legacy"

CHAPTERS = [
    "01 Statistics & Probability",
    "02 Mathematics",
    "03 Machine Learning",
    "04 Deep Learning",
    "05 NLP & Text Mining",
    "06 LLM & Generative AI",
    "07 RAG & Retrieval",
    "08 Computer Vision",
    "09 Knowledge Graphs",
    "10 Transformers & Attention",
    "11 Bayesian & Causal Inference",
    "12 Optimization & Simulation",
    "13 Software Engineering & Python",
    "14 Interview & Career",
]

KEEP_IN_CHAPTER = {"MOC"}  # will be replaced


def main():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for ch in CHAPTERS:
        folder = VAULT / ch
        if not folder.exists():
            folder.mkdir(parents=True)
            continue
        dest = ARCHIVE / ch
        dest.mkdir(parents=True, exist_ok=True)
        for f in folder.glob("*.md"):
            shutil.move(str(f), str(dest / f.name))
        print(f"Archived {ch}")


if __name__ == "__main__":
    main()
