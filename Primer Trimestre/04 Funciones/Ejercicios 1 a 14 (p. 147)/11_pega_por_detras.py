# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Añade un dígito a un número por detrás.\n")

# Comprobación de 11. pega_por_detras
numero = int(input("Introduce el número que usarás de base: "))
pegar = int(input("Introduce lo que quieres añadir por detrás: "))
print(pega_por_detras(numero, pegar))
