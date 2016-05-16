from twilio.rest import TwilioRestClient
import os

ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_API"]
print ACCOUNT_SID
print AUTH_TOKEN

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

#client.messages.create(
#    to="+18019300834", 
#    from_="+15005550006", 
#    body="Hi Jeff!", 
#    media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg", 
#)
