import random
lista=[]
tam=int(random.randint(10,20))
sum=0
mayor=0
menor=1000000
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    lista.append(num)
    sum+=num
    if num>mayor:
        mayor=num
    if num<menor and num!=0:
        menor=num
print(lista)

print(f"el usuario ingreso {tam} numeros")
print(f"la suma es {sum}")
print(f"el promedio es{sum/(tam)} numeros")
print(f"el mayor es {mayor}")
print(f"el menor es {menor}")