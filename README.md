# EssentiaAI

EssentiaAI is a local-first, command-line tool for abstractive text summarization. It uses Hugging Face's `google/pegasus-xsum` model, built on top of PyTorch and Transformers, to generate high-quality summaries from long-form content.

## Features

- High-performance summarization using `google/pegasus-xsum`
- Runs entirely offline after setup — no API keys or external services
- Simple CLI interface for quick usage
- Built with Python 3, PyTorch, and Hugging Face Transformers
- Keeps all input data on your local machine for privacy

## Installation

Ensure Python 3.8 or later is installed.

```bash
git clone https://github.com/michelleduong03/EssentiaAI.git
cd EssentiaAI
pip install -r requirements.txt
