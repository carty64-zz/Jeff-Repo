import time
from slackclient import SlackClient
import os

token = os.environ["JAZZBOT_KEY"]

sc = SlackClient(token)

print sc.api_call(
    "chat.postMessage", channel="#lower_bowl", text="With a gentle push and a mild arc, the old Jazzbot hits home :basketball:",
    username='jazzbot', icon_emoji=:basketball:
)

if sc.rtm_connect():
  while(1):
    message = sc.rtm_read()
    print message
    if len(message) > 0 and message[0].has_key('type') and message[0]['type'] == 'message':
      channel = message[0]['channel']
      if 'hood' in message[0]['text'].lower():
        print sc.api_call
        (
          "chat.postMessage", channel = channel, text=":thermometer:",
          username='jazzbot', icon_emoji=':basketball:'
        )
        #                 elif '@U0X540ZK2' in message[0]['text'] and 'temp c' in message[0]['text'].lower():
        #                   temp_c = round(sensor.get_temperature(W1ThermSensor.DEGREES_C),1)
        #                   print sc.api_call(
        #                     "chat.postMessage", channel = channel, text=":thermometer:" + str(temp_c) + u'\xb0' + "c",
        #                     username='thermobot', icon_emoji=':thermobot:'
        #             )
                        # elif '@U0X540ZK2' in message[0]['text'] and 'temp k' in message[0]['text'].lower():
                        #         temp_k = round(sensor.get_temperature(W1ThermSensor.KELVIN),1)
                        #         print sc.api_call(
                        #                 "chat.postMessage", channel = channel, text=":thermometer:" + str(temp_k) + u'\xb0' + "k",
                        #                 username='thermobot', icon_emoji=':thermobot:'
                        #         )
                        # elif message[0]['channel'][0] == 'D' and not message[0].has_key('username'): # and  message[0]['message']['subtype'] != 'bot_mess$
                        #         temp_f = round(sensor.get_temperature(W1ThermSensor.DEGREES_F),1)
                        #         print sc.api_call(
                        #           "chat.postMessage", channel = channel, text=":thermometer:" + str(temp_f) + u'\xb0' + "f",
                        #           username='thermobot', icon_emoji=':thermobot:'
                        #           )

    time.sleep(1)
else:
  print "Connection Failed, invalid token?"
  
  ######## NEW UPDATES ########
  
import time
from slackclient import SlackClient
import json
import requests
import datetime


token = "xoxb-31174033648-2rFG6jud5QpjJnlA0qLBSLPC"
sc = SlackClient(token)

today =  datetime.date.today().strftime("%Y%m%d")
url = 'http://data.nba.com/data/10s/json/nbacom/2015/gameline/%s/games.json' % today
#url = 'http://data.nba.com/data/10s/json/nbacom/2015/gameline/20160331/games.json'
response = requests.get(url)
data = response.content
nbadata = json.loads(data)
matchup = []
results = []


#for x in nbadata['games']:
#  games = x['teams']
#  for z in games:
#    matchup.append(str(z.get('awayTeam') or z.get('homeTeam')))
#    results.append(z['scores'][0])


def table():
  for c1, c2 in zip(matchup, results):
    return c1, c2

#print sc.api_call(
#    "chat.postMessage", channel="#jazzbot_test", text='%s\n%s' % (matchup,results), as_user='true:'
#)

#print sc.api_call(
#    "chat.postMessage", channel="#lower_bowl", text="I'm bringin my talents to #lower_bowl :basketball:", as_us$
#)

if sc.rtm_connect():
  while(1):
    message = sc.rtm_read()
    print message
    if len(message) > 0 and message[0]['type'] == 'message':
#     print message[0]['message']['text']
      channel = message[0]['channel']
      if 'hood' in message[0]['text'].lower():
        print sc.api_call(
          "chat.postMessage", channel=channel, text="Prince of Threes :dart:",
          username='jazzbot', as_user="true:"
          )
      if 'hood' in message[0]['message']['text'].lower():
        print sc.api_call(
          "chat.postMessage", channel=channel, text="Prince of Threes :dart:",
          username='jazzbot', as_user="true:"
          )
      else:
        print sc.api_call("chat.postMessage", channel=channel, text="GO JAZZ :basketball:", as_user="true:")
    time.sleep(1)
else:
  print "Connection Failed, invalid token?"
