from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from typing import List

# Load the trained model and scaler
model = joblib.load('./app/model.joblib')
scaler = joblib.load('./app/scaler.joblib')  # Load the same scaler used during training
class_names = ['Not Purchased', 'Purchased']
# Create FastAPI app
app = FastAPI()


# Define request body schema
class InputData(BaseModel):
    features: List[int]  # List of numerical features


@app.get('/')
def read_root():
    return {'message': 'Kernel SVM - Navigate to /docs for testing'}


@app.post('/predict')
def predict(data: InputData):
    # Extract features from the request
    features = np.array(data.features).reshape(1, -1)  # Reshape to 2D array

    # Scale the input features using the same scaler as during training
    scaled_features = scaler.transform(features)

    # Make prediction
    prediction = model.predict(scaled_features)
    class_name = class_names[prediction[0]]

    # Return the prediction result
    return {"Class : ", class_name}  # Assuming the prediction is a single value
