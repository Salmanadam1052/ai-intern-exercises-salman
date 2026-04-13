# 🚀 Qwen3 LLM API with FastAPI + Docker + Ollama

This project is a full-stack local AI system that exposes a Large Language Model (Qwen 2.5) through a REST API, containerized with Docker, and connected to a simple chat UI.

---

# 🧠 System Architecture

User (Browser / Curl)
        ↓
FastAPI API (Docker Container)
        ↓
Ollama Server (Local LLM Runtime)
        ↓
Qwen 2.5 Model
        ↓
Response returned to user

---

# ⚙️ Features

- REST API for LLM inference (/generate)
- Local model execution using Ollama
- Dockerized backend
- Chat-style web UI
- CORS-enabled API
- Works locally and via tunneling tools

---

# 🧰 Tech Stack

- FastAPI
- Docker
- Ollama
- Qwen 2.5 0.5B
- HTML/CSS/JS
- Python 3.10

---

# 📁 Project Structure

qwen3-exercise/
├── api/
│   ├── main.py
│   └── requirements.txt
├── docker/
│   └── Dockerfile
├── ui/
│   └── index.html
└── README.md

---

# 🚀 Setup Instructions

## 1. Install Ollama
ollama serve
ollama pull qwen2.5:0.5b

## 2. Build Docker
docker build -f docker/Dockerfile -t qwen-api .

## 3. Run Docker
docker run -p 8000:8000 qwen-api

---

# 📌 API

POST /generate

Request:
{
  "prompt": "Explain AI"
}

Response:
{
  "response": "..."
}

---

# 🌐 Public Access
ngrok http 8000

---

# ⚠️ Notes
- Ollama must run before API
- Use host.docker.internal for Docker → Ollama connection
- First run downloads model

---

# 🎯 Done
Full LLM system working end-to-end

curl -X POST http://localhost:8000/generate \
-H "Content-Type: application/json" \
-d "{\"prompt\": \"What is AI?\"}"