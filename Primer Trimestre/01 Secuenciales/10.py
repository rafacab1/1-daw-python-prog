# 10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
#
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido todas las notas
# Calculo la media de las tres calificaciones parciales
# Calculo los porcentajes de todas las notas
# Sumo todas las notas
# Muestro por pantalla el resultado
#
# Variables: 
# c1, c2, c3 = Calificaciones parciales
# ef = Calificación examen final
# tf = Calificación trabajo final
# mediac = Media calificaciones parciales
# pc = Parte porcentual correspondiente a calificaciones parciales
# ec = Parte porcentual correspondiente a examen final
# tc = Parte porcentual correspondiente a trabajo final
# total = Calificación final del alumno

# Pido las calificaciones
c1 = float(input("Introduce la primera calificación parcial: "))
c2 = float(input("Introduce la segunda calificación parcial: "))
c3 = float(input("Introduce la tercera calificación parcial: "))
ef = float(input("Introduce tu calificación en el examen final: "))
tf = float(input("Introduce tu calificación en el trabajo final: "))

# Calculo la media de las tres calificaciones parciales
mediac = (c1 + c2 + c3) / 3

# Calculo las calificaciones con los porcentajes
pc = mediac * 55 / 100
ec = ef * 30 / 100
tc = tf * 15 / 100

# Sumo todo
total = pc + ec + tc

# Muestro el resultado por pantalla
print("\nTu nota final es:", total)