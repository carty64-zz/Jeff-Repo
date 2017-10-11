#!/usr/bin/python
# This Python file uses the following encoding: utf-8

import os
from datetime import datetime, timedelta
from time import sleep
from slackclient import SlackClient
from numpy import random
from collections import defaultdict

token = os.environ["CHAT_KEY"]
sc = SlackClient(token)

channel_info = sc.api_call(
    "groups.info",
    channel = 'G0XFPT083',
    )

member_ids = channel_info['group']['members']

member_names = []

for member_id in member_ids:
  user_info = sc.api_call("users.info",user = member_id)
  if user_info['user']['deleted'] == False and user_info['user']['is_bot'] == False:
    member_names.append("<@" + user_info['user']['name'] + ">")

if sc.rtm_connect():
  while True:
    message = sc.rtm_read()
    if len(message) > 0 and message[0].has_key('type') and message[0]['type'] == 'message':
      if 'U7F2D8W90' in message[0]['text'] and 'random' in message[0]['text'].lower():
        x = random.randint(0,len(member_names))
        sc.api_call(
        "chat.postMessage", channel="#jazzbot_test", text="How about "+member_names[x]+"?",
        username='Chat', icon_emoji=':bowtie:'
      )

# member_names = random.permutation(member_names)
# member_names = random.permutation(member_names)
# member_names = member_names.tolist()

# num_users = len(member_names)

# if num_users % 2 == 0:
#     matches = num_users / 2
# else:
#     matches = (num_users + 1) / 2

# group1 = member_names[0:matches-1]
# group2 = member_names[matches-1:]

# if len(group2) > len(group1):
#     group1.append("your choice!")

# matched = []
# while matches > 0:
#     matched.append(group2[matches-1] + " and " + group1[matches-1])
#     matches -= 1

# matched = ", ".join(matched)

# sc.api_call(
#     "chat.postMessage", channel = "random", text = matched)


