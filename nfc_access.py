#!/usr/bin/python

import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import binascii
import sys
from time import sleep
import json
import Adafruit_PN532 as PN532

# Configure LCD
lcd_rs =    digitalio.DigitalInOut(board.D6)
lcd_en =    digitalio.DigitalInOut(board.D13)
lcd_d4 =    digitalio.DigitalInOut(board.D20)
lcd_d5 =    digitalio.DigitalInOut(board.D17)
lcd_d6 =    digitalio.DigitalInOut(board.D21)
lcd_d7 =    digitalio.DigitalInOut(board.D22)
lcd_backlight = digitalio.DigitalInOut(board.D4)
lcd_columns = 16
lcd_rows    = 2
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
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
keys = json.load(open('keys.json'))

lcd.clear()

# Main loop to detect cards
while True:
    lcd.clear()
    lcd.message('READY...')
    lcd.blink(True)
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    # Try again if no card is available.
    if uid is None:
        continue
    uid = binascii.hexlify(uid)
    lcd.clear()
    lcd.blink(False)
    if uid in keys and keys[uid][1]==active:
        lcd.message('ACCESS GRANTED.\nHELLO '+keys[uid][0].upper())
    else:
        lcd.message('ACCESS DENIED')
    sleep(2.5)
    lcd.clear()
