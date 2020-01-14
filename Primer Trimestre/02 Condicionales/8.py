# 8. Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el 
# mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a 
# dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe 
# imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 17/10/19
#
# Algoritmo
# Pido la nota
# Pido la edad
# Pido el sexo
# Hago la sentencia...
#   Si nota es mayor o igual que cinco Y edad es mayor o igual que dieciocho Y el sexo es F, muestro ACEPTADA.
#   Si nota es mayor o igual que cinco Y edad es mayor o igual que dieciocho Y el sexo es M, muestro POSIBLE.
#   Si no se cumple nada de lo anterior, muestro NO ACEPTADA.
#
# Variables
# nota = Nota (float)
# edad = Edad (int)
# sexo = Sexo (str)
#

# Pido los datos
nota = float(input("Introduce tu nota: "))
edad = int(input("Introduce tu edad: "))
sexo = str(input("Introduce tu sexo [M/F]: "))

# Hago las sentencias y muestro los resultados
if nota >= 5 and edad >= 18 and sexo.lower() == "f":
    print("\nACEPTADA")
elif nota >= 5 and edad >= 18 and sexo.lower() == "m":
    print("\nPOSIBLE")
else:
    print("\nNO ACEPTADA")
