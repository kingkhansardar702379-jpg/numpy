from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

import joblib

model = joblib.load("model.pkl")

class StudentData(BaseModel):
    hours_studied: float
    exam_score: float

@app.post("/predict")
def predict(data: StudentData):

    features = np.array([[data.hours_studied, data.exam_score]])

    prediction = model.predict(features)

    return {
        "result": int(prediction[0])  # 0 or 1
    }