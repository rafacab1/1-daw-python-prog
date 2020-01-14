# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Le quita a un número n dígitos por delante (por la izquierda).\n")

# Comprobación de 10. quita_por_delante
numero = int(input("Introduce el número: "))
a_quitar = int(input("Introduce la cantidad de dígitos a quitar: "))
print(quita_por_delante(numero, a_quitar))
