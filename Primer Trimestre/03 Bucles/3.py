# 3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ 
# en caso contrario, el programa termina cuando se introduce un espacio.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 22/10/19
#
# Algoritmo
# Mientras que una variable sea distinta de " "
#   Pido un número
#   Si es igual que "a" o "e" o "i" o "u" o "o" y la longitud es 1
#       Muestro VOCAL
#   Si no, compruebo que la longitud sea 1 y no sea " ", si es cierto, muestro "NO VOCAL"
#   Si no, compruebo si es " ", si es cierto, muestro saliendo.
#   Si no es nada de lo anterior, muestro error.
#
# Variables
# caracter = Caracter introducido
#

caracter = "aeiou"

print("Programa que pide un caracter y dice si es vocal. Para salir intruduce un espacio. ")

while caracter != " ":
    caracter = input("\nIntroduce un carácter: ")
    if caracter.lower() == "a" or caracter.lower() == "e" or caracter.lower() == "i" or caracter.lower() == "o" or caracter.lower() == "u" and len(caracter) == 1:
        print("VOCAL")
    elif len(caracter) == 1 and caracter != " ":
        print("NO VOCAL")
    elif caracter == " ":
        print("\nSaliendo...")
    else:
        print("\nHa ocurrido un error. Recuerda que debes introducir un sólo caracter.")