from random import randint

LI = randint(0,10)
acertou = False
palp = 0
while not acertou:
    jogador = int(input('Qual seu palpite?'))
    palp += 1
    if jogador == LI:
        acertou = True
    else:
        if jogador < LI:
            print('Mais...')
        elif jogador > LI:
            print('Menos...')
        elif LI == jogador:
            acertou = True

print('Parabêns vc acertou!')