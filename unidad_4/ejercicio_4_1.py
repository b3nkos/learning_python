#!/usr/bin/python
#-*- coding: utf-8 -*-

def main():
    """El usuario ingresa la tarifa por segundo, cuántas se realizaron
    y la duración de cada comunicación expresada en horas, minutos y segundos.
    Como resultado se informa la duración en segundos de cada comunicación
    y su costo."""
    
    n                    = input('¿Cuántas comunicaciones hubo?: ')
    seconds_short_call   = input('¿Cual es la duración de la llamada corta en segundos?: ')
    tarifa_llamada_corta = input('¿Cuál es la tarifa de 1 segundo de la llamada corta?: ')
    tarifa_llamada_larga = input('¿Cuál es la tarifa de 1 segundo de la llamada larga?: ')
    total                = 0
    for x in range(n):
        hs      = input("¿Cuántas horas?: ")
        min     = input("¿Cuántos minutos?: ")
        seg     = input("¿Cuántos segundos?: ")
        segcalc = asegundos(hs, min, seg)
        if segcalc > seconds_short_call:
            costo = segcalc * tarifa_llamada_larga
        else:
            costo = segcalc * tarifa_llamada_corta
        total = total + costo
        print "Duracion: ", segcalc, "segundos. Costo: ", costo, "$"

    print "El total facturado en la corrida ==>>", total

def asegundos (horas, minutos, segundos):
    segsal = 3600 * horas + 60 * minutos + segundos
    return segsal

main()
