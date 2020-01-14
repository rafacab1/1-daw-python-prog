# 20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
# después de pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos.
#
# Autor: Rafael Alberto Caballero Osuna
#
# 10/10/19
#
# Algoritmo
# Pregunto cuantas monedas tiene de cada
# Calculo cuanto dinero tiene por cada tipo de moneda
# Sumo todo para ver cuantos euros tiene
# Multiplico por 100 para calcular los céntimos totales
# Muestro por pantalla los resultados
# 
# Variables: 
# doseuros = Monedas de 2€ | Cuanto tiene en 2€
# uneuro = Monedas de 1€
# cincent = Monedas de 50 cént | Cuanto tiene en 50 cént
# veicent = Monedas de 20 cént | Cuanto tiene en 20 cént
# diecent = Monedas de 10 cént | Cuanto tiene en 10 cént
# euros = Total de euros que tiene
# centimos = Total de céntimos que tiene (contando los euros)

# Pregunto cuantas monedas de cada tiene
doseuros = float(input("¿Cuántas monedas de 2€ tienes? "))
uneuro = float(input("¿Cuántas monedas de 1€ tienes? "))
cincent = float(input("¿Cuántas monedas de 50 céntimos tienes? "))
veicent = float(input("¿Cuántas monedas de 20 céntimos tienes? "))
diecent = float(input("¿Cuántas monedas de 10 céntimos tienes? "))

# Calculo el valor de las monedas
doseuros = doseuros * 2
cincent = cincent * 0.50
veicent = veicent * 0.20
diecent = diecent * 0.10

# Sumo todos los euros y luego paso a céntimos
euros = round(doseuros + uneuro + cincent + veicent + diecent, 2)
centimos = int(euros * 100)

# Muestro por pantalla los resultados
print("\nTienes", euros, "€")
print("Tienes", centimos, "céntimos (contando los euros).")
