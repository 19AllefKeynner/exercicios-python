from time import sleep
from random import randint
from operator import itemgetter
dic = {'Jogador1': randint(0, 11),
       'Jogador2': randint(0,11),
       'Jogador3': randint(0,11),
       'Jogador4': randint(0,11)}
for k, v in dic.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-='*30)
print('\033[1;33m== RANKING DOS JOGADORES ==\033[m')
resl = sorted(dic.items(), key=itemgetter(1), reverse=True)
for k in range(0,4):
    print(f'{k+1}º Lugar: {resl[k][0]} com {resl[k][1]}')
