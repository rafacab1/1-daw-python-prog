# -*- coding: utf-8 -*-

"""
Colección de funciones para manejar fechas en cadenas de caracteres.

El formato de la cadena es: AAAAMMDD.
Ejemplo: El 15 de diciembre de 2019 sería: "20191215"

Colección de funciones:

1. fechaCorrecta: dice si la fecha que se pasa como parámetro es correcta.

2. fechaMas1Dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.

3. fechaMasNDias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.

4. fechaMenos1Dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.

5. fechaMenosNDias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.

6. esBisiesto: dice si la fecha que se pasa como parámetro es bisiesto.

7. comparaFechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
    segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.

8. fechaFormateada: recibe un fecha y devuelve una cadena con el formato:
    DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")

9. anyo, mes, dia, nombreMes: recibe un fecha y devuelve esos valores.

@author Rafa C.

"""

"""
Dice si la fecha que se pasa como parámetro es correcta.
 
Algoritmo
Miro todos los carácteres de la cadena y miro si son dígitos
Miro las cuatro primeras posiciones (0, 1, 2, 3) de la fecha, si son un número entre 0001 y 2999 guardo en una 
variable que el año es correcto.
Miro las dos siguientes posiciones (4, 5), si es un número entre 01 y 12, guardo en una variable que el mes es 
correcto.
Miro las dos siguientes posiciones (6, 7), si es un número entre 01 y 31, guardo en una variable que el día es 
correcto.
 
Si las tres condiciones anteriores son verdaderas, paso a comprobar si ese día está en ese mes.
Para ello, hago condiciones "si el mes es 01, y el día es 31, devuelvo verdadero".
 

@param fecha
@return verdadero o falso.
"""


def fecha_correcta(fecha):

    if len(fecha) != 8:
        return False
    else:
        y1 = fecha[0]
        y2 = fecha[1]
        y3 = fecha[2]
        y4 = fecha[3]
        m1 = fecha[4]
        m2 = fecha[5]
        d1 = fecha[6]
        d2 = fecha[7]

        if not y1.isdigit():
            return False
        if not y2.isdigit():
            return False
        if not y3.isdigit():
            return False
        if not y4.isdigit():
            return False
        if not m1.isdigit():
            return False
        if not m2.isdigit():
            return False
        if not d1.isdigit():
            return False
        if not d2.isdigit():
            return False

        # Compruebo si el año es correcto
        if obten_anyo(fecha) >= 1 and obten_anyo(fecha) <= 2999:
            anyocorrecto = True
        else:
            anyocorrecto = False
        # Compruebo si el mes es correcto
        if obten_mes(fecha) >= 1 and obten_mes(fecha) <= 12:
            mescorrecto = True
        else:
            mescorrecto = False
        # Compruebo si el día está comprendido entre 01 y 31
        if obten_dia(fecha) >= 1 and obten_dia(fecha) <= 31:
            dia131 = True
        else:
            dia131 = False
        # Miro si las tres condiciones anteriores son verdaderas, si no lo son, devuelvo falso
        if not anyocorrecto or not mescorrecto or not dia131:
            return False

        if obten_mes(fecha) == 1 and obten_dia(fecha) <= 31:  # Enero
            return True
        if obten_mes(fecha) == 2 and obten_dia(fecha) <= 29 and es_bisiesto(fecha):  # Febrero bisiesto
            return True
        elif obten_mes(fecha) == 2 and obten_dia(fecha) <= 28:  # Febrero no bisiesto
            return True
        if obten_mes(fecha) == 3 and obten_dia(fecha) <= 31:  # Marzo
            return True
        if obten_mes(fecha) == 4 and obten_dia(fecha) <= 30:  # Abril
            return True
        if obten_mes(fecha) == 5 and obten_dia(fecha) <= 31:  # Mayo
            return True
        if obten_mes(fecha) == 6 and obten_dia(fecha) <= 30:  # Junio
            return True
        if obten_mes(fecha) == 7 and obten_dia(fecha) <= 31:  # Julio
            return True
        if obten_mes(fecha) == 8 and obten_dia(fecha) <= 31:  # Agosto
            return True
        if obten_mes(fecha) == 9 and obten_dia(fecha) <= 30:  # Septiembre
            return True
        if obten_mes(fecha) == 10 and obten_dia(fecha) <= 31:  # Septiembre
            return True
        if obten_mes(fecha) == 11 and obten_dia(fecha) <= 30:  # Noviembre
            return True
        if obten_mes(fecha) == 12 and obten_dia(fecha) <= 31:  # Diciembre
            return True
    return False


