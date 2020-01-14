# -*- coding: utf-8 -*-
from funciones.funciones2028 import *

# Comprobación de 9_rota_izquierda_array_int

print("Rota n posiciones a la izquierda los números de un array.")

print("\nPrimero vamos a crear un array con enteros aleatorios...")
n = int(input("Introduce la longitud del array: "))
minimo = int(input("Introduce el número mínimo a generar: "))
maximo = int(input("Introduce el número máximo a generar: "))

posiciones = int(input("\nIntroduce cuantas posiciones quieres rotar a la izquierda: "))

print("\nContenido del array")
array = genera_array_int(n, minimo, maximo)
print(array)

print("\nContenido del array rotado")
arrayrotiz = rota_izquierda_array_int(array, posiciones)
print(arrayrotiz)
