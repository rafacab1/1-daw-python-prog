# -*- coding: utf-8 -*-
from funciones.funciones2028 import *

# Comprobación de 1_genera_array_int

print("1. Genera un array de tamaño n con números aleatorios cuyo intervalo (mínimo y máximo) se indica como "
      "parámetro.")

n = int(input("Introduce la longitud del array: "))
minimo = int(input("Introduce el número mínimo a generar: "))
maximo = int(input("Introduce el número máximo a generar: "))

print(genera_array_int(n, minimo, maximo))
