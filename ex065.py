from time import sleep
print('\033[1;32m-=\033[m'*20)
print('\033[1;32mDigite um valor para analizar!      -=-=\033[m')
print('\033[1;32m-=\033[m'*20)
sleep(2)
opcao = 'S'
cont = 0
soma = 0
menor = 0
maior = 0
while opcao == 'S':
    num = int(input('\033[1;34mDigite um número:\033[m'))
    soma += num
    cont += 1
    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        else:
            if num < maior:
                menor = num
    opcao = str(input('\033[1;34mQuer continuar?\033[m [S/N]')).strip().upper()
media = (soma / cont)
sleep(2)
print('')
print('\033[1;32mAnalizando\033[m',end='')
sleep(1)
print('\033[1;32m.\033[m',end='')
sleep(1)
print('\033[1;32m.\033[m',end='')
sleep(1)
print('\033[1;32m.\033[m')
sleep(2)
print('\033[1;34mVocê digitou {} números e a média foi de {:.2f}\033[m!'.format(cont,media))
sleep(1)
print('\033[1;34mA soma de todos os {} números digitados foi {}!\033[m'.format(cont,soma))
sleep(1)
print('\033[1;34mO menor númro digitado foi {} e o maior foi {}\033[m'.format(menor,maior))
print('\033[1;32mFIM!\033[m')