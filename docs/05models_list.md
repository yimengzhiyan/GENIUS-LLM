# 📊 LLM Support

**GENIUS-LLM** adopts a **Protocol-Oriented Architecture**. We utilize the OpenAI Python library not as a provider-specific lock-in, but as a **universal adapter** for the industry-standard completion protocol.

---

## 1. Supported Models Matrix

The following table explicitly lists the models verified with the current release of GENIUS-LLM. Compatibility is achieved by simply updating the `url` and `model` fields in `data_config.yaml`.

| Model Category | Representative Models | Protocol Status |
| :--- | :--- | :--- |
| **Official OpenAI Models** | GPT-4o, GPT-4 Turbo, GPT-3.5 | Native Support |
| **OpenAI-Compatible Models** | DeepSeek (V3/Chat), Qwen, Moonshot (Kimi), Zhipu AI, Llama 3 (via vLLM) | Universal OpenAI-Style Protocol |

---
> By adhering to the **OpenAI-standardized** API format, **GENIUS-LLM** provides seamless integration across a wide range of providers. Users can switch between high-performance proprietary models and cost-effective local or regional alternatives (like **DeepSeek-V3**) without changing a single line of core code.

---

## 2. Decoupled Architecture

Our `src/model/llm_model.py` is designed with **zero hardcoded endpoints**. The internal logic treats the LLM as a black-box service defined by three parameters in the configuration:

1. **`api_key`**: User-provided credential.
2. **`url`**: The entry point for the API (e.g. `https://api.deepseek.com/v1` or `https://api.openai.com/v1` or `anyother API endpoints you want to use`). 
3. **`model`**: The specific model identifier.

### Why use the `openai` library?
The `openai` Python client has evolved into a standardized wrapper for **RESTful LLM APIs**. By leveraging this library, GENIUS-LLM benefits from:
* **Robust Streaming**: Stable handling of long-context gene function descriptions.
* **Automatic Retries**: Built-in exponential backoff for scientific computing stability.
* **Format Consistency**: Ensures that the JSON output from different providers (DeepSeek vs. GPT) is parsed identically.

---

## 3. How to Switch Models (Step-by-Step)

To switch from the default configuration to a different provider, modify your `config/data_config.yaml` as follows:

### Example: Switching to a  (via vLLM)
```yaml
model:
    url: https://api.openai.com/v1 # Here is the base URL for the API; you can modify it according to your specific LLM configuration.
    api_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx # Replace your api_key
    model: GPT-4o #The model you want to use 
```