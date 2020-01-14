# 6. Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), 
# saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 25/10/19
#
# Algoritmo
# Pido la base y el exponente al usuario
# Defino una variable (b1) que sea igual a la base
# Defino una variable que haga de contador
# Mientras que el exponente no sea igual que a la cantidad que lleva el contador...
#   Multiplica la variable b1 por la base
#   Le sumo uno al contador
# Muestro por pantalla el resultado
# 
#
# Variables
# base = Base (int)
# exp = Exponente (int)
# cont = Contador de veces que se multiplica la base (int)
# b1 = Base después de una multiplicación (int)

print("Programa que calcula el resultado de una potencia.")

# Pido los datos
base = int(input("\nIntroduce la base: "))
exp = int(input("Introduce el exponente: "))
b1 = base
cont = 1

# Mientras que el exponente no sea igual que el contador...
while exp != cont:
    b1 = b1 * base
    cont += 1

# Muestro el resultado
print(f"\nEl resultado de {base} elevado a {exp} es {b1}.")