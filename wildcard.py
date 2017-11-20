#!/usr/bin/python

import os
import random

from slackclient import SlackClient

token = os.environ['CHAT_KEY']
slack_client = SlackClient(token)


def wildcard(sender, channel):
    if channel.startswith('C'):
        channel_info = slack_client.api_call('channels.info', channel=channel)['channel']
    elif channel.startswith('G'):
        channel_info = slack_client.api_call('groups.info', channel=channel)['group']
    member_names = [slack_client.api_call('users.info', user=member_id)['user']['name'] for member_id in channel_info['members'] if member_id != sender]
    random_name = random.choice(member_names)
    slack_client.api_call('chat.postMessage', channel=channel, text="How about @%s?" % random_name, as_user=True)
