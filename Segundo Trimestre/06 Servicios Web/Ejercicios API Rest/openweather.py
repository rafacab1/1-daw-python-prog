# -*- coding: utf-8 -*-

import requests
import json
import os
import datetime
import time

# Saco el día de hoy
hoy = datetime.datetime.now(datetime.timezone.utc)
print (hoy)

# Tiempo UNIX
unix = int(time.time())

# Clave OpenWeatherMap
owm = ""
# URL desde la que obtendré los datos
url = "https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid={}".format("Cordoba,ES", owm)
# Obtengo el JSON
response = requests.get(url)
# Lo guardo en una variable (weather)
weather = response.json()

"""
No sé como puedo pasar del tiempo de hoy en el formato normal al formato UNIX.
Mi idea era hacer la media de todas las temperaturas que se devuelven para mañana y para los siguientes días, cogiendo el día de hoy 
en formato natural y sumándole un día y ponerlo a las 00 para sacar todos los datos. Preguntar en clase.

"""

