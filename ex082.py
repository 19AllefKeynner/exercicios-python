pares = []
todos = []
impares = []
while True:
    a = int(input('Digite um número:'))
    todos.append(a)
    if a % 2 == 0:
        pares.append(a)
    else:
        impares.append(a)
    opcao = str(input('Quer continuar? S/N ')).upper().strip()[0]
    if opcao == 'N':
        break
todos.sort()
pares.sort()
impares.sort()
print(f'\033[1;34mTodos os números digitados foram:\033[1;32m{todos}\033[m')
print(f'\033[1;34mA lista para números pares foram: \033[1;32m{pares}\033[m')
print(f'\033[1;34mA lista para números ímpares foram: \033[1;32m{impares}\033[m')