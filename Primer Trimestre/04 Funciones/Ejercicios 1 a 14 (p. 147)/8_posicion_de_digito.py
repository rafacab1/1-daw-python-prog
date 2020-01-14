# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Da la posición de la primera ocurrencia de un dígito dentro de un número entero. "
      "Si no se encuentra, devuelve -1.\n")

# Comprobación de 8. posicion_de_digito
digito = int(input("Introduce un número: "))
numero_b = int(input("Introduce el número a buscar: "))
print(f"El número {numero_b} está en la posición {posicion_de_digito(digito, numero_b)}, recuerda que el 0 cuenta como "
      f"posición.")
