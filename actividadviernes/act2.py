#segundo punto 
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

d2 = {"Zebra": "Cebra",
      "Snake": "Serpiente",
      "Frog": "Rana",
      "Duck": "Pato",
      "Rabbit": "Conejo",
      "Rat": "Rata",
      "Bat": "Murciélago",
      "Dolphin": "Delfín",
      "Whale": "Ballena",
      "Fish": "Pez"}

def añadir1(d1):
    n = input("Ingrese la clave que desea añadir: ")
    x = input("Ingrese el valor que desea añadir: ")
    d1[n] = x

def añadir2(d2):
    n = input("Ingrese la clave que desea añadir: ")
    x = input("Ingrese el valor que desea añadir: ")
    d2[n] = x

def obtener_tupla_espanol(d):
    tupla_espanol = tuple(d.keys())
    return tupla_espanol

def obtener_tupla_ingles(d):
    tupla_ingles = tuple(d.values())
    return tupla_ingles

tupla_espanol_d1 = obtener_tupla_espanol(d1)
tupla_ingles_d1 = obtener_tupla_ingles(d1)

tupla_espanol_d2 = obtener_tupla_espanol(d2)
tupla_ingles_d2 = obtener_tupla_ingles(d2)

def menu():
    print("Bienvenido")
    print("1. Mostrar el diccionario 1")
    print("2. Mostrar el diccionario 2")
    print("3. Añadir nueva entrada al diccionario 1")
    print("4. Añadir nueva entrada al diccionario 2")
    print("5. Mostrar tuplas español,ingles del diccionario 1")
    print("6. Mostrar tuplas español,ingles del diccionario 2")
    print("7. Salir del menú")

opcion = 0

while opcion != 7:
    menu()
    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        print(d1)
    elif opcion == 2:
        print(d2)
    elif opcion == 3:
        añadir1(d1)
    elif opcion == 4:
        añadir2(d2)
    elif opcion == 5:
        print("Animales en español (Diccionario 1):", tupla_espanol_d1)
        print("Animales en inglés (Diccionario 1):", tupla_ingles_d1)
    elif opcion == 6:
        print("Animales en ingles (Diccionario 2):", tupla_espanol_d2)
        print("Animales en español (Diccionario 2):", tupla_ingles_d2)
    elif opcion == 7:
        print("Saliendo del menú")
    else:
        print("La opción no existe")
#tercer y segundo punto unidos 
