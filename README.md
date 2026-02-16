# RNN Question Answering System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


Production-ready Question Answering API built with PyTorch, FastAPI, Docker, and Streamlit.

---

## 🚀 Overview

This project demonstrates how to take a trained PyTorch RNN model and deploy it as a scalable REST API using FastAPI and Docker.

It includes:

- RNN-based Question Answering model
- FastAPI backend
- Streamlit frontend
- Docker containerization
- Docker Hub integration
- Cloud deployment ready (AWS EC2)
- CI/CD ready architecture

---

## 🏗 Architecture

User → Streamlit UI → FastAPI REST API → PyTorch RNN Model

The backend is fully containerized and can be deployed on any Docker-supported infrastructure.

---

## 📦 Tech Stack

- Python 3.10
- PyTorch
- FastAPI
- Uvicorn
- Streamlit
- Docker
- AWS EC2 (deployment target)

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t rnn_qa_system .
```

### Run Container

```bash
docker run -p 8000:8000 rnn_qa_system
```

API available at:

http://localhost:8000/docs

---

## 🎨 Streamlit UI

Run locally:

```bash
streamlit run streamlit_app/app.py
```

---

## 🧠 API Endpoint

POST `/predict`

Request:
```json
{
  "question": "What is the capital of france?"
}
```

Response:
```json
{
  "answer": "paris"
}
```

---

## 🧪 Lessons Learned

During development, key challenges included:

- ASGI module import errors
- Docker image size optimization
- Port binding issues
- Container networking debugging
- Docker Hub push failures
- Image tag management
- Reproducible builds

This project reflects hands-on experience with debugging real-world deployment issues.

---

## 🚀 Future Improvements

- GitHub Actions CI/CD pipeline
- AWS EC2 automated deployment
- Nginx reverse proxy
- HTTPS with Let's Encrypt
- Kubernetes deployment

---

## 📌 Author

Zeeshan  
Machine Learning & Backend Engineering Enthusiast

---

## ⭐ Why This Project Matters

Building ML models is important.

Deploying them reliably, reproducibly, and professionally is engineering.
