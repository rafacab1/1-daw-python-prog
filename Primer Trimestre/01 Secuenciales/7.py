# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido los minutos
# Hago los cálculos, división entera de los minutos entre 60 y el resto de los minutos entre 60
# Muestro el resultado por pantalla
#
# Variables: 
# mins = Minutos indicados por el usuario
# hrs = Horas totales
# minsr = Minutos totales

# Pido los minutos
mins = int(input("Introduce los minutos: "))

# Hago los cálculos
hrs = mins // 60
minsr = mins % 60

# Muestro el resultado por pantalla
print(mins, "minutos equivale a", hrs, "horas y", minsr, "minutos.")