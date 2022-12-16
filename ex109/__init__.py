
import textos

def metade(n=0,formate=False):
    m = n // 2
    return m if formate is False else dinheiro(m)


def aumentar(n=0, p=0,formate=False):
    porc = n * p / 100
    aum = n + porc
    return aum if formate is False else dinheiro(aum)


def diminuir(n=0, p=0,formate=False):
    porc = n * p / 100
    dim = n - porc
    return dim if formate is False else dinheiro(dim)


def fatorial(n=0,formate=False):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f if formate is False else dinheiro(f)


def dobro(n=0,formate=False):
    d = n + n
    return d if formate is False else dinheiro(d)


def dinheiro(a=0, moeda='R$'):
    return f'{moeda}{a:.2f}'.replace('.',',')