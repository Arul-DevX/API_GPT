import streamlit as st
import google.generativeai as genai
genai.configure(api_key=st.secrets["gemini_api"])
def ai(txt):
    
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(" AI Assistant "+txt)
    return response.text

# Layout with image and title
col1, col2 = st.columns([1, 4])
with col2:
    st.title("Chat with AI Assistant")
command = st.chat_input("How can I help you?")

if "message" not in st.session_state:
    st.session_state.message=[]

for chat in st.session_state.message:
    with st.chat_message("role"):
        st.write(chat["message"])


if command:
    with st.chat_message("user"):
        st.write(command)
        st.session_state.message.append({"role":"uer","message":command})
    if "hai"in command:
        with st.chat_message("bot"):
            st.write("Hello there how can I help you !!!....😃")
            st.session_state.message.append({"role":"uer","message":"Hello there how can I help you !!!....😃"})
    elif "Who are you?" in command:
        with st.chat_message("bot"):
            st.write("I am a chat bot ,my name is 'Jerry'!!")
            st.session_state.message.append({"role":"uer","message":"I am a chat bot."})
    elif "what are you doing?" in command:
        with st.chat_message("bot"):
            st.write("I am waiting for your questions!!")
            st.session_state.message.append({"role":"uer","message":"Waiting for your Question"})
    else:
          with st.chat_message("bot"):
            data=ai(command)
            st.write(data)
            st.session_state.message.append({"role":"uer","message":data})       


