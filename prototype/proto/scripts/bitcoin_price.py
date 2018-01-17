#This is the API for BTC price request. 

import json
import urllib.request


url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
req = urllib.request.Request(url, headers=hdr)

readdata = urllib.request.urlopen(req)
json_data = readdata.read()
print(json_data)
