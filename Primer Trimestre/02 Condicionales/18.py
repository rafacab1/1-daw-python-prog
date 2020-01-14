# 18. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
# Si introducimos otro número nos da un error.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pido el número
# Si es 1, es lunes
# Si es 2, es martes
# Si es 3, es miércoles
# Si es 4, es jueves
# Si es 5, es viernes
# Si es 6, es sábado
# Si es 7, es domingo
# Si no es nada de lo anterior, da error.
#
# Variables
# dia = Día de la semana (int)
#

print("Programa que escribe el día de la semana que corresponde al número.\n")

# Pido el día de la semana
dia = int(input("Introduce un día de la semana... (1 a 7) "))

# Hago las sentencias
if dia == 1:
    print("Es lunes.")
elif dia == 2:
    print("Es martes.")
elif dia == 3:
    print("Es miércoles.")
elif dia == 4:
    print("Es jueves.")
elif dia == 5:
    print("Es viernes.")
elif dia == 6:
    print("Es sábado.")
elif dia == 7:
    print("Es domingo.")
else:
    print("Error, no has introducido un número entre 1 y 7.")