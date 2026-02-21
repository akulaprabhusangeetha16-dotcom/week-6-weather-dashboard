from datetime import datetime


def show_datetime():
    now = datetime.now()

    print("\n===== Current Date & Time =====")
    print("Date (DD-MM-YYYY):", now.strftime("%d-%m-%Y"))
    print("Date (Month Name):", now.strftime("%B %d, %Y"))
    print("Time (12-hour):", now.strftime("%I:%M %p"))
    print("Time (24-hour):", now.strftime("%H:%M:%S"))
    print("ISO Format:", now.isoformat())
    print("===============================\n")


if __name__ == "__main__":
    show_datetime()