"""
Suma un día a la fecha que se pasa como parámetro y la devuelve.
 
 
Le sumo uno al día, pero:
Si el día es el último de ese mes, pongo el día a 1 y le sumo 1 al mes, pero también tengo que tener en 
cuenta los bisiestos, que los compruebo antes
y en caso de que fuese bisiesto con una variable booleana controlo que no se vuelva a sumar.

@param fecha
@return nuevo fecha
"""


def fecha_mas1_dia(fecha):
    dia = obten_dia(fecha)
    mes = obten_mes(fecha)
    anyo = obten_anyo(fecha)
    sumado = False
    limites = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and dia == 28 and es_bisiesto(fecha):  # En caso de que sea bisiesto lo hago a parte.
        dia += 1
        sumado = True
    if mes == 12 and dia == 31 and not sumado:  # En caso de que sea 31 de diciembre, también tengo que modificar el año
        dia = 1
        mes = 1
        anyo += 1
        sumado = True
    if dia == limites[mes - 1] and not sumado:  # Si ni es bisiesto ni es 31 de diciembre pero el día es el último...
        dia = 1
        mes += 1
        sumado = True
    if not sumado:  # Si no se ha dado ninguno de los casos anteriores, simplemente sumo un día.
        dia += 1

    return obten_fecha(dia, mes, anyo)


"""
Suma una serie de días a la fecha que se pasa como parámetro y la devuelve.
 
Algoritmo, en un bucle mientras que mi contador sea menor que los días a sumar...
Le voy sumando 1 a los días (hasta n)
Una vez le sume uno, compruebo si el día por el que voy equivale a su último día, que en ese caso pongo el 
día a 1 y le sumo uno al mes, y sigo sumando
En la condición anterior, también tengo que evaluar si la fecha es un 28 de febrero de un año bisiesto y si 
es 31 de diciembre

@param fecha
@param dias
@return nueva fecha
"""


def fecha_mas_n_dias(fecha, dias):
    dia = obten_dia(fecha)
    mes = obten_mes(fecha)
    anyo = obten_anyo(fecha)
    contador = 1
    sumado = False
    limites = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while contador <= dias:
        if mes == 2 and dia == 28 and es_bisiesto(fecha):  # En caso de que sea bisiesto lo hago a parte.
            dia += 1
            sumado = True
        if mes == 12 and dia == 31:  # En caso de que sea 31 de diciembre, también tengo que modificar el año
            dia = 1
            mes = 1
            anyo += 1
            sumado = True
        if dia == limites[mes - 1] or (
                dia == 29 and mes == 2):  # Si no es nada de lo anterior pero el día es el último del mes...
            dia = 1
            mes += 1
            sumado = True
        if not sumado:  # Si no se ha dado ninguno de los casos anteriores, simplemente sumo un día.
            dia += 1
        contador += 1
        sumado = False

    return obten_fecha(dia, mes, anyo)


"""
Resta un día a la fecha que se pasa como parámetro y la devuelve.
 
 
Le resta uno al día, pero si el día es 1 le resto uno al mes y pongo el día al último día del mes anterior.
También controlo los años bisiestos, en ese caso pongo el día a 29 en vez de 28 que vendría en el array con 
todos los límites.
También tengo en cuenta el 1 de enero, en este caso pondría el día a 31, el mes a 12 y le restaría uno al 
año.

@param fecha
@return nuevo fecha
"""


