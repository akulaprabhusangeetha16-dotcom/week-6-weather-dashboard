import requests


class WeatherAPI:
    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError:
            print("City not found or API error.")
        except requests.exceptions.ConnectionError:
            print("Network error. Check your internet connection.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except requests.exceptions.RequestException as e:
            print("Something went wrong:", e)

        return None