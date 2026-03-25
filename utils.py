def format_weather(weather):
    if weather is None:
        return "City not found!"
    
    text =( f"City: {weather['city']}\n"
        f"Temperature:{weather['temperature']}°C\n"
        f"Description: {weather['description']}\n"
        f"Humidity:  {weather['humidity']}%"
    )
    return text