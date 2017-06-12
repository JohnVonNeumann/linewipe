from poloniex import Poloniex
from flask import Flask
from flask import jsonify
polo = Poloniex()
app = Flask(__name__)

@app.route("/")
def post():
  polo = Poloniex()
  lbc_asks = polo.returnOrderBook('BTC_LBC')['asks']
  return jsonify(lbc_asks)
  for each in lbc_asks:
    return('each')  

#def lbcAsks():
#  lbc_asks = polo.returnOrderBook('BTC_LBC')['asks']
#  return('LBC ASKS:')
#  for each in lbc_asks:
#    return each

#def lbcBids():
#  lbc_bids = polo.returnOrderBook('BTC_LBC')['bids']
#  print('LBC BIDS:')
#  for each in lbc_bids:
#    print(each)

if __name__ == "__main__":
  app.run()
