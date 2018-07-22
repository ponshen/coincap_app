import requests
import json

convert = 'USD'

listing_url = "https://api.coinmarketcap.com/v2/listings/"
url_end = "?structure=array&convert=" + convert

request = requests.get(listing_url)
results = request.json()

data = results['data']

ticker_url_pairs = dict()
for currency in data:
    idx = currency['id']
    #name = currency['name']
    symbol = currency['symbol']
    ticker_url_pairs[symbol] = idx

# print(ticker_url_pairs)

while True:

    print()

    choice = input("Enter the ticker symbol of a cryptocurrency: ")
    choice = choice.upper()

    ticker_url = "https://api.coinmarketcap.com/v2/ticker/" + str(ticker_url_pairs[choice]) + '/' + url_end
    # print(ticker_url)

    request = requests.get(ticker_url)
    results = request.json()

    # print(json.dumps(results, sort_keys=True, indent=4))

    currency = results['data'][0]

    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = 0 if currency['circulating_supply'] == None else int(currency['circulating_supply'])
    total_supply = 0 if currency['total_supply'] == None else int(currency['total_supply'])

    quotes = currency['quotes'][convert]
    market_cap = 0 if quotes['market_cap'] == None else int(quotes['market_cap'])
    hour_change = 0 if quotes['percent_change_1h'] == None else quotes['percent_change_1h']
    day_change = 0 if quotes['percent_change_24h'] == None else quotes['percent_change_24h']
    week_change = 0 if quotes['percent_change_7d'] == None else quotes['percent_change_7d']
    price = quotes['price']
    volume = 0 if quotes['volume_24h'] == None else quotes['volume_24h']

    volume_string = '{:,}'.format(volume)
    market_cap_string = '{:,}'.format(market_cap)
    circulating_supply_string = '{:,}'.format(circulating_supply)
    total_supply_string = '{:,}'.format(total_supply)

    circulating_percent = 0 if total_supply == 0 else int(circulating_supply/total_supply * 100)

    print(str(rank) + ": " + name + " (" + symbol + ")")
    print("Market cap: \t\t$" + market_cap_string )
    print("Price: \t\t\t$" + str(price))
    print("24h Volume: \t\t$" + volume_string)
    print("Hour change: \t\t" + str(hour_change) + "%")
    print("Day change: \t\t" + str(day_change) + "%")
    print("Week change: \t\t" + str(week_change) + "%")
    print("Total supply: \t\t" + total_supply_string)
    print("Circulating_supply: \t" + circulating_supply_string)
    print("Percentage of coins in circulation: " + str(circulating_percent) + '%')
    print()

    choice = input('Again? (y/n)')
    if choice == 'n':
        break
