#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telethon import TelegramClient, events, sync
from argparse import ArgumentParser
import json
import requests
import sys
import configparser
import time

"""
Telethon es una librería que aporta una especie de cliente de Telegram para Python mediante MTProto
"""
# Descripción del programa
parser = ArgumentParser(description='%(prog)s es un programa que comprueba la temperatura y si es muy baja avisa por Telegram.')

# Argumentos
parser.add_argument('city', help='Ciudad', type=str)
parser.add_argument('temperatura', help='Temperatura a partir de la cual avisar.', type=float)
args = parser.parse_args()

# Obtención de APIs KEYs
# Obtendré los datos del fichero config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')
# Clave de OpenWeatherMap
def api_owm():
    return config['openweathermap']['key']
# Claves de la API de mi cuenta de Telegram (se pueden obtener desde my.telegram.org)
def api_id_t():
    return config['telegram']['apiid']
def api_hash_t():
    return config['telegram']['apihash']

# Obtener temperatura
def temperatura(apikey, ciudad):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(args.city, apikey)
    # Petición que obtiene el JSON
    response = requests.get(url)
    if response.json()['cod'] == "404":
        print(args.city + " no es una ciudad válida.")
        sys.exit(1) # Sale con código de error 1
    return response.json()

# Creo una instancia de la clase TelegramClient, proporcionada por la libreria telethon.
client = TelegramClient('alerta_frio', api_id_t(), api_hash_t())

# Hago que el cliente empiece a funcionar
client.start()

while True:
    weather = temperatura(api_owm(),args.city)
    # Compruebo si la temperatura en la ciudad es mayor o menos que la temperatura
    # pasada como parámetro y mando un mensaje al canal @alertafrio en Telegram.
    if weather['main']['temp'] < args.temperatura:
        msg = "¡Cuidado!, La temperatura en " + args.city + " es de " + str((weather)['main']['temp']) + "º y eso es menos que " + str(args.temperatura) + "º. Hoy no puedes salir en camiseta sin tirantes. ¡Abrígate! 🧣️"
    else:
        msg = "Hace un buen día para un paseito por " + args.city + " en camiseta sin tirantes... 😎️ La temperatura hoy es de " + str((weather)['main']['temp']) + "º."  
    client.send_message('alertafrio', msg)
    time.sleep(1800)