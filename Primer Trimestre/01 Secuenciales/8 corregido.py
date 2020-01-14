# 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las 
# tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta
# su sueldo base y comisiones.
#
# 15/10/19
#
# Algoritmo
# Pido el salario base.
# Calculo la comisión, el 10% del salario base * 3 ventas realizadas.
# Calculo el total, sumando salario base y comisión.
# Muestro los resultados
#
# Variables: 
# sb = Salario base
# v1, v2, v3 = Ventas
# comision = Comisión por ventas
# total = Dinero total

# Pido el salario base y las ventas
sb = float(input("¿Cual es tu salario base de este mes? "))
v1 = float(input("Dime el precio de la venta 1: "))
v2 = float(input("Dime el precio de la venta 2: "))
v3 = float(input("Dime el precio de la venta 3: "))

# Cálculos
comision = v1 * 0.1 + v2 * 0.1 + v3 * 0.1

# Muestro los resultados por pantalla
print(f"Comisión por ventas: {comision}")
print(f"Sueldo total: {sb + comision}")

