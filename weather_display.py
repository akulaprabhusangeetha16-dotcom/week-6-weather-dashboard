def display_current(current):
    print("\n===== Current Weather =====")
    print(f"City: {current['city']}")
    print(f"Temperature: {current['temperature']} °C")
    print(f"Humidity: {current['humidity']}%")
    print(f"Condition: {current['description']}")
    print("===========================\n")


def display_forecast(forecast):
    print("===== Forecast (Next 5 Time Slots) =====")

    for item in forecast:
        print("-----------------------------------")
        print(f"Date & Time: {item['datetime']}")
        print(f"Temperature: {item['temperature']} °C")
        print(f"Humidity: {item['humidity']}%")
        print(f"Condition: {item['description']}")

    print("========================================\n")