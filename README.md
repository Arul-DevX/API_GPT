# JerryBot – AI Chat App (OpenRouter + Streamlit)

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
```bash
jerrybot/
├── main.py # Streamlit app
├── requirements.txt # Dependencies
└── .streamlit/
└── secrets.toml # API keys (DO NOT commit to GitHub!)
```
---

## 🔑 Setup Instructions

### 1. Clone repo
  ```bash
  git clone https://github.com/Arul-DevX/API_GPT.git
  cd API_GPT
  ```
### 2. Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
### 3. Add API key
#### Create a file .streamlit/secrets.toml:
  ```bash
  openrouter_api = "your_api_key_here"
  ```
### 4. Run app
  ```bash
  streamlit run main.py
  ```
## 🌐 Deployment
- Streamlit Cloud: Connect your GitHub repo, add API key in project settings → Secrets.

## 📸 Screenshot

![Demo Screenshot](https://raw.githubusercontent.com/Arul-DevX/API_GPT/main/Screenshot%202025-08-18%20205244.png)



## 👨‍💻 Author
- Built by Arul ✨ – Data Analyst & AI Enthusiast.
- Feel free to connect on [LinkedIn 🚀](https://linkedin.com/in/arulraman)

