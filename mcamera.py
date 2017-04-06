from gpiozero import MotionSensor
from datetime import datetime
from time import time, sleep
from picamera import PiCamera

camera = PiCamera()
camera.framerate = 30
pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	filename = datetime.now().strftime("%Y-%m-%d-%H.%M.%S.jpg")
	camera.capture('/home/pi/Desktop/camera_pics/%s' % filename)
#.h264")
#	sleep(0.5)
#	camera.start_recording(filename)
	pir.wait_for_no_motion()
	sleep(1)
#	camera.stop_recording()
