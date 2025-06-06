import random
from os import system
from msvcrt import getch

lista=[]

for i in range(0,100):
    lista.append(random.randint(0,100))
    print(lista[i])


for num in lista:
    if num %2==0:
        print(num)



print(f'los numeros par son {num}')
print(f'el numero maximo es {max(lista)}')
print(f'el numero minimo es {min(lista)}')
print(f'la posicion del elemmento mayor es {lista.index(max(lista))}')




