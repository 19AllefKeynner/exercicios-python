lista = ('Borracha',1.90,
         'Lápis',5,
         'Caneta',1,
         'Estojo',25,
         'Hidrocor',30)
cont = 0

print('-='*20)
print('TABELA DE PREÇOS')
print('-='*20)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='R$')
    else:
        print(f'{lista[pos]:>7.2f}')
