#iwconfig wlan0 | grep "ESSID" | cut -d\" -f2
#ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1
from twilio.rest import TwilioRestClient
import os
from subprocess import *

#phone number format "+18009998888"
ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_API"]
me = os.environ["PHONE"]
twilio = os.environ["TWILIO_NUM"]

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

ip = "ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1"
ssid = 'iwconfig wlan0 | grep ESSID | cut -d\" -f2'
device = "hostname"
def get_device(device):
        p = Popen(device, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def get_ip(ip):
        p = Popen(ip, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def get_ssid(ssid):
        p = Popen(ssid, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

text_message = (get_device(device)+get_ssid(ssid)+get_ip(ip))

message = client.messages.create(
    to=me, 
    from_=twilio, 
    body=text_message  
#    media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg", 
)
