"""

# TODO: Archivo para comprobaciones, falta porque aún no sé como aplicar las llamadas a los métodos del archivo hacia la
# TODO: clase... ¿Hago funciones en vez de métodos o hago métodos estáticos?


Colección de funciones para manejar fechas en cadenas de caracteres.

El formato de la cadena es: AAAAMMDD.
Ejemplo: El 15 de diciembre de 2019 sería: "20191215"

Colección de funciones:

1. fecha_correcta: dice si la fecha que se pasa como parámetro es correcta.

2. fecha_mas_1dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.

3. fecha_mas_ndias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.

4. fecha_menos_1dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.

5. fecha_menos_ndias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.

6. es_bisiesto: dice si la fecha que se pasa como parámetro es bisiesto.

7. compara_fechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
   segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.

8. fecha_formateada: recibe un fecha y devuelve una cadena con el formato:
   DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")

9. año, mes, dia, nombre_mes: recibe un fecha y devuelve esos valores.

Hay un script para hacer pruebas: test_fecha.py.

También vamos a hacer las pruebas usando el módulo doctest:
    python3 -m doctest fecha.py -v
    https://python-para-impacientes.blogspot.com/2019/03/probando-el-codigo-con-doctest.html
"""


class Fecha:
    def __init__(self, fecha):
        self.fecha = fecha

    def fecha_correcta(self):
        """
        Dice si la fecha que se pasa como parámetro es correcta.

        @param self
        @return verdadero o falso.

        Test:
        - fecha_correcta("20191215")
        True
        - fecha_correcta("20181111")
        True
        - fecha_correcta("dfdfdw")
        False
        - fecha_correcta("AAAAMMDD")
        False
        - fecha_correcta("20181242")  # diciembre no tiene 42 días
        False
        - fecha_correcta("20010229")  # es bisiesto
        False
        - fecha_correcta("20000229")  # fue bisiesto
        True
        """
        # tiene que tener longitud 8
        if len(self.fecha) != 8:
            return False
        # todos sus caracteres tienen que ser dígitos
        # podemos usar el método isdigit(), pero por motivos didácticos no lo uso
        for i in range(len(self.fecha)):
            c = self.fecha[i]
            if c < '0' or c > '9':
                return False
        # El mes tiene que estar entre 1 y 12
        mes_ = Fecha.mes(self.fecha)
        if mes_ < 1 or mes_ > 12:
            return False
        # Si es año bisiesto el nº de días de febrero es 29.
        # Llamo a una función que me actualiza el nº de días de febrero si es bisiesto
        dias_mes_este_anyo = Fecha.dias_mes_anyo(self.fecha)
        dia_ = Fecha.dia(self.fecha)
        # esta expresión lógica la permite python, equivale a:
        #   dia_>0 and dia_<=dias_mes_este_año[mes_-1]
        return 0 < dia_ <= dias_mes_este_anyo[mes_ - 1]  # restamos 1 al mes para que esté entre 0 y 11

    def fecha_mas_1dia(self):
        """
        Suma un día a la fecha que se pasa como parámetro y la devuelve.

        @param self
        @return nuevo fecha

        Test:
        - fecha_mas_1dia("20160228")
        '20160229'
        - fecha_mas_1dia("20170228")
        '20170301'
        """
        dia_ = Fecha.dia(self)
        mes_ = Fecha.mes(self.fecha)
        anyo_ = Fecha.anyo(self.fecha)
        dias_mes_este_anyo = Fecha.dias_mes_anyo(self.fecha)

        # aumentamos el día
        ultimo_dia_mes = dias_mes_este_anyo[mes_ - 1]
        dia_ += 1
        if dia_ > ultimo_dia_mes:  # mes siguiente si no es 29/2 y bisiesto
            # mes siguiente
            dia_ = 1
            mes_ += 1
            if mes_ > 12:  # nos pasamos de diciembre, año siguiente
                mes_ = 1
                anyo_ += 1
        return Fecha.fecha(dia_, mes_, anyo_)

    def fecha_mas_n_dias(self, dias_):
        """
        Suma una serie de días a la fecha que se pasa como parámetro y la devuelve.

        @param self
        @param dias_
        @return nueva fecha

        Test:
        - fecha_mas_n_dias("20160228", 5)
        '20160304'
        - fecha_mas_n_dias("20160228", -5)
        '20160223'
        """
        fecha2 = self
        if dias_ >= 0:
            for i in range(dias_):
                fecha2 = Fecha.fecha_mas_1dia(fecha2)
        else:
            for i in range(abs(dias_)):
                fecha2 = Fecha.fecha_menos_1dia(fecha2)
        return fecha2

    def fecha_menos_1dia(self):
        """
        Resta un día a la fecha que se pasa como parámetro y la devuelve.

        @param self
        @return nuevo fecha

        Test:
        - fecha_menos_1dia("20160301")
        '20160229'
        - fecha_menos_1dia("20170301")
        '20170228'
        """
        dia_ = Fecha.dia(self.fecha)
        mes_ = Fecha.mes(self.fecha)
        anyo_ = Fecha.anyo(self.fecha)
        dias_mes_este_anyo = Fecha.dias_mes_anyo(self.fecha)
        # disminuimos el día
        dia_ -= 1
        if dia_ == 0:  # mes anterior y último día de mes
            mes_ -= 1
            if mes_ == 0:  # 31 de diciembre del año anterior
                mes_ = 12
                anyo_ -= 1
            dia_ = dias_mes_este_anyo[mes_ - 1]  # último día del mes anterior
        return Fecha.fecha(dia_, mes_, anyo_)

    def fecha_menos_n_dias(self, dias_):
        """
        Resta una serie de días a la fecha que se pasa como parámetro y la devuelve.

        @param self
        @param dias_
        @return nuevo fecha

        Test:
        - fecha_menos_n_dias("20170301", 5)
        '20170224'
        - fecha_menos_n_dias("20170301", -5)
        '20170306'
        """
        fecha2 = self.fecha
        if dias_ >= 0:
            for i in range(dias_):
                fecha2 = Fecha.fecha_menos_1dia(fecha2)
        else:
            for i in range(abs(dias_)):
                fecha2 = Fecha.fecha_mas_1dia(fecha2)
        return fecha2

    def es_bisiesto(self):
        """
        Dice si la fecha que se pasa como parámetro es de un año bisiesto.

        @param self
        @return verdadero o falso

        Test:
        - es_bisiesto("20160108")
        True
        - es_bisiesto("20000101") # acaba en 00 pero es múltiplo de 400
        True
        - es_bisiesto("10112019")
        False
        - es_bisiesto("01021900") # múltiplo de 4 pero acaba en 00 y no es múltiplo de 400
        False
        """
        anyo_ = Fecha.anyo(self)
        return anyo_ % 4 == 0 and (anyo_ % 100 != 0 or anyo_ % 400 == 0)

    def compara_fechas(self, fecha2):
        """
        Recibe dos fechas y devuelve un valor negativo si la 1º es anterior a la 2º,
        cero si son iguales, y un valor positivo si la 1º es posterior a la segunda.

        @param self
        @param fecha2
        @return entero negativo, cero o un entero positivo.

        Test:
        - compara_fechas("20191231", "20191231")
        0
        - compara_fechas("20200106", "20200101") > 0
        True
        - compara_fechas("20200101", "20200106") < 0
        True
        """
        return int(self.fecha) - int(fecha2)

    def fecha_formateada(self):
        """
        Recibe un fecha y devuelve una cadena con el formato DD de {MES} de AAAA
        (Ejemplo: "15 de Diciembre de 2019")

        @param self
        @return fecha formateada

        Test:
        - fecha_formateada("20191215")
        '15 de Diciembre de 2019'
        """
        dia_ = Fecha.dia(self.fecha)
        anyo_ = Fecha.anyo(self.fecha)
        return str(dia_) + " de " + Fecha.nombre_mes(self.fecha) + " de " + str(anyo_)

    def anyo(self):
        """
        Devuelve el año de la fecha

        @param self
        @return año

        Test:
        - año("20200106")
        2020
        """
        return int(self[0:4])

    def mes(self):
        """
        Devuelve el mes de la

        @param self
        @return mes

        Test:
        - mes("20200106")
        1
        """
        return int(self[4:6])

    def nombre_mes(self):
        """
        Devuelve el nombre del mes de la fecha.

        @param self
        @return nombre del mes

        Test:
        - nombre_mes("20200106")
        'Enero'
        """
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                 "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        mes_ = Fecha.mes(self)
        return meses[mes_ - 1]

    def dia(self):
        """
        Devuelve el día de la fecha

        @param self
        @return día del mes

        Test:
        - dia("20200106")
        6
        """
        fechafuncion = str(self)[6:8]
        return int(fechafuncion)

    @staticmethod
    def fecha(d, m, a):
        """
        Devuelve una cadena en formato AAAAMMDD

        @param d, m, a

        Test:
        - fecha(6, 1, 2020)
        '20200106'
        """
        dia_ = str(d).strip()
        mes_ = str(m).strip()
        anyo_ = str(a).strip()
        # día
        if len(dia_) < 2:
            dia_ = "0" + dia_
        # mes
        if len(mes_) < 2:
            mes_ = "0" + mes_
        # año
        for i in range(len(anyo_), 4):
            anyo_ = "0" + anyo_
        return anyo_ + mes_ + dia_

    def dias_mes_anyo(self):
        """
        Esta función se usará para simplificar otras funciones que requieren saber
        el número de días de cada mes y se complican al tener en cuenta el 29 de febrero
        de los años bisiestos.

        @param self
        @return vector con los días de cada mes para el año de fecha_

        Test:
        - dias_mes_año("20200106")    # bisiesto
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        - dias_mes_año("20190102")    # no es bisiesto
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        """
        dias_mes_este_anyo = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(self):
            dias_mes_este_anyo[1] += 1  # hay 29 días en febrero en este caso
        return dias_mes_este_anyo
