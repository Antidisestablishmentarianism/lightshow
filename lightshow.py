#!/usr/bin/sudo / usr/bin/python

import RPi.GPIO as GPIO
import random
from time import sleep

# Use board pin numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Start a new dictionary with desired LED names
leds = {'floor':[], 'top-left':[]}

# TAke name of led and list of pins for RGB
def setupled(name, pins):
	for i in range(0, 3):
		GPIO.setup(pins[i], GPIO.OUT)
		leds[name].append(GPIO.PWM(pins[i], 100))

setupled('floor', [3, 5, 7])
setupled('top-left', [8, 10, 11])

# Start all PWMs
for key, value in leds.items():
	for i in value:
		i.start(0)

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
PURPLE = [255, 0, 255]
CYAN = [0, 255, 255]

def setcolor(led, color):
	for i in xrange(0, 3):
		leds[led][i].ChangeDutyCycle((255 - color[i]) * 100 / 255)
	print('Setting {} to {}'.format(led, color))

# Start program here
colors = []
bools = []
for i in xrange(0, 6):
	colors.append(random.randrange(0, 256))
	bools.append(bool(random.getrandbits(1)))

while True:
	for i in xrange(0, 6):
		if (colors[i] < 1 or colors[i] > 254):
			bools[i] = not bools[i]
		if (bools[i]):
			colors[i] = colors[i] + 1
		elif (not bools[i]):
			colors[i] = colors[i] - 1

	setcolor('floor', colors[0:3])
	setcolor('top-left', colors[3:6])
	sleep(0.001)

# Stop all PWMs
for key, value in leds.items():
	for i in value:
		i.stop()

GPIO.cleanup()
