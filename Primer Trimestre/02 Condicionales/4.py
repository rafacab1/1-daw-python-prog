# 4. Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 17/10/19
#
# Algoritmo
# Pido los números
# Hago la sentencia de si el segundo es cero
#   Si no es cero, hago una división y muestro el resultado.
#   Si es cero, muestro un aviso.
#
# Variables
# n1: Número 1 (float)
# n2: Número 2 (float)
#

print("Programa que hace una división, pero nunca entre 0.\n")

# Pido los números
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

# Hago la sentencia y muestro el resultado
if n2 == 0:
    print("El segundo número es 0, no puedo hacer la división.")

else:
    print(f"El resultado es {n1 / n2}")