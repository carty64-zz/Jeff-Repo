#!/usr/bin/python

import Adafruit_CharLCD as LCD
import binascii
import sys
from time import sleep
import Adafruit_PN532 as PN532

# Configure LCD
lcd_rs        = 06
lcd_en        = 13
lcd_d4        = 20
lcd_d5        = 17
lcd_d6        = 21
lcd_d7        = 22
lcd_backlight = 4
lcd_columns = 16
lcd_rows    = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,lcd_columns, lcd_rows, lcd_backlight)
lcd.clear()

# Configuration for a Raspberry Pi:
CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

# Create an instance of the PN532 class.
pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)

# Call begin to initialize communication with the PN532.  Must be done before
# any other calls to the PN532!
pn532.begin()

# Get the firmware version from the chip and print(it out.)
ic, ver, rev, support = pn532.get_firmware_version()
print('Found PN532 with firmware version: {0}.{1}'.format(ver, rev))

# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

# Load keys dictionary
active = 'active'
inactive = 'invalid'

keys = open('keys.txt','r')
key_list = eval(keys.read())
keys.close()
lcd.clear()

# Main loop to detect cards and read a block.
lcd.message('Waiting...')
lcd.blink(True)

while True:
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    # Try again if no card is available.
    if uid is None:
        continue
    uid = binascii.hexlify(uid)
    if uid in key_list and key_list[uid][1]==active:
        lcd.clear()
        lcd.blink(False)
        lcd.message('ACCESS GRANTED.\nHELLO '+key_list[uid][0].upper())
    else:
        lcd.clear()
        lcd.blink(False)
        lcd.message('ACCESS DENIED')
        sleep(2.0)
        lcd.clear()
    lcd.message('Waiting...')
    lcd.blink(True)
