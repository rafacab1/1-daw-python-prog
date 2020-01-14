# 13. Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 25/10/19
#
# Algoritmo
# Defino la variable resultado
# Pido la cadena
# Para i en el rango de 0 a la longitud de la cadena...
#   Meto el carácter en una variable.
#   Si esa variable en minúscula es igual que el carácter
#       Añado el caracter en mayúscula al resultado
#   Si esa variable en mayúscula es igual que el caracter
#       Añado el caracter en minúscula al resultado
#
# Variables
# resultado = Cadena convertida (str)
# cadena = Cadena sin convertir (str)
# posicion = Caracter en la posición i (str)
#

print("Programa que intercambia mayúsculas por minúsculas y minúsculas por mayúsculas.")

# Defino la variable resultado
resultado = ""

# Pido la cadena
cadena = input("\nIntroduce una cadena: ")

for i in range(0, len(cadena)):
    posicion = cadena[i]
    if posicion.lower() == cadena[i]: # Si el caracter en minúscula es igual al caracter...
        resultado += str(cadena[i].upper()) # Le añado el caracter convertido
    if posicion.upper() == cadena[i]: # Si el caracter en mayúscula es igual al caracter en minúscula...
        resultado += str(cadena[i].lower()) # Le añado el caracter convertido

# Muestro el resultado por pantalla
print(resultado)