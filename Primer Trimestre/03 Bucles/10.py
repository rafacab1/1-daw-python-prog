# 10. Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 25/10/19
#
# Algoritmo
# 
# Pido la cadena y el caracter
# Creo un contador que cuente los caracteres
#   Para i en el rango de 0 a la longitud de la cadena...
#       Si el caracter de la posición i en la cadena en minúscula es igual que el caracter en minúscula, incremento el contador en uno mas.
# Muestro el resultado por pantalla
#   
#
# Variables
# cadena = Cadena (str)
# caracter = Caracter (str)
# contador = Contador de los caracteres iguales al caracter introducido (int)
#

print("Programa que te dice cuantos caracteres iguales tiene una cadena.")

# Pido la cadena y el caracter
cadena = input("\nIntroduce una cadena: ")
caracter = input("Introduce un caracter: ")

# Creo la variable del contador
contador = 0

# Para i en el rango de 0 a la longitud de la cadena...
for i in range(0, len(cadena)):
    if cadena[i].lower() == caracter.lower(): # Si el caracter de la posición i de la cadena en minúscula es igual a el caracter en minúscula
        contador += 1 # Le sumo uno al contador

# Muestro el resultado por pantalla
print(f"\nLa cadena {cadena} tiene {contador} {caracter}.")
    