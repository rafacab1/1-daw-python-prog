# -*- coding: utf-8 -*-
import math

# El nombre de los ejercicios lo he cambiado para adaptarme a las normas de estilo de Python.


def es_capicua(num):
    """
    1. Función que prueba si un número es capicúa.

    Algoritmo
    Recorre el número del revés, y lo va almacenando en una variable
    Compara la variable con el número original, si son iguales, devuelve True, si no, devuelve False.

    Variables
    num = Número original pasado cómo parámetro. Primero (int) y luego (str) para medirlo.
    almacen = Número del revés (str)
    """
    num = str(num)
    almacen = ""

    for i in range(-len(num), 0):
        i = abs(i + 1)
        almacen += num[i]

    if num == almacen:
        return True

    else:
        return False


def es_primo(num):
    """
    2. Función que comprueba si un número es primo

    Algoritmo
    Primero supongo que es primo
    Mientras que un número (primero 2) sea menor o igual que la raíz del número a comprobar, y suponga que es primo
    Compruebo números, es decir, si el resto del número entre n (que primero es 2) da 0, no es primo y acabo porque el
    bucle while ya no es True. Si el resto no es 0, le sumo 1 a n (ahora sería 3) y vuelvo a comprobar.
    Al final, el bucle devuelve la variable 'primo', que es una variable booleana que indica si es primo o no.

    Variables
    num : Número introducido por el usuario (int)
    n : Número con el que divido para calcular si el resto es 0 o no (int)
    primo: Indica si es primo o no, al principio suponemos que si para que entre al bucle a comprobar (boolean)
    """
    n = 2
    primo = True
    while n <= math.sqrt(num) and primo:
        if num % n == 0:
            primo = False
        n += 1
    return primo


def siguiente_primo(num):
    """
    3. Función que devuelve el menor primo que es mayor al número que se pasa como parámetro.

    Algoritmo
    Le sumo uno a 1 al número (ahora ya es el siguiente número). Compruebo si es primo, si lo es devuelvo num, si no...
    En un bucle, compruebo si el número es primo, si no lo es le sumo uno y empiezo el bucle otra vez. Si es primo
    Salgo del bucle y devuelvo el número.

    Variables
    num : Número introducido (int)
    """
    num += 1
    if es_primo(num):
        return num
    else:
        while True:
            if es_primo(num):
                break
            else:
                num += 1
        return num


def potencia(base, exp):
    """
    4. Función que dada una base y un exponente devuelve la potencia.

    Algoritmo
    Guardo la base en otra variable y hago un contador
    Mientras que el contador no sea igual que el exponente, multiplico base que guarde por la base original y lo guardo
    en la variable con la base nueva, y le sumo uno al contador.

    Variables
    b1 : Variable en la que se irá guardando el resultado (int)
    cont : Contador para llegar hasta el exponente (int)
    base : Base introducida por el usuario (int)
    exp : Exponente introducido por el usuario (int)
    """
    b1 = base
    cont = 1

    # Mientras que el exponente no sea igual que el contador...
    while exp != cont:
        b1 = b1 * base
        cont += 1

    return b1


def digitos(num):
    """
    5. Función que cuenta el número de dígitos de un número entero.

    Algortimo
    Si el número es menor que 9, ya sé que tiene un dígito, si tiene mas, lo divido entre 10 y lo almaceno en la misma
    variable, y le añado 1 al contador de dígitos, ahora al volver a comprobar el bucle, si sigue sin ser menor que 9,
    vuelvo a repetir el proceso, y si no, devuelvo el contenido del contador de dígitos.

    Variables
    num : Número introducido por el usuario (int)
    cuenta : Contador de dígitos (int)
    """
    cuenta = 1
    while num > 9:
        num = num / 10
        cuenta = cuenta + 1
    return cuenta


def voltea(num):
    """
    6. Función que le da la vuelta a un número

    Algoritmo
    Paso el número a cadena
    Recorro la cadena al revés y voy guardando los números en la variable almacen, la cual luego devuelvo.

    Variables
    num : Número introducido por el usuario (int primero, luego str)
    almacen : Guarda el número volteado (str, luego se devuelve como int)
    """
    num = str(num)
    almacen = ""
    for i in range(-len(num), 0):
        i = abs(i + 1)
        almacen += num[i]
    return int(almacen)


def digito_n(num, pos):
    """
    7. Función que devuelve el dígito que está en la posición n de un número entero.
    Se empieza contando por el 0 y de izquierda a derecha.

    Algoritmo
    Paso el número a una cadena y saco la posición indicada menos 1, para que empiece a contar desde 0.

    Variables
    num : Número indicado por el usuario (int, después str)
    pos : Posición indicada por el usuario (int)
    """
    num = str(num)
    return num[pos-1]


