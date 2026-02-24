from fastapi import FastAPI
from app.schemas import StudentInput
from app.model.predict import predict_score
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Score Prediction API is running"}

@app.post("/predict")
def predict(data: StudentInput):
    input_data = data.dict()
    result = predict_score(input_data)
    return {"predicted_score": result}

@app.get("/health")
def health_check():
    return {"status": "OK"}

templates = Jinja2Templates(directory="templates")

@app.get("/ui")
def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
