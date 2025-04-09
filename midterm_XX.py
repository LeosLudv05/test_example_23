import math
from time import process_time

PI = math.pi
SHAPE_KRUH = 'kruh'
SHAPE_OBDELNIK = 'obdelnik'
SHAPE_PRAVOUHLY_TROJUHELNIK = 'pravouhly trojuhelnik'

def get_shapes_and_areas(rozmery):
    """
    Funkce vezme data o rozmerech a urci tvar, zapise do jednoho listu, pote podle tvaru vypocita plochu
    a vlozi do druheho listu
    :param rozmery: (tuple) ntice s rozmery tvaru
    :return: obrazce (list); obsahy (list)
    """
    obrazce = []
    obsahy = []

    for tvar in rozmery:
        if len(tvar) == 1:
            polomer = tvar[0]
            obsah = math.pi * polomer ** 2
            obrazce.append(SHAPE_KRUH)
            obsahy.append(obsah)
        elif len(tvar) == 2:
            a, b = tvar
            obsah = a * b
            obrazce.append(SHAPE_OBDELNIK)
            obsahy.append(obsah)
        elif len(tvar) == 3:
            a, b, c = tvar
            obsah = (a * b) / 2
            obrazce.append(SHAPE_PRAVOUHLY_TROJUHELNIK)
            obsahy.append(obsah)

    return obrazce, obsahy

def check_if_can_get_through_hole(rozmery, obrazce, prumer_diry):
    """
    Funkce zjisti z rozmeru a urcenych obrazcu, jestli projde obrazec zadanym promerem diry
    :param rozmery: (list) seznam rozmeru obrazcu
    :param obrazce: (list) seznam nazvu obrazcu
    :param prumer_diry: (int) argument urcujici sirku diry
    :return: list boolean hodnot jestli se vejde ci ne
    """

    list_vysledku = []

    for tvar, nazev in zip(rozmery, obrazce):
        if nazev == SHAPE_KRUH:
            polomer = tvar[0]
            if polomer <= prumer_diry:
                list_vysledku.append(True)
            else:
                list_vysledku.append(False)
        elif nazev == SHAPE_OBDELNIK:
            a, b = tvar
            uhlopricka = math.sqrt(a ** 2 + b ** 2)
            if uhlopricka <= prumer_diry:
                list_vysledku.append(True)
            else:
                list_vysledku.append(False)
        elif nazev == SHAPE_PRAVOUHLY_TROJUHELNIK:
            a, b, c = tvar
            prepona = c
            if prepona <= prumer_diry:
                list_vysledku.append(True)
            else:
                list_vysledku.append(False)
        else:
            continue
    return list_vysledku

def count_area_weighted_letters(obrazce, obsahy, list_vysledku, hledane_pismeno):
    """
    Picovina pocitajici pocet pismen nebo nejaky takovy hovna nevim nejsu vedec
    :param obrazce: (list) obsahuje nazvy jednotlivych tvaru
    :param obsahy:  (list) obsahuje obsahy jednotlivych tvaru
    :param list_vysledku:   (list) bool hodnoty jestli projdou dirou
    :param hledane_pismeno: (str) zadane pismeno, ktere budem hledat a pocitat s nim
    :return: (float) sumy hodnoty vsech tvaru, ktere prosly
    """

    suma = 0.0
    for nazev, obsah, vysled in zip(obrazce, obsahy, list_vysledku):
        if vysled:
            pocet_pismen = nazev.lower().count(hledane_pismeno.lower())
            suma += obsah * pocet_pismen

    return suma

def main(rozmery, prumer_diry, hledane_pismeno, vratit_nazvy = False):
    """
    Main funkce ktera vypisuje vsechny hovadinky z predchozich ukolu
    :param rozmery: (list) rozmery z prvniho ukolu
    :param prumer_diry: (int) ciselna hodnota prumeru diry kterou prochazi obrazce
    :param hledane_pismeno: (str) hledane pismeno v nazvech tvaru
    :param vratit_nazvy: (bool) ma ci nema vyhodit i seznam jednotlivych tvaru - default False
    :return: prosle_tvary (float); nazvy geometrickych tvaru pokud je 4. parametr True (list)
    """

    #Ukol 1
    obrazce, obsahy = get_shapes_and_areas(rozmery)
    #Ukol 2
    list_vysledku = check_if_can_get_through_hole(rozmery, obrazce, prumer_diry)
    #Ukol 3
    celkova_hodnota = count_area_weighted_letters(obrazce, obsahy, list_vysledku, hledane_pismeno)
    #Vystup
    if vratit_nazvy is True:
        return celkova_hodnota, obrazce
    else:
        return celkova_hodnota

if __name__ == '__main__':
    shapes_parameters = [(6,), (3, 5), (5, 3), (3,), (3, 1), (3, 4, 5), (5, 12, 13)]
    hole_diameter = 5
    letter = 'j'

    main(shapes_parameters, hole_diameter, letter)
    # main(shapes_parameters, hole_diameter, letter, True)

