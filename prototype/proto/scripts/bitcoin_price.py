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
    

    api_id = 'Coindesk'
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'               
    json_tree = json_dict['time']['updated'] # Reference this after json data is pulled, to variablize the output and store it.

    def __init__(self):
    
        self.current_us_price = current_us_price
'''    
coindesk_url = Coindesk()
coindeskoutput = coindesk_url.url
print(coindeskoutput)
'''


class Bitstamp:

    api_id = 'Bitstamp'
    url = 'https://www.bitstamp.net/api/ticker/'
    json_tree = json_dict['last']


    def __init__(self, json_dict):

        self.current_us_price = current_us_price


class CoinMarketCap:
    
    api_id = 'CoinMarketCap'
    url = ' '
    json_tree = ' ' #add this when you know what the tree looks like

    def __init__(self):

        self.current_us_price = current_us_price


class CryptoCompare:

    api_id = 'CryptoCompare'
    url = ' '
    json_tree = ' ' #add this when you know what the tree looks like

    def __init__(self):

        self.current_us_price = current_us_price

def fetch_json():

    current_us_price = json_tree #no idea if this will fly... have to try
    return(current_us_price)


