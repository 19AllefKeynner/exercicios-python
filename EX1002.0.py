from random import randint
from time import sleep

print('Sorteanddo 5 valores...')
print('-='*30)
sleep(2.5)
def sorteio(lista):
    print(f'Os números sorteados foram...',end=' ')
    for c in range(0,5):
        n = randint(1,10)
        lista.append(n)
    for v in numeros:
        print(f'{v}',end=' ')
        sleep(0.5)


def somapares(pares):
    for v in numeros:
        if v % 2 == 0:
            pares.append(v)
    print(f'\nOs valores pares digitados foram {pares} e a soma desses valores foi {sum(pares)}')


numeros = list()
lista = list()
sorteio(numeros)
somapares(lista)
print('-='*30)
