# 🛠️ Installation Guide

This guide provides step-by-step instructions for setting up **GENIUS-LLM**. We focus on ensuring a robust installation process across various environments, with a particular emphasis on **Linux-based High-Performance Computing (HPC)** and **Windows (WSL2/Native)** systems.

---

## 1. Prerequisites

Before starting, please ensure your system meets the following requirements to ensure stability:

* **Operating System**: Linux (Ubuntu 20.04+, CentOS 7+), macOS, or Windows 10/11.
* **Python Version**: 3.8, 3.9, or 3.10 (Tested for stability with asynchronous LLM calls).
* **Database**: **MongoDB** (v4.4 or higher) must be available as the backend for gene annotation storage.

---

## 2. Environment Management (Recommended)

To avoid library version conflicts and ensure reproducibility, we strongly recommend using a Conda virtual environment.

```bash
# Create a clean environment
conda create -n genius_llm python=3.9 -y

# Activate the environment
conda activate genius_llm
```
## 3. Installation

To install **GENIUS-LLM**, follow these steps:
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
## 4. 数据库设置与初始化
GENIUS-LLM 利用 MongoDB 进行高速基因数据检索。服务必须处于激活状态，才能运行预测。

🔹 Linux（systemd）：

1.对于拥有 root 权限（sudo）的用户
```
sudo systemctl start mongod
# Verify status
sudo systemctl status mongod
```

2.对于没有 root 权限的用户
```
# Create a local data directory
mkdir -p ~/mongodb_data
# Launch MongoDB locally on the default port
mongod --dbpath ~/mongodb_data --port 27017 --fork --logpath ~/mongodb_data/mongodb.log
```
🔹 对于Windows的用户：
win+R ，输入services.msc，右键启动MongoDB Server (MongoDB)。


"Everything set? Move to Quick Start Guide to run your first gene prediction!"


