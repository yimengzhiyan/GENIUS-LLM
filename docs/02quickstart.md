这是为了**回应审稿人 #5 关于 502 错误**的质疑（教他们如何在本地跑起来）：

# 🚀 Quick Start Guide

This guide will walk you through the standard workflow of **GENIUS-LLM**, from downloading the source code to generating your first gene function prediction.

---

## 1. Download the Project

Use `git` to clone the repository directly from GitHub. This ensures you have the latest version of the framework.

```bash
# Clone the repository
git clone https://github.com/ZhengJieBioinformatics/GENIUS-LLM.git
# Enter the project directory
cd GENIUS-LLM
```

## 2. Fast Configuration
Before running, you must provide your API credentials. GENIUS-LLM is designed to be provider-agnostic.

Edit config/data_config.yaml:
```
model:
    url: https://api.openai.com/v1 # 这里展示API 的基准地址，你可根据自己的情况修改
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
