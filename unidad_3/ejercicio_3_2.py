#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Escribir una función repite_saludo que reciba como parámetro un número
entero n y una cadena saludo y escriba por pantalla el valor de saludo n veces.
Invocarla con distintos valores de n y de saludo.
"""

def repite_saludo(n):
    return "Hola!" * n

veces = input("Digite la cantidad de veces que se dirá la palabra Hola: ")
repite_saludo(veces)
