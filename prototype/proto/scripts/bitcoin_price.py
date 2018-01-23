#This is the API for BTC price request. 

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
