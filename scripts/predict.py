import yaml
import logging
import os
import sys

# 引入项目模块
from src.model.model_factory import ModelFactory
from src.prompt.prompt_factory import PromptFactory

def main():
    """
    GENIUS-LLM 主预测入口函数
    """
    # --- 1. 动态路径处理 (解决 FileNotFoundError) ---
    # 获取当前脚本的绝对路径
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    # 定位项目根目录 (假设 scripts 与 config 平级)
    project_root = os.path.dirname(current_script_path)
    
    config_path = os.path.join(project_root, 'config', 'data_config.yaml')
    log_dir = os.path.join(project_root, 'logs')

    # --- 2. 加载配置 ---
    try:
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config = yaml.safe_load(config_file)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {config_path}")
        sys.exit(1)

    # --- 3. 设置日志 ---
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, 'predict.log')
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    # --- 4. 执行预测逻辑 ---
    print("\n--- GENIUS-LLM Prediction System ---")

    # 检查命令行是否提供了参数，如果没有，则使用默认值或提示退出
    if len(sys.argv) > 1:
        gene_id = sys.argv[1]
    else:
        # 方案 A: 给出默认值
        gene_id = "AT1G03000" 
        print(f"No Gene ID provided, using default: {gene_id}")
        
    logger.info(f"Starting prediction for Gene ID: {gene_id}")

    # Step A: 生成 Prompt
    try:
        prompt_generator = PromptFactory.create_prompt(prompt_type='gene')
        prompt = prompt_generator.generate_prompt(gene_id)
        logger.info(f"Prompt successfully generated.")
    except Exception as e:
        logger.error(f"Prompt Generation Failed: {e}")
        return

    # Step B: 调用模型 (这里会进入你提到的 model_factory 和 llm_model)
    try:
        model = ModelFactory.create_model(model_type='llm')
        result = model.call_api(prompt)
        logger.info("Model response received.")
    except Exception as e:
        logger.error(f"Model API Call Failed: {e}")
        return

    # Step C: 输出结果
    print("\n=== Prediction Result ===\n", result)
    logger.info("Task completed successfully.")

    # Step D: 结果持久化 ---
        # 1. 从 config 中读取你新定义的路径
    rel_result_path = config.get('common', {}).get('predict_result_output_path', 'predict_results')
    
        # 2. 拼接为绝对路径，确保跨平台运行
    results_dir = os.path.join(project_root, rel_result_path)
    
        # 3. 自动创建文件夹 (如果不存在)
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        logger.info(f"Created results directory: {results_dir}")
    
        # 4. 保存为以基因 ID 命名的文本文件
    result_file = os.path.join(results_dir, f"{gene_id}_prediction.txt")
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    logger.info(f"Prediction result successfully saved to {result_file}")

if __name__ == "__main__":
    main()
