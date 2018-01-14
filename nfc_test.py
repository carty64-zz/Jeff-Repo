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
# Configure PN532 to communicate with MiFare cards.
pn532.SAM_configuration()

active = 'active'
inactive = 'inactive'
# Load keys dictionary
keys = open('keys.txt','r')
key_list = eval(keys.read())
keys.close()

def get_uid():
    try:
        print("Scan token...")
        uid1 = pn532.read_passive_target()
        if uid is None:
            continue
        uid1 = binascii.hexlify(uid1)
        sleep(1.5)
        print("Scan again to confirm...")
        sleep(1)
        uid2 = pn532.read_passive_target()
        if uid is None:
            continue
        uid2 = binascii.hexlify(uid2)
        if uid1 == uid2:
            print "Success!"
            return uid
            break
    except:
        print "Tokens did not match. Try again."
        continue

def add_token():
    get_uid
    if uid in key_list:
        print('Token already added.')
        break
    if uid not in key_list:
        try:
            name = raw_input("Token name? ")
            if name == "":
                continue
            confirm = raw_input("You are about to add %s. Confirm (Y/N) " % name).lower()
            if confirm == 'n':
                break
            if confirm == 'y':
                key_list[uid] = [name,active]
                update_key_list
        except:
            continue


def delete_token(uid):


def change_token(uid):

def update_key_list():
    with open('keybackup.log', 'a') as backup:
        backup.write(key_list)
        backup.close()
    open('keys.txt', 'w').close()
    file = open('keys.txt','w')
    file.write(key_list)
    file.close()

try:
    option = raw_input('What do you want to do? \n1) Add new token.\n2) Delete token.\n3) Change access.\n--> ')
    if option in [1,2,3]:
        break
    if option == 1:
        add_token
        break



    while True:
        if run == 'n':
            print "Goodbye"
            sys.exit()
        if run == 'y':
            try:
                # Main loop to detect cards and read a block.
                print('Waiting for new token...')
                while True:
                    # Check if a card is available to read.
                    uid = pn532.read_passive_target()
                    # Try again if no card is available.
                    if uid is None:
                        continue
                    uid = binascii.hexlify(uid)
                    if uid in key_list and key_list[uid][1]==active:
                        print 'Token already added and is active.'
                        run = run = raw_input("Do you want to try again? (Y/N) ")
                    if uid in key_list and key_list[uid][1]==inactive:
                        print 'Token already added but is inactive.'
                    sleep(1.4)
                    print('Waiting...')
