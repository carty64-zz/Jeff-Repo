import urllib
import json as m_json
import time
# -*- coding: UTF-8 -*-

response = urllib.urlopen ('https://api.forecast.io/forecast/a7c7969da1021ba738c1faf83d35fc0e/37.7782,-122.4122').read()
json = m_json.loads(response)
forecast = []

def fcast(hours):
    for time in json['hourly']['data']:
        forecast.append(json['hourly']['data'][1]['temperature'])

print fcast(2)
# data[1] is the best place to start for forecast

forecast1 = int(json['hourly']['data'][1]['temperature'])
forecast3 = int(json['hourly']['data'][3]['temperature'])
cor1 = int(json['hourly']['data'][1]['precipProbability']) * 100
cor3 = int(json['hourly']['data'][3]['precipProbability']) * 100
print "%i\xb0 with %i%% chance of rain." % (forecast1,cor1)
print forecast3
