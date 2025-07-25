import pandas as pd
from app.schemas.request_response import HouseFeatures

def preprocess_input(features: HouseFeatures) -> pd.DataFrame:
    input_data = {
        "location" : [features.location.lower()],
        "area" : [features.area],
        "bedrooms" : [features.bedrooms],
        "bathrooms" : [features.bathrooms],
        "furnishing" : [features.furnishing.lower()],
    }

    return pd.DataFrame(input_data)