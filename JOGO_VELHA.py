# Melhorar cores
# Criar função pra quando o jogo da velha
# Criar função pra contar quantas vezes cada jogador venceu
# Criar função pra jogar denovo
import playsound
import random
from time import sleep
from tkinter import *
JOGADOR = [1]

VENCEU_COLU1 = []
VENCEU_COLU2 = []
VENCEU_COLU3 = []

VENCEU_LIN1 = []
VENCEU_LIN2 = []
VENCEU_LIN3 = []

TRANSVERSAL1 = []
TRANSVERSAL2 = []


def botao1():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=0, row=0)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_COLU1.append('x')
        VENCEU_LIN1.append('x')
        TRANSVERSAL1.append('x')

        if VENCEU_LIN1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)


    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=0, row=0)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_COLU1.append('o')
        VENCEU_LIN1.append('o')
        TRANSVERSAL1.append('o')
        if VENCEU_LIN1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1a WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

def botao2():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=1, row=0)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN1.append('x')
        VENCEU_COLU2.append('x')
        if VENCEU_LIN1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=1, row=0)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN1.append('o')
        VENCEU_COLU2.append('o')
        if VENCEU_LIN1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)


def botao3():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=2, row=0)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN1.append('x')
        VENCEU_COLU3.append('x')
        TRANSVERSAL2.append('x')
        if VENCEU_LIN1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU3.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=2, row=0)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN1.append('o')
        VENCEU_COLU3.append('o')
        TRANSVERSAL2.append('o')
        if VENCEU_LIN1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU3.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)




def botao4():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=0, row=1)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN2.append('x')
        VENCEU_COLU1.append('x')
        if VENCEU_LIN2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=0, row=1)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN2.append('o')
        VENCEU_COLU1.append('o')
        if VENCEU_LIN2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

def botao5():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=1, row=1)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN2.append('x')
        VENCEU_COLU2.append('x')
        TRANSVERSAL1.append('x')
        TRANSVERSAL2.append('x')
        if VENCEU_LIN2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=1, row=1)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN2.append('o')
        VENCEU_COLU2.append('o')
        TRANSVERSAL1.append('o')
        TRANSVERSAL2.append('o')
        if VENCEU_LIN2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

def botao6():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=2, row=1)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN2.append('x')
        VENCEU_COLU3.append('x')
        if VENCEU_LIN2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU3.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=2, row=1)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN2.append('o')
        VENCEU_COLU3.append('o')
        if VENCEU_LIN2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU3.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

def botao7():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=0, row=2)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN3.append('x')
        VENCEU_COLU1.append('x')
        TRANSVERSAL2.append('x')
        if VENCEU_LIN3.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=0, row=2)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN3.append('o')
        VENCEU_COLU1.append('o')
        TRANSVERSAL2.append('o')
        if VENCEU_LIN3.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

def botao8():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=1, row=2)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN3.append('x')
        VENCEU_COLU2.append('x')
        if VENCEU_LIN3.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU2.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=1, row=2)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_LIN3.append('o')
        VENCEU_COLU2.append('o')
        if VENCEU_LIN3.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU2.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

def botao9():
    if sum(JOGADOR) % 2 == 0:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="X", width=10, height=5, bg='#d43d3d')
        texto_calculo.grid(column=2, row=2)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 1", width=25, height=5, bg='#3f1ae6')
        texto_tela.grid(column=3, row=1)
        VENCEU_COLU3.append('x')
        VENCEU_LIN3.append('x')
        TRANSVERSAL1.append('x')
        if VENCEU_LIN3.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU3.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL1.count('x') == 3:
            texto_tela2 = Button(janela, text="PLAYER 2 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
    else:
        JOGADOR.append(1)
        texto_calculo = Label(janela, text="O", width=10, height=5, bg='#3f1ae6')
        texto_calculo.grid(column=2, row=2)
        texto_tela = Button(janela, text="VEZ DO JOGADOR 2", width=25, height=5, bg='#d43d3d')
        texto_tela.grid(column=3, row=1)
        VENCEU_COLU3.append('o')
        VENCEU_LIN3.append('o')
        TRANSVERSAL1.append('o')
        if VENCEU_LIN3.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if VENCEU_COLU3.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)
        if TRANSVERSAL1.count('o') == 3:
            texto_tela2 = Button(janela, text="PLAYER 1 WIN", width=25, height=5, bg='#8d9ae6')
            texto_tela2.grid(column=3, row=2)

listacor = ['#7474ff','#ff7474','#7474ff','#ff7474','#7474ff','#ff7474','#7474ff','#ff7474']
a = random.choice(listacor)

janela = Tk()
janela.geometry("510x320")
janela.title("JOGO DA VELHA")
janela.config(bg=f'{a}')

texto_tela1 = Button(janela, text='JOGADOR 1: 0 PONTOS\nJOGADOR 2: 0 PONTOS', width=25, height=5, bg='#656363',relief='ridge')
texto_tela1.grid(column=3, row=0)

texto_tela = Button(janela, text="JOGADOR 1 COMEÇA", width=25, height=5, bg='#3f1ae6',relief='ridge')
texto_tela.grid(column=3, row=1)

texto_tela2 = Button(janela, text="", width=25, height=5, bg='#656363',relief='ridge')
texto_tela2.grid(column=3, row=2)


botaoa = Button(janela, width=10, height= 5, command=botao1)
botaoa.grid(column=0, row=0, padx=10, pady=10, )

botaob = Button(janela, width=10, height= 5,command=botao2)
botaob.grid(column=1, row=0, padx=10, pady=10, )

botaoc = Button(janela, width=10, height= 5,command=botao3)
botaoc.grid(column=2, row=0, padx=10, pady=10, )


botaod = Button(janela, width=10, height= 5,command=botao4)
botaod.grid(column=0, row=1, padx=10, pady=10, )

botaoe = Button(janela, width=10, height= 5,command=botao5)
botaoe.grid(column=1, row=1, padx=10, pady=10, )

botaof = Button(janela, width=10, height= 5,command=botao6)
botaof.grid(column=2, row=1, padx=10, pady=10, )


botaog = Button(janela, width=10, height= 5,command=botao7)
botaog.grid(column=0, row=2, padx=10, pady=10, )

botaoh = Button(janela, width=10, height= 5,command=botao8)
botaoh.grid(column=1, row=2, padx=10, pady=10, )

botaoi = Button(janela, width=10, height= 5,command=botao9)
botaoi.grid(column=2, row=2, padx=10, pady=10, )

janela.mainloop()