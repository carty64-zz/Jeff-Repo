#https://learn.adafruit.com/matrix-keypad?view=all
import board
import serial
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
import adafruit_matrixkeypad

# Membrane 3x4 matrix keypad on Raspberry Pi -
# https://www.adafruit.com/product/419
cols = [digitalio.DigitalInOut(x) for x in (board.D21, board.D20, board.D16)]
rows = [digitalio.DigitalInOut(x) for x in (board.D12, board.D26, board.D19, board.D13)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

while True: 
    keys = keypad.pressed_keys
    if keys:
        print ("Pressed: ", keys)
    time.sleep(0.2)
   
