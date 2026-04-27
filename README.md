<div align="left">
  <h1>GENIUS-LLM</h1>
  <p><b>This is the official github repository for GENIUS-LLM: An Automated Gene Function Prediction Framework Powered by Large Language Models</b></p>

  <a href="">
    <img src="" alt="preprint">
  </a>
  <a href="https://ZhengJieBioinformatics.github.io/GENIUS-LLM/">
    <img src="https://img.shields.io/badge/docs-latest-blue" alt="docs">
  </a>
</div>

---

## Introduction

The functional annotation of genomic elements remains a cornerstone of bioinformatics. However, the rapidly evolving landscape of Large Language Models (LLMs) introduces significant challenges stemming from API heterogeneity and a lack of workflow standardization. 

To address these issues, we introduce **GENIUS-LLM**, a standardized framework designed to facilitate the integration and application of LLMs in gene function prediction. GENIUS-LLM provides a cohesive, protocol-oriented interface, enabling researchers to access various LLMs (e.g., GPT-4o, DeepSeek, or local Llama models) regardless of architectural differences or coding standards. With standardized APIs and comprehensive documentation, GENIUS-LLM streamlines model switching and comparative analyses, while incorporating best practices for consistent genomic evaluation.

![Figure: Technical workflow of GENIUS-LLM platform. The platform integrates multi-omics data through large language model, uses prompt engineering and related techniques to generate chain-of-thought analysis, and provides feedback correction capabilities to assist researchers in target gene selection.](docs/images/introduction.png)

---

## Installation

We strongly recommend using a Conda virtual environment to ensure dependency stability and reproducibility in scientific computing.

To install **GENIUS-LLM**, follow these steps:
From Source:
```
# 1. Clone the repository
git clone https://github.com/ZhengJieBioinformatics/GENIUS-LLM.git
cd GENIUS-LLM

# 2. Create a clean environment (Optional but highly recommended)
conda create -n genius_llm python=3.12 -y
conda activate genius_llm

# 3. Install dependencies first to avoid failures
pip install -r requirements.txt

# 4. Install GENIUS-LLM in editable mode
pip install -e .
```
Find out packages that lead to failures, then create a new requirements.txt of them and run:
```
pip install -r requirements.txt
```

## Quick Start
GENIUS-LLM simplifies complex bioinformatics pipelines into three standardized commands:
Step 1: Pre-process Raw Data
Clean and format your input data for LLM compatibility.
```bash
genius-process 
```
Step 2: Import Knowledge Base
First, populate your local MongoDB with gene annotation data.
```bash
genius-import 

```
Step 3: Execute Prediction
Run the intelligent prediction engine to infer gene functions.
```bash
genius-predict
```

## Data Format Requirements

Please ensure that all input data files strictly adhere to the following format requirements to ensure successful processing and database ingestion:

| Data Category | Supported File Formats | Description |
| :--- | :--- | :--- |
| **BLAST** | `.csv`, `.txt` | Sequence similarity and alignment results. |
| **Tissue (Expression)** | `.csv`, `.txt` | Tissue-specific gene expression profiles (e.g., TPM). |
| **KEGG** | `.csv`, `.txt` | Pathway enrichment and functional descriptions. |
| **GO** | `.csv`, `.txt` | Gene Ontology terms and functional annotations. |
| **Multi-gene Data** | `.xlsx` | Homologous gene mapping and multi-gene datasets. |
| **TWAS** | `.xlsx` | Transcriptome-Wide Association Study results. |

> **⚠️ Important**: 
> * For **CSV/TXT** files, ensure consistent delimiters (comma or tab) are used. 
> * For **XLSX** files, ensure the data is located in the first sheet unless otherwise specified in the configuration.

