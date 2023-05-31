import random

import random

def multiply_elements(lista, rango):
    multiplied_list = [element * rango for element in lista]
    return multiplied_list

def llenarlista(tam, rango):
    lista = [random.randrange(rango) for _ in range(tam)]
    return lista

l1 = llenarlista(5, 10)

def count_occurrences(lista, element):
    count = lista.count(element)
    return count

def sumalista(lista):
    sum = 0
    for x in lista:
        sum += x
    return sum

def promediolista(lista):
    return sumalista(lista) / len(lista)
