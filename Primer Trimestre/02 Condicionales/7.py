# 7. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. 
# Pueden ocurrir tres cosas:
#
#    El exponente sea positivo, sólo tienes que imprimir la potencia.
#    El exponente sea 0, el resultado es 1.
#    El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 17/10/19
#
# Algoritmo
# Pido la base y el exponente
# Hago las sentencias...
#   Si el exponente es 0, muestro que el resultado es 1.
#   Si no, compruebo si el exponente es positivo, la calculo y muestro el resultado por pantallla.
#   Si tampoco, calculo la potencia haciendo 1/valor absoluto de la potencia.
#
#
#
# Variables
# base = Base (float)
# exp = Exponente (float)
#

print("Programa para calcular potencias.\n")

base = float(input("Introduce la base de la potencia: "))
exp = float(input("Introduce el exponente de la potencia: "))

if exp == 0:
    print(f"El resultado de {base} elevado a {exp} es 1.")
elif exp == abs(exp):
    print(f"El resultado de {base} elevado a {exp} es {base ** exp}.")
else:
    print(f"El resultado de {base} elevado a {exp} es {base ** (1 / abs(exp))}.")