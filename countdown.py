#!/usr/bin/python

import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep

lcd = Adafruit_CharLCD()

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

lcd.begin(16, 1)

def countdown(n):
  t = (0.8)
  while n > 0:
    lcd.clear()
    lcd.message('%s ' % (n))
    n = n - 1

    ##
    GPIO.output(18, True)
    time.sleep(t)
    GPIO.output(18, False)
    time.sleep(t)
    t = t-0.1
    ##
    sleep(1)
  lcd.clear()
  lcd.message('YOU DED')
countdown(10)

n = 8
while (n > 0):
GPIO.output(18, True)
time.sleep(t)
GPIO.output(18, False)
time.sleep(t)
n = n - 1