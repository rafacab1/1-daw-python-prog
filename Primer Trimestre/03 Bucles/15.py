# 15. Introducir una cadena de caracteres e indicar si es un palíndromo. 
# Una palabra palíndroma es aquella que se lee igual adelante que atrás.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 25/10/19
#
# Algoritmo
# Mientras que la cadena no sea espacio
#   Pido cadena
#   Invierto cadena
#   Si cadena en minúsculas es igual que la cadena invertida en minúsculas, es un palíndromo.
#   Si no, no es un palíndromo.
#
# Variables
# cadena = Cadena introducida por el usuario (str)
# cadenainv = Cadena invertida (str)

print("Programa que comprueba si una cadena es un palíndromo.")

# Defino la variable
cadena = ""

# Mientras que cadena no sea espacio...
while cadena != " ":
    cadena = input("Introduce una cadena (para salir introduzca espacio): ") # Pido la cadena
    cadenainv = cadena[::-1] # Invierto la cadena
    if cadena.lower() == cadenainv.lower(): # Comparo la cadena con la cadena invertida
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")