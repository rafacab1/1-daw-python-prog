# 16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la 
# distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar
# y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido la velocidad de los vehículos y la distancia entre los dos
# Divido la distancia entre los dos entre la diferencia de velocidad que tienen los dos coches
# Paso el resultado a minutos
# Muestro el resultado
#
# Variables: 
# v1 = Velocidad vehículo 1 (lento)
# v2 = Velocidad vehículo 2 (rápido)
# d = Distancia entre los dos vehículos
# tarda = El resultado de lo que tarda en alcanzar el vehículo mas lento al más rápido en minutos

# Pedimos los datos
v1 = float(input("¿A qué velocidad viaja el primer vehículo? (Más lento) "))
v2 = float(input("¿A qué velocidad viaja el segundo vehículo? (Más rápido) "))
d = float(input("¿Distancia entre los dos vehículos? "))

# Hacemos el cálculo de la distancia y como el resultado es en horas lo pasamos en minutos
tarda = int((d / (v2 - v1)) * 60)

# Muestro el resultado por pantalla
print("\nEl vehículo más rápido tarda", tarda, "minutos en alcanzar al más lento.")