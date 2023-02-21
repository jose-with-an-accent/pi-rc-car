from evdev import InputDevice, categorize, ecodes
from gpiozero import Motor
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import board

motor = Motor(forward=23, backward=24)

i2c = board.I2C()
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
small_font = ImageFont.truetype('FreeSans.ttf', 12)
large_font = ImageFont.truetype('FreeSans.ttf', 33)
disp.fill(0)
disp.show()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
controller = InputDevice('/dev/input/event1')
print(controller)
def display_status(top_line):
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((0, 0),  top_line, font=large_font, fill=255)
    disp.show()

while True:
    display_status("Car Status")

    for event in controller.read_loop():
        print(categorize(event))
