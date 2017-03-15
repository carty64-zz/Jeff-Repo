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


#print sc.api_call(
#    "chat.postMessage", channel="#jazzbot_test", text="'https://slack.com/api/files.upload?token=%s&filename=test&channels=jazzbot_test&pretty=1'" % token,
#    as_user = 'true'
#)

#print sc.api_call(
#	"https://slack.com/api/files.upload?token=%s&file='/home/pi/pic.jpg'&filename=upload&channels=jazzbot_test&pretty=1" % token
#)


#https://slack.com/api/files.upload?token&filename=Head%20shot&channels=jazzbot_test&pretty=1
