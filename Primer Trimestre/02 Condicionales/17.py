# 17. Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar 
# un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pido el número del dado
# Si es 1, muestro "seis"
# Si es 2, muestro "cinco"
# Si es 3, muestro "cuatro"
# Si es 4, muestro "tres"
# Si es 5, muestro "dos"
# Si es 6, muestro "uno"
# Si el número no es ninguno de entre 1 y 6, muestro "ERROR: número incorrecto"
#
# Variables
# num = Número del dado (int)
#

print("Programa que muestra por pantalla el número en letras de la cara opuesta al resultado obtenido en un dado.\n")

# Pido el número
num = int(input("Introduce el número que has obtenido en el dado (en número): "))

# Hago las sentencias y muestro por pantalla el resultado
if num == 1:
    print("\nEn la cara opuesta está el seis.")
elif num == 2:
    print("\nEn la cara opuesta está el cinco.")
elif num == 3:
    print("\nEn la cara opuesta está el cuatro.")
elif num == 4:
    print("\nEn la cara opuesta está el tres.")
elif num == 5:
    print("\nEn la cara opuesta está el dos.")
elif num == 6:
    print("\nEn la cara opuesta está el uno.")
else:
    print("\nERROR: número incorrecto.")