#This is the API for BTC price request. 
# Make this OBJ oriented. 
# Average all the amounts, and push that to the program

import json
import urllib.request

#Coindesk#


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
