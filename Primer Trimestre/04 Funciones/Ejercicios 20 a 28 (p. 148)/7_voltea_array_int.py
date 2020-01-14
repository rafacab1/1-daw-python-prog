# -*- coding: utf-8 -*-
from funciones.funciones2028 import *

# Comprobación de 7_voltea_array_int

print("Le da la vuelta a un array.")

print("\nPrimero vamos a crear un array con enteros aleatorios...")
n = int(input("Introduce la longitud del array: "))
minimo = int(input("Introduce el número mínimo a generar: "))
maximo = int(input("Introduce el número máximo a generar: "))

print("\nContenido del array sin voltear: ")
array = genera_array_int(n, minimo, maximo)
print(array)

print("\nContenido del array volteado: ")
array_volt = voltea_array_int(array)
print(array_volt)
