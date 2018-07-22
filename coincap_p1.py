import os
import requests
import json
from datetime import datetime
from colorama import Fore, Back, Style
from prettytable import PrettyTable

convert = 'USD'

listing_url = "https://api.coinmarketcap.com/v2/listings/?convert=" + convert

request = requests.get(listing_url)
results = request.json()

# print(json.dumps(results, indent=4))

data = results['data']

ticker_url_pairs = dict()
for currency in data:
    symbol = currency['symbol']
    idx = currency['id']
    # name = currency['name']
    ticker_url_pairs[symbol] = idx
