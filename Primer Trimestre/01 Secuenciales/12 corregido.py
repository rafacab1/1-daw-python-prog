# 12. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
# Calcula y muestra la distancia entre ellos.
#
# 15/10/19
#
# Algoritmo
# Pido los números
# Calculo la diferencia
# Muestro por pantalla el resultado
#
# Variables: 
# x1, y1, x2, y2: Números
# xy1, xy2: Diferencia

import math

# Pido los números
x1 = float(input("Introduce el primer número del primer par (x1): "))
y1 = float(input("Introduce el segundo número del primer par (y1): "))
x2 = float(input("Introduce el primer número del segundo par (x2): "))
y2 = float(input("Introduce el segundo número del segundo par (y2): "))

# Cálculos
distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

# Muestro los resultados por pantalla
print(f"Distancia: {distancia}")