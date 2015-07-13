#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    a = 10
    b = 100
    c = 1000

    expresion_a = ((b * b) - (4 * a * c)) / (2 * a)
    expresion_b = (b * b - 4 * a * c) / (2 * a)
    expresion_c = b * b - 4 * a * c / 2 * a
    expresion_d = (b * b) - (4 * a * c / 2 * a)
    expresion_e = 1 / 2 * b
    expresion_f = b / 2

    print "El valo de la expresión a es:", expresion_a
    print "El valo de la expresión b es:", expresion_b
    print "El valo de la expresión c es:", expresion_c
    print "El valo de la expresión d es:", expresion_d
    print "El valo de la expresión e es:", expresion_e
    print "El valo de la expresión f es:", expresion_f

main()
