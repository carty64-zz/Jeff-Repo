import board
import serial
import digitalio
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
import adafruit_fingerprint

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 5
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)
 
# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()

# Draw Some Text
text = "(e) enroll print (f) find print (d) delete print (s) save fingerprint image (r) reset library (q) quit"
#    c = input("> ")"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 4 - font_width // 4, oled.height // 4 - font_height // 4),
    text,
    font=font,
    fill=255,
)
 
# Display image
oled.image(image)
oled.show()
time.sleep(4)
oled.fill(0)
oled.show()