#!/usr/bin/python

#This is the API for BTC price request. 
# Average all the amounts, and push that to the program

import json
import urllib.request
from jsonpath_rw import parse as parse_jsonpath

class BtcAPI:

    def __init__(self, url, api_id, json_key):
        self.url = url
        self.api_id = api_id
        self.json_key = json_key

    def btc_api_call(self):

        #GET request
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        req = urllib.request.Request(self.url, headers=hdr)
        readdata = urllib.request.urlopen(req)
        json_data = readdata.read()
        
        #parse results
        json_dict = json.loads(json_data)
        results = parse_jsonpath(self.json_key).find(json_dict)
        print(results[0].value) 


class Price:
    

    def __init__(self, api_id, url, json_key):
        
        self.api_id = api_id
        self.url = url
        self.json_key = json_key
    
    #assemble and pass to class method
    def pass_for_request(self):

        get_price = BtcAPI(self.url, self.api_id, self.json_key)
        get_price.btc_api_call() 
        
#API call data (pythonic improvement: place in .ini, via configparser)        

def Coindesk():
    coindesk = Price("coindesk","https://api.coindesk.com/v1/bpi/currentprice.json","bpi.USD.rate_float") #(api_id, url, json_tree)
    coindesk.pass_for_request()

def Bitstamp():
    bitstamp = Price("bitstamp","https://www.bitstamp.net/api/ticker/", "last")

def CoinMarketCap():
    coin_market_cap = BtcAPI("coinmarketcap", "https://api.coinmarketcap.com/v1/ticker/", "[0].price_usd")
    coin_market_cap.pass_for_request()

#def CryptoCompare:


Coindesk()
