from soil_return import soilHumidity
from water_return import waterPump
import RPi.GPIO as GPIO
import time
import csv

PIN_HUMIDADE_TERRA = 37
PIN_BOMBA_AGUA = 40
TEMPO_BOMBA_AGUA = 2 #segundos

try:
    soilHumidity(PIN_HUMIDADE_TERRA) #Para descartar o primeiro erro de leitura
    while True:
        time.sleep(1)
        csv = open('humidade.csv', 'a+')
        localtime = time.asctime(time.localtime(time.time()))
        humidity = soilHumidity(PIN_HUMIDADE_TERRA)
        print("Humidade: " + str(humidity))
        csv.write(str(humidity) + "," + str(localtime))
        if(humidity < 1000):
            waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
            csv.write(", Ativar Rega!")
        csv.write("\n")
        csv.close()
        time.sleep(898) #15min de espera
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Program exiting...")
finally:
    GPIO.cleanup()  # run on exit
