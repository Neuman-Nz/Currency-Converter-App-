import requests

def currency_converter():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    while True:
        # Get user input for conversion
        from_currency = input("Enter the currency you want to convert from (e.g., USD): ")
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ")
        amount = float(input("Enter the amount you want to convert: "))

        querystring = {"from": from_currency, "to": to_currency, "amount": amount}

        # Define currency symbols
        currency_symbols = {
            'USD': '$',
            'EUR': '€',
            'CAD': 'CA $',
            'KES': 'Ksh',
            'GBP': '£',
            'JPY': '¥',
            'AUD': 'A$',
            'INR': '₹',
            'CNY': 'CN¥',
            'CHF': 'CHF',
            'SEK': 'kr',
            'NZD': 'NZ$',
            'SGD': 'S$',
            'HKD': 'HK$',
            'NOK': 'kr',
            'MXN': 'MX$'
        }

        headers = {
            "X-RapidAPI-Key": "19b234196amsh1662b68eb371676p1341e6jsnba6fb9bd52ac",
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            converted_amount = data["result"]["convertedAmount"]
            symbol = currency_symbols.get(to_currency, '')  
            print("Converted Amount:", f"{symbol}{converted_amount}")  
            converted_amount_value = data.get('rates', {}).get(to_currency)  
            if converted_amount_value is not None:
                print(f"{amount} {from_currency} is equal to {symbol}{converted_amount_value} {to_currency}")
            else:
                print(f"Here is the conversion: {from_currency} to {to_currency}")
        else:
            print("An error occurred while fetching data. Please try again later.")

        # Ask if the user wants to perform another conversion
        choice = input("Do you want to perform another conversion? (yes/no): ")
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    currency_converter()

