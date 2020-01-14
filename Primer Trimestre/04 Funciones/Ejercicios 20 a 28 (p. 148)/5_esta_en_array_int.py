# -*- coding: utf-8 -*-
from funciones.funciones2028 import *

# Comprobación de 5_esta_en_array_int

print("Dice si un número está o no dentro de un array.")

print("\nPrimero vamos a crear un array con enteros aleatorios...")
n = int(input("Introduce la longitud del array: "))
minimo = int(input("Introduce el número mínimo a generar: "))
maximo = int(input("Introduce el número máximo a generar: "))

numero = int(input("\nAhora introduce el número que quieres comprobar si está en el array: "))

print("\nContenido del array: ")
array = genera_array_int(n, minimo, maximo)
print(array)

if esta_en_array_int(array, numero):
    print(f"Sí, el {numero} está en el array.")
else:
    print(f"No, el {numero} no está en el array.")
