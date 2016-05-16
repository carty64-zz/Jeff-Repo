from twilio.rest import TwilioRestClient

ACCOUNT_SID = 'AC0c10aca034686c87b96740a0335f6853'
AUTH_TOKEN = '6d42564226d7f2c81cd3ac3ae4ecc5fa'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+18019300834", 
    from_="+15005550006", 
    body="Hi Jeff!", 
    media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg", 
)
