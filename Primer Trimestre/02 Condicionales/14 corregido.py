# 14. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, 
# ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva 
# que entrega en un embarque, considerando lo siguiente: si es de tipo A, 
# se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. 
# Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. 
# Realice un algoritmo para determinar la ganancia obtenida.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19 Corregido a 30/10/2019
#
# Algoritmo
# Pido el precio inicial de la uva
# Pido los kilos
# Pido el tipo de la uva
# Pido el tamaño de la uva
# Según el tipo y el tamaño, sumo los céntimos al precio inicial y lo multiplico por los kilos.
#
# Variables
# pinicial = Precio inicial de la uva (float)
# kilos = Kilos de uvas (float)
# tipo = Tipo de la uva (str)
# tamano = Tamaño de la uva (int)

# Pido los datos
pinicial = float(input("Introduce el precio inicial de la uva: "))
kilos = float(input("Introduce los kilos de uvas: "))
tipo = input("Introduce el tipo de la uva: (A/B) ")
tamano = int(input("Introduce el tamaño de la uva: (1/2) "))

# Calculo el precio de la uva según su tipo y tamaño
if tipo.lower() == "a" and tamano == 1:
    print(f"\nLa ganancia es de {(pinicial * kilos) + (kilos * 0.20)}€")
elif tipo.lower() == "a" and tamano == 2:
    print(f"\nLa ganancia es de {(pinicial * kilos) + (kilos * 0.30)}€")
elif tipo.lower() == "b" and tamano == 1:
    print(f"\nLa ganancia es de {(pinicial * kilos) + (kilos * -0.30)}€")
elif tipo.lower() == "b" and tamano == 2:
    print(f"\nLa ganancia es de {(pinicial * kilos) + (kilos * -0.50)}€")
else:
    print("\nError, datos introducidos incorrectos.")