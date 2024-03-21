import requests
from tabulate import tabulate

url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

headers = {
    "X-RapidAPI-Key": "19b234196amsh1662b68eb371676p1341e6jsnba6fb9bd52ac",
    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    currencies = [(currency['symbol'], currency['name']) for currency in data]
    print(tabulate(currencies, headers=['CURRENCY', 'ORIGIN COUNTRY'], tablefmt='pretty'))
else:
    print("Failed to fetch currency data.")
