import random
from textos import titulo
from time import sleep

desafios = ['Dar uma volta fora de casa sem casaco',
'Pular na piscina',
'Tomar uma ducha de roupa',
'Encenar o trecho de uma novela ou filme',
'Fazer o máximo de flexões em 1 minuto',
'Fazer um elogio na festa ou na rua',
'Escolher uma música e cantar até o final sem errar',
'Engolir um gelo em menos de 1 minuto',
'Passar uma rodada brincando com os olhos tapados',
'Ficar falando como se fosse uma blogueira até o final da brincadeira',
'Mastigar um alho cru',
'Tomar 1 litro de água no menor tempo possível',
'Chupar 1 limão como se fosse uma laranja docinha',
'Segurar apertando um cubo de gelo até ele derreter completamente',
'Enfiar uma colher de farofa na boca e ficar falando de boca cheia sobre o quanto você ama farofa',
'Arrotar o alfabeto',
'Fazer uma pose de yoga e ficar parado nela por 10 segundos',
'Engolir gás hélio, falar com a voz engraçada e não rir',
'Tentar acomodar o máximo possível de marshmallows, uvas ou outros snacks do tipo dentro da boca',
'Colocar o pé atrás da cabeça',
'Comer uma bolacha doce recheada com mostarda e ketchup sem fazer cara de nojo',
'Tomar água de um potinho como se fosse um cachorro']

while True:
    print('\033[1;33m'), print(titulo('SORTEANDO DESAFIO')), print('\033[m',end='')
    print('\033[1;37mSeu desafio é',end=''), sleep(1)
    print('.',end=''), sleep(1), print('.',end=''), sleep(1), print('.'), sleep(1)
    a = random.choice(desafios)
    print(f'\033[1;33m{a}\033[m')
    opcao = str(input('\033[1;37mQuer sortear outro desafio? S/N ')).strip().upper()[0]
    if opcao == 'N':
        break
