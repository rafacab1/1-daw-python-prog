# -*- coding: utf-8 -*-
from funciones.funciones import *

print("Cuenta el número de dígitos de un número entero.\n")

# Comprobación de 5. digitos
contar = int(input("Introduce un número entero y te diré cuántos dígitos tiene: "))
print(f"{contar} tiene {digitos(contar)} dígitos.")
