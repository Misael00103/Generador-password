import random

n=int(input('Entra el tamaño que necesitas de tu contaseña:1'))

def passwordGenerator(n):

    #Definir strings

    lower='abcdefghijklmnñopqrstuvwxyz'
    upper='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    number='0123456789'
    special='!@#$%&*'

    password=''
   

    for i in range(n):
        l=[random.choice(lower),random.choice(upper),random.choice(number),random.choice(special)]
        password=password+random.choice(l)
         
    return password
print('Tu contraseña aleatoria es :',passwordGenerator(n))