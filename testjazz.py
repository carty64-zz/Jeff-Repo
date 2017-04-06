import time
from slackclient import SlackClient
import os

token = os.environ["JAZZBOT_KEY"]

sc = SlackClient(token)

#user can set a favorite team
#def favs():
posttime = 0

def scores():
    sc.api_call("chat.postMessage", channel="jazzbot_test", text="here are the scores!", as_user = 'true')

def pic():
    sc.api_call('files.upload', channels="jazzbot_test", filename='pic.png', file=open('/home/pi/Desktop/camera_pics/2017-04-05-21.46.23.jpg.jpg', 'rb'))


if sc.rtm_connect():
    while(1):
        message = sc.rtm_read()
        print message
        time.sleep(1)
        if len(message) > 0 and message[0].has_key('type') and message[0]['type'] == 'message':
            if '@U0X540ZK2' in message[0]['text'] and 'scores' in message[0]['text'].lower():
                posttime = time.time()
                scores()
            if '@U0X540ZK2' in message[0]['text'] and 'pic' in message[0]['text'].lower() and time.time() - posttime > 1:
                posttime = time.time()
                pic()            

else:
    print "Connection Failed"
