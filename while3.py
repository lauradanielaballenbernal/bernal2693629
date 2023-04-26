num = 1
cont = 0
suma = 0
mayor=0
menor=1000000
while num != 0:
  num = int(input('Ingrese número: '))
  cont += 1
  suma += num
  if num>mayor:
     mayor=num
  if num<menor and num!=0:
     menor=num    

print(f'El usuario ingresó {cont-1} números')
print('La suma de los números es:', suma)
print(f'El promedio es {suma/(cont-1)} números')
print(f'El mayor es {mayor}')
print(f'el menor es´{menor}' )

#la funcion es en listar los numeros pedido y  sumarlos despues dividir y dar un promedio 
#y mostrar cual es mayo o menor 

