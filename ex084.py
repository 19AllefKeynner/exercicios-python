pessoa = []
lista = []
maior = menor = c = 0
while True:
    pessoa.append(str(input('Qual seu nome?')).strip().title())
    pessoa.append(float(input('Qual seu peso?')))
    if len(lista) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
             maior = pessoa[1]
        if pessoa[1] < menor:
             menor = pessoa[1]
    opcao = str(input('Quer continuar S/N?')).strip()[0]
    lista.append(pessoa[:])
    pessoa.clear()
    if opcao in 'nN':
        break

print(f'\033[1;33mVocê cadastrou {len(lista)} pessoas!\033[m')
print(f'\033[1;33mO menor peso foi {menor} e foi de\033[m',end=' ')
for p, v in enumerate(lista):
    if v[1] == menor:
        print(f'\033[1;34m[{lista[p][0]}]\033[m',end=' ')
print(f'\033[1;33m\nO maior peso foi {maior} e foi de\033[m',end=' ')
for p, v in enumerate(lista):
    if v[1] == maior:
        print(f'\033[1;34m[{lista[p][0]}]\033[m',end=' ')



