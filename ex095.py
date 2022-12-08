dic = {}
gols = []
list = []
while True:
    dic['Nome'] = str(input('Nome do jogador: ')).strip().title()
    part = int(input(f'Quantas partidas {dic["Nome"]} jogou? '))
    for c in range(0,part):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dic['Gols'] = gols[:]
    dic['total'] = sum(gols)
    gols.clear()
    list.append(dic.copy())
    opc = str(input('Quer continuar? S/N ')).strip().upper()
    while opc != 'N' and opc != 'S':
        print('\033[1;31mERRO, digite apenas S ou N\033[m')
        opc = str(input('Quer continuar? S/N ')).strip().upper()
    if opc == 'N':
        break
print('=-'*30)
print('  CODNOME            GOLS          TOTAL')
print('-'*60)
for k, v in enumerate(list):
    print(f'{k:>3} ',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end=' ')
    print()
print('-='*30)
cont = 0
while True:
    a = int(input('Qual Jogador quer ver? (999 pra parar)'))
    if a >= 0 and a < len(list):
        print(f'Exibindo levantamento do jogador',end=' ')
        print(f'{list[a]["Nome"]}')
        for c in list[a]["Gols"]:
            print(f'Na partida {cont} fez {c} gols.')
            cont += 1

    elif a >= len(list) and a != 999:
        print('\033[1;31mERRO, Jogador nn existe na lista\033[m')

    elif a == 999:
        break