# coding=utf-8
from __future__ import division
from soil_return import soilHumidity
from water_return import waterPump
from luminosity_return import luminosity
from temperature_return import humidityTemperature
from led_luminosity import riseLuminosity, turnOnLuminosity, turnOffLuminosity
from led_temperature import riseTemperature, turnOnTemperature, turnOffTemperature
import RPi.GPIO as GPIO
import time
import datetime
import csv

PIN_SENSOR_LUMINOSIDADE = 7
PIN_SENSOR_HUMIDADE_TERRA = 37
PIN_BOMBA_AGUA = 40
PIN_SENSOR_TEMPERATURA = 17 #gpio
PIN_LED_LUMINOSIDADE = 38
PIN_LED_TEMPERATURA = 36
DHT = 22
TEMPO_BOMBA_AGUA = 4 #segundos

PRETENDIDO_LUMINOSIDADE_PERCENTAGEM = None
PRETENDIDO_LUMINOSIDADE_HORA_INICIO = None
PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = None
PRETENDIDO_LUMINOSIDADE_HORA_FIM = None
PRETENDIDO_LUMINOSIDADE_MINUTO_FIM = None

PRETENDIDO_REGA_HORA_INICIO = None
PRETENDIDO_REGA_MINUTO_INICIO = None
PRETENDIDO_REGA_HORA_FIM = None
PRETENDIDO_REGA_MINUTO_FIM = None
PRETENDIDO_REGA_HUMIDADE = None
PRETENDIDO_REGA_SEGUNDOS = None

PRETENDIDO_TEMPERATURA_GRAUS = None


def updatePretendido():
    fp = open('/var/www/html/config.txt', "r")
    valores_pretendidos = fp.readline()
    valores = valores_pretendidos.split(",")

    global PRETENDIDO_LUMINOSIDADE_PERCENTAGEM
    global PRETENDIDO_LUMINOSIDADE_HORA_INICIO
    global PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO
    global PRETENDIDO_LUMINOSIDADE_HORA_FIM
    global PRETENDIDO_LUMINOSIDADE_MINUTO_FIM

    global PRETENDIDO_REGA_HORA_INICIO
    global PRETENDIDO_REGA_MINUTO_INICIO
    global PRETENDIDO_REGA_HORA_FIM
    global PRETENDIDO_REGA_MINUTO_FIM
    global PRETENDIDO_REGA_HUMIDADE
    global PRETENDIDO_REGA_SEGUNDOS

    global PRETENDIDO_TEMPERATURA_GRAUS



    # Formato
    # luminosidade
    # hora:minutos (inicio), hora:minutos (fim), intensidade
    # humidade
    # hora:minutos (inicio), hora:minutos (fim), humidade solo, segundos
    # temperatura
    # graus

    if(valores[0] != "" and valores[1] != ""):
        try:
            PRETENDIDO_LUMINOSIDADE_HORA_INICIO = valores[0].split(":")[0]
            PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = valores[0].split(":")[1]
            PRETENDIDO_LUMINOSIDADE_HORA_FIM = valores[1].split(":")[0]
            PRETENDIDO_LUMINOSIDADE_MINUTO_FIM = valores[1].split(":")[1]
        except Exception:
            PRETENDIDO_LUMINOSIDADE_HORA_INICIO = 20
            PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = 0
            PRETENDIDO_LUMINOSIDADE_HORA_FIM = 6
            PRETENDIDO_LUMINOSIDADE_MINUTO_FIM = 30

    if(valores[2] != ""):
        try:
            PRETENDIDO_LUMINOSIDADE_PERCENTAGEM = valores[2]
        except Exception:
            PRETENDIDO_LUMINOSIDADE_PERCENTAGEM = 50 # 50%

    if (valores[3] != "" and valores[4] != ""):
        try:
            PRETENDIDO_REGA_HORA_INICIO = valores[3].split(":")[0]
            PRETENDIDO_REGA_MINUTO_INICIO = valores[3].split(":")[1]
            PRETENDIDO_REGA_HORA_FIM = valores[4].split(":")[0]
            PRETENDIDO_REGA_MINUTO_FIM = valores[4].split(":")[1]
        except Exception:
            PRETENDIDO_REGA_HORA_INICIO = 19
            PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO = 0
            PRETENDIDO_REGA_HORA_FIM = 20
            PRETENDIDO_REGA_MINUTO_FIM = 0

    if(valores[5] != ""):
        try:
            PRETENDIDO_REGA_HUMIDADE = valores[5]
        except Exception:
            PRETENDIDO_REGA_HUMIDADE = 5 # 5%

    if(valores[6] != ""):
        try:
            PRETENDIDO_REGA_SEGUNDOS = valores[6]
        except Exception:
            PRETENDIDO_REGA_SEGUNDOS = 4

    if(valores[7] != ""):
        try:
            PRETENDIDO_TEMPERATURA_GRAUS = valores[7]
        except Exception:
            PRETENDIDO_TEMPERATURA_GRAUS = 25.5 # 25ºC

    fp.close()
    print(PRETENDIDO_TEMPERATURA_GRAUS)

def percentagem(valor_maximo, valor_atual):
    percent = (valor_atual * 100 / valor_maximo)
    percent2 = ('%.1f' % percent).rstrip('0').rstrip('.')
    return percent2

