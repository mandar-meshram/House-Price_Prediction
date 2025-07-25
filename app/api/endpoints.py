from fastapi import APIRouter, HTTPException
from app.models.model import get_model, predict_price
from app.schemas.request_response import HouseFeatures, PredictionResponse
from app.exceptions.custom_exceptions import ModelNotLoadedException
import pickle
import pandas as pd


router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_price(model, features) -> float:
    # Convert input (Pydantic) to DataFrame
    df = pd.DataFrame([features.dict()])
    # Lowercase textual columns
    df['location'] = df['location'].str.lower()
    df['furnishing'] = df['furnishing'].str.lower()
    # One-hot encode as in training
    df = pd.get_dummies(df, columns=['location', 'furnishing'])
    # Reindex columns
    with open("features.pkl", "rb") as f:
        feature_columns = pickle.load(f)
    df = df.reindex(columns=feature_columns, fill_value=0)
    # Predict and return scalar value (not list/array)
    pred = model.predict(df)
    return float(pred[0])
