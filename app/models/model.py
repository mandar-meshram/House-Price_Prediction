import os
import pickle
from app.schemas.request_response import HouseFeatures
from app.services.preprocessing import preprocess_input
from app.exceptions.custom_exceptions import ModelNotLoadedException


MODEL_PATH = "ml/model.pkl"
_model = None

def get_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise ModelNotLoadedException()
        with open(MODEL_PATH, "rb") as f:
            _model = pickle.load(f)
    return _model

def predict_price(model, features: HouseFeatures) -> float:
    input_df = preprocess_input(features)
    result = model.predict(input_df)
    return round(result[0], 2)