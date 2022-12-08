par = 0
n = (int(input('Digite um número:')),int(input('Digite o segundo número:')),int(input('Terceiro número:')),int(input('Ultimo número:')))
print(f'\033[1;35mVocê digitou os números:\033[m \033[1;34m{n}\033[m')
print(f'\033[1;35mO valor 5 apareceu {n.count(5)} vezes!\033[m')
if 2 in n:
 print(f'\033[1;35mO valor 2 apareceu na {n.index(2)+1}ª posição!\033[m')
else:
    print('\033[1;35mO valor 2 não foi digitado!\033[m')
print('\033[1;35mOs números pares foram:\033[m',end=' ')
for n in n:
    if n % 2 == 0:
        print(f'\033[1;34m{n}\033[m',end=' ')
        par += 1
print(f'\033[1;35me no total foram\033[m \033[1;34m{par}\033[m \033[1;35mnúmeros pares!\033[m')
