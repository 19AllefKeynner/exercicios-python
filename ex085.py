valor = [[],[]]
for c in range(0,7):
    a = int(input(f'Digite o {c+1}º valor:'))
    if a % 2 == 0:
        valor[0].append(a)
    elif a % 2 == 1:
        valor[1].append(a)
valor[1].sort()
valor[0].sort()
print(f'\033[1;33mOs valores ímpares foram \033[1;34m{valor[1]}\033[m')
print(f'\033[1;33mOs valores pares foram \033[1;34m{valor[0]}\033[m')