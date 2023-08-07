import matplotlib.pyplot as plt
import numpy as np
import requests
from dateutil import parser

api_url = "https://iot.fvh.fi/opendata/uiras/70B3D57050001A97_v1.json"
response = requests.get(api_url)
response.json()

#raw_data =json.load(response.json())

eventTime = []
water = []
air = []

for e in response.json()['data']:
    eventTime.append(parser.parse(e['time']))
    water.append(e['temp_water'])
    air.append(e['temp_air'])





plt.plot(eventTime, air)
plt.plot(eventTime, water)
  
# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Degrees Celcius')
# giving a title to my graph
plt.title('Temperature Variations')

  
# function to show the plot
plt.show()