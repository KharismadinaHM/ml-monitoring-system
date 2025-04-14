import requests
import json

# Buka file JSON
with open("backend/ml_models/metrics.json", "r") as f:
    metrics_data = json.load(f)

# Kirim ke API monitoring
response = requests.post("http://127.0.0.1:8000/log_metrics", json=metrics_data)

# Print response
print(response.json())
