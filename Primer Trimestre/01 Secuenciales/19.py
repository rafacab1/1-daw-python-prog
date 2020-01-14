# 19. Escribir un algoritmo para calcular la nota final de un estudiante, 
# considerando que por cada respuesta correcta 5 puntos, por una incorrecta -1 
# y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo:
# Pregunto cuantas respuestas correctas, incorrectas y en blanco ha tenido el estudiante.
# Multiplico el número de correctas por 5, el número de incorrectas por -1 y el número de preguntas 
# en blanco por 0.
# Muestro el resultado por pantalla
#
# Variables: 
# correctas = Preguntas correctas
# incorrectas = Preguntas incorrectas
# blanco = Preguntas sin contestar
# resultado = Puntuación final del estudiante

# Pregunto cuantas respuestas correctas, incorrectas y sin contestar ha tenido.
correctas = int(input("¿Cuántas respuestas correctas has tenido?: "))
incorrectas = int(input("¿Cuántas respuestas incorrectas has tenido?: "))
blanco = int(input("¿Y cuántas has dejado sin contestar?: "))

# Calculo el resultado.
resultado = (correctas * 5) - (incorrectas * -1) + (blanco * 0)

# Muestro el resultado por pantalla.
print("En total tienes", resultado, "puntos.")