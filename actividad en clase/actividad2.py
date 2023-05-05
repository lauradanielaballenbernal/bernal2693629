numero = int(input("Ingresa un número entero positivo: "))
#miselanea
if numero > 1:
    es_primo = True
    for i in range(2, int(numero/2)+1):
        if numero % i == 0:
            es_primo = False
        break
    if es_primo: 
        print("El número", numero, "es primo.")
    else:
        print("El número", numero, "no es primo.")
else:
  print("El número ingresado no es válido.")
  