def posicion_de_digito(num, num_b):
    """
    8. Función que da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra,
    devuelve -1.

    Algoritmo
    Paso las variables a cadenas para poder recorrer los números con el bucle for
    Recorro el número y lo voy comparando con el número a buscar.
    Si lo encuentra, pongo la variable encontrado en True y devuelvo el valor de i
    Si se acaba el bucle y no lo encuentra, compruebo que no lo he encontrado y devuelvo -1

    Variables
    num : Número introducido por el usuario (primero int, después str)
    num_b : Número a buscar introducido por el usuario (primero int, después str)
    encontrado : Almacena si encuentra el número o no (boolean)
    """
    num = str(num)
    num_b = str(num_b)
    encontrado = False
    for i in range(0, len(num)):
        if num[i] == num_b:
            encontrado = True
            return i
    if not encontrado:
        return -1


def quita_por_detras(num, cantidad):
    """
    9. Función que le quita a un número n dígitos por detrás (por la derecha).

    Algoritmo
    Paso el número a cadena y creo una variable de tipo string vacía
    Con un bucle for, recorro el número desde la posición 0 hasta la que sea de la longitud total - la cantidad de
    números que quiero retirar. Voy guardando todos los dígitos en otra variable y al acabar devuelvo esa variable.

    Variables
    num : Número introducido por el usuario (int primero, después str)
    cantidad : Cantidad de dígitos a retirar (int)
    almacen : Aquí se van guardando los números que recorre el bucle (str primero, int después)
    """
    num = str(num)
    almacen = ""
    for i in range(0, (len(num)-cantidad)):
        almacen += num[i]
    return int(almacen)


def quita_por_delante(num, cantidad):
    """
    10. Función que le quita a un número n dígitos por delante (por la izquierda).

    Algoritmo
    Paso la número a str.
    Le doy la vuelta a al número con la función voltea que hice antes.
    Ahora le quito los números de la misma manera que antes (con la función anterior).
    Devuelvo el número volteado de nuevo para volver a su posición original.

    Variables
    num : Número introducido por el usuario (int primero, str después)
    almacen : Número volteado sin cortar (str)
    almacen2 : Número volteado cortado (str)
    """
    num = str(num)
    almacen = ""
    almacen2 = ""

    # Primero saco el número del revés
    almacen = voltea(num)

    # Invoco a la función anterior
    almacen2 = quita_por_detras(almacen, cantidad)

    return voltea(almacen2)


def pega_por_detras(num, digito):
    """
    11. Función que añade un dígito a un número por detrás.

    Algoritmo
    Paso tanto el número como el dígito a cadena
    Concateno las dos cadenas y las devuelvo como int

    Variables
    num : Número introducido por el usuario (int primero, str después)
    digito : Número a pegar por detrás (int primero, str después)
    """
    num = str(num)
    digito = str(digito)
    return int(num + digito)


def pega_por_delante(num, digito):
    """
    12. Función que añade un dígito a un número por delante.

    Algoritmo
    Paso tanto el número como el dígito a cadena
    Concateno las dos cadenas y las devuelvo como int

    Variables
    num : Número introducido por el usuario (int primero, str después)
    digito : Número a pegar por detrás (int primero, str después)
    """
    num = str(num)
    digito = str(digito)
    return int(digito + num)


def trozo_de_numero(numero, pos_i, pos_f):
    """
    13. Función que toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
    correspondiente.

    Algoritmo
    Paso el número a str
    Recorro el numero entre la posición inicial y la posición final, guardo los números en una variable
    Devuelvo la variable convertida a int

    Variables
    numero: Número introducido por el usuario (int primero, str después)
    pos_i : Posición inicial indicada por el usuario (int)
    pos_f : Posición final indicada por el usuario (int)
    almacen : Variable en la que guardo el trozo de número (str primero, int después)
    """
    numero = str(numero)
    almacen = ""

    for i in range(pos_i-1, pos_f):
        almacen += numero[i]

    return int(almacen)


def junta_numeros(num1, num2):
    """
    14. Función que pega dos números para formar uno.

    Algoritmo
    Paso los dos números a cadena
    Devuelvo la concatenación de los dos números pasada a int

    Variables
    num1 : Número 1 introducido por el usuario (int primero, str después)
    num2 : Número 2 introducido por el usuario (int primero, str después)
    """
    num1 = str(num1)
    num2 = str(num2)
    return int(num1 + num2)
