# 12. Escribir un programa que lea un año indicar si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pregunto el año
# Si el resto del año entre 4, es 0...
#   Si lo es, compruebo si es divisible entre 100.
#       Si lo es, compruebo si es divisible entre 400
#           Si lo es, es bisiesto.
#           Si no lo es, no es bisiesto.
#       Si no lo es, es bisiesto.
#   Si no lo es, no es bisiesto
#
# Variables
# year = año (int)

print("Programa que indica si un año es bisiesto.\n")

# Pregunto el año
year = int(input("Introduce un año: "))

# Hago las sentencias
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} es bisiesto.")
        else:
            print(f"{year} no es bisiesto.")
    else:
        print(f"{year} es bisiesto.")
else:
    print(f"{year} no es bisiesto.")