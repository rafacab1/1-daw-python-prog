# 12. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. 
# Calcula y muestra la distancia entre ellos.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido los números
# Calculo la diferencia
# Muestro por pantalla el resultado
#
# Variables: 
# x1, y1, x2, y2: Números
# xy1, xy2: Diferencia

# Pido los números
x1 = float(input("Introduce el primer número del primer par (x1): "))
y1 = float(input("Introduce el segundo número del primer par (y1): "))
x2 = float(input("Introduce el primer número del segundo par (x2): "))
y2 = float(input("Introduce el segundo número del segundo par (y2): "))

# Calculo la diferencia
xy1 = abs(x1 - y1)
xy2 = abs(x2 - y2)

# Muestro los resultados por pantalla
print("\nLa distancia entre x1 y y1 es:", xy1)
print("La distancia entre x2 y y2 es:", xy2)