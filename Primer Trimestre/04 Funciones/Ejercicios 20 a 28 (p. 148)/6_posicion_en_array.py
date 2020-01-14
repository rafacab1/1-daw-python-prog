# -*- coding: utf-8 -*-
from funciones.funciones2028 import *

# Comprobación de 6_posicion_en_array

print("Busca un número en un array y devuelve la posición (el índice) en la que se encuentra.")

print("\nPrimero vamos a crear un array con enteros aleatorios...")
n = int(input("Introduce la longitud del array: "))
minimo = int(input("Introduce el número mínimo a generar: "))
maximo = int(input("Introduce el número máximo a generar: "))

numero = int(input("\nAhora introduce del cual quieres saber su posición: "))

print("\nContenido del array: ")
array = genera_array_int(n, minimo, maximo)
print(array)

if posicion_en_array(array, numero) == -1:
    print("Ese número no está en este array.");
else:
    print(f"El número {numero} está en la posicion {posicion_en_array(array, numero)}")
