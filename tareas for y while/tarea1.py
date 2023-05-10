def numnat(X):
 suma=0
 n= 1
 while suma < maximo:
  suma=suma+n
  n=n+1
 return n-1  
maximo = int(input("introdue un numero maximo:"))
lista=numnat(-1)
print("el numero natural mas pequeño nesesario para superar el maximo es:" , lista)
