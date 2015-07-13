#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Escribir otra función repite_saludo que reciba como parámetro un número
entero n y una cadena saludo retorne el valor de n concatenaciones de saludo.
Invocarla con distintos valores de n y de saludo.
"""

def repite_saludo(n, string_hi):
    return string_hi * n

n = input("Digite la cantidad de veces que se concatenara: ")
string_hi = raw_input("Digite el texto a concatenar: ")

print repite_saludo(n, string_hi)
