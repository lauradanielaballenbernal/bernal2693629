#importamos el random
import random
def llenarlista(tam,rango):
  lista=[random.randrange(rango)for i in range(tam)]
  return lista
#definimos la funcion de sumar lista
def sumalista(lista):
  sum=0
  for x in lista:
    sum+=x
    return sum
#definimos la funcion promediolista
def promediolista(lista):
  return sumalista(lista)/len(lista)
  
#imprimimos 
l1=llenarlista(10,50)
print(sumalista(l1))
print(l1)
print(round(promediolista(l1),2))

#el codigo imprime una lista suma la lista y saca el promedio