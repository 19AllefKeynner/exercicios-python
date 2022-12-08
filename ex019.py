import random
n1 = int(input('primeiro numero:'))
n2 = int(input('segundo numero:'))
n3 = int(input('terceiro numero:'))
n4 = int(input('quarto numero:'))
lista = [n1, n2 ,n3, n4]
E = random.choice (lista)
print('o numero escolhido {}'.format(E))
