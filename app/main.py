from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api import endpoints


app = FastAPI(title="House Price Predictor")

templates = Jinja2Templates(directory="app/templates")

app.include_router(endpoints.router)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})