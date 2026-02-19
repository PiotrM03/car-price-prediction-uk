from flask import Flask, request, jsonify, render_template
import joblib
import os
import numpy as np
import pandas as pd

app = Flask(__name__)

MAKES = [
    "abarth",
    "ac",
    "ak",
    "alfa_romeo",
    "alpine",
    "ariel",
    "aston_martin",
    "audi",
    "bac",
    "bentley",
    "bmw",
    "bowler",
    "cadillac",
    "caterham",
    "chevrolet",
    "chrysler",
    "citroen",
    "crendon",
    "cupra",
    "dacia",
    "daewoo",
    "daihatsu",
    "daimler",
    "dax",
    "dfsk",
    "dodge",
    "ds_automobiles",
    "ferrari",
    "fiat",
    "ford",
    "gardener",
    "gbs",
    "genesis_motor",
    "gmc",
    "great_wall",
    "honda",
    "hummer",
    "hyundai",
    "infiniti",
    "isuzu",
    "iveco",
    "jaguar",
    "jba",
    "jeep",
    "kia",
    "ktm",
    "lada",
    "lamborghini",
    "land_rover",
    "levc",
    "lexus",
    "lincoln",
    "london_taxis_international",
    "lotus",
    "maserati",
    "mazda",
    "mclaren",
    "mercedes-benz",
    "mev",
    "mg",
    "mini",
    "mitsubishi",
    "moke",
    "morgan",
    "ng",
    "nissan",
    "oldsmobile",
    "perodua",
    "peugeot",
    "piaggio",
    "polaris",
    "polestar",
    "porsche",
    "proton",
    "radical",
    "renault",
    "robin_hood",
    "rover",
    "royale",
    "saab",
    "seat",
    "skoda",
    "smart",
    "ssangyong",
    "subaru",
    "suzuki",
    "tesla",
    "tiger",
    "toyota",
    "tvr",
    "ultima",
    "vauxhall",
    "volkswagen",
    "volvo",
    "westfield",
    "yamaha"
]

UPPERCASE_BRANDS = {"ak", "bmw", "bac", "ac", "dfsk", "dax", "jba", "mg", "gbs", "gmc", "tvr", "ng"}

model_path = os.path.join("models", "model_pipeline_v2.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html", makes=MAKES, uppercase_brands=UPPERCASE_BRANDS)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    data["age"] = max(0, int(data["age"]) + 3)

    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    input_df = pd.DataFrame([data])

    preds = model.predict(input_df)

    predicted_price = float(preds[0])

    return jsonify({"predicted_price": predicted_price})

if __name__ == "__main__":
    app.run(debug=True)