from urllib import request
import requests

response_raw =  requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
#headers = response.info()
response = response_raw.json()
#import ipdb; ipdb.set_trace()
print(response)

#tickers = []
#for name in response:
#    print("This is the name of the asset: " + name)
#    print(name['0']['name'])

print("This is the name of the asset: " + response[0]["name"])
print(response)
