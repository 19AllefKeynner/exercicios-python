def area(l, c):
    s = l * c
    print(f'O comprimento do seu terreno {l} x {c} é de {s}m² ')

print(' CONTROLE DE TERRENO')
print('=-'*11)
l = float(input('Largura (M) '))
c = float(input('Comprimento (M) '))
area(l, c)


