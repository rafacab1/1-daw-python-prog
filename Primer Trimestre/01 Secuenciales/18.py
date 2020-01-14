# 18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido nombre, apellido y segundo apellido del usuario
# Cojo el primer carácter de cada variable
# Muestro por pantalla el resultado
#
# Variables: 
# nombre = Nombre del usuario
# apellido = Primer apellido del usuario
# apellido2 = Segundo apellido del usuario
#
# https://uniwebsidad.com/libros/algoritmos-python/capitulo-6/operaciones-con-cadenas?from=librosweb

# Pido los datos
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu primer apellido: ")
apellido2 = input("Introduce tu segundo apellido: ")


# Muestro los resultados por pantalla
print("Tus iniciales son", nombre[0], apellido[0], apellido2[0])

