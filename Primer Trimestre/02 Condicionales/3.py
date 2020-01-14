# 2. Escribe un programa que lea un número e indique si es par o impar.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 17/10/19
#
# Algoritmo
# Pido un número
# Cálculo el resto del número, si es 0 es par, si no, es impar
#
# Variables
# n: Número (float)
#

print("Programa que dice si un número es par o impar.\n")

# Pido el número
n = float(input("Introduce el número: "))

# Hago la sentencia de si es par o impar y muestro el resultado por pantalla

if n % 2 == 0:
    print(f"{n} es un número par.")

else:
    print(f"{n} es un número impar.")