from fastapi import FastAPI
from app.schemas import StudentInput
from app.model.predict import predict_score
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

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

@app.get("/ui")
def serve_ui():
    return FileResponse("index.html")
