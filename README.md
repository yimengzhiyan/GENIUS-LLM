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

### 🧬 GENIUS-LLM

gene function inference through integrated multi-omics data with large language models

### 🌟 Overview

Gene function **inference** is critical for modern agricultural research and crop improvement. While deep learning has become the dominant computational approach, it still faces limitations in multi-omics data integration and interpretability.

![Figure: Technical workflow of GENIUS-LLM platform. The platform integrates multi-omics data through large language models, uses prompt engineering and related techniques to perform structured evidence synthesis, and provides feedback correction capabilities to assist researchers in target gene selection.](images/introduction.png)
GENIUS-LLM is a one-stop platform for gene function inference that integrates multi-omics data using a **Retrieval-Augmented Generation (RAG)**-inspired storage system and multi-level prompt engineering. The system transforms biological data—including **sequence similarity**, **co-expression patterns**, and **tissue-specific expression profiles**—into structured natural language descriptions.

By utilizing **priority-based analysis** and **Chain-of-Thought (CoT)** prompting, **GENIUS-LLM** ensures the **accuracy** and **interpretability** of functional **inference** in cotton (Gossypium hirsutum), Arabidopsis thaliana, and rice (Oryza sativa).


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

## Data Input Format Specifications

To ensure the `genius-process` script correctly parses your raw data, please prepare your files according to the required headers and formats listed below.

| Data Type | Required Headers | File Format | Example Record |
| :--- | :--- | :--- | :--- |
| **BLAST** | `query`, `subject`, `similarity`, `alignment_length`, `mismatches`, `gap_openings`, `q_start`, `q_end`, `s_start`, `s_end`, `e_value`, `bit_score` | `TXT` (Space-sep, **No Header**) | `GeneA GeneB 85.5 200 2 0 1 200 50 250 1e-50 450` |
| **Co-expression** | `row`, `col`, `weight` | `TXT` (Space-sep, With Header) | `GeneA GeneB 0.956789` |
| **Expression** | `GeneId`, `Tissue_1`, `Tissue_2`, ... | `CSV` (Comma-separated) | `GeneA, 12.5, 0.0, 8.45` |
| **GO** | `GeneID`, `GO`, `Ontology`, `Description` | `CSV` (Comma-separated) | `GeneA, GO:0008150, BP, cell growth` |
| **KEGG** | `GeneID`, `KEGG`, `KEGG_Description` | `CSV` (Comma-separated) | `GeneA, path:ath00010, Glycolysis` |
| **TWAS** | `GeneID`, `Phenotype`, `Stage`, `TWAS.Zscore` | `XLSX` (Must be **Sheet1**) | `GeneA, FE, Stage_1, 3.4567` |
| **Homolog** | `GeneID`, `Homology of AtGi`, `Symbol`, `Full_name`, `Chr.`, `Start`, `End`, `Function description` | `XLSX` | `GeneA, AT1G01010, ABC1, Protein X, Chr1, 100, 500, Kinase` |

---

### 🛠️ Processing Notes

*   **BLAST Header Requirement**: The system reads BLAST files without a header (`header=None`). Ensure the first line of the file contains actual data.
*   **Co-expression Threshold**: The processor only handles gene pairs with a `weight > 0.9` to ensure the reliability of functional inference.
*   **Dynamic Expression Columns**: Except for the first column (`GeneId`), all subsequent columns are automatically identified as tissue names.
*   **TWAS Phenotype Mapping**: The system includes a built-in mapping dictionary that automatically converts abbreviations (e.g., `FE`, `FS`, `FU`, `FL`) into full fiber trait descriptions.
*   **Homology Data Completion**: If any column in the homology table is missing data, the system will automatically fill the field with `NA`.
