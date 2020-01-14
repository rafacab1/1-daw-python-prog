# 17. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 11/10/19
#
# Algoritmo
# Pido hora, minuto y segundo de la salida, y los segundos que tarda en llegar a B.
# Paso las horas, los minutos y los segundos a segundos
# Sumo esos segundos a los que tarda en llegar a B.
# Paso el total de segundos a horas, minutos y segundos
# Muestro el resultado por pantalla
#
# Variables: 
# hhs = Hora de salida
# mms = Minuto de salida
# sss = Segundo de salida
# tseg = Segundos que tarda en llegar
# hms = La hora, minuto y segundo de salida en segundos
# st = Total de segundos (salida + tiempo para llegar)
# hf = Hora a la que llega
# mf = Minuto al que llega
# sf = Segundo al que llega

# Pido los datos
hhs = int(input("Introduce hora de salida: "))
mms = int(input("Introduce minutos de salida: "))
sss = int(input("Introduce segundos de salida: "))

tseg = int(input("¿Cuantos segundos has tardado en llegar a B?: "))

# Paso todo a segundos
hms = (hhs * 3600) + (mms * 60) + sss

# Sumo todos los segundos
st = hms + tseg

# Paso todos los segundos a horas, minutos y segundos
hf=(int(st / 3600))
mf=int((st - (hf * 3600)) / 60)
sf=st-((hf * 3600) + (mf * 60))

# Muestro el resultado por pantalla
print("Llegas a B a las", hf, "horas,", mf, "minutos y", sf, "segundos.")