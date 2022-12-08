tupla = ('ZERO','UM','DOIS','TRÊS','QUATRO','CINCO',
         'SEIS','SETE','OITO','NOVE')
while True:
    num = int(input('Digite um número entre 0 e 9:'))
    if 0<= num <=9:
        break
    print('Número errado tente novamente...',end='')
print(f'Você digitou o número \033[1;34m{tupla[num]}\033[m')

