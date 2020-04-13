"""
Implementamos la clase fecha basándonos en 
https://github.com/rdelcastillo/DAW-Python/blob/master/Examenes/2019-20_trimestre1/tiempo/fecha.py
"""

class Fecha:
    def __init__(self, dia, mes, anyo):
        assert Fecha.es_correcta(dia, mes, anyo)
        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo

    ## Propiedades

    # Día
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        assert Fecha.es_correcta(value, self.__mes, self.__anyo)
        self.__dia = value

    # Mes
    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        assert Fecha.es_correcta(self.__dias, value, self.__anyo)
        self.__mes = value

    # Año
    @property
    def anyo(self):
        return self.__anyo
    
    @anyo.setter
    def anyo(self, value):
        assert Fecha.es_correcta(self.__dias, self.__mes, value)
        self.__anyo = value
        
    ## Métodos
    def nombre_mes(self):
        meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
        return meses[self.mes-1]

    def __suma_1dia(self):
        """
        :return: Fecha almacenada mas un día.
        """
        # Aumentamos el día
        dia = self.__dia + 1
        mes = self.__mes
        anyo = self.__anyo
        if dia > Fecha.dias_mes(mes, anyo): # Mes siguiente
            dia = 1
            mes += 1
            if mes > 12:  # nos pasamos de diciembre, año siguiente
                mes = 1
                anyo += 1
        return Fecha(dia, mes, anyo)

    
    def __resta_1dia(self):
        """
        :return: Fecha almacenada menos un día.
        """
        # Aumentamos el día
        dia = self.__dia - 1
        mes = self.__mes
        anyo = self.__anyo
        if dia == 0: # Mes anterior
            mes -= 1
            if mes == 0:  # nos pasamos de diciembre, año siguiente
                mes = 12
                anyo -= 1
            dia = Fecha.dias_mes(mes, anyo)
        return Fecha(dia, mes, anyo)

    ## Sobrecarga

    def __str__(self):
        return f"{self.__dia} de {self.nombre_mes()} de {self.__anyo}"

    def __add__(self, n):
        f = Fecha(self.__dia, self.__mes, self.__anyo)
        if n > 0:
            for i in range(n):
                f = f.__suma_1dia()
        else:
            for i in range(abs(n)):
                f = f.__suma_1dia()
        return f

    def __sub__(self, n):
        return self + -1*n

    def __radd__(self, n):
        return self + n     # También vale return self.__add(self, n)

    ## Métodos estáticos

    @staticmethod
    def es_bisiesto(anyo):
        return anyo % 400 == 0 or (anyo % 4 == 0 and anyo % 100 != 0)

    @staticmethod
    def es_correcta(dia, mes, anyo):
        # Tipo de dato correcto
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anyo, int):
            return False
        
        # Comprobar si el año es correcto
        if anyo < 0:
            return False
        
        # Comprobar si el mes es correcto
        if mes < 1 or mes > 12:
            return False

        # Comprobar si el día es correcto
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(anyo):
            dias_mes[1] = 29
        return dia > 0 and dia <= dias_mes[mes-1]

    @staticmethod
    def dias_mes(mes, anyo):
        """
        :return: Días del mes actual
        """
        dias_mes_ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(anyo):
            dias_mes_[1] = 29
        return dias_mes_[mes-1]