#!/usr/bin/python

from collections import defaultdict
from datetime import datetime
from time import time, sleep
import sqlite3
from slackclient import SlackClient
import os

token = os.environ["CHATBOT"]
conn = sqlite3.connect('words.db')
c = conn.cursor()
message = ' '

sc = SlackClient(token)

if sc.rtm_connect():
  while True:
    print sc.rtm_read()
    sleep(1)
  # while True:
  #   message = sc.rtm_read()
  #   if message.has_key[type]
  #   message = message.split()
  #   if message.startswith() == '@chatbot':
#    sc.api_call(
#    "chat.postMessage", channel="#lower_bowl", text="HI",
#    username='Chat', icon_emoji=':bowtie:'
#    )
#  sleep(4)
else:
  print "bad connection"