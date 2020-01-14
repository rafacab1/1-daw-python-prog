# 5. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 9/10/19
#
# Algoritmo
# Pido los grados Celsius
# Hago el cálculo y lo meto en la variable
# Muestro el resultado por pantalla.
#
# Variables: 
# celsius: Grados Celsius
# fahrenheit: Grados Fahrenheit

# Pido grados Celsius
celsius = float(input("Introduce los grados Celsius: "))

# Lo paso a Fahrenheit
fahrenheit = (celsius * 1.8) + 32

# Muestro el resultado por pantalla
print(celsius, "grados Celsius equivale a", fahrenheit, "grados Fahrenheit.")