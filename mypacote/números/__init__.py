def dobro(n):
    d = n + n
    return d


def metade(n):
    m = n // 2
    return m


def aumentar(n, p):
    porc = n * p / 100
    aum = n + porc
    return aum


def diminuir(n, p):
    porc = n * p / 100
    dim = n - porc
    return dim


def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f