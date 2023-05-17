import random
n=int(input("Ingrese la longitdud de la lista: "))
def llenarlista(rango,tam=n):
    lista = [random.randrange(rango) for i in range(n)]
    return lista

x=int(input("Ingrese la longitdud de la lista: "))
def llenarlista2(rango2,tam2=x):
    lista2 = [random.randrange(rango2) for i in range(x)]
    return lista2

def sumarlista(lista):
    sum=0
    for y in lista:
        sum += y
    return sum

def sumarlista(lista2):
    sum=0
    for b in lista2:
        sum += b
    return sum

def sumamayor(lista, lista2):
    suma1 = sum(lista)
    suma2 = sum(lista2)

    if suma1 > suma2:
        return "La suma de la lista 1 es mayor que la suma de la lista 2."
    elif suma1 < suma2:
        return "La suma de la lista 2 es mayor que la suma de la lista 1."
    else:
        return "Ambas sumas son iguales."

def encontrar_mayor(lista1, lista2):
    maximo_lista1 = max(lista1)
    maximo_lista2 = max(lista2)

    if maximo_lista1 > maximo_lista2:
        return maximo_lista1, "La lista 1 tiene el número mayor"
    elif maximo_lista1 < maximo_lista2:
        return maximo_lista2, "La lista 2 tiene el número mayor"
    else:
        return maximo_lista1, "Ambas listas tienen el mismo número mayor"
    
def encontrar_menor(lista1, lista2):
    minimo_lista1 = min(lista1)
    minimo_lista2 = min(lista2)

    if minimo_lista1 < minimo_lista2:
        return minimo_lista1, "La lista 1 tiene el número menor"
    elif minimo_lista1 > minimo_lista2:
        return minimo_lista2, "La lista 2 tiene el número menor"
    else:
        return minimo_lista1, "Ambas listas tienen el mismo número menor"

def promediolista(lista, lista2):
    return (sum(lista) + sum(lista2)) / (len(lista) + len(lista2))

def promediolista2(lista):
    return sumarlista(lista)/len(lista)

def promediolista3(lista2):
    return sumarlista(lista2)/len(lista2)

def promediototal(lista, lista2):
    promedio_combinado = (sum(lista) + sum(lista2)) / (len(lista) + len(lista2))
    promedio_lista1 = sum(lista) / len(lista)
    promedio_lista2 = sum(lista2) / len(lista2)

    if promedio_lista1 > promedio_combinado and promedio_lista2 > promedio_combinado:
        return "Ambas listas tienen un promedio mayor al promedio combinado."
    elif promedio_lista1 > promedio_combinado:
        return "La lista 1 tiene un promedio mayor al promedio combinado."
    elif promedio_lista2 > promedio_combinado:
        return "La lista 2 tiene un promedio mayor al promedio combinado."
    else:
        return "Ninguna lista tiene un promedio mayor al promedio combinado."

def comparar_pares_impares(l1, l2):
    def contar_pares(arr):
        return sum(1 for num in arr if num % 2 == 0)

    n = len(l1)
    pares_l1 = contar_pares(l1)
    pares_l2 = contar_pares(l2)
    impares_l1 = n - pares_l1
    impares_l2 = n - pares_l2

    if pares_l1 > pares_l2:
        resultado_pares = "El primer arreglo tiene una mayor cantidad de pares."
    elif pares_l1 < pares_l2:
        resultado_pares = "El segundo arreglo tiene una mayor cantidad de pares."
    else:
        resultado_pares = "Ambos arreglos tienen la misma cantidad de pares."

    if impares_l1 > impares_l2:
        resultado_impares = "El primer arreglo tiene una mayor cantidad de impares."
    elif impares_l1 < impares_l2:
        resultado_impares = "El segundo arreglo tiene una mayor cantidad de impares."
    else:
        resultado_impares = "Ambos arreglos tienen la misma cantidad de impares."

    return resultado_pares, resultado_impares

l1=llenarlista(50)
l2=llenarlista2(50)

resultado = sumamayor(l1,l2)

resultado2, mensaje = encontrar_mayor(l1, l2)

resultado3, mensaje2 = encontrar_menor(l1, l2)

promedio = promediolista(l1,l2)

result = promediototal(l1, l2)

resultado_pares, resultado_impares = comparar_pares_impares(l1, l2)

def mostrar_menu():
    print("Bienvenido al menú:")
    print("1. mostrar las dos listas")
    print("2. mostrar la suma de las listas")
    print("3. mostara cual lista tiene la suma mayor")
    print("4. cual lista tiene el numero mayor")
    print("5. cual lista tiene el numero menor")
    print("6. mostrar el promedio conjunto de las dos listas")
    print("7. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto")
    print("8. cual lista tiene la mayor cantidad de pares o impares")
    print("9. Salir")


opcion = 0


while opcion != 8:
    
    mostrar_menu()

    opcion = int(input("Ingrese el número de opción deseada: "))

    # Procesar la opción seleccionada
    if opcion == 1:
        print("Ha seleccionado la opción 1")
        print(l1)
        print(l2)
    elif opcion == 2:
        print("Ha seleccionado la opción 2")
        print("la suma de la primera lista es: ", sumarlista(l1))
        print("la suma de la segunda lista es: ", sumarlista(l2))
    elif opcion == 3:
        print("Ha seleccionado la opción 3")
        print(resultado)
    elif opcion == 4:
        print("Ha seleccionado la opción 4")
        print("El número mayor es:", resultado2)
        print(mensaje)
    elif opcion == 5:
        print("Ha seleccionado la opción 5")
        print("El número menor es:", resultado3)
        print(mensaje2)
    elif opcion == 6:
        print("Ha seleccionado la opción 6")
        print("el promedio de las dos listas es:", promedio)
    elif opcion == 7:
        print("Ha seleccionado la opción 7")
        print("el promedio de la lista 1 es:",promediolista2(l1))
        print("el promedio de la lista 2 es:",promediolista3(l2))
        print(result)
    elif opcion == 8:
        print("Ha seleccionado la opción 8")
        print(resultado_pares)
        print(resultado_impares)
    elif opcion == 9:
        print("Saliendo del programa...")
    else:
        print("Opción no válida")