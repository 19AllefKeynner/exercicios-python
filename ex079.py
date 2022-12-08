lista = list()
p = 1
while True:
    n = input('Digite um número:')
    if n not in lista:
        lista.append(n)
    else:
        print('Esse número já existe em lista, não vou adicionar!')

    opcao = str(input('Quer continuar? [S/N]')).upper().strip()
    if opcao == 'N':
       break
print(sorted(lista))