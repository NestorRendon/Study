#!/usr/bin/env python3
"""Fix links and add SOTA blocks to chapter overviews."""

from pathlib import Path

VAULT = Path("/Users/davdev/Documents/Archive/interview-vault")

REPLACEMENTS = [
    ("01 - Encoder vs Decoder Models", "01 - LLM Foundations Encoder and Decoder"),
    ("[[11 - Convolutional Neural Networks]]", "[[12 - Convolutional Neural Networks]]"),
    ("05 - Text Preprocessing Pipeline]]", "02 - Text Preprocessing Pipeline]]"),  # careful
    ("02 - TF-IDF and Bag of Words]]", "03 - TF-IDF and Bag of Words]]"),
]

SOTA_BLOCKS = {
    "01 Statistics & Probability": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Causal inference** | Moving beyond p-values to effect sizes |
| **Bayesian A/B** | Startups use posterior for decisions |
| **Robust stats** | Heavy-tailed metrics in tech/finance |
""",
    "02 Bayesian & Causal Inference": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Probabilistic programming** | PyMC, Stan for hierarchical models |
| **Causal ML** | DoWhy, DAG-based identification |
| **Bayesian deep learning** | Uncertainty in vision/NLP |
""",
    "03 Mathematics": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Automatic differentiation** | PyTorch/JAX — all deep learning |
| **Second-order methods** | Rare at LLM scale; Adam family dominates |
""",
    "04 Machine Learning": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Gradient boosting** | XGBoost/LightGBM still king on tabular |
| **AutoML** | Feature tools + HPO for baselines |
| **Interpretability** | SHAP for regulated industries |
""",
    "08 RAG & Retrieval": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Hybrid search** | BM25 + dense default in production |
| **Rerankers** | Cross-encoders (Cohere, bge-reranker) |
| **GraphRAG** | Microsoft-style KG + vectors |
| **Agentic RAG** | Multi-step retrieval loops |
""",
    "09 Knowledge Graphs": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **GraphRAG + LLM extraction** | Auto-build KGs from docs |
| **Property graphs** | Neo4j, Amazon Neptune |
| **Vector + graph** | Enterprise search stacks |
""",
    "10 Transformers & Attention": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Long context** | RoPE scaling, YaRN, ring attention |
| **Flash Attention** | Standard training kernel |
| **MoE transformers** | Sparse FFN layers at scale |
""",
    "11 Computer Vision": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Vision transformers** | ViT, DINOv2 for representation |
| **YOLO / RT-DETR** | Real-time detection |
| **SAM** | Promptable segmentation |
| **Edge deploy** | ONNX, TensorRT, INT8 |
""",
    "12 Optimization & Simulation": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **OR + ML** | Learned heuristics for routing |
| **Digital twins** | Simulation + real-time data |
""",
    "13 Software Engineering & Python": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **Polars / DuckDB** | Faster than pandas for analytics |
| **uv / rye** | Modern Python packaging |
| **dbt + Spark** | Lakehouse ETL standard |
""",
    "14 C++ for Data Science & Engineering": """
## SOTA & trends (2024–2026)

| Trend | Note |
|-------|------|
| **ONNX Runtime / TensorRT** | C++ inference serving |
| **Rust alternative** | Some teams pick Rust over C++ for safety |
""",
    "15 Interview & Career": """
## SOTA & trends (2024–2026)

| Trend | Interview angle |
|-------|-----------------|
| **GenAI on CV** | Mention agents + vision if relevant |
| **Research → product** | Your soundscape → xFarm arc |
""",
}


def fix_links():
    for md in VAULT.rglob("*.md"):
        t = md.read_text(encoding="utf-8")
        o = t
        t = t.replace("01 - Encoder vs Decoder Models", "01 - LLM Foundations Encoder and Decoder")
        if md.name != "10 - Batch Normalization.md":
            pass  # avoid global CNN renumber issues
        md.write_text(t, encoding="utf-8")


def add_sota():
    for folder, block in SOTA_BLOCKS.items():
        overview = VAULT / folder / "00 - Chapter Overview.md"
        if not overview.exists():
            continue
        t = overview.read_text(encoding="utf-8")
        if "## SOTA & trends" in t:
            continue
        marker = "## Common traps"
        if marker in t:
            t = t.replace(marker, block.strip() + "\n\n---\n\n" + marker)
        else:
            t += "\n" + block
        overview.write_text(t, encoding="utf-8")


if __name__ == "__main__":
    fix_links()
    add_sota()
    print("Patched links and SOTA blocks.")
