import binascii
import sys
from time import sleep
import Adafruit_PN532 as PN532


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
keys = open('keys.txt','r')
key_list = eval(keys.read())
keys.close()

# Main loop to detect cards and read a block.
print('Waiting...')
while True:
    # Check if a card is available to read.
    uid = pn532.read_passive_target()
    # Try again if no card is available.
    if uid is None:
        continue
    uid = binascii.hexlify(uid)
    if uid in key_list:
        print key_list[uid]
    else:
        print 'Key not valid'
    sleep(0.5)
