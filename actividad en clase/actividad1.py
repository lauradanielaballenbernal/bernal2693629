num = int(input("Introduce un número: "))

divisores = []

for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)

print("Los divisores de", num, "son:", divisores)
#miselanea