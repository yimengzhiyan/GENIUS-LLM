# 🛠️ Installation Guide

This guide provides step-by-step instructions for setting up **GENIUS-LLM**. We focus on ensuring a robust installation process across various environments, with a particular emphasis on **Linux-based High-Performance Computing (HPC)** and **Windows (WSL2/Native)** systems.

---

## 1. Prerequisites

Before starting, please ensure your system meets the following requirements to ensure stability:

* **Operating System**: Linux (Ubuntu 20.04+, CentOS 7+), macOS, or Windows 10/11.
* **Python Version**: 3.9, 3.10, or 3.12 (Tested for stability with asynchronous LLM calls).
* **Database**: **MongoDB** (v4.4 or higher) must be available as the backend for gene annotation storage.

---

## 2. Environment Management (Recommended)

To avoid library version conflicts and ensure reproducibility, we strongly recommend using a Conda virtual environment.

```bash
# Create a clean environment
conda create -n genius_llm python=3.12 -y

# Activate the environment
conda activate genius_llm
```
## 3. Installation

To install **GENIUS-LLM**, follow these steps:
```
# 1. Clone the repository
git clone https://github.com/ZhengJieBioinformatics/GENIUS-LLM.git
cd GENIUS-LLM

# 2. Install dependencies first to avoid failures
pip install -r requirements.txt

# 3. Install GENIUS-LLM in editable mode
pip install -e .
```
Find out packages that lead to failures, then create a new requirements.txt of them and run:
```
pip install -r requirements.txt
```
## 4. Database Setup & Initialization
GENIUS-LLM utilizes **MongoDB** for high-speed genomic data retrieval. The MongoDB service must be active before running any predictions.
```bash
conda install mongodb mongodb-shell mongodb-tools -c conda-forge -y
```

🔹 For Linux Users (systemd):

Option 1: Users with Root/Sudo Privileges
```bash
sudo systemctl start mongod
# Verify status
sudo systemctl status mongod
```

Option 2: Users without Root Privileges (Local Instance)
```bash
# Create a local data directory
mkdir mongodb_data
# Launch MongoDB locally on the default port
mongod --dbpath ~/mongodb_data --port 27017 --fork --logpath ~/mongodb_data/mongodb.log
```
🔹 For Windows Users:

1. Press **Win + R**, type **services.msc**, and hit **Enter**.

2. Locate **MongoDB Server (MongoDB)** in the list.

3. Right-click it and select **Start**.


"Everything set? Move to **Quick Start Guide** to run your first gene prediction!"


