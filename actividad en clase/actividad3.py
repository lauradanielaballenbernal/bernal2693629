def NumeroPerfecto(num):
    suma=0

    for i in range(1, num):
        if (num % (i) == 0):
           suma += (i)
    if num == suma:
         return True
    else:
         return False

num = int(input("Digite numero:"))
if NumeroPerfecto(num):
    print(" es un numero perfecto", num)
else:
    print("No es un numero perfecto", num)
    #miselanea