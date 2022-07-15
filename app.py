import json, config
from flask import Flask, request, jsonify
from binance.client import Client
from binance.enums import *
#libraries to import
app = Flask(__name__)

#client = Client(config.API_KEY, config.API_SECRET, tld='com')
client = Client(config.API_KEY, config.API_SECRET)

#we are creating a new client object
#def order(side, quantity, symbol, order_type=ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC = 'GTC' ):
def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    #binance constants 
    try:
        print(f"sending order test {order_type} - {side} - {quantity} - {symbol}")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return order



@app.route('/')
def algo_world0():
    return 'Hello, World!'

@app.route('/algo', methods=['POST'])
def algo():
    data = json.loads(request.data)
    if data['passphrase'] != config.webook_pass:
        {
            "code":"error"
        }
    
    side = data['strategy']['order_action'].upper() #the order action is made upper case
    quantity = data['strategy']['order_contracts']
    symbol = data['ticker']
    order_price = data['strategy']['order_price']
    order_response = order (side, quantity, symbol)
    
    #gets the data in Json format

    if order_response:
        return {
            "code":"success",
            "message":"order executed"
            #"message": data1
            #prints the data in Json format
        }
    else:
        print("order failed")
        return{
            "code":"error",
            "message":"order failed"
        }

#def algo2():
