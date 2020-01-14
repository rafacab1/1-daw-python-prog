# 9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pido el total de la compra sin descuento
# Calculo el descuento y se lo resto a la compra
# Muestro en pantalla lo que tendrá que pagar en total
#
# Variables: 
# compra = Total de la compra sin descuento
# descuento = Total de la compra con descuento

# Pido el total de la compra sin descuento
compra = float(input("Introduce el total de la compra: "))

# Calculo el descuento
descuento = compra - (compra * 15 / 100)

# Muestro por pantalla lo que deberá pagar
print("Debes pagar", descuento,"€ en total.")