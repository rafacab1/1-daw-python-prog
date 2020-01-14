# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Devuelve el menor primo que es mayor al número que se pasa como parámetro.\n")

# Comprobación de 3. siguiente_primo
sprimo = int(input("Introduce un número y te diré cual es el siguiente primo: "))
print(f"El siguiente primo es {siguiente_primo(sprimo)}")