def fecha_menos1_dia(fecha):
    dia = obten_dia(fecha)
    mes = obten_mes(fecha)
    anyo = obten_anyo(fecha)
    restado = False
    limites = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 3 and dia == 1 and es_bisiesto(fecha):  # En el caso de que sea bisiesto
        mes -= 1
        dia = 29
        restado = True
    if dia == 1 and mes == 1 and not restado:  # En el caso de que sea uno de enero
        dia = 31
        mes = 12
        anyo -= 1
    if dia == 1 and not restado:  # En el caso de que sea día 1
        dia = limites[mes - 2]
        mes -= 1
        restado = True
    if not restado:  # Si no se cumple ninguno de los casos anteriores...
        dia -= 1

    return obten_fecha(dia, mes, anyo)


"""
Resta una serie de días a la fecha que se pasa como parámetro y la devuelve.
 
En un bucle mientras mi contador sea menor que los días a restar...
Compruebo, si ĺa fecha es un 1 de marzo de un año bisiesto, pongo le resto uno al mes y pongo el día a 29.
Si la fecha es un 1 de enero, pongo el mes a 12, el día a el límite de diciembre y le resto uno al año.
Si el día es simplemente 1, le resto uno al mes y pongo el día a el límite del mes anterior.
Si no se cumple nada de lo anterior, simplemente resto.

@param fecha
@param dias
@return nuevo fecha
"""


def fecha_menos_n_dias(fecha, dias):
    dia = obten_dia(fecha)
    mes = obten_mes(fecha)
    anyo = obten_anyo(fecha)
    contador = 1
    restado = False
    limites = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while contador <= dias:
        if mes == 3 and dia == 1 and es_bisiesto(fecha):  # En caso de que sea bisiesto lo hago a parte.
            dia = 29
            mes -= 1
            restado = True
        if mes == 1 and dia == 1:  # En caso de que sea 1 de enero, también tengo que modificar el año
            dia = 31
            mes = 12
            anyo -= 1
            restado = True
        if dia == 1:  # Si el día es 1, tengo que ir al mes anterior
            dia = limites[mes - 2]
            mes -= 1
            restado = True
        if not restado:  # Si no se ha dado ninguno de los casos anteriores, simplemente resto un día.
            dia -= 1
        contador += 1
        restado = False
    return obten_fecha(dia, mes, anyo)


"""
Dice si la fecha que se pasa como parámetro es de un año bisiesto.
 
Un año es bisiesto cuando es multiplo de 4 excepto multiplo de 100 que sólo lo será si a su vez es múltiplo 
de 400.
 
Algoritmo
Si el resto del año entre 4, es 0...
   Si lo es, compruebo si es divisible entre 100.
         Si lo es, compruebo si es divisible entre 400
           Si no lo es, no es bisiesto.  
         Si no lo es, es bisiesto.
   Si no lo es, no es bisiesto.       

@param fecha
@return verdadero o falso
"""


def es_bisiesto(fecha):
    year = obten_anyo(fecha)
    bisiesto = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                bisiesto = True  # Este es el caso de que sea múltiplo de 4, de 100 y de 400.
        else:
            bisiesto = True  # Este es el caso de que sea múltiplo de 4 y no de 100
    return bisiesto


"""
Recibe dos fechas y devuelve un valor negativo si la 1º es anterior a la 2º,
cero si son iguales, y un valor positivo si la 1º es posterior a la segunda.

Algoritmo
Si el año 1 es menor al año 2, -1
 Si no, si el año 1 es mayor que el año 2, 1
 Si tampoco se da ese caso, es que son iguales, entonces empiezo a considerar los meses
   Si el mes 1 es menor al mes 2, -1
     Si no, si el mes 1 es mayor que el mes 2, 1
     Si tampoco se da este caso, tanto los años como los meses son iguales, entonces empiezo ya a considerar
    los días
       Si el día 1 es menor que el día 2, -1
       Si el día 1 es mayor que el día 2, 1
       Si no se da ninguno de estos casos, es que las dos fechas son iguales, 0.
    
@param fecha1
@param fecha2
@return entero negativo, cero o un entero positivo.
"""


