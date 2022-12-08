nuns = list()
maior = 0
menor = 0
for n in range(0,5):
    nuns.append(int(input(f'Digite um número para a posição {n}:')))
    if n == 0:
        menor = maior = nuns[n]
    else:
        if nuns[n] > maior:
            maior = nuns[n]
        if nuns[n] < menor:
            menor = nuns[n]
print(f'Você digitou {nuns}')
print(f'O menor número foi {menor} e apareceu nas posições',end=' ')
for c, v in enumerate(nuns):
    if v == menor:
        print(f'{c}...',end=' ')
print(f'\nO maior número foi {maior} e apareceu nas posições',end=' ')
for c, v in enumerate(nuns):
    if v == maior:
        print(f'{c}...',end=' ')