c = cont = soma = 0
while c != 999:
    num = int(input('Digite um número:'))
    cont += 1
    if num == 999:
        break
    soma += num
print(f'o resultado da soma de todos os {cont-1} números foi {soma}')