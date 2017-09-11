from urllib import request
import requests

response_raw =  requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/')
headers = response_raw.headers
response = response_raw.json()
#import ipdb; ipdb.set_trace()
print(headers)

tickers = []
for each in response:
    print("This is the name of the asset: " + each['name'])

print("This is the name of the asset: " + response[0]["name"])
