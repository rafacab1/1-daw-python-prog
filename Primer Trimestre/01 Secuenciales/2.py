# 2. Calcular el perí­metro y área de un rectángulo dada su base y su altura.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 9/10/19
#
# Algoritmo
# Pido el ancho y el alto y los meto en una variable.
# Hago los cálculos y los meto en una variable.
# Imprimo por pantalla los resultados.
#
# Variables: 
# ancho: El ancho del rectángulo
# alto: El alto del rectángulo
# perimetro: El cálculo del perímetro 2 * (a + b)
# area: El cálculo del área a + b

# Pido los datos
ancho = float(input("Introduce el ancho del rectángulo: "))
alto = float(input("Introduce el alto del rectángulo: "))

# Hago los cálculos
perimetro = 2 * (ancho + alto)
area = ancho * alto

# Muestro un salto de línea para separar y muestro los resultados por pantalla
print("\n")
print("El perímetro del rectángulo es ", perimetro)
print("El área del rectángulo es", area)
