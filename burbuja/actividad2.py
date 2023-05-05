import random

n = 10
arr1 = [random.randint(1, 200) for _ in range(n)]  
arr2 = [random.randint(1, 200) for _ in range(n)]  
if sum(arr1) > sum(arr2):
    print("El primer arreglo tiene la suma más alta.")
elif sum(arr1) < sum(arr2):
    print("El segundo arreglo tiene la suma más alta.")
else:
    print("Ambos arreglos tienen la misma suma.")

# b) comparación del número mayor
if max(arr1) > max(arr2):
    print("El primer arreglo tiene el número mayor.")
elif max(arr1) < max(arr2):
    print("El segundo arreglo tiene el número mayor.")
else:
    print("Ambos arreglos tienen el mismo número mayor.")

# c) comparación del número menor
if min(arr1) < min(arr2):
    print("El primer arreglo tiene el número menor.")
elif min(arr1) > min(arr2):
    print("El segundo arreglo tiene el número menor.")
else:
    print("Ambos arreglos tienen el mismo número menor.")

# d) cálculo del promedio conjunto
promedio = (sum(arr1) + sum(arr2)) / (2 * n)
print(f"El promedio conjunto es: {promedio}")

# e) comparación de los promedios individuales con el promedio conjunto
promedio_arr1 = sum(arr1) / n
promedio_arr2 = sum(arr2) / n
if promedio_arr1 > promedio and promedio_arr2 > promedio:
    print("Ambos arreglos están por encima del promedio conjunto.")
elif promedio_arr1 < promedio and promedio_arr2 < promedio:
    print("Ambos arreglos están por debajo del promedio conjunto.")
else:
    print("Los arreglos tienen promedios individuales en ambos lados del promedio conjunto.")

# f) conteo de pares e impares
pares_arr1 = sum(1 for num in arr1 if num % 2 == 0)
pares_arr2 = sum(1 for num in arr2 if num % 2 == 0)
impares_arr1 = n - pares_arr1
impares_arr2 = n - pares_arr2
if pares_arr1 > pares_arr2:
    print("El primer arreglo tiene mayor cantidad de pares.")
elif pares_arr1 < pares_arr2:
    print("El segundo arreglo tiene mayor cantidad de pares.")
else:
    print("Ambos arreglos tienen la misma cantidad de pares.")
if impares_arr1 > impares_arr2:
    print("El primer arreglo tiene mayor cantidad de impares.")
elif impares_arr1 < impares_arr2:
    print("El segundo arreglo tiene mayor cantidad de impares.")
else:
    print("Ambos arreglos tienen la misma cantidad de impares.")
    