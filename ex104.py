def leianum(a):
    n = input(a)
    if n.isnumeric():
        return n
    else:
        while True:
            print('\033[1;31mERRO!\033[m')
            n = input(a)
            if n.isnumeric():
                break
        return n


r = leianum('Digite um número: ')
print(f'Vc acabou de digitar {r}')