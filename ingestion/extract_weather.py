import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = "https://api.openweathermap.org/data/2.5/weather"

CITIES = [
    {"city": "Brasilia", "country": "BR"},
    {"city": "Sao Paulo", "country": "BR"},
    {"city": "Rio de Janeiro", "country": "BR"}
]

def extract(city, country):
    params = {
        "q": f"{city},{country}",
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()
    return response.json()

def main():
    results = []
    execution_time = datetime.utcnow().isoformat()

    for c in CITIES:
        data = extract(c["city"], c["country"])
        data["extraction_timestamp"] = execution_time
        results.append(data)

    filename = f"weather_{datetime.utcnow().date()}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("Arquivo criado:", filename)

if __name__ == "__main__":
    main()