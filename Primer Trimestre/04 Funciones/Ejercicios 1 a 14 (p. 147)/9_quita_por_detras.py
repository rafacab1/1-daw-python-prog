# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Le quita a un número n dígitos por detrás (por la derecha).\n")

# Comprobación de 9. quita_por_detras
numero = int(input("Introduce el número: "))
a_quitar = int(input("Introduce la cantidad de dígitos a quitar: "))
print(quita_por_detras(numero, a_quitar))
