Frase = str(input('Digite uma frase:')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(Frase.count('A')))
print('A primeira letra A aparece na posicao {}'.format(Frase.find('A')+1))
print('A ultima letra A aparece na posicao {}'.format(Frase.rfind('A')+1))