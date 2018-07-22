import requests
import json
import os

os.system('cls')
###############################################

CURRENCY = "JPY"
url = "https://api.coinmarketcap.com/v2/ticker/?limit=100&sort=rank&structure=array"
url = url + "&convert=" +CURRENCY
api_request = requests.get(url)
api = json.loads(api_request.content)

#print("json parsed api has type " + str(type(api)))
#print(api)

print('Name\t\t\t\tRank\t\tSymbol\t\tPrice (' + CURRENCY + ')')
print('-' * 75)
for item in api['data']:
    price = str(round(item['quotes'][CURRENCY]['price']))
    rank = str(item['rank'])
    symbol = item['symbol']
    name = item['name']
    if len(name) < 8:
        print(name + "\t\t\t\t" + rank + "\t\t" + symbol + "\t\t" + price)
    elif len(name) < 16:
        print(name + "\t\t\t" + rank + "\t\t" + symbol + "\t\t" + price)
    else:
        print(name + "\t\t" + rank + "\t\t" + symbol + "\t\t" + price)
