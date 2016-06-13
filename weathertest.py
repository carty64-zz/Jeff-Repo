import urllib
import json
import time
import os
# -*- coding: UTF-8 -*-

DS_API = os.environ["DARK_SKY"]
response = urllib.urlopen ('https://api.forecast.io/forecast/%s/37.7782,-122.4122' % DS_API).read()
json = json.loads(response)

#file = open('weatherjson.json', 'r')
#data = file.read()
#json = json.loads(data, encoding="utf-8")


summary = json['minutely']['summary']
summary = summary.lower()
forecast = json['hourly']['summary']
forecast = forecast.lower()
t0 = int(time.time())
temp_current = int(round(json['currently']['temperature'],1))
x = 0
#temps = []
#for hour in json['hourly']['data']:
#  temps.append(hour['temperature'])

#times = []
#for t in json['hourly']['data']:
#  times.append(t['time'])

#rain = []
#for r in json['hourly']['data']:
#  rain.append(r['precipProbability'])

#print t0
#print (times[0] - t0)/60, (times[1] - t0)/60, (times[2] - t0)/60

#if json['hourly']['data'][1]['time'] - t0 > 30:
# print 'greater'
#else:
# print 'less'
rain = json['hourly']['data'][x]['precipProbability'] * 100
temp1 = json['hourly']['data'][3]['temperature']
temp1 = int(round(temp1,1))
#temp2 = int(temps[1])

#print int(temps[x])

# data[1] is the best place to start for forecast
print "Current:\n%i with %i%% chance of rain and %s\n" % (temp_current,rain,summary)
print "Forecast:\n%i and %s\n" % (temp1,forecast)
#x = int(raw_input('How far ahead? '))
