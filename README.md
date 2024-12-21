# Kernel SVM with FastAPI Deployment on Docker

This repository contains a Kernel SVM model trained on the "Social Network Ads" dataset. The model is deployed using a FastAPI application, allowing for easy interaction and prediction through RESTful APIs.

## Features

- **Kernel SVM** model trained with scikit-learn using RBF kernel.
- **FastAPI** for serving the model as a web application.
- Dockerized setup for easy deployment.

---

## Project Structure
```bash
. ├── app/ 
│ ├── Server.py # FastAPI server code 
│ ├── model.joblib # Trained Kernel SVM model 
│ ├── scaler.joblib # Scaler for input feature preprocessing 
│ └── requirements.txt # Python dependencies 
├── Dockerfile # Docker configuration 
└── README.md # Project documentation
```
---

## Requirements

- **Docker**: Ensure Docker is installed on your machine.
- **Python 3.11** (if running locally without Docker).
- Python dependencies (listed in `requirements.txt`).

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/kernel-svm-fastapi-docker.git
cd kernel-svm-fastapi-docker
```
### 2. Build and Run the Docker Container
#### Build the Docker Image
```bash
docker build -t kernel-svm-fastapi .
```
#### Run the Docker Container
```bash
docker run -d -p 8000:8000 kernel-svm-fastapi
```
The FastAPI app will be accessible at `http://localhost:8000`.

## Usage
### Testing the API
- Navigate to the Swagger UI: http://localhost:8000/docs
- Use the /predict endpoint to make predictions.

### Sample Payload for /predict
```bash
{
  "features": [30, 87000]
}
```
### Sample Response
```bash
{
  "Class : ": "Purchased"
}
```
## Running Locally (Optional)
- If you prefer running the application locally without Docker:
1. Install Dependencies
```bash
pip install -r app/requirements.txt
```
2. Run the Application
```bash
python app/Server.py
```
## Customization
### Training the Model
The model is trained using the "`Social Network Ads`" dataset. Update the dataset or model parameters in `model.py` as needed and retrain using the same process.

### Scaling Inputs
The input features are scaled using a saved `StandardScaler`. Update the scaler logic if your dataset changes.
