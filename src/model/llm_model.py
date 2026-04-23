# model/llm_model.py

import yaml
import os
from openai import OpenAI
from .base_model import BaseModel

class LLMModel(BaseModel):
    def __init__(self):
        # --- 核心改进：基于文件物理位置定位项目根目录 ---
        # 1. 获取当前文件 (llm_model.py) 的绝对路径
        current_file_path = os.path.abspath(__file__)
        
        # 2. 向上跳三级找到项目根目录
        # 第一级: src/model/ (当前目录)
        # 第二级: src/
        # 第三级: 20260410GENIUS-LLM/ (项目根目录)
        model_dir = os.path.dirname(current_file_path)
        src_dir = os.path.dirname(model_dir)
        project_root = os.path.dirname(src_dir)

        # 3. 组合最终的 config 路径，不再使用依赖当前路径的 os.getcwd()
        config_path = os.path.join(project_root, 'config', 'data_config.yaml')

        # 4. 加载配置
        try:
            with open(config_path, 'r', encoding='utf-8') as config_file:
                config = yaml.safe_load(config_file)
        except FileNotFoundError:
            # 增加更详细的错误提示，方便审稿人调试
            raise FileNotFoundError(f"Config file not found. Expected path: {config_path}")

        # 严格配置驱动逻辑 (URL 的去硬编码) 
        model_config = config.get('model')
        if not model_config:
            raise ValueError("Error: 'model' section is missing in data_config.yaml.")

        # 强制要求用户提供 URL，代码中不存任何默认服务器地址
        self.base_url = model_config.get('url')
        if not self.base_url:
            raise ValueError(
                "Critical Error: 'url' is missing in data_config.yaml. "
                "Please specify your LLM API endpoint (e.g., DeepSeek or OpenAI)."
            )

        # 强制要求 API Key
        self.api_key = model_config.get('api_key')
        if not self.api_key:
            raise ValueError("Critical Error: 'api_key' is missing in data_config.yaml.")

        # 强制要求模型名称
        self.model_name = model_config.get('model')
        if not self.model_name:
            raise ValueError("Critical Error: 'model' (ID) is missing in data_config.yaml.")

        # --- 初始化协议适配器 ---
        # 此时 self.base_url 完全来自用户的配置文件
        # 这里的 OpenAI 库仅作为支持标准协议的“引擎”
        self.client = OpenAI(
            api_key=self.api_key, 
            base_url=self.base_url
        )
    def call_api(self, prompt):
        """调用 API 生成预测结果，包含断点续接逻辑"""
        full_content = ""

        try:
            # 第一次请求
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "system", "content": "You are a helpful assistant specialized in gene prediction."},
                          {"role": "user", "content": prompt}],
                stream=False
            )

            full_content = response.choices[0].message.content

            # 你的原始逻辑：如果因为长度截止，则循环继续
            while response.choices[0].finish_reason == "length":
                # 使用当前已生成内容作为 Prompt 继续
                prompt = full_content 
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "system", "content": "You are a helpful assistant specialized in gene prediction."},
                              {"role": "user", "content": prompt}],
                    stream=False
                )
                full_content += response.choices[0].message.content

            return full_content
        except Exception as e:
            return f"Error calling API: {str(e)}"