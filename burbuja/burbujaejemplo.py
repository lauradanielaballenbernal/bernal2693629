import random
list=[]
tam=int(random.randint(5,10))
#print(tam)
for i in range (tam):
     num=int(random.randrange(100))
     list.append(num)
print(list)

for i in range(len(list)):
     for j in range(i+1,tam):
          if list[i]>list[j]:
               aux=list[i]
               list[i]=list[j]
               list[j]=aux
print(list)
#el programa va a dar factores desorganisados pero al ingresar el comando
# va a organizar los factores de menor a mayo
# si queremos que lo organice de mayor a menor si,plemente se le cambia el signo            
               
