# 6. Calcular la media de tres números pedidos por teclado.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 9/10/19
#
# Algoritmo
# Pido los tres números
# Sumo los tres números y los divido entre 3
# Muestro el resultado por pantalla
#
# Variables: 
# n1, n2, n3: Números
# media: Resultado

# Pido los números
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))

# Calculo la media
media = (n1 + n2 + n3) / 3

# Muestro el resultado
print("El resultado es:", media)