# coding=utf-8
from __future__ import division
from soil_return import soilHumidity
from water_return import waterPump
from luminosity_return import luminosity
from temperature_return import humidityTemperature
import RPi.GPIO as GPIO
import time
import datetime
import csv

PIN_SENSOR_LUMINOSIDADE = 7
PIN_SENSOR_HUMIDADE_TERRA = 37
PIN_BOMBA_AGUA = 40
PIN_SENSOR_TEMPERATURA = 17 #gpio
DHT = 22
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
    time.sleep(5)
    #waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
    while True:
        #csv = open('humidade.csv', 'a+')
        valores_atuais = open('/var/www/html/current_values.txt', "w")
        now = datetime.datetime.now()
        soil_humidity = soilHumidity(PIN_SENSOR_HUMIDADE_TERRA)
        luminosity = luminosity(PIN_SENSOR_LUMINOSIDADE)
        [temperature, air_humidity] = humidityTemperature(DHT, PIN_SENSOR_TEMPERATURA)
        #temp2 = humidityTemperature(DHT, PIN_SENSOR_TEMPERATURA)
        #time.sleep(2)
        #temp3 = humidityTemperature(DHT, PIN_SENSOR_TEMPERATURA)
        #temp = (temp1 + temp2 + temp3) / 3
        hum_perc = percentagem(300000, soil_humidity)
        lum_perc = percentagem_luminosidade(500, 50000, luminosity)
        print("HUM SOLO: " + str(soil_humidity) + " Percent: " + str(hum_perc))
        print("LUM: " + str(luminosity) + " Percent: " + str(lum_perc))
        print("HUM AR: " + str('{0:0.1f}%'.format(air_humidity)))
        print("TEMP: " + str('{0:0.1f}ºC'.format(temperature)))
        #'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
#       print("TEMP: " + str(temp))

        #escrita dos dados
        valores_atuais.write(str(hum_perc)+","+str(lum_perc)+","+str('{0:0.1f}'.format(temperature))+","+str('{0:0.1f}'.format(air_humidity))+",")

        dia_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]


        tempo = "%s %d:%d:%d %d/%d/%d" % (dia_semana[now.weekday()], now.hour+1, now.minute, now.second, now.day, now.month, now.year) #+1 porque hora está atrasada
        valores_atuais.write(str(tempo))
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
