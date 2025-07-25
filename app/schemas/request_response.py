from pydantic import BaseModel

class HouseFeatures(BaseModel):
    location : str
    area : float
    bedrooms : int
    bathrooms : int
    furnishing : str


class PredictionResponse(BaseModel):
    price : float