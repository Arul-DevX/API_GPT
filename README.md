# 🤖 JerryBot – AI Chat App (OpenRouter + Streamlit)

JerryBot is a simple AI chatbot built with [Streamlit](https://streamlit.io/) and [OpenRouter](https://openrouter.ai).  
It lets you chat with different open-source and premium AI models in a clean web UI.

---

## 🚀 Features
- 🟢 Chat with AI in a Streamlit app
- 🧠 Uses OpenRouter API (supports many models like Mistral, LLaMA, Gemma, GPT, Claude, etc.)
- 💾 Maintains conversation history (session state)
- ⚡ Easy to deploy on Streamlit Cloud or HuggingFace Spaces

---

## 📂 Project Structure
jerrybot/
├── main.py # Streamlit app
├── requirements.txt # Dependencies
└── .streamlit/
└── secrets.toml # API keys (DO NOT commit to GitHub!)

yaml
Copy
Edit

---

## 🔑 Setup Instructions

### 1. Clone repo
- git clone https://github.com/<your-username>/jerrybot.git
- cd jerrybot
### 2. Install dependencies
- pip install -r requirements.txt
### 3. Add API key
- Create a file .streamlit/secrets.toml:
- openrouter_api = "your_api_key_here"
### 4. Run app
- streamlit run main.py
## 🌐 Deployment
- Streamlit Cloud: Connect your GitHub repo, add API key in project settings → Secrets.

## 📸 Screenshot
<img width="1917" height="1015" alt="image" src="https://github.com/user-attachments/assets/67d71aed-90a8-4f12-aa10-8e80ecd14d90" />


## 👨‍💻 Author
- Built by Scarlet ✨ – Data Analyst & AI Enthusiast.
- Feel free to connect on LinkedIn 🚀










Ask ChatGPT
