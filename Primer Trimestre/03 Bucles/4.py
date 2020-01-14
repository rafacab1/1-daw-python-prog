# 4. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 30/10/19
#
# Algoritmo
# Pido los dos números
# Compruebo si n1 es menor que n2, si lo es muestro una advertencia, si no sigo.
# En el rango de n1 a n2...
#   Si el resto de i entre 2 es 0, muestro i, ya que es par
#
# Variables
# n1 = Número 1 (int)
# n2 = Número 2 (int)
#

print("Programa que muestra los números pares que hay entre dos números.")

# Pido los números
n1 = int(input("\nIntroduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))

# Si n2 es menor que n1...
if n2 < n1:
    print("Escribe primero el número mas pequeño, y después el mas grande.") # Muestro una advertencia
else:
    for i in range(n1, n2 + 1):
        if i % 2 == 0: # Si el resto es 0, eso significa que el número es par
            print(i)