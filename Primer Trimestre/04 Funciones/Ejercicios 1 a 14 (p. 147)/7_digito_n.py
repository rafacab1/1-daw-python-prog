# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda "
      "a derecha.\n")

# Comprobación de 7. digito_n
digito = int(input("Introduce el número que quieres usar: "))
posi = int(input("¿Qué posición del número quieres que saque? "))
print(digito_n(digito, posi))