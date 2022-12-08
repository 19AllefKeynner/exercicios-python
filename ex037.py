numero = int(input('Digite um número inteiro?'))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O número {} convertido pra binário é {}'.format(numero,bin(numero)))
elif opção ==2:
    print('O número {} convertido para octal é {}'.format(numero,oct(numero)))
elif opção ==3:
    print('O número {} convertido para hexadecimal é {}'.format(numero,hex(numero)))
else:
    print('Opção invalida, tente novamente!!!')