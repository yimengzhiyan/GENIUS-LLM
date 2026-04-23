import logging
import os
import sys

# 导入你的工具类
from src.utils.config_loader import load_config
from src.processors.processor_factory import DataProcessorFactory

def setup_logging(log_path: str):
    """Set up logging configuration"""
    # 确保 log_path 也是绝对路径
    os.makedirs(log_path, exist_ok=True)
    logging.basicConfig(
        filename=os.path.join(log_path, "process_data.log"),
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    # --- 1. 获取项目根目录 (GPS 逻辑) ---
    # 这里的逻辑和 config_loader 保持一致，确保万无一失
    current_file = os.path.abspath(__file__)
    # scripts/process_data.py -> 向上跳一级就是根目录
    project_root = os.path.dirname(os.path.dirname(current_file))

    # --- 2. 加载配置 (不再传参数，靠 loader 自己找) ---
    try:
        config = load_config()
    except Exception as e:
        print(f"Critical Error loading config: {e}")
        return

    # --- 3. 转换 Log 路径并初始化 ---
    # 将配置里的 common/log_path 转换为绝对路径
    absolute_log_path = os.path.join(project_root, config['common']['log_path'])
    setup_logging(absolute_log_path)
    
    # --- 4. 准备数据处理器工厂 ---
    processor_factory = DataProcessorFactory()
    
    # --- 5. 循环处理数据 (路径全量绝对化) ---
    for data_type, paths in config['data_paths'].items():
        try:
            # 关键步骤：将配置里的相对路径拼接为绝对路径
            abs_input = os.path.join(project_root, paths['input'])
            abs_output = os.path.join(project_root, paths['output'])

            # 自动创建输出文件夹（防止报错）
            os.makedirs(os.path.dirname(abs_output), exist_ok=True)

            print(f"Processing {data_type}...")
            print(f"  Input: {abs_input}")

            processor = processor_factory.get_processor(
                data_type,
                abs_input,
                abs_output
            )
            processor.run()
            
            logging.info(f"Successfully processed {data_type} data")
            print(f"✅ {data_type} processed successfully.")

        except Exception as e:
            error_msg = f"Error processing {data_type} data: {str(e)}"
            logging.error(error_msg)
            print(f"❌ {error_msg}")

if __name__ == "__main__":
    main()