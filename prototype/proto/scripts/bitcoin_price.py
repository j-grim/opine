#!/usr/bin/python

#This is the API for BTC price request. 
# Average all the amounts, and push that to the program

import json
import urllib.request


class BtcAPI:

    def __init__(self, url, api_id):
        self.url = url
        self.api_id = api_id

    def btc_api_call(self):

        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
        req = urllib.request.Request(url, headers=hdr)
        readdata = urllib.request.urlopen(req)
        json_data = readdata.read()

        json_dict = json.loads(json_data)
        return(json_dict)

'''
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
api_id ="Coindesk"

get_price = BtcAPI(url, api_id)
get_price.btc_api_call()
'''


class Coindesk:
            
    def __init__(self, json_dict):

        self.current_utc_time = current_utc_time
        self.current_us_price = current_us_price
        api_id = 'Coindesk'
        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'               
        json_tree = json_dict['time']['updated']


class Bitstamp:

    def __init__(self, json_dict):

        self.current_us_price = current_us_price
        api_id = 'Bitstamp'
        url = 'https://www.bitstamp.net/api/ticker/'
        json_tree = json_dict['last']

def fetch_json():

    current_us_price = json_tree #no idea if this will fly... have to try
    return(current_us_price)

'''

class CoinMarketCap:


class CryptoCompare:


api_url_dict = { 

        'Coindesk' : 'https://api.coindesk.com/v1/bpi/currentprice.json' , 
        'Coinbase' : 'https://api.coinbase.com/v2/prices/spot?currency=USD', 
        'Bitstamp' : ' ', 
        'CoinMarketCap' : ' ' , 
        'CryptoCompare' : 'https://www.cryptocompare.com/api/#-api-data-pricehistorical-'
        
        }  
'''
