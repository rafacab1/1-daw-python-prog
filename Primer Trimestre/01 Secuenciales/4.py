# 4. Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 9/10/19
#
# Algoritmo
# Pido los dos números.
# Hago los cálculos y meto cada uno de ellos en una variable.
# Muestro las variables por pantalla.
#
# Variables: 
# n1: Número 1
# n2: Número 2
# suma: Cálculo de la suma
# resta: Cálculo de la resta
# division: Cálculo de la división
# multiplicacion: Cálculo de la multiplicación

# Pido los números
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

# Realizo los cálculos
suma = n1 + n2
resta = n1 - n2
division = n1 / n2
multiplicacion = n1 * n2

# Muestro los resultados
print("\n")
print("El resultado de la suma es:", suma)
print("El resultado de la resta es:", resta)
print("El resultado de la division es:", division )
print("El resultado de la multiplicacion es:", multiplicacion )