from time import sleep
import random
lista = ('PEDRA','PAPEL','TESOURA')
a2 = random.choice(lista)
print('\033[1;34m-=\033[m'*10)
print(' [1] PEDRA\n [2] PAPEL\n [3] TESOURA')

a1 = int(input('Qual sua opção?'))
print('O computador escolheu \033[1;34m{}\033[m'.format(a2))
print('\033[1;34m-=\033[m'*10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[1;34m-=\033[m'*10)

if a1 == 3 and a2 == 'PAPEL':
    print('\033[1;32mVocê ganhou!\033[m')
elif a1 == 2 and a2 == 'PEDRA':
    print('\033[1;32mVocê ganhou!\033[m')
elif a1 == 1 and a2 == 'TESOURA':
    print('\033[1;32mVocê ganhou!\033[m')
elif a1 == 1 and a2 == 'PEDRA':
    print('EMPATE')
elif a1 == 2 and a2 == 'PAPEL':
    print('EMPATE')
elif a1 == 3 and a2 == 'TESOURA':
    print('EMPATE')
else:
    print('\033[1;31mVOCÊ PERDEU\033[m')