"""
Prueba de funciones de ej3.py
Programación Orientada a Objetos
"""

import ej3

# Testeamos funciones fecha correcta
fechas = ["20191215",  # correcto
          "20181111",  # correcto
          "dfdfdw",  # incorrecto
          "AAAAMMDD",  # incorrecto
          "20181242",  # incorrecto (diciembre no tiene 42 días)
          "20010229",  # incorrecto (no es bisiesto)
          "20000229"  # correcto (fue bisiesto)
          ]
for f in fechas:
    fec = ej3.Fecha(f)
    print(f"La fecha {f} tiene un formato ", end="")
    if fec.fecha_correcta():
        print("CORRECTO")
    else:
        print("INCORRECTO")
print()

# Testeamos suma y resta de días
fec1 = ej3.Fecha("20160228")
fec2 = ej3.Fecha("20160301")
fec3 = ej3.Fecha("20170228")
fec4 = ej3.Fecha("20170301")
print("Si sumamos un día a '" + fec1.fecha_formateada() + "' obtenemos: " +
fec1.fecha_mas_1dia()) # TODO: No consigo pasar de aqui, por lo que sea la función dia me recorta la fecha y en vez del día lee 'ec'.
print("Si restamos un día a '" + fec2.fecha_formateada() + "' obtenemos: " +
      fec2.fecha_menos_1dia())
print("Si sumamos un día a '" + fec3.fecha_formateada() + "' obtenemos: " +
      fec3.fecha_mas_1dia())
print("Si restamos un día a '" + fec4.fecha_formateada() + "' obtenemos: " +
      fec4.fecha_menos_1dia())
print()

suma = int(input("¿Cuantos días quieres sumar a " + fec1.fecha_formateada() + "? "))
print("La fecha resultante es " + fec1.fecha_mas_n_dias(suma))
print()

resta = int(input("¿Cuantos días quieres restar a " + fec1.fecha_formateada() + "? "))
print("La fecha resultante es " + fec1.fecha_menos_n_dias(resta))
print()
