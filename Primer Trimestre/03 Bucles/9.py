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
# c = contador (int)

import math

print("Programa que muestra los n primeros números primos.")

# Pido el número de primos a mostrar
n = int(input("\nIntroduce cuantos números quieres mostrar: "))

# Creo la variable que hará de contador
c = 0

for i in range(2, 999999):
        fc = math.factorial((i-1)) # Calculo el factorial de i menos 1
        if c < n: # Si no he superado el límite para contador...
            if (fc + 1) % i == 0: # Le sumo uno al resultado del factorial y compruebo si el resto es 0
                print(i) # Muestro el número primo
                c += 1 # Le sumo uno al contador
        else:
            break