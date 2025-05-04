# 🧠 DeepSeek Agent

A local AI assistant powered by [LangChain](https://github.com/langchain-ai/langchain), [LangGraph](https://github.com/langchain-ai/langgraph), and [Ollama](https://github.com/ollama/ollama), using the `deepseek-coder-v2` model.

Supports:
- 🖥 Terminal interface
- 🌐 Web UI with Gradio
- 🧩 Plug-and-play LangChain agents

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/ekalachev/agent_ai.git
cd agent_ai
```

2.	(Optional but recommended) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3.	Install dependencies:

```bash
pip install -r requirements.txt
```


⸻

🤖 Run in Terminal

```bash
./run_agentic_cli.sh
```

You’ll see:

🔹 DeepSeek Agent (terminal mode). Type Ctrl-C or 'exit' to quit.



⸻

🌐 Run the Web UI

```bash
./run_agentic_app.sh
```

The UI will launch in your browser. You can also share the link with others.

⸻

🧠 Model Used

This project uses the `deepseek-coder-v2:16b-lite-instruct-q4_K_M` model via Ollama.

Make sure it’s installed locally:
```bash
ollama pull deepseek-coder-v2:16b-lite-instruct-q4_K_M
```

⸻

🔐 Optional: Use Tavily Search Tool

If you want to enable search with Tavily, set your API key:

```python
export TAVILY_API_KEY=your_api_key_here
```

And uncomment this line in src/agent.py:

```python
# search = TavilySearchResults(max_results=2)
# tools = [search]
```
