"""
@author: Jie Zheng 
@last modified by: Jie Zheng
@time: 2026/4/17 10:38
"""

from setuptools import setup, find_packages
import sys
from pathlib import Path

# --- 1. 环境硬检查  ---
# 考虑到 LLM 库和异步请求，建议至少 3.8+
if sys.version_info < (3, 8):
    sys.exit('GENIUS-LLM requires Python >= 3.8')

# 获取项目根目录路径
HERE = Path(__file__).parent

# --- 2. 动态读取依赖  ---
# 这样你以后只需要修改 requirements.txt 即可
def read_requirements():
    req_file = HERE / 'requirements.txt'
    if req_file.exists():
        return [l.strip() for l in req_file.read_text('utf-8').splitlines() if l.strip() and not l.startswith('#')]
    # 如果没有文件，则使用你的默认列表
    return ["openai", "pandas", "pymongo", "pyyaml", "mkdocs-material", "openpyxl"]
setup(
    name="genius_llm",
    version="1.1.0",
    author="Zheng Jie",
    packages=find_packages(), # 它现在能自动找到包含 __init__.py 的所有文件夹
    # 这样修改后，setup.py 才会真正去读取 requirements.txt 的内容
    install_requires=read_requirements(), 
    include_package_data=True, # 记得加上这个，否则 MANIFEST.in 不生效,
    entry_points={
        'console_scripts': [
            # 这样定义后，审稿人只需在终端输入 genius-predict 就能运行你的脚本
            'genius-process=scripts.process_data:main',
            'genius-import=scripts.import_data:main',
            'genius-predict=scripts.predict:main',
        ],
    },
)