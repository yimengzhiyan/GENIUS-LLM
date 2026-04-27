# 📊 LLM Support

**GENIUS-LLM** adopts a **Protocol-Oriented Architecture**. We utilize the OpenAI Python library not as a provider-specific lock-in, but as a **universal adapter** for the industry-standard completion protocol.

---

## 1. Supported Models Matrix

The following table explicitly lists the models verified with the current release of GENIUS-LLM. Compatibility is achieved by simply updating the `url` and `model` fields in `data_config.yaml`.

| Model Category | Representative Models | Protocol Status | Support Level |
| :--- | :--- | :--- | :--- |
| **OpenAI Series** | GPT-4o, GPT-4-turbo, GPT-3.5 | Native | ✅ Verified |
| **DeepSeek Series** | DeepSeek-V3, DeepSeek-Chat | OpenAI-Compatible | ✅ Verified |
| **Local LLMs** | Llama 3, Qwen, Mistral | via vLLM / Ollama | ✅ Verified |
| **National LLMs** | Moonshot (Kimi), Zhipu AI | OpenAI-Compatible | ✅ Verified |
| **Other Protocols**| Claude, Gemini | Native SDK | 🔄 via Proxy* |

> **Note on Claude/Gemini**: To maintain a lightweight codebase without dependency bloat, native SDKs for Anthropic/Google are not included. However, users can access these models via API gateways (e.g., **One-API** or **LiteLLM**) that convert their requests into the standard OpenAI format.

---

## 2. Decoupled Architecture

Our `src/model/llm_model.py` is designed with **zero hardcoded endpoints**. The internal logic treats the LLM as a black-box service defined by three parameters in the configuration:

1. **`api_key`**: User-provided credential.
2. **`url`**: The entry point for the API (e.g., `https://api.deepseek.com/v1`).
3. **`model`**: The specific model identifier.

### Why use the `openai` library?
The `openai` Python client has evolved into a standardized wrapper for **RESTful LLM APIs**. By leveraging this library, GENIUS-LLM benefits from:
* **Robust Streaming**: Stable handling of long-context gene function descriptions.
* **Automatic Retries**: Built-in exponential backoff for scientific computing stability.
* **Format Consistency**: Ensures that the JSON output from different providers (DeepSeek vs. GPT) is parsed identically.

---

## 3. How to Switch Models (Step-by-Step)

To switch from the default configuration to a different provider, modify your `config/data_config.yaml` as follows:

### Example: Switching to a Local Llama-3 (via vLLM)
```yaml
model:
  api_key: "not-needed-for-local"
  url: "http://localhost:8000/v1"
  model: "meta-llama/Meta-Llama-3-8B-Instruct"
```