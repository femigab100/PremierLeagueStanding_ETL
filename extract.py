import requests
from config import API_URL, HEADERS

def extract_data():
    #Extract standings data from football-data.org API.
    
    response = requests.get(API_URL, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"API Request failed: {response.status_code}")

    data = response.json()
    return data
