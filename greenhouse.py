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

PRETENDIDO_LUMINOSIDADE_PERCENTAGEM = 0
PRETENDIDO_LUMINOSIDADE_HORA_INICIO = 0
PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = 0
PRETENDIDO_LUMINOSIDADE_HORA_FIM = 0
PRETENDIDO_LUMINOSIDADE_MINUTO_FIM = 0

def updatePretendido():
    fp = open('/var/www/html/config.txt', "r")
    valores_pretendidos = fp.readline()
    valores = valores_pretendidos.split(",")
    # Formato
    # luminosidade
    # hora:minutos (inicio), hora:minutos (fim), intensidade
    #
    #
    if(valores[0] != "" and valores[1] != ""):
        try:
            PRETENDIDO_LUMINOSIDADE_HORA_INICIO = valores[0].split(":")[0]
            PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = valores[0].split(":")[1]
            PRETENDIDO_LUMINOSIDADE_HORA_FIM = valores[1].split(":")[0]
            PRETENDIDO_LUMINOSIDADE_MINUTO_FIM = valores[1].split(":")[1]
        except Exception:
            PRETENDIDO_LUMINOSIDADE_HORA_INICIO = 0
            PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = 0
            PRETENDIDO_LUMINOSIDADE_HORA_FIM = 0
            PRETENDIDO_LUMINOSIDADE_MINUTO_FIM = 0
    if(valores[2] != ""):
        PRETENDIDO_LUMINOSIDADE_PERCENTAGEM = valores[2]
            


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
    #updatePretendido()
    #time.sleep(50)
    #waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
    while True:
        valores_atuais = open('/var/www/html/current_values.txt', "w")
        now = datetime.datetime.now()
        soil_humidity = soilHumidity(PIN_SENSOR_HUMIDADE_TERRA)
        luminosity = luminosity(PIN_SENSOR_LUMINOSIDADE)
        [temperature, air_humidity] = humidityTemperature(DHT, PIN_SENSOR_TEMPERATURA)
        hum_perc = percentagem(300000, soil_humidity)
        lum_perc = percentagem_luminosidade(500, 50000, luminosity)
        print("HUM SOLO: " + str(soil_humidity) + " Percent: " + str(hum_perc))
        print("LUM: " + str(luminosity) + " Percent: " + str(lum_perc))
        print("HUM AR: " + str('{0:0.1f}%'.format(air_humidity)))
        print("TEMP: " + str('{0:0.1f}ºC'.format(temperature)))

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
