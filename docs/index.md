## Installation


We strongly recommend using a Conda virtual environment to ensure dependency stability and reproducibility in scientific computing.
From Source：
```bash
# Clone the repository
git clone [https://github.com/ZhengJieBioinformatics/GENIUS-LLM.git]

# Install in editable mode (registers CLI commands like 'genius-predict')
pip install -e .
```

## Quick Start
GENIUS-LLM simplifies complex bioinformatics pipelines into three standardized commands:

注意导入数据的格式要符合要求：
1. blast、Tissue、KEGG、GO的输入要为csv或txt格式。
2. multi_gene_data、TWAS的输入要为xlsx格式。

