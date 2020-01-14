# 12. Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 29/10/19
#
# Algoritmo
# Pido la cadena y los caracteres
# Creo una variable para ir metiendo todos los caracteres
# Compruebo si la longitud de lo introducido es un 1
#   Si lo es, en un rango de 0 a cadena
#       Compruebo si el caracter de la posición es igual que el primero introducido. Si lo es, añado el segundo caracter
#       Compruebo si el caracter de la posición no es igual que el primero introducido. Si es cierto, añado el mismo caracter.
#   Si no lo es, digo que no se han introducido bien los caracteres
# Muestro el contenido de repl
#
# Variables
# cadena = Cadena introducida por el usuario (str)
# c1 = Primer caracter (str)
# c2 = Segundo caracter (str)
# repl = Nueva cadena con los caracteres reemplazados (str)
#

print("Programa que a partir de una cadena reemplaza un caracter indicado por otro.")

# Pido la cadena y los caracteres
cadena = input("\nIntroduce una cadena: ")
c1 = input("Introduce un caracter: ")
c2 = input("Introduce otro caracter: ")

# Creo la variable
repl = ""

if len(c1) == 1 and len(c2) == 1: # Compruebo si es un caracter
    for i in range(0, len(cadena)):
        if cadena[i].lower() == c1.lower(): # Si coincide con el primer introducido
            repl += c2 # Añado el segundo introducido
        if cadena[i].lower() != c1.lower(): # Si no coincide con el primer introducido
            repl += cadena[i] # Añado el mismo
else:
    print("\nNo has introducido bien los caracteres.")

print(f"\n{repl}")