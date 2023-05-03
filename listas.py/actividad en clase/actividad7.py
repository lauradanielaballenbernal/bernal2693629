maximo = int(input("Introduce el número máximo: ")) 

suma = 0 
n = 1 

while suma <= maximo:
    suma += n 
    n += 1 

print("El número mínimo de términos para superar el número máximo es:", n-1)
