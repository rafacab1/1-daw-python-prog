"""
3. Haz un programa que reciba como parámetro un fichero encriptado con el método César y y almacene el resultado en
otro, que también pasamos como parámetro, de manera que:

    · Si el programa no recibe dos parámetros termina con un error 1.

    · Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
    antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.

    · Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
    código 2.

    · Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje
     de error y código 2.

    · Para desencriptar necesitas una clave que debes pedir al usuario.

    · ¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave? Coméntala, y si te atreves...
    ¡impleméntala!
"""
import sys
import string

# Código reutilizado del ejercicio anterior (modificado)


def desencripta(linea, desplaza):
    """
    Función desencripta, lee cada caracter línea por línea y lo reemplaza según el desplazamiento indicado.
    :param linea:
    :param desplaza:
    :return:
    """
    linea_encriptada = ""
    letras = string.ascii_letters + "áéíóúñÁÉÍÓÚÑ"
    for c in linea:
        if c in letras:
            pos_donde_esta = letras.index(c)
            pos_c_desencriptado = (pos_donde_esta - desplaza) % len(letras)
            if pos_c_desencriptado < 0:
                pos_c_desencriptado = len(letras) + pos_c_desencriptado
            c_descifrada = letras[pos_c_desencriptado]
            linea_encriptada += c_descifrada
    return linea_encriptada


# Si el número de parámetros es menor que dos, devuelve código de error 1.
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("Número de parámetros incorrecto, saliendo...", file=sys.stderr)
    sys.exit(1)

cifrado = sys.argv[1]

# Si se pasa un sólo fichero como parámetro, se sobreescribe el fichero con el contenido.
if len(sys.argv) == 2:
    print("Sólo un fichero como parámetro, se sobreescribirá " + cifrado)
    input("Pulse Intro para aceptar o Ctrl+C para salir sin cambios...")
    no_cifrado = cifrado
else:
    no_cifrado = sys.argv[2]

# Manejador fichero cifrado (a leer)
try:
    manejador_cif = open(cifrado, "r")
except FileNotFoundError:
    print("Error, no ha sido posible abrir" + cifrado)
    sys.exit(2)

# Lee el contenido de cifrado y cierra el manejador
txt_cifrado = manejador_cif.readlines()
manejador_cif.close()

# Manejador fichero no cifrado (a escribir)
try:
    manejador_nocif = open(no_cifrado, "w")
except PermissionError or FileNotFoundError:
    print("Error, no ha sido posible abrir" + no_cifrado)
    sys.exit(2)

# Desencriptador
while True:
    try:
        desp = int(input("¿Que desplazamiento quieres usar para desencriptar? "))
    except ValueError:
        print("Debes introducir un entero...")
    else:
        break

for i in txt_cifrado:
    manejador_nocif.write(desencripta(i, desp))
manejador_nocif.close()
