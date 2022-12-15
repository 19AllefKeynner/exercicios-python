def fatorial(n, show = 0):
    """
    >> Calcula o fatorial de um número!
    :param n: O número a ser calculado!
    :param show: (Opcional) Show 0 não mostra calculo e Show 1 mostra!
    :return: sem retorno!
    """
    f = 1
    for c in range(n, 0, -1):
        if show == 1:
            print(f'{c}',end=' ')
            if c > 1:
                print(' x ',end=' ')
            else:
                print(f' = {f} ',end='  ')
        f*=c
    if show == 0:
            print(f)


a = int(input('Número:'))
b = int(input('Digite (1) para mostrar calculo e (0) para não mostrar;'))
fatorial(n=a, show=b)
print('\n')
