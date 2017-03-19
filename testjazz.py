import time
from slackclient import SlackClient
import os

token = os.environ["JAZZBOT_KEY"]

sc = SlackClient(token)

#user can set a favorite team
def favs():




def scores():
    sc.api_call("chat.postMessage", channel="jazzbot_test", text="here are the scores!", as_user = 'true')

if sc.rtm_connect():
    while(1):
        message = sc.rtm_read()
        print message
        time.sleep(1)
        if len(message) > 0 and message[0].has_key('type') and message[0]['type'] == 'message':
            if <@jazzbot> in message[0]['text'] and "scores" in message[0]['text'].lower:
                scores()

else:
    print "Connection Failed"
