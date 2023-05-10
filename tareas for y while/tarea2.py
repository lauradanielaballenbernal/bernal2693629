def NumeroPerfecto(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma == num
   
Perfect_Number = []

for i in range(1, 1001):
    if NumeroPerfecto(i):
          Perfect_Number.append(i)
          
print("Hay", len(Perfect_Number), "números perfectos entre 1 y 1000, que son:", Perfect_Number)
