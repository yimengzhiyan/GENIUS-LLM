20260410GENIUS-LLM/ 
├── docs/                    # MkDocs 说明文档          √
├── scripts/                 # 命令行脚本入口           √
│   ├── process_data.py      # 已注入 GPS 逻辑
│   ├── import_data.py       # 已注入 GPS 逻辑
│   └── predict.py           # 已注入 GPS 逻辑
├── src/                     # 核心代码包               √
│   ├── model/
│   ├── prompt/
│   ├── utils/
│   │   └── config_loader.py # 核心 GPS 逻辑所在地
│   └── data/                # 存放默认数据
├── config/                  # 配置文件                 √
│   └── data_config.yaml
├── MANIFEST.in              # 打包行李清单（新增）      √
├── mkdocs.yml               # 文档网站配置（新增）
├── setup.py                 # 安装与命令注册配置        √
├── README.md                # 仓库主页                 √
└── .gitignore               # 忽略垃圾文件             √

至少包括上述内容

<div align="center">
  <h1>GENIUS-LLM</h1>
  <p><b>An Automated Gene Function Prediction Framework Powered by Large Language Models</b></p>

  <a href="https://github.com/yimengzhiyan/GENIUS-LLM/issues">
    <img src="https://img.shields.io/github/issues/yimengzhiyan/GENIUS-LLM?color=teal" alt="Issues">
  </a>
  <a href="https://yimengzhiyan.github.io/GENIUS-LLM/">
    <img src="https://img.shields.io/badge/docs-latest-blue" alt="Documentation">
  </a>
  <a href="https://github.com/yimengzhiyan/GENIUS-LLM/stargazers">
    <img src="https://img.shields.io/github/stars/yimengzhiyan/GENIUS-LLM?color=indigo" alt="Stars">
  </a>
</div>

---

## Introduction

The functional annotation of genomic elements remains a cornerstone of bioinformatics. However, the rapidly evolving landscape of Large Language Models (LLMs) introduces significant challenges stemming from API heterogeneity and a lack of workflow standardization. 

To address these issues, we introduce **GENIUS-LLM**, a standardized framework designed to facilitate the integration and application of LLMs in gene function prediction. GENIUS-LLM provides a cohesive, protocol-oriented interface, enabling researchers to access various LLMs (e.g., GPT-4o, DeepSeek, or local Llama models) regardless of architectural differences or coding standards. With standardized APIs and comprehensive documentation, GENIUS-LLM streamlines model switching and comparative analyses, while incorporating best practices for consistent genomic evaluation.



---

## Installation

### From Source
We strongly recommend using a Conda virtual environment to ensure dependency stability and reproducibility in scientific computing.

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