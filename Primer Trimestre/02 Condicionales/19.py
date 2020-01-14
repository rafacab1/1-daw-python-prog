# 19. Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pido el mes en número.
# Si es 1, es enero, 31 días.
# Si es 2, es febrero, 28 días.
# Si es 3, es marzo, 31 días.
# Si es 4, es abril, 30 días.
# Si es 5, es mayo, 31 días.
# Si es 6, es junio, 30 días.
# Si es 7, es julio, 31 días.
# Si es 8, es agosto, 31 días.
# Si es 9, es septiembre, 30 días.
# Si es 10, es octubre, 31 días.
# Si es 11, es noviembre, 30 días.
# Si es 12, es diciembre, 31 días.
#
# Variables
# mes = Mes (int)
#

print("Programa que te dice cuantos días tiene un mes.\n")

# Pido el mes
mes = int(input("Introduce el mes... (1 a 12) "))

# Hago las sentencias
if mes == 1:
    print(f"El mes {mes} es enero, tiene 31 días.")
elif mes == 2:
    print(f"El mes {mes} es febrero, tiene 28 días.")
elif mes == 3:
    print(f"El mes {mes} es marzo, tiene 31 días.")
elif mes == 4:
    print(f"El mes {mes} es abril, tiene 30 días.")
elif mes == 5:
    print(f"El mes {mes} es mayo, tiene 31 días.")
elif mes == 6:
    print(f"El mes {mes} es junio, tiene 30 días.")
elif mes == 7:
    print(f"El mes {mes} es julio, tiene 31 días.")
elif mes == 8:
    print(f"El mes {mes} es agosto, tiene 31 días.")
elif mes == 9:
    print(f"El mes {mes} es septiembre, tiene 30 días.")
elif mes == 10:
    print(f"El mes {mes} es octubre, tiene 31 días.")
elif mes == 11:
    print(f"El mes {mes} es noviembre, tiene 30 días.")
elif mes == 12:
    print(f"El mes {mes} es diciembre, tiene 31 días.")
else:
    print("Lo que has introducido no es un número del 1 al 12")