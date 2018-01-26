#This is the API for BTC price request. 
# Make this OBJ oriented. 
# Average all the amounts, and push that to the program

import json
import urllib.request

#Coindesk#
'''

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
req = urllib.request.Request(url, headers=hdr)

readdata = urllib.request.urlopen(req)
json_data = readdata.read()
#print(json_data)

json_dict = json.loads(json_data)

current_utc_time = json_dict['time']['updated']
current_us_price = json_dict['bpi']['USD']['rate_float']

print(current_utc_time)
print(current_us_price)


#Coinbase API


url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
#https://developers.coinbase.com/docs/wallet/guides/price-data  <- API Doc
#has a pip installable lib. Dependency undesirable, but better than cURL.



#Bitstamp API
#https://www.bitstamp.net/api/



#Coinmarketcap API
# https://coinmarketcap.com/api/
# Will offer historical data

#Cryptocompare API (Very robust, in terms of data)
#https://www.cryptocompare.com/api/#-api-data-pricehistorical-
'''

import json
import urllib.request

class BTC_API:

    def __init__(self, url, api_id):
        self.url = url
        self.api_id = api_id

    def build_api_url(self):
        #build api url or pass it to args

    def api_req(self):
        #GET request

    def return_data(self):
        # Parse JSON, return data


api_url_dict = { 'Coindesk' : 'https://api.coindesk.com/v1/bpi/currentprice.json' , 'Coinbase' : 'https://api.coinbase.com/v2/prices/spot?currency=USD', 'Bitstamp' : ' ', 'CoinMarketCap' : ' ' , 'CryptoCompare' : ' ' }  

# Loop through dict to pull both name and url into variables, instantiate classes, pull data, parse, and boom!
