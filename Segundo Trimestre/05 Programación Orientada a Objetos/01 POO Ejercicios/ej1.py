# -*- coding: utf-8 -*-
# Fichero ej1test.py para comprobar los métodos


class Tiempo:
    """
    Clase tiempo, los parámetros que se le pasan son las horas, minutos y los segundos.
    """

    def __init__(self, horas, minutos, segundos):
        """
        Constructor.
        :param horas:
        :param minutos:
        :param segundos:
        """
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def pasa_segs(self):
        """
        Simplemente pasa horas, minutos y segundos a segundos. (Este método no se pedía, pero vi bien usarlo para
        otros métodos)
        :return: segundos
        """
        segundos = self.horas * 3600
        segundos += self.minutos * 60
        segundos += self.segundos

        return segundos

    @staticmethod
    def static_pasa_segs(horasf, minutosf, segundosf):
        """
        Método estático para pasar a segundos los parámetros de los métodos sumar y restar. (Este método no se pedía,
        pero vi bien usarlo para otros métodos)
        :param horasf:
        :param minutosf:
        :param segundosf:
        :return: segundos
        """
        segundos = horasf * 3600
        segundos += minutosf * 60
        segundos += segundosf

        return segundos

    # Crea métodos para:
    # Sumar y restar otro objeto de la clase Tiempo.

    def suma_tiempos(self, t2):
        """
        Pasa las horas, minutos y segundos a segundos, los suma, y los vuelve a pasar a horas, minutos y segundos.
        :param t2: segundo tiempo
        :return: horas, minutos, segundos
        """
        # Paso las horas, minutos y segundos a segundos
        segundos1 = self.pasa_segs()
        segundos2 = t2.pasa_segs()

        # En este momento, tenemos los dos tiempos en segundos

        # Sumo los segundos de los dos tiempos
        segundos_t = segundos1 + segundos2

        # Paso los segundos a horas, minutos, segundos.
        self.horas = int(segundos_t/3600)
        self.minutos = int((segundos_t-(self.horas*3600))/60)
        self.segundos = segundos_t-((self.horas*3600)+(self.minutos*60))

        return self.horas, self.minutos, self.segundos

    def resta_tiempos(self, t2):
        """
        Pasa las horas, minutos y segundos a segundos, los resta, y los vuelve a pasar a horas, minutos y segundos.
        :param t2: segundo tiempo
        :return: horas, minutos, segundos
        """
        # Paso las horas, minutos y segundos a segundos
        segundos1 = self.pasa_segs()
        segundos2 = t2.pasa_segs()

        # En este momento, tenemos los dos tiempos en segundos

        # Resto los segundos de los dos tiempos
        segundos_t = segundos1 - segundos2

        # Paso los segundos a horas, minutos, segundos.
        self.horas = int(segundos_t/3600)
        self.minutos = int((segundos_t-(self.horas*3600))/60)
        self.segundos = segundos_t-((self.horas*3600)+(self.minutos*60))

        return self.horas, self.minutos, self.segundos

    # Crea métodos para:
    # Sumar y restar segundos, minutos y/o horas.
    def sumar(self, hrs, mins, segs):
        """
        Suma el objeto y horas, minutos y segundos pasados como parámetros
        :param hrs:
        :param mins:
        :param segs:
        :return:
        """
        # Paso a segundos
        segundos1 = self.pasa_segs()
        segundos2 = self.static_pasa_segs(hrs, mins, segs)

        # Sumo ambas variables
        segundos_t = segundos1 + segundos2

        # Paso los segundos a horas, minutos, segundos.
        self.horas = int(segundos_t/3600)
        self.minutos = int((segundos_t-(self.horas*3600))/60)
        self.segundos = segundos_t-((self.horas*3600)+(self.minutos*60))

        return self.horas, self.minutos, self.segundos

    def restar(self, hrs, mins, segs):
        """
        Resta el objeto y horas, minutos y segundos pasados como parámetros
        :param hrs:
        :param mins:
        :param segs:
        :return:
        """
        # Paso a segundos
        segundos1 = self.pasa_segs()
        segundos2 = self.static_pasa_segs(hrs, mins, segs)

        # Sumo ambas variables
        segundos_t = segundos1 - segundos2

        # Paso los segundos a horas, minutos, segundos.
        self.horas = int(segundos_t/3600)
        self.minutos = int((segundos_t-(self.horas*3600))/60)
        self.segundos = segundos_t-((self.horas*3600)+(self.minutos*60))

        return self.horas, self.minutos, self.segundos

    # Crea métodos para:
    # Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

    def tiempoalm(self):
        """
        Función que devuelve el tiempo formateado
        :return: por ejemplo, "10h 35m 5s"
        """
        return str(self.horas) + "h " + str(self.minutos) + "m " + str(self.segundos) + "s"
