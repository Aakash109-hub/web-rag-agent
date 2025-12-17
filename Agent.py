from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_community.vectorstores import FAISS


def create_rag_agent(vector_store: FAISS):
    """Create a RAG agent using an existing vector store."""

    @tool
    def retrieve_context(query: str) -> str:
        """Retrieve relevant context from the ingested article."""
        docs = vector_store.similarity_search(query, k=3)
        return "\n\n".join(doc.page_content for doc in docs)

    model = ChatOllama(model="qwen3:1.7b")

    system_prompt = (
        "You are a helpful assistant. "
        "Answer questions ONLY using the provided article context. "
        "If the answer is not found in the article, say so clearly."
    )

    agent = create_agent(
        model=model,
        tools=[retrieve_context],
        system_prompt=system_prompt,
    )

    return agent
