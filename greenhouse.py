from __future__ import division
from soil_return import soilHumidity
from water_return import waterPump
from luminosity_return import luminosity
import RPi.GPIO as GPIO
import time
import csv

PIN_SENSOR_LUMINOSIDADE = 7
PIN_SENSOR_HUMIDADE_TERRA = 37
PIN_BOMBA_AGUA = 40
TEMPO_BOMBA_AGUA = 2 #segundos

def percentagem(valor_maximo, valor_atual):
    percent = (valor_atual * 100 / valor_maximo)
    percent2 = ('%.1f' % percent).rstrip('0').rstrip('.')
    return percent2

def percentagem_luminosidade(valor_maximo, valor_minimo, valor_atual):
    intervalo = valor_minimo - valor_maximo
    percent =  100- ((valor_atual / intervalo) * 100)
    #return '{0:.1g}'.format(percent)
    percent2 = ('%.1f' % percent).rstrip('0').rstrip('.')
    return percent2


try:
    soilHumidity(PIN_SENSOR_HUMIDADE_TERRA) #Para descartar o primeiro erro de leitura
    time.sleep(1)
    #waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
    while True:
        time.sleep(1)
        #csv = open('humidade.csv', 'a+')
        valores_atuais = open('/var/www/html/current_values.txt', "w")
        localtime = time.asctime(time.localtime(time.time()))
        humidity = soilHumidity(PIN_SENSOR_HUMIDADE_TERRA)
        time.sleep(1)
        lumino = luminosity(PIN_SENSOR_LUMINOSIDADE)
        time.sleep(1)
        hum_perc = percentagem(300000, humidity)
        lum_perc = percentagem_luminosidade(500, 50000, lumino)
        print("HUM: " + str(humidity) + " Percent: " + str(hum_perc))
        print("LUM: " + str(lumino) + " Percent: " + str(lum_perc))
        #print("Humidade: " + str(humidity))

        #escrita dos dados
        valores_atuais.write(str(hum_perc)+","+str(lum_perc)+","+str("25")+",")

        valores_atuais.write(str(localtime))
	valores_atuais.close()
        #csv.write(str(humidity) + "," + str(localtime))
        #if(humidity < 1000):
        #    waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
        #    csv.write(", Ativar Rega!")
        #csv.write("\n")
        #csv.close()
        time.sleep(898) #15min de espera
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Program exiting...")
finally:
    GPIO.cleanup()  # run on exit
