# -*- coding: utf-8 -*-
from funciones.funciones2028 import *

# Comprobación de 4_media_array_int

print("Devuelve la media del array que se pasa como parámetro.")

print("\nPrimero vamos a crear un array con enteros aleatorios...")
n = int(input("Introduce la longitud del array: "))
minimo = int(input("Introduce el número mínimo a generar: "))
maximo = int(input("Introduce el número máximo a generar: "))

print("\nContenido del array: ")
array = genera_array_int(n, minimo, maximo)
print(array)

print(f"La media es {media_array_int(array)}")
