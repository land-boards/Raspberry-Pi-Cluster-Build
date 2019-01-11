#!/usr/bin/env python

'''pyPi-Atx.py

Code to EXERCISE the LEDs on the PI-ATX card for a Raspberry Pi Model B.

This code must be run as Superuser on the Raspberry Pi.

============
Dependencies
============

Need to: 

* sudo apt-get install python-dev
* sudo apt-get install python-pip python2.7-dev
* sudo apt-get install python-rpi.gpio
* sudo pip install flask

====
Code
====
'''

import RPi.GPIO as GPIO
import os
import time

HDD_LED = 27
PWR_LED_POS = 17
PWR_LED_NEG = 24
BOARD_LED = 25

RESET_LO = 18
PWR_SW = 23

def blinkLED(channel):
	'''Function to blink an LED attached to an output channel
	Drives line high for a short time and then drives it low.
	The high level output turns on the LED.
	'''
	GPIO.output(channel, 1)
	time.sleep(0.25)
	GPIO.output(channel, 0)
	
GPIO.setmode(GPIO.BCM)	# setup GPIO using Board numbering

# Set all of the pins to outputs
GPIO.setup(HDD_LED, GPIO.OUT)
GPIO.setup(PWR_LED_POS, GPIO.OUT)
GPIO.setup(PWR_LED_NEG, GPIO.OUT)
GPIO.setup(BOARD_LED, GPIO.OUT)

GPIO.output(HDD_LED, 0)
GPIO.output(PWR_LED_POS, 0)
GPIO.output(PWR_LED_NEG, 0)
GPIO.output(BOARD_LED, 0)

GPIO.setup(RESET_LO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PWR_SW, GPIO.IN)

# Blink all of the LEDs one at a time forever
# CTRL-C to exit which is not a particularly elegant exit strategy, but this is a demo program

lastReset = GPIO.input(RESET_LO)
print 'initial reset', lastReset

lastPowerSw = GPIO.input(PWR_SW)
print 'initial power switch', lastPowerSw

while 1:
	blinkLED(HDD_LED)
	blinkLED(PWR_LED_POS)
	blinkLED(PWR_LED_NEG)
	blinkLED(BOARD_LED)
	time.sleep(0.25)
	initReset = GPIO.input(RESET_LO)
	initPowerSw = GPIO.input(PWR_SW)
	if initReset != lastReset:
		lastReset = initReset
		print 'reset changed',initReset
	if initPowerSw != lastPowerSw:
		lastPowerSw = initPowerSw
		print 'power switch changed',initPowerSw
		