# -*- coding: utf-8 -*-


class Fraccion:
    """
    Clase Fraccion, se le pasa el numerador y denominador
    """

    def __init__(self, numerador, denominador):
        """
        Constructor

        :param numerador:
        :param denominador:
        """

        self.__numerador = 1
        self.__denominador = 1
        self.numerador = numerador
        self.denominador = denominador

    # Obtener y modificar numerador y denominador. No se puede dividir por cero.
    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, value):
        self.__numerador = value

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, value):
        if value == 0:
            print("ERROR: El denominador no puede ser 0.")
        else:
            self.__denominador = value

    # Obtener la fracción como cadena de caracteres.
    def a_cadena(self):
        """
        Pasa a cadena la fracción
        :return:
        """
        return f"El numerador es {self.numerador} y el denominador es {self.denominador}"

    # Obtener resultado de la fracción (número real)
    def resultado(self):
        """
        Divide numerador entre denominador
        :return:
        """
        return self.__numerador/self.__denominador

    # Multiplicar la fracción por un número
    def multiplica_num(self, numero):
        """
        Multiplica la fracción por un número
        :param numero:
        :return:
        """
        self.numerador = self.__numerador * numero
        return self.__numerador, self.__denominador

    # Multiplicar, sumar y restar fracciones
    # Multiplicar fracciones
    def multiplica(self, frac):
        """
        Multiplica la fracción por otra fracción
        :param frac:
        :return:
        """
        self.numerador = self.__numerador * frac.__numerador
        self.denominador = self.__denominador * frac.__denominador
        return self.__numerador, self.__denominador

    # Sumar fracciones
    def sumar(self, frac):
        """
        Suma dos fracciones
        :param frac:
        :return:
        """
        if self.__denominador == frac.denominador:
            self.numerador = self.__numerador+frac.__numerador
            return self.__numerador, self.__denominador
        else:
            self.numerador = (self.__numerador*frac.__denominador)+(self.__denominador*frac.__numerador)
            self.denominador = self.__denominador * frac.__denominador
            return self.__numerador, self.__denominador

    # Restar fracciones
    def resta(self, frac):
        """
        Resta dos fracciones
        :param frac:
        :return:
        """
        if self.__denominador == frac.denominador:
            self.numerador = self.__numerador - frac.__numerador
            return self.__numerador, self.__denominador
        else:
            self.numerador = (self.__numerador * frac.__denominador) - (self.__denominador * frac.__numerador)
            self.denominador = self.__denominador * frac.__denominador
            return self.__numerador, self.__denominador

    # Simplificar la fracción
    def simplifica(self):
        """
        Algoritmo
        En un bucle, mientras que "simplificado" sea falso, compruebo lo siguiente...
            variable a 2
            Si el resto del numerador entre "variable" es 0 y el resto del denominador entre "variable" también es 0
                Divido numerador entre "variable", y denominador también lo divido entre variable"
                Pongo "variable" a 2
            Si no, incremento variable en 1
            Si "variable" es mayor que 600, pongo "simplificado" como verdadero
        :return:
        """
        simplificado = False
        variable = 2
        while not simplificado:
            if self.__numerador % variable == 0 and self.__denominador % variable == 0:
                self.__numerador = self.__numerador / variable
                self.__denominador = self.__denominador / variable
                variable = 2
            else:
                variable += 1
            if variable > 600:
                simplificado = True

        return self.__numerador, self.__denominador


if __name__ == "__main__":
    f = Fraccion(42, 68)

    # Obtener numerador y denominador
    print(f.numerador)
    print(f.denominador)
    # Modificar numerador y denominador
    numeradormod = int(input("\nIntroduce un nuevo numerador: "))
    denominadormod = int(input("Introduce un nuevo denominador: "))

    # Obtener la fracción como cadena de caracteres.
    print(f.a_cadena())

    # Obtener resultado de la fracción
    print(f"El resultado de la fracción es {f.resultado()}")

    # Multiplicar la fracción por un número
    n_multiplicar = int(input("\nIntroduce un número por el que multiplicar la fracción: "))
    f.multiplica_num(n_multiplicar)
    print(f.a_cadena())

    # Multiplicar, sumar y restar fracciones
    f2 = Fraccion(62, 58)
    print(f"Segunda fracción: {f2.a_cadena()}")
    # Multiplicar fracciones
    f.multiplica(f2)
    print("\nFracciones multiplicadas: ")
    print(f.a_cadena())
    # Sumar fracciones
    f.sumar(f2)
    print("\nFracciones sumadas: ")
    print(f.a_cadena())
    # Restar fracciones
    f.resta(f2)
    print("\nFracciones restadas: ")
    print(f.a_cadena())

    # Simplificar la fracción
    f.simplifica()
    print("\nFracción simplificada: ")
    print(f.a_cadena())
