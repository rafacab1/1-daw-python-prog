# -*- coding: utf-8 -*-

import ej1 as tm

t = tm.Tiempo(1, 20, 30)  # Tiempo 1
ti2 = tm.Tiempo(2, 12, 23)  # Tiempo 2 (para la suma)
ti3 = tm.Tiempo(1, 23, 14)  # Tiempo 3 (para la resta)

# Muestro los dos tiempos
print(f"El primer tiempo es {t.tiempoalm()}")
print(f"El segundo tiempo (que luego sumare) es {ti2.tiempoalm()}")
print(f"El segundo tiempo (que luego restare) es {ti3.tiempoalm()}")

# Prueba método suma_tiempos
# Sumo los dos tiempos
t.suma_tiempos(ti2)
# Con el método tiempoalm, muestro el tiempo sumado
print(f"La suma de los dos tiempos es: {t.tiempoalm()}")

# Prueba método resta_tiempos
# Resto los dos tiempos
t.resta_tiempos(ti3)
# Con el método tiempoalm, muestro el tiempo restado
print(f"La resta de los dos tiempos es: {t.tiempoalm()}")

# Prueba método sumar
horassum = int(input(f"\nIntroduce cuántas horas quieres sumar a {t.tiempoalm()} : "))
minutossum = int(input(f"Introduce cuántos minutos quieres sumar a {t.tiempoalm()} : "))
segundossum = int(input(f"Introduce cuántos segundos quieres sumar a {t.tiempoalm()} : "))
# Guardo el tiempo antes de cambiarlo, para poder mostrarlo luego
anterior_t = t.tiempoalm()
# Invoco al método que me lo sumará
t.sumar(horassum, minutossum, segundossum)
# Con el método, tiempoalm, muestro el tiempo sumado
print(f"\nLa suma de {anterior_t} + {horassum}h {minutossum}m {segundossum}s es: {t.tiempoalm()}")

# Prueba método restar
horasres = int(input(f"\nIntroduce cuántas horas quieres restar a {t.tiempoalm()} : "))
minutosres = int(input(f"Introduce cuántos minutos quieres restar a {t.tiempoalm()} : "))
segundosres = int(input(f"Introduce cuántos segundos quieres restar a {t.tiempoalm()} : "))
# Guardo el tiempo antes de cambiarlo, para poder mostrarlo luego
anterior_t = t.tiempoalm()
# Invoco al método que me lo sumará
t.restar(horasres, minutosres, segundosres)
# Con el método, tiempoalm, muestro el tiempo sumado
print(f"\nLa resta de {anterior_t} - {horasres}h {minutosres}m {segundosres}s es: {t.tiempoalm()}")
