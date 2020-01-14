# 13. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
# Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, 
# ¿cómo se puede calcular?
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido el número
# Calculo la raíz cuadrada y la cúbica
# Muestro el resultado por pantalla
#
# Variables: 
# n = Número
# cuadrada = Raíz cuadrada
# cubica = Raíz cúbica
#

import math

# Pido el número
n = float(input("Introduce un número: "))

# Calculo la raíz cuadrada y la raíz cúbica
cuadrada = math.sqrt(n)
cubica = n ** (1/3)

# Muestro los resultados por pantalla
print("La raíz cuadrada es", cuadrada)
print("La raíz cúbica es", cubica)