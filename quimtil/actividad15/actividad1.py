import random

def calcular_quintiles(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    indice_20 = int(n * 0.2)
    indice_40 = int(n * 0.4)
    indice_60 = int(n * 0.6)
    indice_80 = int(n * 0.8)
    quintil_20 = lista_ordenada[indice_20]
    quintil_40 = lista_ordenada[indice_40]
    quintil_60 = lista_ordenada[indice_60]
    quintil_80 = lista_ordenada[indice_80]
    return quintil_20, quintil_40, quintil_60, quintil_80, indice_20, indice_40, indice_60, indice_80

# Generar longitud aleatoria entre 15 y 125
longitud = random.randint(15, 125)

# Generar lista de valores aleatorios entre 1.50 y 2.00 con dos decimales
lista = [round(random.uniform(1.50, 2.00), 2) for _ in range(longitud)]

# Calcular quintiles utilizando la función personalizada
quintil_20, quintil_40, quintil_60, quintil_80, indice_20, indice_40, indice_60, indice_80 = calcular_quintiles(lista)

print("Lista generada:", lista)
print("Quintil 20:", quintil_20, "en la posición", indice_20)
print("Quintil 40:", quintil_40, "en la posición", indice_40)
print("Quintil 60:", quintil_60, "en la posición", indice_60)
print("Quintil 80:", quintil_80, "en la posición", indice_80)