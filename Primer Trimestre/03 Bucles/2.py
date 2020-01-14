# 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). 
# El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 22/10/19
#
# Algoritmo
# Pido la cantidad de números
#   Mientras que i no sea la cantidad de números
#       Pido números
#           Si el número es mayor que 0, le sumo uno a su variable
#           Si el número es mayor que 0, le sumo uno a su variable
#           Si el número es 0, le sumo uno a su variable
#   Muestro los resultados
#
# Variables
# i = Cantidad de números
# mayor = Números mayores que 0
# menor = Números menores que 0
# cero = Números iguales que 0
# x = Cantidad de números incrementable dentro del bucle
# y = Número introducido dentro del bucle
#

print("Programa que dada una cantidad de números pide números y muestra cuantos son mayores, menores o iguales que 0.")
# Pido la cantidad de números
i = int(input("\nIntroduce cuántos números quieres que te pida: "))

# Defino las variables
mayor = 0
menor = 0
cero = 0
x = 0

# Mientras que la cantidad de números sea distinta de la cantidad de números después de un ciclo del bucle...
while i != x:
    y = int(input("Introduce un número: "))
    if y > 0:
        mayor += 1
    if y < 0:
        menor += 1
    if y == 0:
        cero += 1
    x += 1

# Muestro los resultados
print(f"Has introducido {mayor} mayores que 0.")
print(f"Has introducido {menor} menores que 0.")
print(f"Has introducido {cero} iguales que 0.")