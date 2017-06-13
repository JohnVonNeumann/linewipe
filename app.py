import json
from poloniex import Poloniex
from flask import Flask, jsonify, Response
polo = Poloniex()
app = Flask(__name__)

@app.route("/")
def post():
  lbc_asks = polo.returnOrderBook('BTC_LBC')['asks']
  json_asks = jsonify(lbc_asks)
  for each in json_asks:  
    return Response(json.dumps(each), mimetype='application/json') 

def lbcAsks(self):
  lbc_asks = polo.returnOrderBook('BTC_LBC')['asks']
  for each in lbc_asks:  
    return jsonify(each)

def lbcBids(self):
  lbc_bids = polo.returnOrderBook('BTC_LBC')['bids']
  return('LBC BIDS:')
  for each in lbc_bids:
    return jsonify(each)

if __name__ == "__main__":
  app.run(debug = True, port = 5000)
