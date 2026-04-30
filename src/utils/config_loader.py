<<<<<<< HEAD
import yaml
import os
from typing import Dict, Any

def load_config(config_path: str = None) -> Dict[str, Any]:
    """
    稳健的配置加载器：无论从哪运行，都能自动定位根目录
    """
    if config_path is None or not os.path.isabs(config_path):
        # 1. 获取当前文件 src/utils/config_loader.py 的绝对路径
        current_file = os.path.abspath(__file__)
        # 2. 向上跳两级回到项目根目录 (utils -> src -> root)
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_file)))
        
        # 3. 如果没传路径，默认找 config/data_config.yaml
        if config_path is None:
            config_path = os.path.join(project_root, 'config', 'data_config.yaml')
        else:
            # 如果传了相对路径（如 "config/data_config.yaml"），将其转换为绝对路径
            config_path = os.path.join(project_root, config_path)

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"❌ 找不到配置文件: {config_path}")
        
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML: {str(e)}")
=======
# src/utils/config_loader.py
import yaml
from typing import Dict, Any
import os

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from YAML file
    
    Args:
        config_path (str): Path to configuration file
        
    Returns:
        Dict[str, Any]: Configuration dictionary
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        yaml.YAMLError: If config file is invalid
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            
        return config
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing configuration file: {str(e)}")
>>>>>>> upstream/main
