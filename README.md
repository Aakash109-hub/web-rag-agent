# Web-Based RAG Agent 🧠🔗

A **Web-based Retrieval-Augmented Generation (RAG) application** that allows users to paste any blog or article URL and ask questions strictly based on the provided content.

This project demonstrates an **end-to-end RAG pipeline** with web content ingestion, vector indexing, multi-turn chat, agent-based retrieval, and full observability using **LangSmith**.

---

## 🚀 Features

* 🌐 **Web Content Ingestion** – Load and parse articles directly from URLs
* ✂️ **Text Chunking** – Recursive character-based splitting
* 🧩 **Vector Indexing** – FAISS vector store with HuggingFace embeddings
* 🤖 **Agent-based RAG** – LangChain agent with tool-based retrieval
* 💬 **Multi-turn Chat** – Conversation memory using Streamlit session state
* 📊 **Observability** – Full tracing and monitoring with LangSmith
* 🖥️ **Interactive UI** – Built using Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **FAISS**
* **HuggingFace Embeddings** (`all-mpnet-base-v2`)
* **Ollama** (local LLM inference)
* **Streamlit** (web UI)
* **LangSmith** (monitoring & tracing)

---

## 📂 Project Structure

```
web-rag-agent/
│
├── app.py                # Streamlit UI
├── Indexing.py           # Web loading + vector store creation
├── Agent.py              # RAG agent definition
├── .env                  # Environment variables (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Aakash109-hub/web-rag-agent.git
cd web-rag-agent
```

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=Webbase-rag
```

Make sure **Ollama** is running locally with a supported model (e.g., `qwen3:1.7b`).

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. User pastes a **web article URL**
2. The system:

   * Loads web content
   * Splits text into chunks
   * Creates embeddings
   * Stores them in FAISS
3. User asks questions about the article
4. The agent retrieves relevant chunks and generates answers
5. All steps are **monitored in LangSmith**

---

## 📹 Demo Use Case

Example queries:

* *What is Google Antigravity and how can it be used?*
* *How can we set up a project in Google Antigravity?*

These questions ensure the **retriever is invoked**, not just the LLM’s pre-trained knowledge.

---

## 📈 Observability with LangSmith

LangSmith provides visibility into:

* Agent runs
* Tool calls
* Retrieved chunks
* Token usage & latency

This helps debug and improve RAG performance.

---

## 🎯 Learning Outcomes

* Understanding of RAG pipelines
* Agent-based orchestration
* Vector databases & embeddings
* Monitoring LLM systems
* Building production-style AI apps

---

## 🤝 Future Improvements

* Source citations for answers
* Chunk preview in UI
* Multiple document support
* Retrieval score thresholds

---
---

⭐ If you find this project useful, feel free to star the repository!
