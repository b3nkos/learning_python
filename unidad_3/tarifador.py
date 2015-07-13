#!/usr/bin/python
#-*- coding: utf-8 -*-

def main():
    """El usuario ingresa la tarifa por segundo, cuántas se realizaron
    y la duración de cada comunicación expresada en horas, minutos y segundos.
    Como resultado se informa la duración en segundos de cada comunicación
    y su costo. """

    f = input('¿Cuánto cuesta 1 segundo de comunicación?: ')
    n = input('¿Cuántas comunicaciones hubo?: ')
    total = 0
    for x in range(n):
        hs      = input("¿Cuántas horas?: ")
        min     = input("¿Cuántos minutos?: ")
        seg     = input("¿Cuántos segundos?: ")
        segcalc = asegundos(hs, min, seg)
        costo   = segcalc * f
        total = total + costo
        print "Duracion: ", segcalc, "segundos. Costo: ",costo, "$."

    print "El total facturado en la corrida ==>>", total

def asegundos (horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()
