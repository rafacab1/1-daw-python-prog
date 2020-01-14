# -*- coding: utf-8 -*-
import random

# El nombre de los ejercicios lo he cambiado para adaptarme a las normas de estilo de Python.


"""
1. Genera un array de tamaño n con números aleatorios
cuyo intervalo (mínimo y máximo) se indica como parámetro.

Algoritmo
Creo un array
Recorro el array y en cada entrada guardo un número aleatorio
Devuelvo el array

Variables
n = Longitud del array (int)
minimo = Número mínimo a generar (int)
maximo = Número máximo a generar (int)
array_int = Array de enteros

"""


def genera_array_int(n, minimo, maximo):
    array_int = [None] * n
    for i in range(0, n):
        array_int[i] = random.randint(minimo, maximo)
    return array_int


"""
2. Devuelve el mínimo del array que se pasa como pará-
metro.

Recorro el array, comparándolo con el anterior mínimo, si la posición en la que estoy del array es menor, actualizo
la variable que contiene el mínimo

Variables
array = Array pasado como parámetro
minimo = Número mínimo (int)

"""


def minimo_array_int(array):
    minimo = 99999999
    for i in range(0, len(array)):
        if array[i] <= minimo:
            minimo = array[i]
    return minimo


"""
3. Devuelve el máximo del array que se pasa como pará-
metro.

Recorro el array, comparándolo con el anterior maximo, si la posición en la que estoy del array es mayor, actualizo
la variable que contiene el máximo

Variables
array = Array pasado como parámetro
maximo = Número maximo (int)

"""


def maximo_array_int(array):
    maximo = -99999999
    for i in range(0, len(array)):
        if array[i] >= maximo:
            maximo = array[i]
    return maximo


"""
4. Devuelve la media del array que se pasa como paráme-
tro.

Algortimo
Recorro el array y voy sumando todo en una variable
Devuelvo el resultado de la división de la variable entre la longitud del array

Variables
array : Array introducido por el usuario
sumatorio : Contiene la suma de todos los números del array (int)

"""


def media_array_int(array):
    sumatorio = 0
    for i in range(0, len(array)):
        sumatorio += array[i]
    return sumatorio/len(array)


"""
5. Dice si un número está o no dentro de un array.

Algoritmo
Recorro el array, si el número del array es igual que el número introducido, marco que si que está en una variable, la
función devuelve esta última variable

Variables
esta = Controla si el número está en el array (boolean)
array = Array introducido por el usuario
numero = Número introducido por el usuario

"""


def esta_en_array_int(array, numero):
    esta = False
    for i in range(0, len(array)):
        if array[i] == numero:
            esta = True
    return esta


"""
6. Busca un número en un array y devuelve la posición
(el índice) en la que se encuentra.

Algoritmo
Recorro el array y comparo el número con la posición actual del array, si es igual, guardo la posición en una variable.

Variables
array : Array introducido por el usuario
numero : Número introducido por el usuario (int)
pos : Posición del número en el array (int)

"""


def posicion_en_array(array, numero):
    pos = -1
    for i in range(0, len(array)):
        if array[i] == numero:
            pos = i
    return pos


"""
7. Le da la vuelta a un array

Algoritmo
Recorro el array, y voy guardando en las últimas posiciones del array volteado el número actual del ciclo del array 
principal, devuelvo el array volteado.

Variables
array : Array introducido por el usuario
array_volt : Array volteado

"""


def voltea_array_int(array):
    array_volt = [None] * len(array)
    for i in range(0, len(array)):
        array_volt[(len(array)-1)-i] = array[i]
    return array_volt


"""
8. Rota n posiciones a la derecha los números de un
array.

Algoritmo
Recorro el array, si la suma de i y las posiciones a rotar son iguales o mayores que la longitud del array, meto
los números al principio del array (si no, no volvería a empezar por la izquierda). En el caso de que esa condición
fuese falsa, mete los números en la posición i + posiciones a rotar.

Variables
array : Array introducido por el usuario
n : Número de posiciones a rotar
j : Contador para volver a empezar el array por el principio
array_dcha : Array rotado a la derecha

"""


def rota_derecha_array_int(array, n):
    array_dcha = [None] * len(array)
    j = -1
    for i in range(0, len(array)):
        if i+n >= len(array):
            j += 1
            array_dcha[1*j] = array[i]
        else:
            array_dcha[i+n] = array[i]
    return array_dcha


"""
9. Rota n posiciones a la izquierda los números de
un array.

Algoritmo
Volteo el array
Aprovecho la función anterior de rotar a la derecha, lo roto hacia la derecha
Vuelvo a voltear el array
Devuelvo el array

Variables
array : Array introducido por el usuario
n : Posiciones a rotar
avolt : Array volteado
array_izda : Array rotado

"""


def rota_izquierda_array_int(array, n):
    avolt = voltea_array_int(array)
    array_izda = voltea_array_int(rota_derecha_array_int(avolt, n))
    return array_izda
