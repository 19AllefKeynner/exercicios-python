import random
print('------|Estou pensando em um numero, tente adivinhar|------')
f = int(input('Digete um numero de 1 a 9:'))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e = random.choice (lista)
if f == e:
    print('Parabens vc acetou!!!')

else:
    print('Desculpa nao foi dessa vez! :(')


