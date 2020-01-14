# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Añade un dígito a un número por delante.\n")

# Comprobación de 12. pega_por_delante
numero = int(input("Introduce el número que usarás de base: "))
pegar = int(input("Introduce lo que quieres añadir por delante: "))
print(pega_por_delante(numero, pegar))
