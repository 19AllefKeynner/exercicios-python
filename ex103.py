def jogador(nome=0 , gols=0):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = '0'
    if gols <= '999':
        ''
    else:
        gols = '0'
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


a = str(input('Nome do jogador: '))
b = str(input('Quantos gols? '))
jogador(a,b)