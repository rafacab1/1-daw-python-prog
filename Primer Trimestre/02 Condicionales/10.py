# 10. Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos 
# circunferencias y las clasifique en uno de estos estados:
#
# exteriores
# tangentes exteriores
# secantes
# tangentes interiores
# interiores
# concéntricas
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pido los datos.
# Calculo la distancia entre los dos puntos.
# Valoro como son las dos circurferencias:
# Si d es mayor que la suma de los radios, son exteriores.
# Si d es menor que la suma de los radios y mayor que su diferencia, son secantes.
# Si d es mayor que 0 y menor que su diferencia, son interiores.
# Si d es igual que la suma de los radios, son tangentes exteriores.
# Si d es igual que la diferencia de los radios, son tangentes interiores.
# Si d es 0, son concéntricas.
#
# Variables
# d = Distancia entre las dos circurferencias (float)
# x1 = Posición x de la primera circurferencia (float)
# x2 = Posición x de la segunda circureferencia (float)
# y1 = Posición y de la primera circurferencia (float)
# y2 = Posición y de la segunda circureferencia (float)
# r1 = Radio de la primera circurferencia (float)
# r2 = Radio de la segunda circurferencia (float)

import math

# Pido los datos
x1 = float(input("Introduce x1: "))
x2 = float(input("Introduce x2: "))
y1 = float(input("Introduce y1: "))
y2 = float(input("Introduce y2: "))
r1 = float(input("Introduce r1: "))
r2 = float(input("Introduce r2: "))

# Calculo la distancia entre las dos circurferencias
d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# Hago las sentencias
if d > (r1 + r2):
    print("\nLas dos circurferencias son exteriores.")

if d < (r1 + r2) and d > (r1 - r2):
    print("\nLas dos circurferencias son secantes.")

if d > 0 and d < (r1 - r2):
    print("\nLas dos circurferencias son interiores.")

if d == (r1 + r2):
    print("\nLas dos circurferencias son tangentes exteriores.")

if d == (r1 - r2):
    print("\nLas dos circurferencias son tangentes interiores.")

if d == 0:
    print("\nLas dos circurferencias son concéntricas.")