def percentagem_luminosidade(valor_maximo, valor_minimo, valor_atual):
    intervalo = valor_minimo - valor_maximo
    percent =  100 - ((valor_atual / intervalo) * 100)
    #return '{0:.1g}'.format(percent)
    percent2 = ('%.1f' % percent).rstrip('0').rstrip('.')
    return percent2


try:
    soilHumidity(PIN_SENSOR_HUMIDADE_TERRA) #Para descartar o primeiro erro de leitura
    #updatePretendido()
    #time.sleep(50)
    #waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
    #turnOnLuminosity(PIN_LED_LUMINOSIDADE)
    #time.sleep(2)
    #turnOffLuminosity(PIN_LED_LUMINOSIDADE)
    #turnOnTemperature(PIN_LED_TEMPERATURA)
    #time.sleep(2)
    #turnOffTemperature(PIN_LED_TEMPERATURA)
    while True:
        GPIO.setwarnings(False)
        updatePretendido()
        valores_atuais = open('/var/www/html/current_values.txt', "w")
        now = datetime.datetime.now()
        soil_humidity = soilHumidity(PIN_SENSOR_HUMIDADE_TERRA)
        luminosity = luminosity(PIN_SENSOR_LUMINOSIDADE)
        [temperature, air_humidity] = humidityTemperature(DHT, PIN_SENSOR_TEMPERATURA)
        hum_perc = percentagem(100000, soil_humidity)
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

        time.sleep(2)
        # Temperatura pretendida é superior à atual, ligar aquecimento
        print(PRETENDIDO_TEMPERATURA_GRAUS)
        if(PRETENDIDO_TEMPERATURA_GRAUS != None):
            print("TOP")
            if(float(PRETENDIDO_TEMPERATURA_GRAUS) > float(temperature)):
                turnOnTemperature(PIN_LED_TEMPERATURA)
            else:
                turnOffTemperature(PIN_LED_TEMPERATURA)
        else:
            print("NAO")
            turnOffTemperature(PIN_LED_TEMPERATURA)

        print("TEST")

        # Luminosidade dentro do horário
        if(PRETENDIDO_LUMINOSIDADE_HORA_INICIO != None and PRETENDIDO_LUMINOSIDADE_HORA_FIM != None and PRETENDIDO_LUMINOSIDADE_PERCENTAGEM != None and PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO != None and PRETENDIDO_LUMINOSIDADE_MINUTO_FIM != None):
            if(PRETENDIDO_LUMINOSIDADE_HORA_INICIO > PRETENDIDO_LUMINOSIDADE_HORA_FIM):
                if PRETENDIDO_LUMINOSIDADE_HORA_INICIO < now.hour+1 or now.hour+1 < PRETENDIDO_LUMINOSIDADE_HORA_FIM:
                    if PRETENDIDO_LUMINOSIDADE_PERCENTAGEM >= int(lum_perc):
                        turnOnLuminosity(PIN_LED_LUMINOSIDADE)
                    else:
                        turnOffLuminosity(PIN_LED_LUMINOSIDADE)
                elif(now.hour+1 == PRETENDIDO_LUMINOSIDADE_HORA_INICIO and now.minute >= PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO):
                    if PRETENDIDO_LUMINOSIDADE_PERCENTAGEM >= int(lum_perc):
                        turnOnLuminosity(PIN_LED_LUMINOSIDADE)
                    else:
                        turnOffLuminosity(PIN_LED_LUMINOSIDADE)
                else:
                    turnOffLuminosity(PIN_LED_LUMINOSIDADE)
            else:
                if PRETENDIDO_LUMINOSIDADE_HORA_INICIO < now.hour+1 < PRETENDIDO_LUMINOSIDADE_HORA_FIM:
                    if PRETENDIDO_LUMINOSIDADE_PERCENTAGEM >= int(lum_perc):
                        turnOnLuminosity(PIN_LED_LUMINOSIDADE)
                    else:
                        turnOffLuminosity(PIN_LED_LUMINOSIDADE)
                elif(now.hour + 1 == PRETENDIDO_LUMINOSIDADE_HORA_INICIO and now.minute >= PRETENDIDO_LUMINOSIDADE_MINUTO_INICIO):
                    if PRETENDIDO_LUMINOSIDADE_PERCENTAGEM >= int(lum_perc):
                        turnOnLuminosity(PIN_LED_LUMINOSIDADE)
                    else:
                        turnOffLuminosity(PIN_LED_LUMINOSIDADE)
                else:
                    turnOffLuminosity(PIN_LED_LUMINOSIDADE)
        else:
            turnOffLuminosity(PIN_LED_LUMINOSIDADE)

        #---
        #	time.sleep(5)
        #	waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)

        #csv.write(str(humidity) + "," + str(localtime))
        #if(humidity < 1000):
        #    waterPump(PIN_BOMBA_AGUA, TEMPO_BOMBA_AGUA)
        #    csv.write(", Ativar Rega!")
        #csv.write("\n")
        #csv.close()
        #time.sleep(898) #15min de espera
	break
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Program exiting...")
finally:
    #GPIO.cleanup()  # run on exit
    exit(1)