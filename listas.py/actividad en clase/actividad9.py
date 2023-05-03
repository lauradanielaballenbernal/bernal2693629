x = int(input("Introduce la base x: ")) 
n = int(input("Introduce el exponente n: ")) 

resultado = 1 

while n > 0:
    resultado *= x 
    n -= 1 

print("El resultado de", x, "elevado a", n, "es:", resultado)
