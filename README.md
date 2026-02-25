# RNN Question Answering System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-red)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


Production-ready Question Answering API built with PyTorch, FastAPI, AWS, Docker, and Streamlit.

---

🚀 Overview

This project demonstrates how to take a trained PyTorch RNN model and deploy it as a scalable REST API using FastAPI and Docker, with a Streamlit frontend connected to the backend running on EC2.

It includes:

RNN-based Question Answering model

FastAPI backend (Dockerized)

Streamlit frontend

AWS EC2 deployment

Docker containerization

Docker Hub integration

CI/CD ready architecture

🏗 Architecture

User → Streamlit UI → FastAPI REST API → PyTorch RNN Model

The backend is fully containerized and can be deployed on any Docker-supported infrastructure.

📦 Tech Stack

Python 3.10

PyTorch

FastAPI

Uvicorn

Streamlit

Docker

AWS EC2 (deployment target)

🐳 Docker Usage
Build Image
docker build -t rnn_qa_system .
Run Container
docker run -p 8000:8000 rnn_qa_system

API available at:

http://localhost:8000/docs
🌐 AWS EC2 Deployment Steps
1️⃣ Pull Docker Image
docker pull username/fastapi-ec2
2️⃣ Run Container on EC2
docker run -d -p 8000:8000 username/fastapi-ec2

-d = run in background

-p 8000:8000 = map EC2 port 8000 to container port 8000

3️⃣ Security Groups

Go to AWS EC2 → Security Groups → Inbound rules

Add:

Type: Custom TCP
Port: 8000
Source: 0.0.0.0/0
4️⃣ Connect Frontend to Backend

Update frontend code API URL from localhost to EC2 public IP:

API_URL = "http://<EC2-PUBLIC-IP>:8000/predict"
5️⃣ Test

FastAPI: http://EC2-PUBLIC-IP:8000

Swagger Docs: http://EC2-PUBLIC-IP:8000/docs

Streamlit frontend calling EC2 backend API

🎨 Streamlit UI

Run locally:

streamlit run streamlit_app/app.py
🧠 API Endpoint

POST /predict

Request:

{
  "question": "What is the capital of france?"
}

Response:

{
  "answer": "paris"
}
🧪 Lessons Learned

During development, key challenges included:

ASGI module import errors

Docker image size optimization

Port binding issues

Container networking debugging

Docker Hub push failures

Frontend-backend EC2 connectivity

Public IP configuration

This project reflects hands-on experience with debugging real-world deployment issues and full-stack cloud deployment.

🚀 Future Improvements

GitHub Actions CI/CD pipeline

Nginx reverse proxy + HTTPS

Kubernetes deployment

Elastic IP for consistent backend URL

Environment variable usage for API URLs

📌 Author

Zeeshan
Machine Learning & Backend Engineering Enthusiast

⭐ Why This Project Matters

Building ML models is important.
Deploying them reliably, reproducibly, and professionally is engineering.