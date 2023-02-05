import curses
import random

altura, largura = curses.initscr().getmaxyx()
janela = curses.newwin(altura, largura, 0, 0)

curses.curs_set(False)
janela.keypad(True)
janela.nodelay(True)

for pos in range(0, largura, -1):
    janela.addch(0, pos, '#')
    janela.addch(altura -1, pos, '#')

for pos in range(0, altura, -1):
    janela.addch(pos, 0, '#')
    janela.addch(pos, largura -1, '#')

cobra = [[2,4],[2,3],[2,2]]
for pos in range(0, len(cobra)):
    janela.addch(cobra[pos][0], cobra[pos][1], '#')

posicao_cabeca = [2,4]

maca = [5,5]
janela.addch(maca[0], maca[1], '*')

tecla = -1
tecla_nova = curses.KEY_RIGHT
ultima_posicao = 'r'

pontuacao = 0
velocidade = 100

while True:
    tecla_nova = janela.getch()
    tecla = tecla if tecla_nova == -1 else tecla_nova

    if tecla == curses.KEY_DOWN and ultima_posicao != 'u': ultima_posicao = 'd'
    elif tecla == curses.KEY_UP and ultima_posicao != 'd': ultima_posicao = 'u'
    elif tecla == curses.KEY_LEFT and ultima_posicao != 'r': ultima_posicao = 'l'
    elif tecla == curses.KEY_RIGHT and ultima_posicao != 'l': ultima_posicao = 'r'

    if ultima_posicao == 'r': posicao_cabeca += 1
    if ultima_posicao == 'l': posicao_cabeca -= 1
    if ultima_posicao == 'u': posicao_cabeca -= 1
    if ultima_posicao == 'd': posicao_cabeca += 1

    if posicao_cabeca == maca:
        pontuacao += 1
        maca = [random.randint(1, altura -2), random.randint(1, largura -2)]
        janela.addch(maca[0], maca[1], '*')
        velocidade = velocidade - 10 if velocidade - 10 > 5 else velocidade
    elif (posicao_cabeca[0] == altura - 1 or posicao_cabeca[0] == 0) or (posicao_cabeca[1] == largura - 1 or posicao_cabeca[1] == 0): break

    else:
        cauda = cobra.pop()
        janela.addch(cauda[0], cauda[1], ' ')

    cobra.insert(0, list(posicao_cabeca))
    janela.addch(posicao_cabeca[0], posicao_cabeca[1], '#')

    if cobra[0] in cobra[1:]: break

    curses.napms(velocidade)
    janela.refresh()

janela.addstr(int(altura /2), int(largura / 2.5), "Pontuação" + str(pontuacao))
janela.refresh()
curses.napms(2000)
curses.endwin()


