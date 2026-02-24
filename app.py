from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import sklearn

app = Flask(__name__)

model = joblib.load(open("student_score_pipeline.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return jsonify({
        "predicted_score": round(float(prediction[0]), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
