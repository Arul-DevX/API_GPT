import streamlit as st
import openai

# Configure OpenRouter API
openai.api_key = st.secrets["openrouter_api"]
openai.api_base = "https://openrouter.ai/api/v1"

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are Jerry, a helpful assistant."}]

st.title("🤖 Jerry - Chatbot using OpenRouter")

# Chat input
user_input = st.chat_input("Ask Jerry anything...")

# Show past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process new message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = openai.ChatCompletion.create(
                model="mistralai/mistral-7b-instruct",  # Or try: meta-llama/llama-3-8b-instruct
                messages=st.session_state.messages,
            )
            reply = response.choices[0].message["content"]
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
