import requests

from datetime import datetime, timedelta

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"  
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].lower()  # ALLY: ADDED .lower()
        }
        return weather
    else:
        return f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}"



def get_forecast(city, api_key, days=3):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(forecast_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        forecast_data = []
        
        # Get today's date to filter the forecast for the next `days` days
        today = datetime.now()
        end_date = today + timedelta(days=days)
        
        for entry in data["list"]:
            forecast_date = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S")
            
            # Filter forecast entries to only include those within the specified days
            
            if forecast_date.date() <= end_date.date():
                forecast = {
                    "date": forecast_date.strftime("%A, %B %d %Y, %I:%M %p"),  # Format date and time
                    "temperature": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"].lower() #ALLY: ADDED .lower()
                }
                forecast_data.append(forecast)
        
        return forecast_data
    else:
        return f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}"
    
