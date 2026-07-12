from fastapi import FastAPI
from pydantic import BaseModel
from services.prediction import predict_flood_risk
from services.llm_explainer import generate_explanation

app = FastAPI()

class Input(BaseModel):
    rainfall: float
    discharge: float
    soil_moisture: float

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/predict")
def predict(data: Input):
    score, level = predict_flood_risk(
        data.rainfall, data.discharge, data.soil_moisture
    )

    explanation = generate_explanation({
        "rainfall": data.rainfall,
        "discharge": data.discharge,
        "soil_moisture": data.soil_moisture,
        "risk_score": score,
        "risk_level": level
    })

    return {
        "risk_score": score,
        "risk_level": level,
        "explanation": explanation
    }
