import sqlite3

import requests
import requests_cache

requests_cache.install_cache('coinmarketcap_cache', \
                             backend='sqlite', \
                             expire_after=300)

response_raw =  requests.get('https://api.coinmarketcap.com/v1/ticker/')
headers = response_raw.headers
response = response_raw.json()
#import ipdb; ipdb.set_trace()

tickers = []
ticker_count = 0
for each in response:
    print("This is the name of the asset: " + each['name'])
    tickers.append(each['name'])
    ticker_count += 1

