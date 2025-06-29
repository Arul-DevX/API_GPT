import streamlit as st
from openai import OpenAI

# Setup OpenRouter (new openai client)
client = OpenAI(
    api_key=st.secrets["openrouter_api"],
    base_url="https://openrouter.ai/api/v1"
)

# Chat UI
st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are Jerry, a helpful assistant."}]

user_input = st.chat_input("Ask something...")

# Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            chat_completion = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct",  # You can change model
                messages=st.session_state.messages
            )
            reply = chat_completion.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
