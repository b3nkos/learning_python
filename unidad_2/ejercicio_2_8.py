#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Escribir un programa que use un ciclo definido con rango numérico,
que averigue a cuántos amigos quieren saludar,
les pregunte los nombres de esos amigos/as, y los salude.
"""

number_of_friends = input("Digite el número de amigos que desea saludar: ")

for x in range(number_of_friends):
    best_fiend = raw_input("Nombre del mejor amigo: ")
    print "Hola", best_fiend + "!"
