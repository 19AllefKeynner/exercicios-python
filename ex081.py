lista = list()
cont = 0
while True:
    lista.append(input('Adicione um número:'))
    cont += 1
    opcao = str(input('Quer continuar?')).strip()
    if opcao in 'nN':
        break
print(f'\033[1;34mVocê digitou {cont} números e são:\033[m \033[1;32m{lista}\033[m')
lista.sort(reverse= True)
print(f'\033[1;34mOs números na ordem decrescente são:\033[m \033[1;32m{lista}\033[m')
if lista.count('5') >= 1:
    print('\033[1;34mO númer 5 está presente na lista!\033[m')
else:
    print('\033[1;34mO número 5 não está presente na lista!\033[m')

