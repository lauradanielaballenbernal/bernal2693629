num = 1
cont = 0
suma = 0

while num != 0:
  num = int(input('Ingrese número: '))
  cont += 1
  suma += num

print(f'El usuario ingresó {cont} números')
print('La suma de los números es:', suma)

