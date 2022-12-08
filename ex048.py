s = 0
cont = 0
A = int(input('Onde quer começar?'))
B = int(input('Onde termina?'))
C = int(input('De quantos em quantos?'))
for i in range(A,B,C):
    if i %3 == 0:
        cont = cont + 1
        s = s + i
print('\033[1;36mO resultado da soma desses {} valores foi = {}\033[m'.format(cont,s))