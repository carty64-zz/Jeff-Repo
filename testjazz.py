import time
from slackclient import SlackClient
import os

token = os.environ["JAZZBOT_KEY"]

sc = SlackClient(token)

#print sc.api_call(
#    "chat.postMessage", channel="#lower_bowl", text="'https://slack.com/api/files.upload?token=%s&filename=test&channels=jazzbot_test&pretty=1'" % token,
#    as_user = 'true'
#)

print sc.api_call(
	"https://slack.com/api/files.upload?token=%s&file='/home/pi/pic.jpg'&filename=upload&channels=jazzbot_test&pretty=1" % token
)


#https://slack.com/api/files.upload?token&filename=Head%20shot&channels=jazzbot_test&pretty=1
