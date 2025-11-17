from flask import Flask, request, jsonify
import joblib
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

model_path = os.path.join("models", "model_pipeline_v1.pkl")
model = joblib.load(model_path)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    input_df = pd.DataFrame([data])

    preds = model.predict(input_df)

    predicted_price = float(preds[0])

    return jsonify({"predicted_price": predicted_price})

if __name__ == "__main__":
    app.run(debug=True)