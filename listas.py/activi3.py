import random


def suma(num):
    return num + random.randrange(100)

m = int(input("Introcude un numero:"))
s = 0
n = 1

while s <= m:
    s=s+n
    n=n+1

print("El numero naturalo mas pequeño que se necesita para superar elmaximo es: ", n-1)
print(suma(n-1))