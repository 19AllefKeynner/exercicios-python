num = int(input('Digite um número:'))
tot = 0
for e in range(1,num+1,1):
    if num % e ==0:
        print('\033[1;31m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{}'.format(e), end=' ')
print('\033[m')
if tot == 2:
    print('{} foi divisível por {}, sendo assim ele é \033[1;32mPRIMO!!!\033[m '.format(num,tot))
else:
    print('{} foi divisível por {}, sendo assim ele \033[1;31mNÃO é PRIMO!!!\033[m'.format(num,tot))