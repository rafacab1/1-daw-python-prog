# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.\n")
# Comprobación de 13. trozo_de_numero
numero = int(input("Introduce un número: "))
pos_i = int(input("Introduce la posición inicial: "))
pos_f = int(input("Introduce la posición final: "))
print(trozo_de_numero(numero, pos_i, pos_f))
