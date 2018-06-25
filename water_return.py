#! /usr/bin/python
# Import the libraries we need
import RPi.GPIO as GPIO
import time

def waterPump(PIN, TEMPO=3):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    time.sleep(TEMPO)
    GPIO.output(PIN, False)
