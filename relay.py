#!/usr/bin/env python3


import sys
import time

import automationhat
time.sleep(0.1) # Short pause after ads1015 class creation recommended


try:
    from PIL import Image, ImageDraw
except ImportError:
    print("""This example requires PIL.
Install with: sudo apt install python{v}-pil
""".format(v="" if sys.version_info.major == 2 else sys.version_info.major))
    sys.exit(1)
import ST7735 as ST7735

print(""" Running Agrocube bio cell management system 

Press CTRL+C to exit.
""")

def draw_states(channels):
    # Open our background image.
    # image = Image.open("images/agrocube.JPG")
    # draw = ImageDraw.Draw(image)
    offset = 0

    disp.display(image)
    time.sleep(2) 

# Create ST7735 LCD display class.
disp = ST7735.ST7735(
    port=0,
    cs=ST7735.BG_SPI_CS_FRONT,
    dc=9,
    backlight=25,
    rotation=270,
    spi_speed_hz=4000000
)

# Initialize display.
disp.begin()

#on_colour = (99, 225, 162)
#off_colour = (235, 102, 121)
#bg_colour = (25, 16, 45)


while True:
       image = Image.open("images/agrocube.JPG")
       draw = ImageDraw.Draw(image)
       # Toggle channel back.
       disp.display(image)
       automationhat.relay.on()
       time.sleep(1)
       # def draw_states(channels):
       # Open our background image.
       #image = Image.open("images/agrocube.JPG")
       #draw = ImageDraw.Draw(image)
       offset = 0
       automationhat.relay.off()
       time.sleep(10)
       #increase the off time to required number of hours. i.e for 6 hours delay will be 21600 seconds 
       disp.display(image)
