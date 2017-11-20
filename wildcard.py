#!/usr/bin/python

from slackclient import SlackClient
import os
import random

token = os.environ["CHAT_KEY"]
sc = SlackClient(token)
chatbot = '<@U7F2D8W90>'

def wildcard(sender,channel):
  if channel.startswith('C') == True:
      channel_info = sc.api_call("channels.info", channel=channel)
      member_ids = channel_info['channel']['members']
  elif channel.startswith('G') == True:
      channel_info = sc.api_call("groups.info",channel=channel)
      member_ids = channel_info['group']['members']
  member_names = []
  for member_id in member_ids:
    user_info = sc.api_call("users.info",user = member_id)
    member_names.append("<@" + user_info['user']['name'] + ">")
# Inital group only had bots and me, so ignoring bots left an empty list
# should create an error for this, which would apply in a DM
#    if user_info['user']['deleted'] == False and user_info['user']['is_bot'] == False:
#      member_names.append("<@" + user_info['user']['name'] + ">")
  sender = sc.api_call("users.info",user = sender)
  sender = "<@" + sender['user']['name'] + ">"
  pos = member_names.index(sender)
  del member_names[pos]
  x = random.randint(0,len(member_names)-1)
  name = member_names[x]
  sc.api_call("chat.postMessage", channel=channel, text="How about "+name+"?", as_user = 'true')

if __name__ == "__wildcard__":
  wildcard()
