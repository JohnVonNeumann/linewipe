from poloniex import Poloniex
from flask import Flask
polo = Poloniex()
app = Flask(__name__)

@app.route("/")
def hello():
  return lbcAsks() 

def orderBook():
  lbc_asks = polo.returnOrderBook('BTC_LBC')['asks']
  lbc_bids = polo.returnOrderBook('BTC_LBC')['bids']

def lbcAsks():
  print('LBC ASKS:')
  for each in orderBook.lbc_asks:
    print(each)

def lbcBids():
  print('LBC BIDS:')
  for each in orderBook.lbc_bids:
    print(each)

if __name__ == "__main__":
  app.run()
