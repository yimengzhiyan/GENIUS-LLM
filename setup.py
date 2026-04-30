"""
@author: Jie Zheng 
@last modified by: Jie Zheng
@time: 2026/4/17 10:38
"""

from setuptools import setup, find_packages
import sys
from pathlib import Path

# --- 1. Environment Hard Check ---
# Python 3.8+ is recommended to support modern LLM libraries and asynchronous requests.
if sys.version_info < (3, 8):
    sys.exit('GENIUS-LLM requires Python >= 3.8')

# Get the project root directory path
HERE = Path(__file__).parent

# --- 2. Dynamic Requirement Loading ---
# This ensures you only need to modify requirements.txt in the future.
def read_requirements():
    req_file = HERE / 'requirements.txt'
    if req_file.exists():
        return [l.strip() for l in req_file.read_text('utf-8').splitlines() if l.strip() and not l.startswith('#')]
    
    # Fallback to default list if requirements.txt is missing
    return ["openai", "pandas", "pymongo", "pyyaml", "mkdocs-material", "openpyxl"]

setup(
    name="genius_llm",
    version="1.1.0",
    author="Zheng Jie",
    packages=find_packages(), # Automatically finds all packages containing __init__.py
    
    # Passing the parsed requirements.txt content to install_requires
    install_requires=read_requirements(), 
    
    include_package_data=True, # Must be True for MANIFEST.in to take effect
    
    entry_points={
        'console_scripts': [
            # Defined commands allow users to run scripts directly from the terminal
            'genius-process=scripts.process_data:main',
            'genius-import=scripts.import_data:main',
            'genius-predict=scripts.predict:main',
        ],
    },
)