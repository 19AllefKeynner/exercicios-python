def leiareal(a):
    while True:
        try:
            n = float(input(a))
        except ValueError as TypeError:
            print('\033[1;31mERRO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mPrograma fechado pelo usuário!\033[m')
            return 0
        else:
            return n



def leiaint(a):
    while True:
        try:
            n = int(input(a))
        except ValueError as TypeError:
            print('\033[1;31mERRO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mPrograma fechado pelo usuário!\033[m')
            return 0
        else:
            return n


r = leiaint('Digite um número inteiro: ')
re = leiareal('Digite um número real: ')
print(f'O número inteiro foi {r} e o número real foi {re}!')