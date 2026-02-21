from .weather_api import WeatherAPI
from .weather_parser import parse_current_weather, parse_forecast
from .weather_display import display_current, display_forecast
from config import API_KEY


def main():
    city = input("Enter city name: ")

    # Create API object
    weather = WeatherAPI(API_KEY)

    # Fetch data
    data = weather.get_weather(city)

    if not data:
        print("Error fetching weather data.")
        return

    # Parse data
    current = parse_current_weather(data)
    forecast = parse_forecast(data)

    # Display data
    display_current(current)
    display_forecast(forecast)


if __name__ == "__main__":
    main()