#!/usr/bin/sudo / usr/bin/python

import RPi.GPIO as GPIO
import random
from time import sleep

# Use board pin numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Start a new dictionary with desired LED names
leds = {'floor':[], 'top-left':[]}

# Take name of led and list of pins for RGB
def setupled(name, pins):
	for i in range(0, 3):
		GPIO.setup(pins[i], GPIO.OUT)
		leds[name].append(GPIO.PWM(pins[i], 100))

setupled('1', [3, 5, 7])
setupled('2', [8, 10, 11])
setupled('3', [0, 0, 0])
setupled('4A', [3, 5, 7])
setupled('4B', [8, 10, 11])
setupled('5A', [0, 0, 0])
setupled('5B', [3, 5, 7])

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

def phase():
        colors = []
        bools = []
        for i in xrange(0, 21):
                colors.append(random.randrange(0, 256))
                bools.append(bool(random.getrandbits(1)))

        try:
                while True:
                        for i in xrange(0, 21):
                                if (colors[i] < 1 or colors[i] > 254):
                                	bools[i] = not bools[i]
                                if (bools[i]):
                                	colors[i] = colors[i] + 1
                                elif (not bools[i]):
                                	colors[i] = colors[i] - 1

                        setcolor('1', colors[0:3])
                        setcolor('2', colors[3:6])
						setcolor('3', colors[6:9])
						setcolor('4A', colors[9:12])
						setcolor('4B', colors[12:15])
						setcolor('5A', colors[15:18])
						setcolor('5B', colors[18:21])
                        sleep(0.005)
        except KeyboardInterrupt:
                pass

def cyclecolors():
        try:
                while True:
                    wait = 0.1

					setcolor('1', WHITE)
					setcolor('2', RED)
					setcolor('3', GREEN)
					setcolor('4A', BLUE)
					setcolor('4B', YELLOW)
					setcolor('5A', PURPLE)
					setcolor('5B', CYAN)
					sleep(wait)

					setcolor('1', CYAN)
					setcolor('2', WHITE)
					setcolor('3', RED)
					setcolor('4A', GREEN)
					setcolor('4B', BLUE)
					setcolor('5A', YELLOW)
					setcolor('5B', PURPLE)
					sleep(wait)

					setcolor('1', PURPLE)
					setcolor('2', CYAN)
					setcolor('3', WHITE)
					setcolor('4A', RED)
					setcolor('4B', GREEN)
					setcolor('5A', BLUE)
					setcolor('5B', YELLOW)
					sleep(wait)

					setcolor('1', YELLOW)
					setcolor('2', PURPLE)
					setcolor('3', CYAN)
					setcolor('4A', WHITE)
					setcolor('4B', RED)
					setcolor('5A', GREEN)
					setcolor('5B', BLUE)
					sleep(wait)

					setcolor('1', BLUE)
					setcolor('2', YELLOW)
					setcolor('3', PURPLE)
					setcolor('4A', CYAN)
					setcolor('4B', WHITE)
					setcolor('5A', RED)
					setcolor('5B', GREEN)
					sleep(wait)

					setcolor('1', GREEN)
					setcolor('2', BLUE)
					setcolor('3', YELLOW)
					setcolor('4A', PURPLE)
					setcolor('4B', CYAN)
					setcolor('5A', WHITE)
					setcolor('5B', RED)
					sleep(wait)

					setcolor('1', RED)
					setcolor('2', GREEN)
					setcolor('3', BLUE)
					setcolor('4A', YELLOW)
					setcolor('4B', PURPLE)
					setcolor('5A', CYAN)
					setcolor('5B', WHITE)
					sleep(wait)
        except KeyboardInterrupt:
                pass

def epilepsy():
	try:
		while True:
			if bool(random.getrandbits(1)):
				setcolor('1', WHITE)
			else
				setcolor('1', BLACK)

			if bool(random.getrandbits(1)):
				setcolor('2', WHITE)
			else
				setcolor('2', BLACK)

			if bool(random.getrandbits(1)):
				setcolor('3', WHITE)
			else
				setcolor('3', BLACK)

			if bool(random.getrandbits(1)):
				setcolor('4A', WHITE)
			else
				setcolor('4A', BLACK)

			if bool(random.getrandbits(1)):
				setcolor('4B', WHITE)
			else
				setcolor('4B', BLACK)

			if bool(random.getrandbits(1)):
				setcolor('5A', WHITE)
			else
				setcolor('5A', BLACK)

			if bool(random.getrandbits(1)):
				setcolor('5B', WHITE)
			else
				setcolor('5B', BLACK)

			sleep(0.01)
	except KeyboardInterrupt:
		pass

# Start program here
while True:
	phase()
	cyclecolors()
	epilepsy()

# Stop all PWMs
for key, value in leds.items():
	for i in value:
		i.stop()

GPIO.cleanup()
