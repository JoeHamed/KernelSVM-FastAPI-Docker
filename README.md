# Kernel SVM with FastAPI Deployment on Docker

This repository contains a Kernel SVM model trained on the "Social Network Ads" dataset. The model is deployed using a FastAPI application, allowing for easy interaction and prediction through RESTful APIs.

## Features

- **Kernel SVM** model trained with scikit-learn using RBF kernel.
- **FastAPI** for serving the model as a web application.
- Dockerized setup for easy deployment.

---

## Project Structure

. ├── app/ 
│ ├── Server.py # FastAPI server code 
│ ├── model.joblib # Trained Kernel SVM model 
│ ├── scaler.joblib # Scaler for input feature preprocessing 
│ └── requirements.txt # Python dependencies 
├── Dockerfile # Docker configuration 
└── README.md # Project documentation
