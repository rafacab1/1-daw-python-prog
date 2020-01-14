# 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las 
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta
# su sueldo base y comisiones.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido el salario base.
# Calculo la comisión, el 10% del salario base * 3 ventas realizadas.
# Calculo el total, sumando salario base y comisión.
# Muestro los resultados
#
# Variables: 
# sb = Salario base
# comision = Comisión por ventas
# total = Dinero total

# Pido el salario base
sb = float(input("¿Cual es tu salario base de este mes? "))

# Calculo la comisión y el total
comision = (sb * 10 / 100) * 3
total = comision + sb

# Muestro los resultados por pantalla
print("Cobrarás", comision,"€ en concepto de comisión.")
print("Cobrarás", total,"€ en total.")

