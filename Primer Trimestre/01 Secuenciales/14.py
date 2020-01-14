# 14. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido el número (n)
# Saco el resto de dividir n entre 10, lo multiplico por 10 y le sumo lo que de n entre 10.
# Muestro el resultado por pantalla
#
# Variables: 
# n = Número original
# ni = Número invertido
#
# https://www.lawebdelprogramador.com/foros/Java/1647142-Invertir-numero-metodo-recursivo.html

# Pido un número
n = int(input("Introduce un número de dos cifras: "))

# Hago los calculos
ni = (n % 10) * 10 + (n // 10)

# Muestro el resultado por pantalla
print(ni)