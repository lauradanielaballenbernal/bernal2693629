import random
lista=[]
tam=int(random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
print(lista)

suma= sum(lista)
mayor= max(lista)
menor=min(lista)
cont=len(lista)

print(f"el usuario ingreso {cont-1} numeros")
print(f"la suma es {suma}")
print(f"el promedio es{suma/(cont-1)} numeros")
print(f"el mayor es {mayor}")
print(f"el menor es {menor}")