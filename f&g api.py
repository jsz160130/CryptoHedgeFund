#Pulls Fear and Greed and calculates MA. Trying to graph values, etc...

#Libraries
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

import json
import requests
import urllib

from datetime import datetime
from datetime import datetime, timedelta

#MA function
def movingaverage(values,window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights,'valid')
    return smas

#Data
url = requests.get('https://api.alternative.me/fng/?limit=100').json()


#Data Organization 
n = 0
x = [0,0]
y = [0,0]
while n < 99:
    n = n+1
    val = (url['data'][n]['value'])
    time = int((url['data'][n]['timestamp']))
    x.append(time)
    y.append(val)
    #print("F&G:",val,"@ ",datetime.fromtimestamp(time))


#MA
malist = (movingaverage(list(map(float,y)),50))
count = 0
current_date = datetime.now()
first_date = current_date - timedelta(days=len(malist))

for i in malist:
    count = count + 1
    new_date = first_date + timedelta(days=count)
    print(i, "@", new_date.strftime('%Y-%m-%d'))

#Graph(graphing is a fucking cunt)
#plt.plot(x, y)
#plt.show()

