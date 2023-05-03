x=5
y=3
flag=False
while not (x%y==0 or y%x==0):
    print('rutina para saber si dos numeros son factor')
    x= int(input('ingrese numero'))
    y= int(input('ingrese numero'))

print('son factor')

# el while no se sabe cuanto se va a repetir el factor 
# este dejara de repetirce cuando el factor sea de ambos valores y hay terminara el programa 
# al notar que no son factor mandara un mensaje que dice rutina para saber si dos numeros son factor
