from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    hours = float(data["hours"])
    attendance = float(data["attendance"])

    # Demo formula (replace with ML model)
    prediction = hours * 5 + attendance * 0.3

    return jsonify({"prediction": round(prediction, 2)})

if __name__ == "__main__":
    app.run(debug=True)
