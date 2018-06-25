#! /usr/bin/python

# Import the libraries we need
import RPi.GPIO as GPIO
import time
# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

def riseTemperature(pin_to_circuit, duration):
    #LED = 36
    LED = pin_to_circuit
    # Set the LED GPIO pin as an output
    GPIO.setup(LED, GPIO.OUT)
    # Turn the GPIO pin on
    GPIO.output(LED, True)
    # Wait n seconds
    time.sleep(duration)
    # Turn the GPIO pin off
    GPIO.output(LED, False)



def turnOnTemperature(pin_to_circuit):
    LED = pin_to_circuit
    # Set the LED GPIO pin as an output
    GPIO.setup(LED, GPIO.OUT)
    # Turn the GPIO pin on
    GPIO.output(LED, True)

def turnOffTemperature(pin_to_circuit):
    LED = pin_to_circuit
    # Set the LED GPIO pin as an output
    GPIO.setup(LED, GPIO.OUT)
    # Turn the GPIO pin off
    GPIO.output(LED, False)