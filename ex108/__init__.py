def metade(n=0):
    m = n // 2
    return m


def aumentar(n=0, p=0):
    porc = n * p / 100
    aum = n + porc
    return aum


def diminuir(n=0, p=0):
    porc = n * p / 100
    dim = n - porc
    return dim


def fatorial(n=0):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f

def dobro(n=0):
    d = n + n
    return d

def dinheiro(a=0, moeda='R$'):
    return f'{moeda}{a:.2f}'.replace('.',',')