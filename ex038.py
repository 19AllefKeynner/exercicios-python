n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número:'))
if n1 > n2:
    print('O número maior é {}'.format(n1))
elif n1 == n2:
    print('Ambos são iguais!')
elif n1 < n2:
    print('O número {} é maior!'.format(n2))