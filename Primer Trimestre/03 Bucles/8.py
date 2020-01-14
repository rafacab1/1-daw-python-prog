# 8. Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.
# Para hacer una espera en Python podemos usar el método sleep del módulo time.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 25/10/19
#
# Algoritmo
# Defino unas variables a 0, para las horas, los minutos y los segundos.
# Mientras que sea verdadero...
#   Le sumo un segundo a los segundos
#   Si los segundos son 60...
#       Pongo los segundos a 0
#       Sumo uno a los minutos
#   Si los minutos son 60
#       Pongo los minutos a 0
#       Sumo uno a las horas
#   Imprimo el resultado por pantalla
#   Espero un segundo
# 
# Variables
# seg = Segundos (int)
# mins = Minutos (int)
# hrs = Horas (int)
#

from time import sleep

print("Programa que hace de cronómetro.")

# Defino las variables

seg = 0
mins = 0
hrs = 0

while True:
    seg += 1 #Sumo un segundo
    if seg == 60: # Si llevo 60 segundos, pongo los segundos a 0 y sumo un minuto
        seg = 0
        mins += 1
    if mins == 60: # Si llevo 60 minutos, pongo los minutos 0 y sumo una hora
        mins = 0
        hrs += 1
    print(f"{hrs}:{mins}:{seg}") # Muestro lo que llevo
    sleep(1) # Espero un segundo