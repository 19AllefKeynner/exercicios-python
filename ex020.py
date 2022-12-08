from random import shuffle
a1 = str(input('aluno 1:'))
a2 = str(input('aluno2:'))
a3 = str(input('aluno 3:'))
a4 = str(input('aluno 4:'))
lista = [a1, a2, a3 ,a4]
shuffle(lista)
print('a ordem de apresentacao ser:')
print(lista)
