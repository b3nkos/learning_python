#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Un programa sencillo para calcular el cuadrado de números """

def main():
    print "Se calcularán cuadrados de números"

    n1 = input("Ingrese un número entero:")
    n2 = input("Ingrese otr número entero:")

    for x in range(n1, n2):
        print "El cuadrado de", x, "es :", x * x

    print "Es todo por ahora"

main()