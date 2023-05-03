import random
list=[]
tam=int(random.randint(10,20))
print(tam)
for i in range (tam):
     num=int(random.randrange(100))
     list.append(num)

print(list)