# 5. Escribe un programa que pida el limite inferior y superior de un intervalo. 
# Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
#	La suma de los números que están dentro del intervalo (intervalo abierto).
#	Cuantos números están fuera del intervalo.
#	Informa si hemos introducido algún número igual a los límites del intervalo.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 25/10/19
#
# Algoritmo
# Pido los límites
# Mientras el límite inferior sea mayor que el superior, pido los límites de nuevo.
# Defino las variables que cuentan los números y la del mismo número
# Mientras el número no sea 0...
#   Pido un número
#   Si es 0, muestro el resultado de los contadores
#   Si es menor que el superior y mayor que el inferior, sumo uno en dentro
#   Si es menor que el inferior o mayor que el superior, sumo uno en fuera
#   Si es igual que el inferior o igual que el superior, sumo uno en igual
#
# Variables
# sup = Límite superior (int)
# inf = Límite inferior (int)
# num = Número introducido (int)
# dentro = Números dentro del intervalo (int)
# fuera = Números fuera del intervalo (int)
# igual = Números iguales al intervalo (int)
#

print("Programa que pide un intervalo y luego pide números. Muestra cuantos números estan dentro, fuera o iguales al intervalo.")
print("Para salir, introduzca un 0.")

# Pido los límites
sup = int(input("\nIntroduce el límite superior: "))
inf = int(input("Introduce el límite inferior: "))

# Si el límite inferior es mayor que el superior, vuelvo a pedirlos
while inf > sup:
    print("\nEl límite inferior no puede ser mayor que el límite superior. Introduce los datos de nuevo.")
    sup = int(input("Introduce el límite superior: "))
    inf = int(input("Introduce el límite inferior: "))

# Defino las variables de los contadores
num = 1
dentro = 0
fuera = 0
igual = 0

# Mientras que el número no sea 0...
while num != 0:
    num = int(input("Introduce un número: "))
    if num == 0:
        print(f"\nHas introducido {dentro} números dentro del intervalo, {fuera} números fuera del intervalo y {igual} números iguales que los límites.")
        print("Saliendo...")
    if num < sup and num > inf:
        dentro += 1
    elif num < inf or num > sup:
        fuera += 1
    elif num == inf or num == sup:
        igual += 1
    