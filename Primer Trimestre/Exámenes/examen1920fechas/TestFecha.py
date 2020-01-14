from tiempo.Fecha import *

"""
*
  * Prueba funciones de Fecha.java.
  *
  * @author rafa
  *
"""

# Testeamos funciones fecha correcta
fechas = {"20191215",  # correcto
          "20181111",  # correcto
          "dfdfdw",  # incorrecto
          "AAAAMMDD",  # incorrecto
          "20181242",  # incorrecto (diciembre no tiene 42 días)
          "20010229",  # incorrecto (no es bisiesto)
          "20000229"  # correcto (fue bisiesto)
          }

for f in fechas:
    print(f"La fecha {f} tiene un formato ", end="")  # Original: print("La fecha " + f + " tiene un formato ",end="")
    if fecha_correcta(f):
        print("CORRECTO")
    else:
        print("INCORRECTO")

print()

# Testeamos suma y resta de días
fecha1 = "20160228"
fecha2 = "20160301"
fecha3 = "20170228"
fecha4 = "20170301"
print("Si sumamos un día a '" + fecha_formateada(fecha1) + "' obtenemos: " +
      fecha_mas1_dia(fecha1))
print("Si restamos un día a '" + fecha_formateada(fecha2) + "' obtenemos: " +
      fecha_menos1_dia(fecha2))
print("Si sumamos un día a '" + fecha_formateada(fecha3) + "' obtenemos: " +
      fecha_mas1_dia(fecha3))
print("Si restamos un día a '" + fecha_formateada(fecha4) + "' obtenemos: " +
      fecha_menos1_dia(fecha4))
print()

suma = int(input("¿Cuantos días quieres sumar a " + fecha_formateada(fecha1) + "? "))
print("La fecha resultante es " + fecha_mas_n_dias(fecha1, suma))
print()

resta = int(input("¿Cuantos días quieres restar a " + fecha_formateada(fecha1) + "? "))
print("La fecha resultante es " + fecha_menos_n_dias(fecha1, resta))
print()

# Testeamos comparaciones de fechas
fecha2 = "20160120"
fecha3 = "20190101"
print("El resultado de comparar " + fecha_formateada(fecha1) + " con " +
      fecha_formateada(fecha2) + " es " + str(compara_fechas(fecha1, fecha2)))
print("El resultado de comparar " + fecha_formateada(fecha1) + " con " +
      fecha_formateada(fecha3) + " es " + str(compara_fechas(fecha1, fecha3)))
print("El resultado de comparar " + fecha_formateada(fecha3) + " con " +
      fecha_formateada(fecha2) + " es " + str(compara_fechas(fecha3, fecha2)))
print("El resultado de comparar " + fecha_formateada(fecha3) + " con " +
      fecha_formateada(fecha3) + " es " + str(compara_fechas(fecha3, fecha3)))
