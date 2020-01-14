# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 9/10/19
#
# Algoritmo
# Pido los catetos
# Hago los cálculos y los meto en una variable.
# Imprimo por pantalla los resultados.
#
# Variables: 
# c1: Cateto 1
# c2 : Cateto 2
# hipotenusa: Hipotenusa (resultado)

import math

# Pedimos los catetos
c1 = float(input("Introduce el cateto 1: "))
c2 = float(input("Introduce el cateto 2: "))

# Hacemos cálculos
hipotenusa = math.sqrt(c1 ** 2 + c2 ** 2)

# Muestro la respuesta
print("La hipotenusa es: ", hipotenusa)