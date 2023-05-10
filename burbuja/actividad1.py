import random

lista=[]
tam = random.randint(15,20)

for i in range (tam):
     lista.append(random.randint(0,9))
x=int(input("ingrese el numeroa buscar: "))
if x in lista:
     print("El numero si aparece en la lista ")
if not x in lista:
     print("el numero no esta en la lista")
contador=0
for numero in lista:
     if numero == x:
          contador+=1
print(F"el numero {x} aparece {contador} veces en la lista{lista}")



