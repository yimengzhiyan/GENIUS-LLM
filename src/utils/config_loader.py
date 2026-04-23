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