#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import os
from datetime import datetime, timedelta
from time import sleep
from slackclient import SlackClient
from collections import defaultdict
import random
import wildcard

token = os.environ["CHAT_KEY"]
sc = SlackClient(token)

channel_info = sc.api_call(
    "groups.info",channel = 'G0XFPT083')

member_ids = channel_info['group']['members']
#print member_ids
member_names = []

for member_id in member_ids:
  user_info = sc.api_call("users.info",user = member_id)
  if user_info['user']['deleted'] == False and user_info['user']['is_bot'] == False:
    member_names.append("<@" + user_info['user']['name'] + ">")


#chatbot id is @U7F2D8W90
if sc.rtm_connect():
  while True:
    message = sc.rtm_read()
    print message
    sleep(1)
    if len(message) > 0 and message[0].has_key('type') and message[0]['type'] == 'message':
      text = message[0]['text']
      if '@U7F2D8W90' in text:
        text = text.lower()
        if 'random' in text:
          wildcard.wildcard(member_names)	
        if 'smile' in text:
          sc.api_call("chat.postMessage", channel="jazzbot_test", text=":smile:", as_user = 'true')
