#Diseñar e implementar un programa que solicite a su usuario un valor no negativo n y visualice la siguiente salida:

n = int(input("Ingrese un valor no negativo: "))

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
