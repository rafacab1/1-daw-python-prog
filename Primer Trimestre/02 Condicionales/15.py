# 15. El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe 
# cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente:
# si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, 
# de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. 
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pregunto la cantidad de alumnos.
# Si son mas de 100, multiplico el número de alumnos por 65. Muestro por pantalla el resultado (65 * n alumnos)
# Si son de 50 a 99, multiplico el número de alumnos por 70. Muestro por pantalla el resultado (70 * n alumnos) 
# Si son de 30 a 49, multiplico el número de alumnos por 95. Muestro por pantalla el resultado (90 * n alumnos)
# Si son menos de 30, imprimo por pantalla que el precio de cada alumno es 4000 / número de alumnos, y el total es 4000€
#
# Variables
# alumnos = Número de alumnos (int)

print("Programa que calcula cuanto debe de pagar un número de alumnos para el pago a la compañía de autobuses.\n")

# Pido el número de alumnos.
alumnos = int(input("Introduce el número de alumnos: "))

# Hago las sentencias y muestro el resultado por pantalla.
if alumnos > 100:
    print(f"\nCada alumno debe pagar 65€, se pagaría un total de {alumnos * 65}€.")
elif alumnos < 99 and alumnos > 50:
    print(f"\nCada alumno debe pagar 70€, se pagaría un total de {alumnos * 70}€.")
elif alumnos < 49 and alumnos > 30:
    print(f"\nCada alumno debe pagar 95€, se pagaría un total de {alumnos * 95}€.")
elif alumnos < 30:
    print(f"\nCada alumno debe pagar {4000 / alumnos}€, se pagaría un total de 4000€.")
else:
    print("\nHa ocurrido un error.")