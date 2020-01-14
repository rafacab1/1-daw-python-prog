# 20. Una compañía de transporte internacional tiene servicio en algunos países de 
# América del Norte, América Central, América del Sur, Europa y Asia. 
# El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. 
# Lo anterior se muestra en la tabla:
#
# ZONA  UBICACIÓN	        COSTO/GRAMO
# 1	    América del Norte	24.00 euros
# 2	    América Central	    20.00 euros
# 3	    América del Sur	    21.00 euros
# 4	    Europa	            10.00 euros
# 5	    Asia	            18.00 euros
#
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, 
# esto por cuestiones de logística y de seguridad. 
#
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
#
#
# Autor: Rafael Alberto Caballero Osuna
#
#
# 18/10/19
#
# Algoritmo
# Pido el peso en gramos del paquete.
# Pido la zona a la que se envía.
# Hago la sentencia.
# Si el peso es mayor que 5000 gramos, rechazo la entrega.
# Si no, hago las siguientes sentencias:
#   Si va a la zona 1, peso * 24 y lo muestro por pantalla.
#   Si va a la zona 2, peso * 20 y lo muestro por pantalla.
#   Si va a la zona 3, peso * 21 y lo muestro por pantalla.
#   Si va a la zona 4, peso * 10 y lo muestro por pantalla.
#   Si va a la zona 5, peso * 18 y lo muestro por pantalla.
#
# Variables
# peso = Peso del paquete en gramos (int)
# zona = Zona a la que se envía (int)

print("Programa que calcula el precio del envío según la zona.\n")

# Pido el peso
peso = int(input("Introduce el peso en gramos del paquete: "))

# Muestro un menú para pedir la zona de destino
print("\nElige una zona:")
print("\n1. América del Norte")
print("2. América Central")
print("3. América del Sur")
print("4. Europa")
print("5. Asia")

zona = int(input("\nIntroduce el número de la zona de destino: "))

# Hago las sentencias
if peso > 5000:
    print("\nEnvío rechazado. El paquete no puede pesar mas de 5 kg.")
elif zona == 1:
    print(f"\nEl precio del envío con destino América del Norte es de {peso * 24}€.")
elif zona == 2:
    print(f"\nEl precio del envío con destino América Central es de {peso * 20}€.")
elif zona == 3:
    print(f"\nEl precio del envío con destino América del Sur es de {peso * 21}€.")
elif zona == 4:
    print(f"\nEl precio del envío con destino Europa es de {peso * 10}€.")
elif zona == 5:
    print(f"\nEl precio del envío con destino Asia es de {peso * 18}€.")
else:
    print("\nHa ocurrido un error, la zona indicada no es correcta.")