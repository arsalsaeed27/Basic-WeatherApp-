import requests
API_KEY = "9a5cc69ac09e10360c7d2f3c02e944b7"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city): # func to get the weather from API
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