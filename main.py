import streamlit as st
from openai import OpenAI  # Requires openai>=1.0.0

# Setup OpenRouter-compatible client
client = OpenAI(
    api_key=st.secrets["openrouter_api"],
    base_url="https://openrouter.ai/api/v1"
)

# Title
st.title("💬 Chat with Jerry (via OpenRouter)")

# Initialize session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Jerry, a helpful assistant."}
    ]

# Input box
user_input = st.chat_input("Ask something...")

# Display conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Process input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="mistralai/mistral-7b-instruct",  # Or try other free models
                    messages=st.session_state.messages,
                )
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"❌ Error: {e}"
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
