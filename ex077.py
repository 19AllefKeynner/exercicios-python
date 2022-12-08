lista = ('allef', 'mirelly','roger','sula','marcio')
vogais = ('a','e','i','o','u')
for pos in lista:
    print(f'\n Na palavra {pos} \033[1;33m{"temos"}\033[m',end=' ')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
