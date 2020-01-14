# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Dada una base y un exponente devuelve la potencia.\n")

# Comprobación de 4. potencia
base = int(input("Introduce la base: "))
exp = int(input("Introduce el exponente: "))
print(f"El resultado de {base} elevado a {exp} es {potencia(base, exp)}")
