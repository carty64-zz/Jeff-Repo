
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

t = (0.8)

while (t > 0.2):
  GPIO.output(18, True)
  time.sleep(t)
  GPIO.output(18, False)
  time.sleep(t)
  t = t-0.1
t = 0.1
n = 8
while (n > 0):
 GPIO.output(18, True)
 time.sleep(t)
 GPIO.output(18, False)
 time.sleep(t)
 n = n - 1
