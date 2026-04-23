import os
import logging
import sys
from pymongo import MongoClient

# --- 1. 动态确定项目根目录 ---
# scripts/import_data.py -> 向上跳一级即为根目录
current_file = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(current_file))

# 将根目录添加到 sys.path 以确保 src 模块可被导入
if project_root not in sys.path:
    sys.path.append(project_root)

from src.utils.config_loader import load_config
from src.importers.importer_factory import MongoImporterFactory

def setup_logging(log_path: str):
    """设置日志配置，使用绝对路径确保 Linux 环境稳健"""
    os.makedirs(log_path, exist_ok=True)
    log_file = os.path.join(log_path, "import_data.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    # --- 2. 加载配置 (使用我们重构后的 load_config) ---
    try:
        config = load_config() # 不传参，它会自动定位项目根目录下的 config/data_config.yaml
    except Exception as e:
        print(f"Critical Error loading config: {e}")
        return

    # --- 3. 处理日志路径 ---
    # 将配置里的相对路径转为绝对路径
    abs_log_path = os.path.join(project_root, config['common']['log_path'])
    setup_logging(abs_log_path)
    
    # --- 4. 初始化 MongoDB 客户端 ---
    client = None
    try:
        client = MongoClient(config['mongodb']['uri'])
        db = client[config['mongodb']['database']]
        
        importer_factory = MongoImporterFactory()
        
        # --- 5. 循环导入数据 (全量路径绝对化) ---
        for data_type, import_config in config['data_imports'].items():
            print(f"Starting import for {data_type}...")
            
            # 关键：将配置中的相对输入路径转为绝对路径
            abs_file_path = os.path.join(project_root, import_config['input_path'])
            
            print(f"  Source file: {abs_file_path}")
            logging.info(f"Starting import for {data_type} from {abs_file_path}")

            try:
                # 检查文件物理是否存在，防止后续报错
                if not os.path.exists(abs_file_path):
                    msg = f"  ❌ File Not Found: {abs_file_path}"
                    print(msg)
                    logging.error(msg)
                    continue

                importer = importer_factory.get_importer(
                    data_type,
                    db_uri=config['mongodb']['uri'],
                    db_name=config['mongodb']['database']
                )
                
                # 传入绝对路径进行导入
                importer.run(
                    file_path=abs_file_path,
                    collection_name=import_config['collection']
                )
                
                logging.info(f"Successfully imported {data_type} data")
                print(f"  ✅ Finished import for {data_type}.")
                
            except Exception as e:
                error_msg = f"Error importing {data_type} data: {str(e)}"
                logging.error(error_msg)
                print(f"  ❌ {error_msg}")
                
    except Exception as e:
        msg = f"Error connecting to MongoDB: {str(e)}"
        logging.error(msg)
        print(msg)
        
    finally:
        if client:
            client.close()

if __name__ == "__main__":
    main()