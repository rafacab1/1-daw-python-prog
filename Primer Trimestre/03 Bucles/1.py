# 1. Crea una aplicación que permita adivinar un número. 
# La aplicación genera un número aleatorio del 1 al 100. 
# A continuación va pidiendo números y va respondiendo 
# si el número a adivinar es mayor o menor que el introducido,
# a demás de los intentos que te quedan (tienes 10 intentos para acertarlo).
# El programa termina cuando se acierta el número 
# (además te dice en cuantos intentos lo has acertado), 
# si se llega al limite de intentos te muestra el número que había generado.
#
# Para usar números aleatorios en Python: http://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 22/10/19
#
# Algoritmo
# Genero un número aleatorio del 1 al 100 y lo guardo
# Defino una variable a 0
# En un bucle, mientras la variable sea distinta de 10
#   Pido un número
#       Si el número es mayor que el que he generado, muestro que es mayor.
#       Si el número es menor que el que he generado, muestro que es menor.
#           (en estos dos casos, si i es 10, cambio el mensaje por uno que dice que no lo has conseguido)
#       Si el número es el mismo que he generado, muestro que lo ha acertado.
#
# Variables
# num = Número
# i = Variable que cuenta los intentos
# inputnum = Número introducido por el usuario
# y = Variable para controlar cuando el usuario ha conseguido adivinar el número

import random

print("Programa en el que tienes que adivinar un número. Tienes 10 intentos.")

# Genero el número
num = random.randrange(100)

# Defino las variables para controlar el bucle
i = 1
y = 0

# Hago un bucle, en el que mientras i no sea 11 y y no sea 11
while i != 11 and y != 1:
    inputnum = int(input("\nIntroduce un número: "))
    if inputnum > num and i == 10:
        print(f"Lo siento, no lo has adivinado, el número era el {num}.")
    if inputnum < num and i == 10:
        print(f"Lo siento, no lo has adivinado, el número era el {num}.")
    if inputnum > num and i != 10:
        print(f"Intento {i}. El número introducido es mayor que el generado. Es decir, buscamos uno menor que {inputnum}.")
    if inputnum < num and i != 10:
        print(f"Intento {i}. El número introducido es menor que el generado. Es decir, buscamos uno mayor que {inputnum}.")
    if inputnum == num:
        print(f"Enhorabuena, has acertado con {i} intentos.")
        y = 1
    i += 1
