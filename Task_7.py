# Program 1
import requests
class countryInfo:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.data = response.json()
            else:
                print(response.status_code)
        except Exception as e:
            print(e)
    def display_country_and_currency(self):
        if self.data:
            for country in self.data:
                name = country.get("name", {}).get("common", "N/A")
                currencies = country.get("currencies", {})
                for code, details in currencies.items():
                    print(f"Country: {name}, Currency: {details.get('name', "N/A")}, Symbol: {details.get('symbol', "N/A")}")
        else:
            print("No data available")

    def display_country_with_currency(self, currency_name):
        if self.data:
            for country in self.data:
                currencies = country.get("currencies",{})
                for code, details in currencies.items():
                    if details.get("symbol", "").lower() == currency_name.lower():
                        print(country.get("name", {}).get("common", "N/A"))
        else:
            print("No data")


url = "https://restcountries.com/v3.1/all"
country_info = countryInfo(url)
country_info.fetch_data()

print("Countries, their currencies, and symbols:")
country_info.display_country_and_currency()

print("\nCountries using Dollar as a currency")
country_info.display_country_with_currency("$")

print("\nCountries using Euro as a currency")
country_info.display_country_with_currency("€")


# Program 2
import requests
from collections import Counter
class BreweryInfo:
    def __init__(self):
        self.base_url = "https://www.openbrewerydb.org/"
        self.states = ["Alaska", "Maine", "New York"]
        self.data = []



