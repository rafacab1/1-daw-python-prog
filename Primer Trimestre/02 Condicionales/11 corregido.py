# 11. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
#
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# (mirar análisis en GitHub)
# 
#
# Variables
# ladoa = valor de a (float)
# ladob = valor de b (float)
# ladoc = valor de c (float)
#

import math

# Pido A, B y C
ladoa = float(input("Introduce el valor de A: "))
ladob = float(input("Introduce el valor de B: "))
ladoc = float(input("Introduce el valor de C: "))

# Primero comprobamos si es equilátero, este caso es excluyente.
if ladoa == ladob and ladob == ladoc: # Python permitiría ladoa == ladob == ladoc
    print("El triángulo es equilátero.")
else:
    # Comprobamos si es rectángulo
    if ladoa ** 2 == (ladob ** 2 + ladoc ** 2) or ladob ** 2 == (ladoa ** 2 + ladoc ** 2) or ladoc ** 2 == (ladob ** 2 + ladoa ** 2):
        print("El triángulo es rectángulo.")
    # Comprobamos si es isósceles o escaleno
    if ladoa == ladob or ladoa == ladoc or ladob == ladoc:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")