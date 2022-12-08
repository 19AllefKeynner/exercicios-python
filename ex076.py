lista = ('Borracha',1.90,
         'Lápis',5,
         'Caneta',1,
         'Estojo',25,
         'Hidrocor',30)
cont = 0

print('-='*15)
print('TABELA DE PREÇOS')
print('-='*15)

for l in lista:
    print(l,end=' ')
    cont += 1
    if cont == 1:
        print('........R$ ',end='')
    if cont == 2:
        print(end='\n')
    if cont == 3:
        print('...........R$ ',end='')
    if cont == 4:
        print(end='\n')
    if cont == 5:
        print('..........R$ ',end='')
    if cont == 6:
        print(end='\n')
    if cont == 7:
        print('..........R$ ',end='')
    if cont == 8:
        print(end='\n')
    if cont == 9:
        print('........R$ ',end='')
print(' ')