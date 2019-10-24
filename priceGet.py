# This file uses the CryptoCompare API to grab current price, historical data, and today's daily average price of BTC
# To use this API, you need to make an account at https://www.cryptocompare.com and get an API key
# Don't use my username and API key, because each user only gets 100 requests per day without paying

import requests

def getBtcPrice(user, apiKey):
    URL = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    data = requests.get(URL, auth=(user, apiKey)).json()
    return data

def getBtcHistorical(user, apiKey):
    limit = 10 # gets 10 units of timeFrame
    timeFrame = "day" # (day, hour, minute)
    URL = "https://min-api.cryptocompare.com/data/histo" + timeFrame + "?fsym=BTC&tsym=USD&limit=" + str(limit-1)
    data = requests.get(URL, auth=(user, apiKey)).json()
    return data

def getBtcDailyAvg(user, apiKey):
    URL = "https://min-api.cryptocompare.com/data/dayAvg?fsym=BTC&tsym=USD"
    data = requests.get(URL, auth=(user, apiKey)).json()
    return data

########################## MAIN ##########################

user = 'jack.zumwalt'
apiKey = '0e8d5efdad7b13a47343c8df519cd255182d9dfc14e814f4e1d0e474181cbba9'

print("----------------")
print("Current BTC price: " + str(getBtcPrice(user, apiKey)))
print("Daily average of BTC: " + str(getBtcDailyAvg(user, apiKey)))
print("----------------")

history = getBtcHistorical(user, apiKey)

i = 1
for x in history['Data']:
    print("----- Day " + str(i) + " -----")
    print("time: " + str(x.get('time')))
    print("high: " + str(x.get('high')))
    print("low: " + str(x.get('low')))
    print("open: " + str(x.get('open')))
    print("volFrom: " + str(x.get('volumefrom')))
    print("volTo: " + str(x.get('volumeto')))
    print("close: " + str(x.get('close')))
    i += 1





