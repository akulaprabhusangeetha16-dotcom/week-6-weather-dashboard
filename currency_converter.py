import requests


def get_exchange_rates(base_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["result"] == "success":
            return data["rates"]
        else:
            print("Error fetching exchange rates.")
            return None

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None


def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)

    if not rates:
        return None

    if to_currency not in rates:
        print("Invalid target currency.")
        return None

    return amount * rates[to_currency]


def main():
    print("\n===== Currency Converter =====")

    amount = float(input("Enter amount: "))
    from_currency = input("From Currency (e.g., INR): ").upper()
    to_currency = input("To Currency (e.g., USD): ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    if result:
        print(f"\nConverted Amount: {result:.2f} {to_currency}")
    else:
        print("Conversion failed.")

    print("==============================\n")


if __name__ == "__main__":
    main()