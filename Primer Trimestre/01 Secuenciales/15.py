# 15. Dadas dos variables numéricas A y B, que el usuario debe teclear, 
# se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre 
# cuanto valen al final las dos variables.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido los dos números
# Meto en una variable nueva (z) el valor de a, para no perderlo
# Cambio el valor de a y establezco el de b
# Cambio el valor de b y establezco el de z (que en verdad es el que tenía a originalmente)
#
# Variables: 
# a, b = Número
# z = Número (usado para guardar el valor de a)

a = float(input("Introduce valor de A: "))
b = float(input("Introduce valor de B: "))

z = a
a = b
b = z

print("\nA vale", a)
print("B vale:", b)