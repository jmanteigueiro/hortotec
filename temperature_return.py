# !/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def temperature(pin_to_circuit):
    global count
    try:
        #time.sleep(0.1)
        count = 0

        # Output on the pin for
        GPIO.setup(pin_to_circuit, GPIO.OUT)
        GPIO.output(pin_to_circuit, GPIO.LOW)
        time.sleep(0.1)

        # Change the pin back to input
        GPIO.setup(pin_to_circuit, GPIO.IN)

        # Count until the pin goes highz<
        while (GPIO.input(pin_to_circuit) == GPIO.LOW):
            count += 1
            if(count > 50000): # min
                break

    except KeyboardInterrupt:
        return 0
    finally:
        #if(count < 500): # max
        #    count = 500
        return count

