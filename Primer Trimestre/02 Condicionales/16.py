# 16. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, 
# el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos 
# cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos,
# y a partir del décimo minuto, 50 céntimos. 
#
# Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. 
# Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pido el tiempo de la llamada
# Pregunto si la llamada fue en domingo
# Pregunto si fue por la mañana o por la tarde
# Hago las sentencias:
#   Si duró menos de 5 minutos multiplico los minutos por 1
#   Si duró 8 o menos minutos, multiplico los minutos - 5 * 0.80 y le sumo los 5€
#   Si duró 10 minutos o menos, multiplico los minutos - 8 * 0.70 y le sumo los 5€ y 2,4€
#   Si duró mas de 10 minutos, multiplico los minutos - 10 * 0.50 y le sumo los 5€ + 2,4€ + 1,4€
# En cualquier caso, valoro si fue domingo, si no, valoro si fue por la mañana, si no, valoro si fue por la tarde, y si tampoco, dará error.
# Y en estos casos, muestro por pantalla el precio base, el porcentaje del impuesto correspondiente y el total.
#
# Variables
# tiempo = Tiempo de la llamada en minutos (float)
# domingo = Indica si la llamada fue un domingo (str)
# horario = Indica si es turno de mañana o de tarde (str)
# t5 = Cuando el tiempo es hasta 5 minutos (float)
# t8 = Cuando el tiempo es hasta 8 minutos (float)
# t10 = Cuando el tiempo es hasta 10 minutos (float)
# t = Cuando el tiempo es de mas de 10 minutos (float)

print("Programa que calcula el precio de una llamada telefónica.\n")

# Pido el tiempo, si fue domingo, y si no lo es, el horario
tiempo = float(input("¿Cuánto duró la llamada? (Minutos) "))
domingo = input("\n¿Esa llamada se hizo un domingo? [S/n] ")
if domingo.lower() == "n":
    horario = input("\n¿Fue por la tarde o por la mañana? [M/t] ")

# Hago las sentencias
if tiempo <= 5:
    t5 = tiempo * 1
    if domingo.lower() == "s":
        print(f"\nPrecio base: {round(t5, 2)}€")
        print(f"Impuesto por llamada en domingo: {round(((t5 / 100) * 3), 2)}€")
        print(f"El precio total de la llamada es de {round(t5 + ((t5 / 100) * 3), 2)}€")
    elif horario.lower() == "m":
        print(f"\nPrecio base: {round(t5, 2)}€")
        print(f"Impuesto por llamada en horario de mañana: {round(((t5 / 100) * 15), 2)}€")
        print(f"El precio total de la llamada es de {round(t5 + ((t5 / 100) * 15), 2)}€")
    elif horario.lower() == "t":
        print(f"\nPrecio base: {round(t5, 2)}€")
        print(f"Impuesto por llamada en horario de tarde: {round(((t5 / 100) * 10), 2)}€")
        print(f"El precio total de la llamada es de {round(t5 + ((t5 / 100) * 10), 2)}€")
    else:
        print("Ha ocurrido un error.")
elif tiempo <= 8:
    t8 = ((tiempo - 5) * 0.80) + 5
    if domingo.lower() == "s":
        print(f"\nPrecio base: {round(t8, 2)}€")
        print(f"Impuesto por llamada en domingo: {round(((t8 / 100) * 3), 2)}€")
        print(f"El precio total de la llamada es de {round(t8 + ((t8 / 100) * 3), 2)}€")
    elif horario.lower() == "m":
        print(f"\nPrecio base: {round(t8, 2)}€")
        print(f"Impuesto por llamada en horario de mañana: {round(((t8 / 100) * 15), 2)}€")
        print(f"El precio total de la llamada es de {round(t8 + ((t8 / 100) * 15), 2)}€")
    elif horario.lower() == "t":
        print(f"\nPrecio base: {round(t8, 2)}€")
        print(f"Impuesto por llamada en horario de tarde: {round(((t8 / 100) * 10), 2)}€")
        print(f"El precio total de la llamada es de {round(t8 + ((t8 / 100) * 10), 2)}€")
    else:
        print("Ha ocurrido un error.")
elif tiempo <= 10:
    t10 = ((tiempo - 8) * 0.70) + 5 + 2.4
    if domingo.lower() == "s":
        print(f"\nPrecio base: {round(t10, 2)}€")
        print(f"Impuesto por llamada en domingo: {round(((t10 / 100) * 3), 2)}€")
        print(f"El precio total de la llamada es de {round(t10 + ((t10 / 100) * 3), 2)}€")
    elif horario.lower() == "m":
        print(f"\nPrecio base: {round(t10, 2)}€")
        print(f"Impuesto por llamada en horario de mañana: {round(((t10 / 100) * 15), 2)}€")
        print(f"El precio total de la llamada es de {round(t10 + ((t10 / 100) * 15), 2)}€")
    elif horario.lower() == "t":
        print(f"\nPrecio base: {round(t10, 2)}€")
        print(f"Impuesto por llamada en horario de tarde: {round(((t10 / 100) * 10), 2)}€")
        print(f"El precio total de la llamada es de {round(t10 + ((t10 / 100) * 10), 2)}€")
    else:
        print("Ha ocurrido un error.")
elif tiempo > 10:
    t = ((tiempo - 10) * 0.50) + 5 + 2.4 + 1.4
    if domingo.lower() == "s":
        print(f"\nPrecio base: {round(t, 2)}€")
        print(f"Impuesto por llamada en domingo: {round(((t / 100) * 3), 2)}€")
        print(f"El precio total de la llamada es de {round(t + ((t / 100) * 3), 2)}€")
    elif horario.lower() == "m":
        print(f"\nPrecio base: {round(t, 2)}€")
        print(f"Impuesto por llamada en horario de mañana: {round(((t / 100) * 15), 2)}€")
        print(f"El precio total de la llamada es de {round(t + ((t / 100) * 15), 2)}€")
    elif horario.lower() == "t":
        print(f"\nPrecio base: {round(t, 2)}€")
        print(f"Impuesto por llamada en horario de tarde: {round(((t / 100) * 10), 2)}€")
        print(f"El precio total de la llamada es de {round(t + ((t / 100) * 10), 2)}€")
    else:
        print("Ha ocurrido un error.")
else:
    print("Ha ocurrido un error.")