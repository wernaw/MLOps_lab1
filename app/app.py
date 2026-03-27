from fastapi import FastAPI
from .inference import (
    load_model,
    load_feature_and_target_names,
    predict as run_prediction,
)
from .models.iris import PredictRequest, PredictResponse


app = FastAPI()

model = load_model()
_, target_names = load_feature_and_target_names()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = run_prediction(model, target_names, request.model_dump())
    return PredictResponse(prediction=prediction)
