import requests
import json

url = "http://127.0.0.1:5000/predict"

payload = {
    "make": "aston_martin",
    "model": "vantage",
    "body_type": "coupe",
    "transmission": "automatic",
    "fuel_type": "petrol",
    "engine_vol": 4,
    "engine_size": 503,
    "miles": 22000,
    "age": 6
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.json())