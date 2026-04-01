import requests

API_KEY = "fe2ee5bd1ee28ea089fce4af"
AGENT_CUT_PER = 0.087

def getExchangeRates():
    url = "https://v6.exchangerate-api.com/v6/" + API_KEY + "/latest/USD"
    response = requests.get(url)
    data = response.json()["conversion_rates"]
    return data



def getCountryCurrencyMapping():
    print("Fetching country data... please wait.")
    try:
        url = "https://restcountries.com/v3.1/all?fields=name,currencies"
        response = requests.get(url)
        countries = response.json()
        
        mapping = {}
        for country in countries:
            common_name = country.get("name", {}).get("common", "").lower()
            official_name = country.get("name", {}).get("official", "").lower()
            currencies = country.get("currencies", {})
            
            if currencies:
                # Get the first currency code
                currency_code = list(currencies.keys())[0]
                if common_name:
                    mapping[common_name] = currency_code
                if official_name:
                    mapping[official_name] = currency_code
        
        return mapping
    except Exception as e:
        print(f"Error fetching country data: {e}")
        return {}

def resolveCurrency(user_input, all_rates, country_map):
    user_input_clean = user_input.strip().upper()
    
    # 1. Check if it's already a valid currency code
    if user_input_clean in all_rates:
        return user_input_clean
    
    # 2. Check if it's a country name
    country_name_lower = user_input.strip().lower()
    if country_name_lower in country_map:
        return country_map[country_name_lower]
    
    return None

all_rates = getExchangeRates()
country_map = getCountryCurrencyMapping()

print("\nBasic currency convertor: ")
print("You can now enter Country names (e.g., India, USA, France) or Currency codes (e.g., INR, USD, EUR).")

amount_input = input("Enter the amount you want to convert: ")
try:
    amount = float(amount_input)
except ValueError:
    print("Invalid amount. Please enter a numeric value.")
    exit()

from_input = input("Enter the country or currency you want to convert from: ")
to_input = input("Enter the country or currency you want to convert to: ")   

fromCurrency = resolveCurrency(from_input, all_rates, country_map)
toCurrency = resolveCurrency(to_input, all_rates, country_map)

if not fromCurrency:
    print(f"Could not find currency for: {from_input}")
    exit()
if not toCurrency:
    print(f"Could not find currency for: {to_input}")
    exit()

if amount < 1 or amount > 1000000:
    print("Invalid amount. Please enter a amount between 1 and 1000000.")
else:
    # All good, proceed with calculation
    exchangeRate = all_rates[toCurrency] / all_rates[fromCurrency]
    print(f"\nExchange Rate: 1 {fromCurrency} = {exchangeRate:.4f} {toCurrency}")
    print(f"Original Amount: {amount} {fromCurrency}")

    # convert the currency and print
    convertedAmount = amount * exchangeRate
    print(f"Converted Amount: {convertedAmount:.2f} {toCurrency}")

    # calculate and print agent cut
    agentCut = convertedAmount * AGENT_CUT_PER
    print(f"Agent Cut: {agentCut:.2f} {toCurrency}")

    # show final amount
    finalAmount = convertedAmount - agentCut
    print(f"Final Amount: {finalAmount:.2f} {toCurrency}")









# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()  # loads variables from .env

# api_key = os.getenv("API_KEY")
# # db_host = os.getenv("DB_HOST")

# # print(api_key)
# # print(db_host)
# AGENT_CUT = 8.7

# #WHAT IF PEOPLE DON'T KNOW THE COUNTRY CURRENCY NAME --> SEARCH THE COUNTRY AND THEN IT'S CURRENCY'NAME

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

#     from_curr = input("From currency: ").strip().upper()
#     to_curr = input("To currency: ").strip().upper()

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


# # if __name__ == "__main__":

# main()