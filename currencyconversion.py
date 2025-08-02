import requests
import json

geo_api_url = "https://ipgeolocation.abstractapi.com/v1/?api_key=931cc28cf80a47debf334b21f7d077c6&ip_address=103.71.18.142"
response = requests.get(geo_api_url)
geo_data = json.loads(response.text)

base_currency = geo_data["currency"]["currency_code"]
print(f"Detected base currency based on your location: {base_currency}")

target_currency = input("Enter the currency code you want to convert your money to (e.g., USD, EUR): ").strip().upper()

exchange_api_url = f"https://v6.exchangerate-api.com/v6/d3f0a01ef7e97f3d1661ee77/pair/{base_currency}/{target_currency}"
exchange_response = requests.get(exchange_api_url)
exchange_data = json.loads(exchange_response.text)

last_updated = exchange_data["time_last_update_utc"]
conversion_rate = exchange_data["conversion_rate"]

print(f"\nExchange Rate Information (as of {last_updated})")
print(f"1 {base_currency} = {conversion_rate} {target_currency}")

try:
    amount = float(input(f"\nEnter the amount in {base_currency}: "))
    converted_amount = amount * conversion_rate
    print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
except ValueError:
    print("Invalid amount entered. Please enter a numeric value.")
