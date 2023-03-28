import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()
DATADOG_URL = os.getenv('DATADOG_URL')
DATADOG_API_KEY = os.getenv('DATADOG_API_KEY')
DATADOG_APP_KEY = os.getenv('DATADOG_APP_KEY')

def search_metrics_list(query):
  search_query = f"/search?q={query}"
  url = f"{DATADOG_URL}{search_query}"
  headers = {
    "Accept": "application/json",
    "DD-API-KEY": DATADOG_API_KEY,
    "DD-APPLICATION-KEY": DATADOG_APP_KEY,
  }

  response = requests.get(url, headers=headers)

  return json.loads(response.text)

res = search_metrics_list("postgresql")

print(res["results"]["metrics"])
