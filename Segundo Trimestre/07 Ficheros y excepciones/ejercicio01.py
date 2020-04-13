"""
1. Modifica el ejercicio 1 del tema anterior de manera que:

· El programa admita dos parámetros:

· El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la ciudad es errónea el programa
termina con un mensaje de error y código 2.

· El segundo es opcional, y si existe, es el directorio donde vamos a crear un fichero html con la información
formateada como una tabla del pronóstico de la temperatura, si no existe la información se muestra por pantalla.
Consideraciones:
este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo:
"Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html" si el fichero no se puede crear el programa termina con un
mensaje de error y código 3.

· Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de error (código 1) diciendo
que la sintaxis es incorrecta.

· Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto explicando qué hace.
"""

import os
import sys
import requests

