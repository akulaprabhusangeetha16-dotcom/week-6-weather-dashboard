# weather_app/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key safely
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL for OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5"

# Cache duration (seconds)
CACHE_DURATION = 600  # 10 minutes

# Basic validation
if not API_KEY:
    raise ValueError(" OPENWEATHER_API_KEY not found in .env file")