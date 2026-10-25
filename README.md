# 🚀 Local Private RAG MCP Server

A Model Context Protocol (MCP) server that empowers your AI clients (like Claude Desktop or Cursor) to securely search through your local documents (PDFs, URLs, and text files) using a local vector database and Ollama embeddings—**100% offline and private**.

---

## ✨ Features

- **🛡️ 100% Private & Local**: Powered by [Ollama](https://ollama.com/) (`nomic-embed-text`) and [LanceDB](https://lancedb.com/), keeping your sensitive documents entirely on your machine.
- **⚡ Dynamic MCP Tools**: Automatically scans your `pdf_inbox/` directory and creates custom search tools per folder based on their `description.md`.
- **👀 Auto-Sync File Watcher**: Drop new PDFs or URL reference files into your inbox folders, and they are automatically embedded and indexed in real time.
- **🔌 Seamless MCP Integration**: Connects effortlessly with Claude Desktop, Cursor, or any other MCP-compliant client.

---

## 🛠️ Prerequisites

Before getting started, make sure you have the following installed:

1. **Python 3.13+** & [uv](https://github.com/astral-sh/uv) (recommended package manager)
2. **Ollama**: Running locally with the embedding model installed.

### Setting up Ollama

1. Download and install [Ollama](https://ollama.com/).
2. Pull the required embedding model (`nomic-embed-text`):
   ```bash
   ollama pull nomic-embed-text
   ```
3. Ensure Ollama is running in the background (usually starts automatically or via `ollama serve`).

---

## 🚀 Setup & Installation

1. **Clone the repository and install dependencies:**
   ```bash
   git clone https://github.com/bartosz-builds/pocket-rag
   cd pocket-rag
   uv sync
   ```

2. **Add your documents to the Inbox:**
   Place your reference materials inside `pdf_inbox/` organized by folders. Each folder should contain:
   - Your PDF files or `.url` files.
   - **URL or Web Location files** (`.url`, `.webloc`) pointing to `llms.txt` endpoints to scrape and index them automatically.
   - A `description.md` explaining what the folder contains (this text is used as the description for the generated MCP search tool).

---

## 🔌 Configuring Claude Desktop (MCP)

To let Claude use your local MCP server, edit your Claude configuration file.

Add `pocket-rag` to your `mcpServers` dictionary (make sure to use the absolute path to your project and `uv`):

```json
{
  "mcpServers": {
    "pocket-rag": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/pocket-rag",
        "run",
        "pocket-rag"
      ]
    }
  }
}
```

Restart Claude Code, and it will automatically have access to your custom local search tools!

---

## 💻 Running Manually / Development

You can test or run the server directly via standard I/O:

```bash
uv run python main.py
```

---

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
