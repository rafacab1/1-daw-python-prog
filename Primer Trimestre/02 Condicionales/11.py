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
# Pido A, B y C
# Hago el Teorema de Pitágoras y evaluo si el resultado es igual a algún lado
#   Si es igual, muestro por pantalla que es un triángulo rectángulo.
#   Si no es igual, compruebo si los tres lados son iguales.
#       Si los tres lados son iguales, muestro por pantalla que es un triángulo equilátero.
#       Si no, compruebo si al menos dos de los lados son iguales.
#           Si lo son, muestro por pantalla que es un triángulo isósceles.
#           Si no lo son, muestro por pantalla que es un triángulo escaleno.
# 
#
# Variables
# a = valor de a (float)
# b = valor de b (float)
# c = valor de c (float)
#

import math

# Pido A, B y C
a = float(input("Introduce el valor de A: "))
b = float(input("Introduce el valor de B: "))
c = float(input("Introduce el valor de C: "))

hipotenusa = max(a, b, c)

# Hago el Teorema de Pitágoras y evaluo si el resultado es igual a la dimensión mas grande.
if hipotenusa == (math.sqrt((b ** 2) + (c ** 2))) or hipotenusa == (math.sqrt((a ** 2) + (c ** 2))) or hipotenusa == (math.sqrt((a ** 2 + b ** 2))):
    print("Este triángulo es un triángulo rectángulo.")
elif a == b == c:
    print("Este triángulo es un triángulo equilátero.")
elif a == b or a == c or b == c:
    print("Este triángulo es un triángulo isósceles.")
else:
    print("Este triángulo es un triángulo escaleno.")