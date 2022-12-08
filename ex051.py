print('='*30)
print('\033[1;32m10 TERMOS DE UMA PA\033[m')
print('='*30)
a = int(input('PRIMEIRO TERMO:'))
b = int(input('RAZÃO:'))
C = a + (10-1) * b
for i in range(a,C,b):
    print(i,'>', end=' ')
print('ACABOU')