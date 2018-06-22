#!/usr/bin/python
import Adafruit_DHT

def humidityTemperature(sensor, pin):
    global humidity, temperature
    try:
       humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    except KeyboardInterrupt:
        return 0
    finally:
       if humidity is not None and temperature is not None:
          return [temperature, humidity]
       else:
          return [None, None]


