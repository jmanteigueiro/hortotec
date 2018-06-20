# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.IN)
#
# while(True):
#     print GPIO.input(4)


# ! usr/bin/python

# import time
#
# from gpiozero import LightSensor
#
# ldr = LightSensor(4)
#
# while True:
#     print(ldr.value)
#     time.sleep(0.3)

# import RPi.GPIO as GPIO
#
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4,GPIO.IN)
#
# while(1):
#     print (float(GPIO.input(4)))


# !/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def soilHumidity(pin_to_circuit):
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

        # Count until the pin goes high
        while (GPIO.input(pin_to_circuit) == GPIO.LOW):
            count += 1
            if(count > 500000):
                break

    except KeyboardInterrupt:
        return 0
    finally:
        return count

