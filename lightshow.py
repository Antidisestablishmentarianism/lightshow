#!/usr/bin/sudo / usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

leds = {'floor':[], 'top-left':[]}

def setupled(name, pins):
	for i in range(0, 3):
		GPIO.setup(pins[i], GPIO.OUT)
		leds[name].append(GPIO.PWM(pins[i], 100))

setupled('floor', [11, 13, 15])
setupled('top-left', [12, 16, 18])

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
while True:
	setcolor('floor', RED)
	sleep(1)
	setcolor('top-left', GREEN)
	sleep(1)
	setcolor('floor', BLUE)
	sleep(1)
	setcolor('top-left', YELLOW)
	sleep(1)
	setcolor('floor', PURPLE)
	sleep(1)
	setcolor('top-left', CYAN)
	sleep(1)
	setcolor('floor', WHITE)
	sleep(1)
	setcolor('top-left', BLACK)
	sleep(1)
	
	for i in xrange(0, 256):
		setcolor('floor', [i, i, i])
		sleep(0.01)
	
	for x in xrange(0, 256):
		y = 255 - x
		setcolor('top-left', [y, y, y])
		sleep(0.01)

for key, value in rooms.items():
	for i in value:
		i.stop()

GPIO.cleanup()
