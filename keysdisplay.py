#https://learn.adafruit.com/matrix-keypad?view=all
import board
import serial
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
import adafruit_matrixkeypad
import time
from adafruit_ht16k33.segments import Seg14x4
 
i2c = board.I2C()
display = Seg14x4(i2c)

cols = [digitalio.DigitalInOut(x) for x in (board.D21, board.D20, board.D16)]
rows = [digitalio.DigitalInOut(x) for x in (board.D12, board.D26, board.D19, board.D13)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True: 
    keys = keypad.pressed_keys
    display.fill(0)
    if keys:
        print keys.strip('"\'')
    time.sleep(0.2)