def compara_fechas(fecha1, fecha2):
    dia1 = obten_dia(fecha1)
    mes1 = obten_mes(fecha1)
    anyo1 = obten_anyo(fecha1)
    dia2 = obten_dia(fecha2)
    mes2 = obten_mes(fecha2)
    anyo2 = obten_anyo(fecha2)

    resultado = 2

    if anyo1 < anyo2:
        resultado = -1
    elif anyo1 > anyo2:
        resultado = 1
    elif anyo1 == anyo2:
        if mes1 < mes2:
            resultado = -1
        elif mes1 > mes2:
            resultado = 1
        elif mes1 == mes2:
            if dia1 < dia2:
                resultado = -1
            elif dia1 > dia2:
                resultado = 1
            else:
                resultado = 0
    return resultado


"""       
Recibe un fecha y devuelve una cadena con el formato DD de {MES} de AAAA
(Ejemplo: "15 de Diciembre de 2019")

Algoritmo
Obtengo el dia, el nombre del mes y el año y lo meto todo en una cadena

@param fecha
@return fecha formateada
"""


def fecha_formateada(fecha):
    dia = str(obten_dia(fecha))
    mes = str(nombre_mes(fecha))
    anyo = str(obten_anyo(fecha))

    cadena = dia + ' de ' + mes + ' de ' + anyo

    return cadena


"""
Devuelve el año de la fecha.

Algoritmo
Saco de la cadena de la posición 0 a la 3, que debería corresponder al año.

@param fecha
@return
"""


def obten_anyo(fecha):
    anyo = int(fecha[0:4])
    return anyo


"""
Devuelve el nombre del mes de la fecha.

Algoritmo
Si el mes es 01, es enero, y así con todos los meses

@param fecha
@return nombre del mes
"""


def nombre_mes(fecha):
    n_mes = ""

    if obten_mes(fecha) == 1:
        n_mes = "enero"
    elif obten_mes(fecha) == 2:
        n_mes = "febrero"
    elif obten_mes(fecha) == 3:
        n_mes = "marzo"
    elif obten_mes(fecha) == 4:
        n_mes = "abril"
    elif obten_mes(fecha) == 5:
        n_mes = "mayo"
    elif obten_mes(fecha) == 6:
        n_mes = "junio"
    elif obten_mes(fecha) == 7:
        n_mes = "julio"
    elif obten_mes(fecha) == 8:
        n_mes = "agosto"
    elif obten_mes(fecha) == 9:
        n_mes = "septiembre"
    elif obten_mes(fecha) == 10:
        n_mes = "octubre"
    elif obten_mes(fecha) == 11:
        n_mes = "noviembre"
    elif obten_mes(fecha) == 12:
        n_mes = "diciembre"
    return n_mes


"""
Devuelve el mes de la fecha.

Algoritmo
Saco de la cadena de la posición 4 a 6, que debería corresponder al mes.

@param fecha
@return 
"""


def obten_mes(fecha):
    mes = int(fecha[4:6])
    return mes


"""
Devuelve el día de la fecha.

Algoritmo
Saco de la cadena de la posición 6 a 8, que debería corresponder al día.

@param fecha
@return
"""


def obten_dia(fecha):
    dia = int(fecha[6:8])
    return dia


"""
Devuelve una cadena en formato AAAAMMDD

@param d día del mes
@param m día del año
@param a año
@return
"""


def obten_fecha(d, m, a):
    dia = str(d).strip()
    mes = str(m).strip()
    anyo = str(a).strip()
    # día
    if len(dia) < 2:
        dia = "0" + dia
    # mes
    if len(mes) < 2:
        mes = "0" + mes
    # año
    for i in range(len(anyo), 4):
        anyo = "0" + anyo
    return anyo + mes + dia
