import urllib
import json as m_json
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

KEY = os.environ["WEATHER_API"]

try:
    while(1):
        response = urllib.urlopen ('https://api.forecast.io/forecast/%s/37.7782,-122.4122'%KEY).read()
        json = m_json.loads(response)
        temp = json['currently']['temperature']
        temp = round(temp, 1)
#        print temp
#        print temp < 56
#        print 56 < temp < 67
#        print temp >= 67
        if temp < 57.0:
            GPIO.setup(11, GPIO.OUT)
            GPIO.output(11, True)
            time.sleep(600)
            GPIO.output(11, False)
        elif 57.0 < temp < 67.0:
            GPIO.setup(12, GPIO.OUT)
            GPIO.output(12, True)
            time.sleep(600)
            GPIO.output(12, False)
        elif temp >= 67.0:
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, True)
            time.sleep(600)
            GPIO.output(13, False)
        else:
            time.sleep(60)

except KeyboardInterrupt:
    print " Interrupted :("

finally:
    GPIO.cleanup()
