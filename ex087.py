tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
resultado = maior = 0
for l in range(0,3):
    for c in range(0,3):
        tabela[l][c] = int(input(f'Digite um número para [{l}, {c}]'))
        if tabela[l][c] % 2 == 0: pares.append(tabela[l][c])
print('\033[1;33m-=TABELA=-\033[m')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{tabela[l][c]:^5}]',end='')
    print('')
print('')
o = 0
for c in pares:
    resultado += pares[o]
    o += 1
print(f'\033[1;33mA soma de todos números pares foi {resultado}\033[m')
print(f'\033[1;33mA soma dos valores da terceira coluna foi {tabela[0][2] + tabela[1][2] + tabela[2][2]}\033[m')
for v in range(0,3):
    if v == 0: maior = tabela[1][v]
    else:
        if tabela[1][v] > maior: maior = tabela[1][v]
print(f'\33[1;33mO maior valor da segunda fila foi {maior}\033[m')
