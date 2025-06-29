import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["gemini_api"])

def ai(txt):
    model = genai.GenerativeModel('models/gemini-1.5-pro')  # ✅ Correct model name
    response = model.generate_content("AI Assistant " + txt)
    return response.text

# Layout with image and title
col1, col2 = st.columns([1, 4])
with col2:
    st.title("Chat with AI Assistant")

command = st.chat_input("How can I help you?")

if "message" not in st.session_state:
    st.session_state.message = []

for chat in st.session_state.message:
    with st.chat_message(chat["role"]):  # ✅ Use correct role
        st.write(chat["message"])

if command:
    with st.chat_message("user"):
        st.write(command)
        st.session_state.message.append({"role": "user", "message": command})  # ✅ Fix spelling

    if "hai" in command:
        reply = "Hello there, how can I help you! 😃"
    elif "Who are you?" in command:
        reply = "I am a chat bot, my name is 'Jerry'!!"
    elif "what are you doing?" in command:
        reply = "I am waiting for your questions!!"
    else:
        reply = ai(command)

    with st.chat_message("bot"):
        st.write(reply)
        st.session_state.message.append({"role": "bot", "message": reply})  # ✅ Fix spelling
