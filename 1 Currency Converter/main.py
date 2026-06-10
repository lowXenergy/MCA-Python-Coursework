# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

# api_key = os.getenv("API_KEY")
# db_host = os.getenv("DB_HOST")

# AGENT_CUT = 8.7

# # 1. Fail fast if API key is missing
# if not api_key:
#     raise ValueError("API_KEY not found. Check your .env file.")


# # --- NEW: Country → Currency helper ---
# def get_currency_from_country(country_name):
#     try:
#         url = f"https://restcountries.com/v3.1/name/{country_name}"
#         response = requests.get(url)

#         if response.status_code != 200:
#             return None

#         data = response.json()

#         # take first match
#         currencies = data[0].get("currencies", {})
#         if not currencies:
#             return None

#         # return first currency code (e.g., INR, USD)
#         return list(currencies.keys())[0]

#     except:
#         return None


# def convert_currency(amount, from_curr, to_curr):
#     url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_curr}"

#     response = requests.get(url)
#     data = response.json()

#     if data["result"] != "success":
#         return None

#     rates = data["conversion_rates"]

#     if to_curr not in rates:
#         return None

#     rate = rates[to_curr]
#     converted = amount * rate

#     commission = converted * (AGENT_CUT / 100)
#     final_amount = converted - commission

#     return converted, commission, final_amount


# def main():
#     try:
#         amount = float(input("Enter amount: ").strip())
#     except ValueError:
#         print("Invalid number.")
#         return

#     if amount < 1 or amount > 100000:
#         print("Amount must be between 1 and 100000.")
#         return

#     from_curr = input("From currency (code or country): ").strip()
#     to_curr = input("To currency (code or country): ").strip()

#     # normalize
#     from_curr = from_curr.upper()
#     to_curr = to_curr.upper()

#     # 3. Validate currency inputs OR try country detection
#     if len(from_curr) != 3:
#         detected = get_currency_from_country(from_curr)
#         if detected:
#             print(f"Detected {from_curr} → {detected}")
#             from_curr = detected
#         else:
#             print("Invalid 'from' currency or country.")
#             return

#     if len(to_curr) != 3:
#         detected = get_currency_from_country(to_curr)
#         if detected:
#             print(f"Detected {to_curr} → {detected}")
#             to_curr = detected
#         else:
#             print("Invalid 'to' currency or country.")
#             return

#     if from_curr == to_curr:
#         print(f"No conversion needed. Amount remains {amount:.2f} {from_curr}")
#         return

#     result = convert_currency(amount, from_curr, to_curr)

#     if result is None:
#         print("Currency conversion failed.")
#         return

#     converted, commission, final_amount = result

#     print(f"Converted Amount: {converted:.2f} {to_curr}")
#     print(f"Agent Cut (8.7%): {commission:.2f} {to_curr}")
#     print(f"Final Amount: {final_amount:.2f} {to_curr}")


# main()

# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

# API_KEY = os.getenv("API_KEY")
# AGENT_CUT = 8.7

# def convert_currency(amount, from_curr, to_curr):
#     url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_curr}"

#     response = requests.get(url)
#     data = response.json()

#     if data["result"] != "success":
#         return

#     rate = data["conversion_rates"][to_curr]

#     converted = amount * rate
#     commission = converted * AGENT_CUT / 100
#     final_amount = converted - commission

#     print(f"\nConverted Amount: {converted:.2f} {to_curr}")
#     print(f"Agent Cut: {commission:.2f} {to_curr}")
#     print(f"Final Amount: {final_amount:.2f} {to_curr}")


# amount = float(input("Enter amount: "))
# from_curr = input("From currency: ").upper()
# to_curr = input("To currency: ").upper()

# convert_currency(amount, from_curr, to_curr)

# Currency Converter

rates = [
    ["USD", 83],      # US Dollar
    ["EUR", 90],      # Euro
    ["GBP", 105],     # British Pound
    ["JPY", 0.57],    # Japanese Yen
    ["AUD", 55],      # Australian Dollar
    ["CAD", 61],      # Canadian Dollar
    ["SGD", 62],      # Singapore Dollar
    ["AED", 22.6],    # UAE Dirham
    ["CNY", 11.5],    # Chinese Yuan
    ["CHF", 94],      # Swiss Franc
    ["INR", 1]        # Indian Rupee
]

def get_rate(currency, rates):
    for item in rates:
        if item[0] == currency:
            return item[1]
    return None

print("\n" + "=" * 45)
print("       Welcome to Currency Converter")
print("=" * 45)

print("\nAvailable Currencies:")
for currency, rate in rates:
    print(f"- {currency}")

amount = float(input("\nEnter amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()

from_rate = get_rate(from_currency, rates)
to_rate = get_rate(to_currency, rates)

if from_rate is None or to_rate is None:
    print("\nInvalid currency entered!")
    print("\nAvailable currencies are:")
    for currency, rate in rates:
        print(f"- {currency}")
else:
    converted = amount * (from_rate / to_rate)

    print("\n" + "-" * 35)
    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    print("-" * 35)