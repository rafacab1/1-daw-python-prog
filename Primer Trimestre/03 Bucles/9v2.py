# 9. Mostrar en pantalla los N primero número primos. 
# Se pide por teclado la cantidad de números primos que queremos mostrar.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 29/10/19
#
# Algoritmo
# Pido la cantidad de números a mostrar
# Creo una variable que haga de contador
# En un rango de 2 (primer primo) a un número muy largo
# Compruebo si no he superado el contador
# Calculo el factorial de i-1, para luego sumar 1 y ver si el resto del mismo entre i es 0 (en ese caso es primo) https://www.wikiprimes.com/como-saber-si-un-numero-es-primo/
# Si el resto es 0, muestro i y le sumo uno al contador
# Si he superado el contador, salgo del bucle

# Variables
# n = número introducido por el usuario (int)
# num = Número de inicio (int)
# es_prime = Indica si es primo o no (bool)

import math

# Inicializo pensando que es primo
es_primo = True

print("Programa que muestra los n primeros números primos.")

# Pido el número de primos a mostrar
n = int(input("\nIntroduce cuantos números quieres mostrar: "))

num = 2
while num<=math.sqrt(n) and es_primo:
  if n%num == 0:
    es_primo = False
  num += 1

if es_primo:
  print("Es primo.")
else:
  print("No es primo.")