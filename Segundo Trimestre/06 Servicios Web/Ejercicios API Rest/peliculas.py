# -*- coding: utf-8 -*-

import requests
import json

# Guardo la clave de acceso a The Movie Database API
tmdb = ""

# URL desde la que obtendré los géneros
urlgen = " https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=es-ES".format(tmdb)

# Obtengo el JSON
responsegen = requests.get(urlgen)

# Lo guardo en una variable (moviesgenres)
moviesgenres = responsegen.json()

for i in moviesgenres['genres']:
    print("- " + str(i['id']) + "\t" + i['name'])
# print(moviesgenres['genres']) # No sé como mostrar los géneros de mejor manera.

todos = input("\n¿Quieres ver el trending topic de algún genero en concreto? [s/n] ")
if todos == "s":
    generob = int(input("¿De que género quieres ver el trending topic? (Introduce el ID) :  "))

diasem = input("¿Quieres ver el trending topic diario o semanal [d/s] ")

urlday = "https://api.themoviedb.org/3/trending/all/day?api_key={}&language=es-ES".format(tmdb)
urlweek = "https://api.themoviedb.org/3/trending/all/week?api_key={}&language=es-ES".format(tmdb)

# Si quiere ver el TT de todos los géneros del día
if todos == "n" and diasem == "d": 
    r_n_d = requests.get(urlday)
    m_n_d = r_n_d.json()
    print("\nTrending Topic diario de todas las categorías: \n")
    for i in range(0, 5):
        print("- " + m_n_d['results'][i]['title'])

# Si se quiere ver el TT de todos los géneros de la semana
if todos == "n" and diasem == "s":
    r_n_s = requests.get(urlweek)
    m_n_s = r_n_s.json()
    print("\nTrending Topic semanal de todas las categorías: \n")
    for i in range(0, 5):
        print("- " + m_n_s['results'][i]['title'])

"""
No consigo comparar los ids de que devuelve la API con el que introduce el usuario


# Si se quiere ver el TT de algún género concreto del día
if todos == "s" and diasem == "d":
    r_s_d = requests.get(urlday)
    m_s_d = r_s_d.json()
    print("\nTrending Topic diario de la categoría " + str(generob) + ": \n")
    for i in range(0, 5):
        encontrado = False
        contador = 0
        while not encontrado:
            if m_s_d['results'][contador]['genre_ids'] == generob:
                print("- " + m_s_d['results'][contador]['title'])
                encontrado = True
            else:
                contador += 1

# Si se quiere ver el TT de algún género concreto de la semana   
if todos == "s" and diasem == "s":
    r_s_s = requests.get(urlweek)
    m_s_s = r_s_s.json()
    print("\nTrending Topic diario de la categoría " + str(generob) + ": \n")
    for i in range(0, 5):
        encontrado = False
        contador = 0
        while not encontrado:
            if m_s_d['results'][contador]['genre_ids'] == generob:
                print("- " + m_s_s['results'][contador]['title'])
                encontrado = True
            else:
                contador += 1
"""