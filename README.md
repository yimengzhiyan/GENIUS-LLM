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

注意导入数据的格式要符合要求：
1. blast、Tissue、KEGG、GO的输入要为csv或txt格式。
2. multi_gene_data、TWAS的输入要为xlsx格式。

