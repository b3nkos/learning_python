#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Escribir una función repite_saludo que reciba como parámetro un número
entero n y una cadena saludo y escriba por pantalla el valor de saludo n veces.
Invocarla con distintos valores de n y de saludo.
"""

def repite_saludo(n, string_hi):
    for x in range(n):
        print string_hi

veces     = input("Digite la cantidad de veces que se saludará: ")
string_hi = raw_input("Digite el texto de saludo: ")
repite_saludo(veces, string_hi)
