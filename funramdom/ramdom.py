# Genera un número aleatorio entre 0 y 50 y lo asigna a la variable "num_aleatorio"
import random

num_aleatorio = random.randint(0, 50)

num_usuario = int(input("Ingrese un número: "))

# Bucle while que se ejecuta mientras el número ingresado no sea igual al número aleatorio
while num_aleatorio != num_usuario:
   
    if num_usuario > num_aleatorio:
        print("Te pasaste, un poco más abajo")
        num_usuario = int(input("Ingrese un número: "))
   
    elif num_usuario < num_aleatorio:
        print("Te pasaste, un poco más arriba")
        num_usuario = int(input("Ingrese un número: "))

print("Adivinaste el número, este era: ", num_aleatorio)
