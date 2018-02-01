#!/usr/bin/python

#This is the API for BTC price request. 
# Average all the amounts, and push that to the program

import json
import urllib.request
#https://www.cryptocompare.com/api/#-api-data-pricehistorical-


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

    def pull_json(self, json_dict):

        current_utc_time = json_dict['time']['updated']
        current_us_price = json_dict['bpi']['USD']['rate_float']
            
        return(current_utc_time)
        return(current_us_price)



'''


class Coinbase:


class Bitstamp:


class CoinMarketCap:


class CryptoCompare:


api_url_dict = { 

        'Coindesk' : 'https://api.coindesk.com/v1/bpi/currentprice.json' , 
        'Coinbase' : 'https://api.coinbase.com/v2/prices/spot?currency=USD', 
        'Bitstamp' : ' ', 
        'CoinMarketCap' : ' ' , 
        'CryptoCompare' : ' ' 
        
        }  
'''
# Loop through dict to pull both name and url into variables, instantiate classes, pull data, parse, and boom!
