# weather_app/weather_parser.py

from datetime import datetime


def parse_current_weather(data: dict) -> dict:
    """Extract useful current weather data"""

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["description"].title(),
        "icon": data["weather"][0]["main"],
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M"),
        "last_updated": datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
    }


def parse_current_weather(data):
    return {
        "city": data["city"]["name"],
        "temperature": data["list"][0]["main"]["temp"],
        "humidity": data["list"][0]["main"]["humidity"],
        "description": data["list"][0]["weather"][0]["description"],
    }


def parse_forecast(data):
    forecast_data = []

    for item in data["list"][:5]:
        forecast_data.append({
            "datetime": item["dt_txt"],
            "temperature": item["main"]["temp"],
            "humidity": item["main"]["humidity"],
            "description": item["weather"][0]["description"],
        })

    return forecast_data