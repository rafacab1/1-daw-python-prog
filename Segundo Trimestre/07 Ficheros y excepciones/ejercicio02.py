"""
2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también
pasamos como parámetro, de manera que:

    · Si el programa no recibe dos parámetros termina con un error 1.

    · Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.

    · Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
código 2.

    · Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje
de error y código 2.

    · Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.
"""

import sys
import string


def encripta(linea, desplaza):
    """
    Función encripta, lee cada caracter línea por línea y lo desplaza según el desplazamiento indicado.
    :param linea:
    :param desplaza:
    :return:
    """
    linea_encriptada = ""
    letras = string.ascii_letters + "áéíóúñÁÉÍÓÚÑ"
    for c in linea:
        if c in letras:
            pos_donde_esta = letras.index(c)
            pos_c_encriptado = (pos_donde_esta + desplaza) % len(letras)
            c_cifrado = letras[pos_c_encriptado]
        else:
            c_cifrado = c
        linea_encriptada += c_cifrado
    return linea_encriptada


# Si el número de parámetros es menor que dos, devuelve código de error 1.
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Número de parámetros incorrecto, saliendo...", file=sys.stderr)
    sys.exit(1)

no_cifrado = sys.argv[1]

# Si se pasa un sólo fichero como parámetro, se sobreescribe el fichero con el contenido.
if len(sys.argv) == 2:
    print("Sólo un fichero como parámetro, se sobreescribirá " + no_cifrado)
    input("Pulse Intro para aceptar o Ctrl+C para salir sin cambios...")
    cifrado = no_cifrado
else:
    cifrado = sys.argv[2]

# Manejador fichero sin cifrar
try:
    manejador_ncif = open(no_cifrado, "r")
except FileNotFoundError:
    print("Error, no ha sido posible abrir" + no_cifrado)
    sys.exit(2)

# Lee el contenido de no_cifrado y cierra el manejador
txt_sin_cifrar = manejador_ncif.readlines()
manejador_ncif.close()

# Manejador fichero cifrado
try:
    manejador_cif = open(cifrado, "w")
except PermissionError or FileNotFoundError:
    print("Error, no ha sido posible abrir" + cifrado)
    sys.exit(2)

# Encriptador
while True:
    try:
        desp = int(input("¿Que desplazamiento quieres usar para encriptar? "))
    except ValueError:
        print("Debes introducir un entero...")
    else:
        break

for i in txt_sin_cifrar:
    manejador_cif.write(encripta(i, desp))
manejador_cif.close()
