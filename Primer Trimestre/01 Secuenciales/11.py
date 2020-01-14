# 11. Pide al usuario dos números y muestra la "distancia" entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido los dos números
# Los resto y indico que quiero sacar el valor absoluto
# Muestro por pantalla el resultado
#
# Variables: 
# n1 = Número 1
# n2 = Número 2
# distancia = Distancia entre los dos números

# Pido los números
n1 = float(input("Introduce el número 1: "))
n2 = float(input("Introduce el número 2: "))

# Calculo la distancia y el valor absoluto
distancia = abs(n1 - n2)

# Muestro por pantalla el resultado
print("La distancia entre esos dos números es", distancia)