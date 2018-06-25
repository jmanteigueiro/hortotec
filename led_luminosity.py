#! /usr/bin/python

# Import the libraries we need
import RPi.GPIO as GPIO
import time
# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

def riseLuminosity(pin_to_circuit, duration):
    #LED = 38
    LED = pin_to_circuit
    # Set the LED GPIO pin as an output
    GPIO.setup(LED, GPIO.OUT)
    # Turn the GPIO pin on
    GPIO.output(LED, True)
    # Wait n seconds
    time.sleep(duration)
    # Turn the GPIO pin off
    GPIO.output(LED, False)

def turnOnLuminosity(pin_to_circuit):
    LED = pin_to_circuit
    # Set the LED GPIO pin as an output
    GPIO.setup(LED, GPIO.OUT)
    # Turn the GPIO pin on
    GPIO.output(LED, True)

def turnOffLuminosity(pin_to_circuit):
    LED = pin_to_circuit
    # Set the LED GPIO pin as an output
    GPIO.setup(LED, GPIO.OUT)
    # Turn the GPIO pin off
    GPIO.output(LED, False)