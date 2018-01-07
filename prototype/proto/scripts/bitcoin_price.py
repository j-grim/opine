#This is the API for BTC price request. 

import json
import urllib.request

exchange_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
user_agent= 'Mozilla/5.0 (Windows NT 6.1; Win64; X64)'
values = {'name' : 'Mischa Kolding',
        'location' : 'Los Angeles',
        'language' : 'Python' }
headers = {'User-Agent' : user_agent }

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(exchange_url, data, headers)
with urllib.request.urlopen(req) as response:
    the_json = response.read()
print(the_json)
