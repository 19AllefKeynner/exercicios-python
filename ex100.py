from random import randint
from time import sleep
lista = []
print(f'Sorteando 5 valores... ',end='')


def sorteio(a):
        print(f'{a}',end=' ')
        lista.append(a)
        sleep(0.5)


for c in range(1,6):
    sorteio(randint(1,6))
sleep(2.5)
print(f'\nOs números pares são',end=' ')
pares = []


def soma(num):
    pares.append(num)


for c in lista:
    if c % 2 == 0:
        soma(c)
print(f'{pares}',end=',')
sleep(0.5)
print(f' temos: {sum(pares)}')