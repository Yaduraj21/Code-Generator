import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

#Frontend

st.title("🧠 Code-Generator 🧠")
st.caption("This Deepseek AI model helps you to generate code")

#Slidern configuration

with st.sidebar:
    st.header("⚙️ Model Configuration ")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1: 7b"],
        index = 0
    )

    st.divider()     
    st.markdown("### 🧠 Model Capabilities")
    st.markdown("""
        -Python Expert
        -Debugging Assistant
        -Code Documentation
        -Solution Design
        """)
    st.divider()
    st.markdown("Built with  [Ollama](http://ollama.ai/) | [Langchain](http://python.langchain.com/)")
    st.markdown("Powered by [Deepseek](http://deepseek.ai/)")
    st.header("Developed by:- Yaduraj Singh Yadav")

# Backend

# Function to build prompt chain
def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

#Initiate chat engine
llm_engine = ChatOllama(model = selected_model,
                        base_url = "http://localhost:11434",
                        temperature = 0.3)
system_prompt = SystemMessagePromptTemplate.from_templete(
    "You are an expert AI coding assistant. Provide consise, correct sollutions"
    "with strategic print statements for drbugging. Always response in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today?"}]  

# Chat container
chat_container = st.conatiner()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
user_query = st.chat_input("Type your question here...")
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})

    # AI response
    with st.spinner("Processing..."):
        prompt_chain = build_prompt_chain() 
        ai_response = generate_ai_response(prompt_chain)
    # Add AI response to message log
    st.session_state.message_log.append({"role": "ai", "content": ai_response})

    # Return to update chat display
    st.rerun()