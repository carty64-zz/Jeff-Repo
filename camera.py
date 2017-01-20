from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
camera.annotate_text_size = 140
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')
camera.annotate_text = "This is so much text!"
sleep(3)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
