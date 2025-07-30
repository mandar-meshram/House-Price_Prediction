from fastapi import APIRouter, HTTPException
from app.models.model import get_model, predict_price
from app.schemas.request_response import HouseFeatures, PredictionResponse
from app.exceptions.custom_exceptions import ModelNotLoadedException
import logging

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(features: HouseFeatures):
    try:
        model = get_model()  # my model loading function
        prediction = predict_price(model, features)
        return PredictionResponse(price=prediction)
    except ModelNotLoadedException:
        raise HTTPException(status_code=503, detail="Model not loaded")
    except Exception as e:
        logging.error(f'Prediction failed: {str(e)}')
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
