tabela = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        tabela[l][c] = int(input(f'Escreva um número para [{l}, {c}]'))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{tabela[l][c]:^5}]',end='')
    print('')

