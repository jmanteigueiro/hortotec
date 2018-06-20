#! /usr/bin/python
# Import the libraries we need
import RPi.GPIO as GPIO
import time

def waterPump(PIN, TEMPO):
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    time.sleep(TEMPO)
    GPIO.output(PIN, False)
