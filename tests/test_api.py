import requests
import json

url = "http://127.0.0.1:5000/predict"

payload = {
    "make": "vauxhall",
    "model": "astra",
    "body_type": "hatchback",
    "transmission": "automatic",
    "fuel_type": "petrol",
    "engine_vol": 1.6,
    "engine_size": 113,
    "miles": 50000,
    "age": 11
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.json())