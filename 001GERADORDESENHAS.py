#Deixa o programa mais bonito!

import random
from time import sleep
abc = ['a','E','b','A','c','D','d','C','e','B']
num = [1,2,3,4,5,6,7,8,9,0]
simb = ['@','#','&']
six = random.randint(10,99)
senha = []

print('GERADOR DE SENHAS')
tamanho = int(input('Qual o tamanho da senha? 4,6 ou 8 dígitos:'))
if tamanho != 4 and tamanho != 6 and tamanho != 8:
    while True:
        print('\033[1;31mERRO, digite um tamanho de senha inválido!\033[m')
        tamanho = int(input('Digite o tamanho da senha! 4,6 ou 8 dígitos:'))
        if tamanho == 4 or tamanho == 6 or tamanho == 8:
            break
if tamanho == 4:
    a = random.choice(abc)
    senha.append(a)
    b = random.choice(num)
    senha.append(b)
    c = random.choice(abc)
    senha.append(c)
    d = random.choice(simb)
    senha.append(d)
    print('')
    print('Gerando sua senha', end=' '), sleep(1), print('(•', end=''), sleep(1), print('•', end=''), sleep(1), print('•)')
    print('Sua senha: ', end='')
    for c in senha:
        print(f'{c}', end='')
    print('\n')
    opc = int(input('Deseja gerar outra senha: (0 para NÃO, 1 para SIM)'))
    while opc == 1:
        senha.clear()
        a = random.choice(abc)
        senha.append(a)
        b = random.choice(num)
        senha.append(b)
        c = random.choice(abc)
        senha.append(c)
        d = random.choice(simb)
        senha.append(d)
        print('')
        print('Gerando sua senha', end=' '), sleep(1), print('(•', end=''), sleep(1), print('•', end=''), sleep(1), print('•)')
        print('Sua senha: ', end='')
        for c in senha:
            print(f'{c}', end='')
        print('\n')
        opc = int(input('Deseja gerar outra senha: (0 para NÃO, 1 para SIM)'))
        if opc == 0:
            break
    print('Até logo!')

elif tamanho == 6:
    a = random.choice(abc)
    senha.append(a)
    b = random.choice(num)
    senha.append(b)
    c = random.choice(abc)
    senha.append(c)
    d = random.choice(simb)
    senha.append(d)
    senha.append(six)
    print('')
    print('Gerando sua senha', end=' '), sleep(1), print('(•', end=''), sleep(1), print('•', end=''), sleep(1), print('•)')
    print('Sua senha: ',end='')
    for c in senha:
        print(f'{c}', end='')
    print('\n')
    opc = int(input('Deseja gerar outra senha: (0 para NÃO, 1 para SIM)'))
    while opc == 1:
        senha.clear()
        a = random.choice(abc)
        senha.append(a)
        b = random.choice(num)
        senha.append(b)
        c = random.choice(abc)
        senha.append(c)
        d = random.choice(simb)
        senha.append(d)
        senha.append(six)
        print('')
        print('Gerando sua senha', end=' '), sleep(1), print('(•', end=''), sleep(1), print('•', end=''), sleep(1), print('•)')
        print('Sua senha: ', end='')
        for c in senha:
            print(f'{c}', end='')
        print('\n')
        opc = int(input('Deseja gerar outra senha: (0 para NÃO, 1 para SIM)'))
        if opc == 0:
            break
    print('Até logo!')


else:
    print('Ainda não temos essa opção! Desculpe.')

