#!/usr/bin/env python
 
from time import sleep
import RPi.GPIO as GPIO
 
GPIO.setmode (GPIO.BOARD)
LED = 7 # LED connected to GPIO 7
ledState = False # Set the initial LED State to off
HALL_SENSOR = 18 # Hall sensor connected to GPIO 18
hallActive = False # State Hall effect sensor
 
GPIO.setwarnings(False)
 
GPIO.setup (LED, GPIO.OUT) # Setup the GPIO pin connected to the LED as output
GPIO.setup (HALL_SENSOR, GPIO.IN) # Setup the GPIO pin connected to the Hall Sensor to read as input
 
GPIO.output(LED, ledState)
 
# Main program loop
while True:
 
 try:
    # Wait for a falling or rising edge from the hall sensor before executing the code below
    GPIO.wait_for_edge(HALL_SENSOR, GPIO.BOTH)
 
    # NOTE - The Hall effect sensor is HIGH by default
    # and low if there is a magnet.
 
    # Get the current state of the hall sensor and store it in a variable
    hallActive = GPIO.input(HALL_SENSOR)
 
    if( hallActive == False ):
        print("Switch state active, falling edge detected - LED ON")
        ledState = True
    else:
        print("Switch state off, rising edge detected - LED OFF")
        ledState = False
 
    # Turn on the LED when the sensor is activated
    GPIO.output(LED, ledState)
 
 except KeyboardInterrupt:
    GPIO.output(LED, False) # Turn off the LED on keyboard interrupt
    GPIO.cleanup() # Clean up GPIO on CTRL+C exit
 
# End of main program loop
 
# Clean up on normal exit
GPIO.output(LED, False)
GPIO.cleanup()
