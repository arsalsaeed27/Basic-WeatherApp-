import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):# func to get the weather from API
    params ={
        "q":city,
        "appid":API_KEY,
        "units": "metric"
    }
    response= requests.get(BASE_URL, params=params)
    
    if response.status_code ==200:
        data= response.json()
        weather_data ={
            "city":data["name"],
            "temperature": data["main"]["temp"],
            "description":data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
        return weather_data
    else:
        return None