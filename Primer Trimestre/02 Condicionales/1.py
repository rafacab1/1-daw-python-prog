# 1. Algoritmo que pida dos números e indique si el primero es mayor que el segundo o no.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 17/10/19
#
# Algoritmo
# Pido los dos números
# Hago la sentencia, si el número x es mayor que y, x es mayor, si no, y es mayor
# Muestro por pantala cual es el mayor
#
# Variables
# x: Número 1 (float)
# y: Número 2 (float)

print("Programa que dice cual es el mayor de dos números.\n")

# Pido los números

x = float(input("Introduce el primer número: "))
y = float(input("Introduce el segundo número: "))

# Hago la sentencia y muestro por pantalla el resultado

if x > y:
    print(f"{x} es mayor que {y}")

else:
    print(f"{y} es mayor que {x}")