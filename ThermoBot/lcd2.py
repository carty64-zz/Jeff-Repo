#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from w1thermsensor import W1ThermSensor

lcd = Adafruit_CharLCD()


lcd.begin(16, 1)

sensor = W1ThermSensor()

#temp_k = sensor.get_temperature(W1ThermSensor.KELVIN)
   #temp_f = sensor.get_temperature(W1ThermSensor.DEGREES_F)
   #temp_c = sensor.get_temperature(W1ThermSensor.DEGREES_C)

lcd.clear()

while 1:
  temp_all = sensor.get_temperatures([W1ThermSensor.DEGREES_C, W1ThermSensor.DEGREES_F])
  lcd.message(datetime.now().strftime('%b %d  %l:%M %p\n'))
  lcd.message('  %.1fF  %.1fC' % (round(temp_all[1], 1),round(temp_all[0],1)))
  lcd.home()
  sleep(0)
