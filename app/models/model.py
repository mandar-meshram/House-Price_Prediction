import os
import pickle
from app.schemas.request_response import HouseFeatures
from app.services.preprocessing import preprocess_input
from app.exceptions.custom_exceptions import ModelNotLoadedException
import pandas as pd


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
    df = pd.DataFrame([features.dict()])

    df['location'] = df['location'].str.lower()
    df['furnishing'] = df['furnishing'].str.lower()

    df = pd.get_dummies(df, columns=['location', 'furnishing'])

    with open("ml/features.pkl", "rb") as f:
        feature_columns = pickle.load(f)

    df = df.reindex(columns=feature_columns, fill_value=0)

    prediction = model.predict(df)

    return float(prediction[0])