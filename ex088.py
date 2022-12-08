import random
from time import sleep
numeros = []
sorteio = []
lista = []
cont = 1
for c in range(1,61):
    lista.append(c)
print('-='*15)
print(f'\033[1;33m{"JOGAR NA MEGA SENA":^30}\033[m')
print('-='*15)
opcao = int(input('\033[1;33mQuantos sorteios quer fazer hoje?\033[m'))
sleep(1)
print('',f'\n{"-="*3}\033[1;33mSORTEANDO NÚMEROS\033[m{"-="*3}')
sleep(1)
for c in range(0,opcao):
    for e in range(0,6):
        a = random.choice(lista)
        if a not in sorteio:
            sorteio.append(a)
        if e == 5:
            numeros.append(sorteio[:])
            sorteio.clear()
    print(f'\033[1;34mJogo {c+1}: {numeros[c]}\033[m')
    sleep(1)
print(f'{"=-"*5}\033[1;33mBOA SORTE\033[m{"-="*5}')
