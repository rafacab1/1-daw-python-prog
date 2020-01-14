# 6. Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 17/10/19
#
# Algoritmo
# Pido la letra
# Hago la sentencia de si es mayúscula.
#   Si es mayúscula y la longitud es 1, muestro por pantalla que lo es.
#   Si no, muestro por pantalla que no lo es.
#
# Variables
# letra = letra (str)
#

print("Programa que identifica si lo que introduce el usuario es una letra mayúscula.\n")

# Pido que el usuario introduzca una letra
letra = input("Introduce una letra: ")

# Hago la sentencia
if letra == letra.upper() and len(letra) == 1:
    print(f"{letra} es una letra mayúscula.")

else:
    print(f"{letra} no es una letra mayúscula.")