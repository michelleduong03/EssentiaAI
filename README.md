# 🧠 EssentiaAI

EssentiaAI is a lightweight, local-first command-line tool for abstractive text summarization. It leverages Hugging Face's `google/pegasus-xsum` — a state-of-the-art transformer model — to generate concise and context-aware summaries from long-form text.

The project is designed to be privacy-conscious, fast to set up, and easy to use. All processing happens locally, ensuring full control over your data.

---

## 🚀 Features

- **High-quality summarization** using `google/pegasus-xsum`, optimized for short, informative summaries
- **Runs locally** after setup — no internet access, API keys, or external dependencies required at runtime
- **Built on robust libraries**: Hugging Face Transformers and PyTorch
- **Simple, interactive CLI** for pasting or typing input directly into the terminal
- **Privacy-first design** — nothing is sent over the network, and no data is logged or stored

---

## 📦 Installation

Ensure Python 3.8 or higher is installed on your system.

```bash
git clone https://github.com/michelleduong03/EssentiaAI.git
cd EssentiaAI
pip install -r requirements.txt
