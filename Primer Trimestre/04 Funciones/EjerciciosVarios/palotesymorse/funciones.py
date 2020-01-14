# -*- coding: utf-8 -*-

# El nombre de los ejercicios lo he cambiado para adaptarme a las normas de estilo de Python.


"""
Ejercicio 35.
Crea una función con la siguiente cabecera:
public static String convierteEnPalotes(int n)
Esta función convierte el número n al sistema de palotes y lo devuelve en una
cadena de caracteres. Por ejemplo, el 470213 en decimal es el | | | | - | | | | | |
| - - | | - | - | | | en el sistema de palotes. Utiliza esta función en un programa
para comprobar que funciona bien. Desde la función no se debe mostrar nada
por pantalla, solo se debe usar print desde el programa principal.

Algoritmo
En un bucle, voy recorriendo el número, y para cada dígito guardo en una variable tal cantidad de palotes,
luego devuelvo esta variable.

Variables
n : Entero introducido por el usuario
almacen : Voy guardando los palotes (str)

"""


def convierte_en_palotes(n):
    almacen = ""
    for i in range(0, len(str(n))):
        if str(n)[i] == "0":
            almacen += ""
        if str(n)[i] == "1":
            almacen += "|"
        if str(n)[i] == "2":
            almacen += "||"
        if str(n)[i] == "3":
            almacen += "|||"
        if str(n)[i] == "4":
            almacen += "||||"
        if str(n)[i] == "5":
            almacen += "|||||"
        if str(n)[i] == "6":
            almacen += "||||||"
        if str(n)[i] == "7":
            almacen += "|||||||"
        if str(n)[i] == "8":
            almacen += "||||||||"
        if str(n)[i] == "9":
            almacen += "|||||||||"
        if i+1 != len(str(n)):
            almacen += " - "
    return almacen


"""
Crea una función con la siguiente cabecera:
public String convierteEnMorse(int n)
Esta función convierte el número n al sistema Morse y lo devuelve en una
cadena de caracteres. Por ejemplo, el 213 es el . . _ _ _ . _ _ _ _ . . . _ _ en
Morse. Utiliza esta función en un programa para comprobar que funciona bien.
Desde la función no se debe mostrar nada por pantalla, solo se debe usar print
desde el programa principal.

Algoritmo

Variables

"""


def convierte_en_morse(n):
    almacen = ""
    for i in range(0, len(str(n))):
        if str(n)[i] == "0":
            almacen += "_ _ _ _ _"
        if str(n)[i] == "1":
            almacen += ". _ _ _ _"
        if str(n)[i] == "2":
            almacen += ".. _ _ _"
        if str(n)[i] == "3":
            almacen += ". . . _ _"
        if str(n)[i] == "4":
            almacen += ". . . . _"
        if str(n)[i] == "5":
            almacen += ". . . . ."
        if str(n)[i] == "6":
            almacen += "_ . . . ."
        if str(n)[i] == "7":
            almacen += "_ _ . . ."
        if str(n)[i] == "8":
            almacen += "_ _ _ . ."
        if str(n)[i] == "9":
            almacen += "_ _ _ _ ."
    return almacen
