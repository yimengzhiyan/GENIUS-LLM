# 🚀 Quick Start Guide

This guide will walk you through the standard workflow of **GENIUS-LLM**, from downloading the source code to generating your first gene function prediction.

---
## 1. Download the Project

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

## 2. Fast Configuration
Before running, you must provide your API credentials. GENIUS-LLM is designed to be provider-agnostic.

Edit config/data_config.yaml:
```
model:
    url: https://api.openai.com/v1 # 这里展示API 的基准地址，你可根据自己的LLM情况自行修改
    api_key: sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx # replace your api_key
    model: The model you want to use # 你使用的模型名称
```

## 3. The Three-Step Workflow
GENIUS-LLM simplifies complex bioinformatics pipelines into three standardized commands.

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

## 4. Expected Output
After running genius-predict, you should see logs indicating the progress. The final results will be saved in the directory defined in your config (default: predict_results/).

Sample Log Output(以deepseek输出结果为例):
```Plaintext
--- GENIUS-LLM Prediction System ---
2026-04-23 18:51:42,984 - INFO - Starting prediction for Gene ID: AT1G03000
2026-04-23 18:51:48,205 - INFO - Prompt successfully generated.
2026-04-23 18:51:49,612 - INFO - HTTP Request: POST https://api.deepseek.com/chat/completions "HTTP/1.1 200 OK"
2026-04-23 18:52:06,390 - INFO - Model response received.

=== Prediction Result ===
            *
            *
            *
2026-04-23 18:52:06,391 - INFO - Task completed successfully.
2026-04-23 18:52:06,391 - INFO - Prediction result successfully saved to predict_results\AT1G03000_prediction.txt
```
