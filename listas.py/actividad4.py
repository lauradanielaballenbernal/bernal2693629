import random
q=int(random.randint (1,15))

def lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

numeros = [random.randrange (100) for i in range(q) ]

# Llamar a la función y mostrar el resultado
print("La suma de la lista es:", lista(numeros))