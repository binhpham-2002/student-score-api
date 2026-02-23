import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "student_score_pipeline.pkl")

pipeline = joblib.load(MODEL_PATH)

def predict_score(data_dict):
    # Convert dict -> DataFrame 1 row
    input_df = pd.DataFrame([data_dict])
    
    prediction = pipeline.predict(input_df)
    return float(prediction[0])
