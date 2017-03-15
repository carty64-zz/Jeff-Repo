import time
from slackclient import SlackClient
import os

token = os.environ["JAZZBOT_KEY"]

sc = SlackClient(token)

if sc.rtm_connect():
    while(1):
      message = sc.rtm_read()
      print message
      time.sleep(1)
#    if message == "scores":
#      scores()
else:
  print "Connection Failed, invalid token?"

def scores():
  sc.api_call(
    "chat.postMessage", channel="jazzbot_test", text="here are the scores!", as_user = 'true'
  )
