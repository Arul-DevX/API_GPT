import streamlit as st
from openai import OpenAI  # Requires openai>=1.0.0

# Setup OpenRouter-compatible client
client = OpenAI(
    api_key=st.secrets["openrouter_api"],
    base_url="https://openrouter.ai/api/v1"
)

# Title
st.title("Jerry - Your AI Buddy (OpenRouter)")

# Initialize session
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Jerry, a helpful assistant."}
    ]

# Sidebar: Model selector
model = st.sidebar.selectbox(
    "Choose a model",
    [
        "mistralai/mistral-7b-instruct",
        "meta-llama/llama-2-13b-chat",
        "google/gemma-7b-it"
    ]
)

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
            response = None
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=st.session_state.messages,
                )
                # ✅ Correct attribute access
                reply = response.choices[0].message.content
            except Exception as e:
                reply = f"❌ Error: {e}"
            st.markdown(reply)
    
    # Save reply to history
    st.session_state.messages.append({"role": "assistant", "content": reply})
    
    # Sidebar token usage info
    if response and hasattr(response, "usage"):
        st.sidebar.write("Tokens used:", response.usage.total_tokens)
