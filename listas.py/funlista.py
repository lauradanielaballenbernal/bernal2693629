#importamos el random
import random

n = int(input("Ingrese la longitud de la lista: "))

def llenarlista(tam, rango):
    lista = [random.randrange(rango) for i in range(tam)]
    return lista

#definimos la funcion de sumar lista
def sumalista(lista):
    sum = 0
    for x in lista:
        sum += x
    return sum

#definimos la funcion promediolista
def promediolista(lista):
    return sumalista(lista) / len(lista)

l1 = llenarlista(20, 60)

def mayor(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

resultado = mayor(l1)

def menor(lista):
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

resultado2 = menor(l1)

<<<<<<< HEAD
import random
#ejemplo 1
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range (tam)] 
    return lista
def llenarLista(tam, rango):
    lista=[random.randrange(rango) for i in range (tam)] 
    return lista

def sumaLista(lista):
    suma1=sum(l1)
    suma2=sum(l2)

    if suma1 > suma2:
        print(f"la suma de la lista 1:{suma1} es mayor que la suma de la lista 2")
    else:
        suma1< suma2




#def sumaMayor(lista)






        

    
    
    






l1=llenarLista(5,10)
l2=llenarLista(5,10)
print("lista 1:",l1,"la suma es:",sumaLista(l1))
print("lista 2:",l2,"la suma es:",sumaLista(l2))
print("la suma mas alta esta en la lista :",(l1))
=======
print("Lista generada:", l1)
print("La suma de la lista es:", sumalista(l1))
print("El promedio de la lista es:", round(promediolista(l1),2))
print("El número mayor en la lista es:", resultado)
print("El número menor en la lista es:", resultado2)
#terminar
>>>>>>> 03b0ae4f490c57a9a6b1971144de75e84e164ea1
