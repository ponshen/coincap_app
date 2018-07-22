import json
import requests

listing_url = "https://api.coinmarketcap.com/v2/listings/"

request = requests.get(listing_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data = results['data']
for currency in data:
    idx = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(idx) + ': ' + name + ' (' + symbol +')')
