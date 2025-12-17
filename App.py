import streamlit as st
from Indexing import build_vector_store_from_url
from Agent import create_rag_agent

import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Web RAG Agent", layout="wide")

st.title("🔗 Web-based RAG Agent")
st.write("Paste a blog or article URL, then ask questions about it.")

# ---------------------------
# Session State Initialization
# ---------------------------
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "agent" not in st.session_state:
    st.session_state.agent = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------------------
# URL Input & Indexing
# ---------------------------
url = st.text_input("Article / Blog URL")

if st.button("Process Article"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Processing article..."):
            st.session_state.vector_store = build_vector_store_from_url(url)
            st.session_state.agent = create_rag_agent(
                st.session_state.vector_store
            )

            # Clear old chat when new article is indexed
            st.session_state.chat_history = []

        st.success("Article indexed successfully! You can now chat with it.")

# ---------------------------
# Chat Interface
# ---------------------------
if st.session_state.agent:

    st.markdown("### 💬 Chat")

    # Display previous messages
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    # User input
    query = st.chat_input("Ask a question about the article")

    if query:
        # Save user message
        st.session_state.chat_history.append(
            {"role": "user", "content": query}
        )

        st.chat_message("user").write(query)

        # Agent response
        with st.spinner("Generating answer..."):
            for event in st.session_state.agent.stream(
                {"messages": st.session_state.chat_history},
                stream_mode="values",
            ):
                response = event["messages"][-1].content

        # Save assistant message
        st.session_state.chat_history.append(
            {"role": "assistant", "content": response}
        )

        st.chat_message("assistant").write(response)

