tot = 0
dic = {}
golsp = []
nome = str(input('Nome do jogador: ')).strip().title()
dic['Nome'] = nome
part = int(input(f'Quantas partidas o jogador {nome} jogou? '))
for c in range(0,part):
    gols = (int(input(f'Quantos gols na partida {c} ')))
    golsp.append(gols)
    dic['Gols'] = golsp[:]
    tot += gols
dic['Total'] = tot
print('-='*30)
print(dic)
print('=-'*30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor de {v}')
print('-='*30)
print(f'O jogador {nome} jogou {part} partidas')
for c in range(0,part):
    print(f'>> Na partida {c}, {dic["Gols"][c]} gols.')
print(f'Sendo o total de {tot} gols')
print('=-'*30)