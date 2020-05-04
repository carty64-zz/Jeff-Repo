"""
https://learn.adafruit.com/adafruit-led-backpack/0-54-alphanumeric-circuitpython-and-python-usage
"""
import time
import board
from adafruit_ht16k33.segments import Seg14x4
 
i2c = board.I2C()
display = Seg14x4(i2c)

#display = displayBackpack16x8(i2c, address=0x71)

display.brightness = 0.2
display.blink_rate = 0


#display.print("1234")

#display.marquee("HI DANIELLE I HOPE YOUR SHIFT IS GOING WELL    ", 0.3, False)

x = 10

while x != 0:
    display.print(x)
    x -= 1
    time.sleep(1)
    display.fill(0)
    if x == 0:
        display.print("BOOM")