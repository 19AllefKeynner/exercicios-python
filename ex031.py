V = int(input('Qual a distãncia da viagem?'))
print('Vc esta prestes a iniciar uma viagem de {} km'.format(V))
if V <= 200:
    print('O valor da passagem é: R${}'.format(V*0.50))
else:
    print('O valor da passagem é: R${}'.format(V*0.45))