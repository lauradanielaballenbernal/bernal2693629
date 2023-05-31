import random
from sys import path
path.append("C:\pythonbernal")#("..\\pythonbernal\\dylanD")
#import dylanD.lsitas.salpi

from dylanD.diccio.papa import añadir1
from dylanD.diccio.papa import llaves
from dylanD.diccio.papa import reverse_dictionary
from dylanD.diccio.papa import remove_entry
from dylanD.diccio.papa import search_value
from dylanD.lsitas.salpi import llenarlista
from dylanD.lsitas.salpi import multiply_elements 
from dylanD.lsitas.salpi import count_occurrences
from dylanD.lsitas.salpi import sumalista
from dylanD.lsitas.salpi import promediolista
d1 = {"Perro": "Dog",
      "Gato": "Cat",
      "Elefante": "Elephant",
      "León": "Lion",
      "Tigre": "Tiger",
      "Caballo": "Horse",
      "Vaca": "Cow",
      "Mono": "Monkey",
      "Jirafa": "Giraffe",
      "Oso": "Bear"}
l1=llenarlista(40,10)
count = count_occurrences(l1, 2)


print(l1)
print(multiply_elements(l1,6))
print(count)
print("la suma de la lista es: ",sumalista(l1))
print("el promedio de la lista es: ",promediolista(l1))
#print(d1)
#print(añadir1(d1))
#print(d1)
#print("las llaves de la lista son:",llaves(d1))
#print(reverse_dictionary(d1))
#remove_entry(d1, "Tigre")
#print(d1)
#keys = search_value(d1, "Cat")
#print(keys)
#keys = search_value(d1, "Bear")
#print(keys)

