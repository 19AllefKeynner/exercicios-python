num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('\033[1;34mQual o número? [999 para parar]\033[m'))
    if num != 999:
        soma += num
        cont += 1
print('\033[1;32mVocê digitou {} números e a soma entre eles foi de {}!\033[m'.format(cont,soma))
print('\033[1;32mVocê digitou {} númeoros!\033[m'.format(cont))
