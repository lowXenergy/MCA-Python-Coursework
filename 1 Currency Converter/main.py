import requests

API_KEY = "Your api key"
AGENT_CUT = 8.7


def convert_currency(amount, from_curr, to_curr):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_curr}"

    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        return None

    rates = data["conversion_rates"]

    if to_curr not in rates:
        return None

    rate = rates[to_curr]
    converted = amount * rate

    commission = converted * (AGENT_CUT / 100)
    final_amount = converted - commission

    return converted, commission, final_amount


def main():
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Invalid number.")
        return

    if amount < 1 or amount > 100000:
        print("Amount must be between 1 and 100000.")
        return

    from_curr = input("From currency: ").strip().upper()
    to_curr = input("To currency: ").strip().upper()

    if from_curr == to_curr:
        print(f"No conversion needed. Amount remains {amount:.2f} {from_curr}")
        return

    result = convert_currency(amount, from_curr, to_curr)

    if result is None:
        print("Currency conversion failed.")
        return

    converted, commission, final_amount = result

    print(f"Converted Amount: {converted:.2f} {to_curr}")
    print(f"Agent Cut (8.7%): {commission:.2f} {to_curr}")
    print(f"Final Amount: {final_amount:.2f} {to_curr}")


# if __name__ == "__main__":
main()
