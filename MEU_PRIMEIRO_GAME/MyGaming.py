import turtle
import random
import winsound
from tkinter import *
import PySimpleGUI as sg
# Trocar imagens!
# Terminar parte do cadastro!
# Colocar som no game!

def botaosim():
    lista1d = []
    # Entrar na sua conta
    layout = [
        [sg.Text('Bem vindo ao paypague, o que deseja hoje?')],
        [sg.Button('         Entrar         '), sg.Button('         Cadastrar         ')],
    ]

    janela = sg.Window('paypague', layout=layout)
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED:
            break
        if eventos == '         Entrar         ':
            layout = [
                [sg.Text('Usuário ou email:')],
                [sg.Input(key='usuario')],
                [sg.Text('Digite sua senha:')],
                [sg.Input(key=('senha'))],
                [sg.Button('Entrar')],
                [sg.Text('', key='mensagem')]
            ]
            janela = sg.Window('paypague', layout=layout)

            while True:
                eventos, valores = janela.read()
                if eventos == sg.WIN_CLOSED:
                    break
                elif eventos == 'Entrar':
                    usuario = valores['usuario']
                    senha = valores['senha']
                    listacon = []
                    listacon2 = []
                    conte = 0
                    with open('DADOS1.txt', 'r') as arquivo3:
                        for c in arquivo3:
                            if str(c.strip()) == usuario:
                                listacon.append(conte)
                                conte = 0

                    with open('DADOS1.txt', 'r') as arquivo3:
                        for c in arquivo3:
                            if str(c.strip()) == senha:
                                listacon2.append(conte)
                                break
                            conte += 1
                    a = 0
                    b = 0
                    for c in listacon:
                        a += (c)
                    for c in listacon2:
                        b += (c)

                    if int(a) + 1 == b:
                        janela['mensagem'].update('Login correto!')
                    else:
                        janela['mensagem'].update('Login incorreto!')
                    email = valores['usuario']

                    with open(f'{email}.txt', 'r') as arquivo:
                        for c in arquivo:
                            lista1d.append(c)

                    total = int(lista1d[1])
                    nome = str(lista1d[0])
                    record = 0

                    # Tela
                    wm = turtle.Screen()
                    wm.title('Game by @Allef.K')
                    wm.bgpic('background_03.jpg')
                    wm.bgcolor('black')
                    wm.setup(width=830, height=485)
                    wm.tracer(0)
                    wm.delay(0)

                    wm.addshape("pocao2.gif")
                    wm.addshape("among1.gif")
                    wm.addshape("light.gif")
                    wm.addshape("coracao2.gif")
                    wm.addshape("Apple.gif")

                    # Jogador A
                    jogador_a = turtle.Turtle()
                    jogador_a.speed(0)
                    jogador_a.shape("among1.gif")
                    jogador_a.penup()
                    jogador_a.goto(-200, 0)

                    # Bola
                    bola = turtle.Turtle()
                    bola.speed(0)
                    bola.shape("pocao2.gif")
                    bola.goto(1, 0)
                    bola.penup()
                    bola.dx = 0.2
                    bola.dy = 0.2
                    bola.veloc = 1

                    # Bola2
                    bola2 = turtle.Turtle()
                    bola2.speed(0)
                    bola2.shape("pocao2.gif")
                    bola2.goto(1, 1)
                    bola2.penup()
                    bola2.dx = 0.2
                    bola2.dy = 0.2
                    bola2.veloc = 1

                    # Bola3
                    bola3 = turtle.Turtle()
                    bola3.speed(0)
                    bola3.shape("pocao2.gif")
                    bola3.goto(1, 0)
                    bola3.penup()
                    bola3.dx = -0.2
                    bola3.dy = 0.2
                    bola3.veloc = 1

                    # Bola4
                    bola4 = turtle.Turtle()
                    bola4.speed(0)
                    bola4.shape("pocao2.gif")
                    bola4.goto(1, 1)
                    bola4.penup()
                    bola4.dx = -0.2
                    bola4.dy = 0.2
                    bola4.veloc = 1

                    # maçã
                    maca = turtle.Turtle()
                    maca.speed(0)
                    maca.shape("Apple.gif")
                    maca.goto(0, 1)
                    maca.penup()
                    maca.dx = -0.2
                    maca.dy = -0.2
                    maca.veloc = 0.5

                    # Vidas
                    vidas = 3

                    coracao = turtle.Turtle()
                    coracao.speed(0)
                    coracao.shape("coracao2.gif")
                    coracao.penup()
                    coracao.goto(-380, 210)

                    coracao1 = turtle.Turtle()
                    coracao1.speed(0)
                    coracao1.shape("coracao2.gif")
                    coracao1.penup()
                    coracao1.goto(-340, 210)

                    coracao2 = turtle.Turtle()
                    coracao2.speed(0)
                    coracao2.shape("coracao2.gif")
                    coracao2.penup()
                    coracao2.goto(-300, 210)

                    # Caneta
                    caneta = turtle.Turtle()
                    caneta.speed(0)
                    caneta.color("black")
                    caneta.penup()
                    caneta.hideturtle()
                    caneta.goto(0, 180)
                    caneta.write(f"Record atual: {total}\nPontuação: 0", align="center", font=("courrier", 20, "normal"))

                    # Caneta2
                    caneta2 = turtle.Turtle()
                    caneta2.speed(0)
                    caneta2.color("white")
                    caneta2.penup()
                    caneta2.hideturtle()
                    caneta2.goto(300, -200)
                    caneta2.write(f'Jogador: {nome.title()}',  align="center", font=("courrier", 20, "normal"))

                    # Funções
                    def jogador_a_up():
                        y = jogador_a.ycor()
                        if y != 240:
                            y += 20
                            jogador_a.sety(y)

                    def jogador_a_down():
                        y = jogador_a.ycor()
                        if y != -220:
                            y -= 20
                            jogador_a.sety(y)

                    def jogador_a_left():
                        jogador_a.shape("light.gif")

                        x = jogador_a.xcor()
                        if x != -400:
                            x -= 20
                            jogador_a.setx(x)

                    def jogador_a_right():
                        jogador_a.shape("among1.gif")
                        x = jogador_a.xcor()
                        if x != 400:
                            x += 20
                            jogador_a.setx(x)

                    # Teclas
                    wm.listen()
                    wm.onkeypress(jogador_a_left, "Left")
                    wm.onkeypress(jogador_a_right, "Right")
                    wm.onkeypress(jogador_a_up, "Up")
                    wm.onkeypress(jogador_a_down, "Down")

                    while True:
                        wm.update()

                        # Limites da tela para bola
                        bola.forward(bola.veloc)
                        if bola.ycor() > 240:
                            bola.sety(240)
                            bola.setheading(random.randint(0, 360))

                        if bola.ycor() < -240:
                            bola.sety(-240)
                            bola.setheading(random.randint(0, 360))

                        if bola.xcor() > 400:
                            bola.setx(400)
                            bola.setheading(random.randint(0, 360))

                        if bola.xcor() < -400:
                            bola.setx(-400)
                            bola.setheading(random.randint(0, 360))

                        # Limites da tela para bola2
                        bola2.forward(bola2.veloc)
                        if bola2.ycor() > 240:
                            bola2.sety(240)
                            bola2.setheading(random.randint(0, 360))

                        if bola2.ycor() < -240:
                            bola2.sety(-240)
                            bola2.setheading(random.randint(0, 360))

                        if bola2.xcor() > 400:
                            bola2.setx(400)
                            bola2.setheading(random.randint(0, 360))

                        if bola2.xcor() < -400:
                            bola2.setx(-400)
                            bola2.setheading(random.randint(0, 360))

                        # Limites da tela para bola 3
                        bola3.forward(bola3.veloc)
                        if bola3.ycor() > 240:
                            bola3.sety(240)
                            bola3.setheading(random.randint(0, 360))

                        if bola3.ycor() < -240:
                            bola3.sety(-240)
                            bola3.setheading(random.randint(0, 360))

                        if bola3.xcor() > 400:
                            bola3.setx(400)
                            bola3.setheading(random.randint(0, 360))

                        if bola3.xcor() < -400:
                            bola3.setx(-400)
                            bola3.setheading(random.randint(0, 360))

                        # Limites da tela para bola 4
                        bola4.forward(bola4.veloc)
                        if bola4.ycor() > 240:
                            bola4.sety(240)
                            bola4.setheading(random.randint(0, 360))

                        if bola4.ycor() < -240:
                            bola4.sety(-240)
                            bola4.setheading(random.randint(0, 360))

                        if bola4.xcor() > 400:
                            bola4.setx(400)
                            bola4.setheading(random.randint(0, 360))

                        if bola4.xcor() < -400:
                            bola4.setx(-400)
                            bola4.setheading(random.randint(0, 360))

                        # Limites da tela para maçã
                        maca.forward(maca.veloc)
                        if maca.ycor() > 240:
                            maca.sety(240)
                            maca.setheading(random.randint(0, 360))

                        if maca.ycor() < -240:
                            maca.sety(-240)
                            maca.setheading(random.randint(0, 360))

                        if maca.xcor() > 400:
                            maca.setx(400)
                            maca.setheading(random.randint(0, 360))

                        if maca.xcor() < -400:
                            maca.setx(-400)
                            maca.setheading(random.randint(0, 360))

                        # Colisão da bola com o jogador
                        if bola.xcor() + 20 >= jogador_a.xcor() - 20 and bola.xcor() - 20 <= jogador_a.xcor() + 20 and bola.ycor() + 20 >= jogador_a.ycor() - 20 and bola.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da bola2 com o jogador
                        if bola2.xcor() + 20 >= jogador_a.xcor() - 20 and bola2.xcor() - 20 <= jogador_a.xcor() + 20 and bola2.ycor() + 20 >= jogador_a.ycor() - 20 and bola2.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola2.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da bola3 com o jogador
                        if bola3.xcor() + 20 >= jogador_a.xcor() - 20 and bola3.xcor() - 20 <= jogador_a.xcor() + 20 and bola3.ycor() + 20 >= jogador_a.ycor() - 20 and bola3.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola3.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da bola4 com o jogador
                        if bola4.xcor() + 20 >= jogador_a.xcor() - 20 and bola4.xcor() - 20 <= jogador_a.xcor() + 20 and bola4.ycor() + 20 >= jogador_a.ycor() - 20 and bola4.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola4.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da fruta com o jogador
                        if maca.xcor() + 20 >= jogador_a.xcor() - 20 and maca.xcor() - 20 <= jogador_a.xcor() + 20 and maca.ycor() + 20 >= jogador_a.ycor() - 20 and maca.ycor() - 20 <= jogador_a.ycor() + 20:
                            maca.goto(random.randint(-400, 400), random.randint(-240, 240))
                            record += 1
                            caneta.clear()
                            caneta.write(f"Record atual: {total}\nPontuação: {record}", align="center",
                                         font=("courrier", 20, "normal"))

                        if vidas == 0:
                            if record > total:
                                total = record
                                with open(f'{valores["email"]}.txt', 'a') as arquivo4:
                                    arquivo4.write((str(f'{total}')))
                            bola.goto(1, 0)
                            bola2.goto(1, 1)
                            bola3.goto(1, 0)
                            bola4.goto(1, 1)
                            vidas = 3
                            record = 0
                            caneta.clear()
                            caneta.write(f"Record atual: {total}\nPontuação: {record}", align="center",
                                         font=("courrier", 20, "normal"))
                            coracao2.shape("coracao2.gif")
                            coracao1.shape("coracao2.gif")
                            coracao.shape("coracao2.gif")















        # Cadastrar conta
        elif eventos == '         Cadastrar         ':
            layout = [
                [sg.Text('Digite seu nome completo:')],
                [sg.Input(key=('nome'))],
                [sg.Text('', key='mensagem3')],
                [sg.Text('Crie um email:')],
                [sg.Input(key=('email'))],
                [sg.Text('', key='mensagem1')],
                [sg.Text('Crie uma senha de 8 digitos:')],
                [sg.Input(key=('senha'))],
                [sg.Text('', key='mensagem2')],
                [sg.Button('Entrar')],
                [sg.Text('', key='mensagem')],
            ]

            janela = sg.Window('paypague', layout=layout)
            listadados = []
            cont = 0
            while True:
                eventos, valores = janela.read()
                if eventos == sg.WIN_CLOSED:
                    break
                elif eventos == 'Entrar':
                    email = valores['email']
                    with open('DADOS1.txt', 'r') as arquivo3:
                        for c in arquivo3:
                            listadados.append(c)
                            if str(c.strip()) == email:
                                cont += 1
                            else:
                                cont = 0
                    if cont >= 1:
                        janela['mensagem1'].update('Esse email já esta em uso, por favor digite outro email')
                    elif cont == 0:
                        janela['mensagem1'].update('')

                    senha = valores['senha']
                    contee = 0
                    with open('DADOS1.txt', 'r') as arquivo3:
                        for c in arquivo3:
                            listadados.append(c)
                            if str(c.strip()) == senha:
                                contee += 1
                            else:
                                contee = 0
                    if contee >= 1:
                        janela['mensagem2'].update('Senha fraca')
                    elif len(senha) < 8:
                        janela['mensagem2'].update('Senha muito curta')
                    elif contee == 0 and cont == 0:
                        janela['mensagem2'].update('Dados cadastrados, aguarde alguns segundos!')

                    with open('DADOS1.txt', 'a') as arquivo4:
                        arquivo4.write((str(valores['email'] + '\n')))
                        arquivo4.write((str(valores['senha'] + '\n')))

                    with open(f'{valores["email"]}.txt', 'a') as arquivo4:
                        arquivo4.write((str(valores['nome'] + '\n')))

                    record = 0
                    total = 0

                    # Tela
                    wm = turtle.Screen()
                    wm.title('Game by @Allef.K')
                    wm.bgpic('background_03.jpg')
                    wm.bgcolor('black')
                    wm.setup(width=830, height=485)
                    wm.tracer(0)
                    wm.delay(0)

                    wm.addshape("pocao2.gif")
                    wm.addshape("among1.gif")
                    wm.addshape("light.gif")
                    wm.addshape("coracao2.gif")
                    wm.addshape("Apple.gif")

                    # Jogador A
                    jogador_a = turtle.Turtle()
                    jogador_a.speed(0)
                    jogador_a.shape("among1.gif")
                    jogador_a.penup()
                    jogador_a.goto(-200, 0)

                    # Bola
                    bola = turtle.Turtle()
                    bola.speed(0)
                    bola.shape("pocao2.gif")
                    bola.goto(1, 0)
                    bola.penup()
                    bola.dx = 0.2
                    bola.dy = 0.2
                    bola.veloc = 1

                    # Bola2
                    bola2 = turtle.Turtle()
                    bola2.speed(0)
                    bola2.shape("pocao2.gif")
                    bola2.goto(1, 1)
                    bola2.penup()
                    bola2.dx = 0.2
                    bola2.dy = 0.2
                    bola2.veloc = 1

                    # Bola3
                    bola3 = turtle.Turtle()
                    bola3.speed(0)
                    bola3.shape("pocao2.gif")
                    bola3.goto(1, 0)
                    bola3.penup()
                    bola3.dx = -0.2
                    bola3.dy = 0.2
                    bola3.veloc = 1

                    # Bola4
                    bola4 = turtle.Turtle()
                    bola4.speed(0)
                    bola4.shape("pocao2.gif")
                    bola4.goto(1, 1)
                    bola4.penup()
                    bola4.dx = -0.2
                    bola4.dy = 0.2
                    bola4.veloc = 1

                    # maçã
                    maca = turtle.Turtle()
                    maca.speed(0)
                    maca.shape("Apple.gif")
                    maca.goto(0, 1)
                    maca.penup()
                    maca.dx = -0.2
                    maca.dy = -0.2
                    maca.veloc = 0.5

                    # Vidas
                    vidas = 3

                    coracao = turtle.Turtle()
                    coracao.speed(0)
                    coracao.shape("coracao2.gif")
                    coracao.penup()
                    coracao.goto(-380, 210)

                    coracao1 = turtle.Turtle()
                    coracao1.speed(0)
                    coracao1.shape("coracao2.gif")
                    coracao1.penup()
                    coracao1.goto(-340, 210)

                    coracao2 = turtle.Turtle()
                    coracao2.speed(0)
                    coracao2.shape("coracao2.gif")
                    coracao2.penup()
                    coracao2.goto(-300, 210)

                    # Caneta
                    caneta = turtle.Turtle()
                    caneta.speed(0)
                    caneta.color("black")
                    caneta.penup()
                    caneta.hideturtle()
                    caneta.goto(0, 180)
                    caneta.write("Record atual: 0\nPontuação: 0", align="center", font=("courrier", 20, "normal"))

                    # Funções
                    def jogador_a_up():
                        y = jogador_a.ycor()
                        if y != 240:
                            y += 20
                            jogador_a.sety(y)

                    def jogador_a_down():
                        y = jogador_a.ycor()
                        if y != -220:
                            y -= 20
                            jogador_a.sety(y)

                    def jogador_a_left():
                        jogador_a.shape("light.gif")
                        x = jogador_a.xcor()
                        if x != -400:
                            x -= 20
                            jogador_a.setx(x)

                    def jogador_a_right():
                        jogador_a.shape("among1.gif")
                        x = jogador_a.xcor()
                        if x != 400:
                            x += 20
                            jogador_a.setx(x)

                    # Teclas
                    wm.listen()
                    wm.onkeypress(jogador_a_left, "Left")
                    wm.onkeypress(jogador_a_right, "Right")
                    wm.onkeypress(jogador_a_up, "Up")
                    wm.onkeypress(jogador_a_down, "Down")

                    while True:
                        wm.update()

                        # Limites da tela para bola
                        bola.forward(bola.veloc)
                        if bola.ycor() > 240:
                            bola.sety(240)
                            bola.setheading(random.randint(0, 360))

                        if bola.ycor() < -240:
                            bola.sety(-240)
                            bola.setheading(random.randint(0, 360))

                        if bola.xcor() > 400:
                            bola.setx(400)
                            bola.setheading(random.randint(0, 360))

                        if bola.xcor() < -400:
                            bola.setx(-400)
                            bola.setheading(random.randint(0, 360))

                        # Limites da tela para bola2
                        bola2.forward(bola2.veloc)
                        if bola2.ycor() > 240:
                            bola2.sety(240)
                            bola2.setheading(random.randint(0, 360))

                        if bola2.ycor() < -240:
                            bola2.sety(-240)
                            bola2.setheading(random.randint(0, 360))

                        if bola2.xcor() > 400:
                            bola2.setx(400)
                            bola2.setheading(random.randint(0, 360))

                        if bola2.xcor() < -400:
                            bola2.setx(-400)
                            bola2.setheading(random.randint(0, 360))

                        # Limites da tela para bola 3
                        bola3.forward(bola3.veloc)
                        if bola3.ycor() > 240:
                            bola3.sety(240)
                            bola3.setheading(random.randint(0, 360))

                        if bola3.ycor() < -240:
                            bola3.sety(-240)
                            bola3.setheading(random.randint(0, 360))

                        if bola3.xcor() > 400:
                            bola3.setx(400)
                            bola3.setheading(random.randint(0, 360))

                        if bola3.xcor() < -400:
                            bola3.setx(-400)
                            bola3.setheading(random.randint(0, 360))

                        # Limites da tela para bola 4
                        bola4.forward(bola4.veloc)
                        if bola4.ycor() > 240:
                            bola4.sety(240)
                            bola4.setheading(random.randint(0, 360))

                        if bola4.ycor() < -240:
                            bola4.sety(-240)
                            bola4.setheading(random.randint(0, 360))

                        if bola4.xcor() > 400:
                            bola4.setx(400)
                            bola4.setheading(random.randint(0, 360))

                        if bola4.xcor() < -400:
                            bola4.setx(-400)
                            bola4.setheading(random.randint(0, 360))

                        # Limites da tela para maçã
                        maca.forward(maca.veloc)
                        if maca.ycor() > 240:
                            maca.sety(240)
                            maca.setheading(random.randint(0, 360))

                        if maca.ycor() < -240:
                            maca.sety(-240)
                            maca.setheading(random.randint(0, 360))

                        if maca.xcor() > 400:
                            maca.setx(400)
                            maca.setheading(random.randint(0, 360))

                        if maca.xcor() < -400:
                            maca.setx(-400)
                            maca.setheading(random.randint(0, 360))

                        # Colisão da bola com o jogador
                        if bola.xcor() + 20 >= jogador_a.xcor() - 20 and bola.xcor() - 20 <= jogador_a.xcor() + 20 and bola.ycor() + 20 >= jogador_a.ycor() - 20 and bola.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da bola2 com o jogador
                        if bola2.xcor() + 20 >= jogador_a.xcor() - 20 and bola2.xcor() - 20 <= jogador_a.xcor() + 20 and bola2.ycor() + 20 >= jogador_a.ycor() - 20 and bola2.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola2.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da bola3 com o jogador
                        if bola3.xcor() + 20 >= jogador_a.xcor() - 20 and bola3.xcor() - 20 <= jogador_a.xcor() + 20 and bola3.ycor() + 20 >= jogador_a.ycor() - 20 and bola3.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola3.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da bola4 com o jogador
                        if bola4.xcor() + 20 >= jogador_a.xcor() - 20 and bola4.xcor() - 20 <= jogador_a.xcor() + 20 and bola4.ycor() + 20 >= jogador_a.ycor() - 20 and bola4.ycor() - 20 <= jogador_a.ycor() + 20:
                            bola4.goto(random.randint(-400, 400), random.randint(-240, 240))
                            if vidas == 3:
                                coracao2.shape("blank")
                                vidas -= 1
                            elif vidas == 2:
                                coracao1.shape("blank")
                                vidas -= 1
                            elif vidas == 1:
                                coracao.shape("blank")
                                vidas -= 1

                        # Colisão da fruta com o jogador
                        if maca.xcor() + 20 >= jogador_a.xcor() - 20 and maca.xcor() - 20 <= jogador_a.xcor() + 20 and maca.ycor() + 20 >= jogador_a.ycor() - 20 and maca.ycor() - 20 <= jogador_a.ycor() + 20:
                            maca.goto(random.randint(-400, 400), random.randint(-240, 240))
                            record += 1
                            caneta.clear()
                            caneta.write(f"Record atual: {total}\nPontuação: {record}", align="center",
                                         font=("courrier", 20, "normal"))

                        if vidas == 0:
                            if record > total:
                                total = record
                                with open(f'{valores["email"]}.txt', 'w') as arquivo4:
                                    arquivo4.write((str(f'{total}')))
                            bola.goto(1, 0)
                            bola2.goto(1, 1)
                            bola3.goto(1, 0)
                            bola4.goto(1, 1)
                            vidas = 3
                            record = 0
                            caneta.clear()
                            caneta.write(f"Record atual: {total}\nPontuação: {record}", align="center",
                                         font=("courrier", 20, "normal"))
                            coracao2.shape("coracao2.gif")
                            coracao1.shape("coracao2.gif")
                            coracao.shape("coracao2.gif")










def botaonao():
    cont = 0
    record = 0
    total = 0

    # Tela
    wm = turtle.Screen()
    wm.title('Game by @Allef.K')
    wm.bgpic('background_03.jpg')
    wm.bgcolor('black')
    wm.setup(width=830, height=485)
    wm.tracer(0)
    wm.delay(0)

    wm.addshape("pocao2.gif")
    wm.addshape("among1.gif")
    wm.addshape("light.gif")
    wm.addshape("coracao2.gif")
    wm.addshape("Apple.gif")

    # Jogador A
    jogador_a = turtle.Turtle()
    jogador_a.speed(2)
    jogador_a.shape("among1.gif")
    jogador_a.penup()
    jogador_a.goto(-200, 0)

    # Bola
    bola = turtle.Turtle()
    bola.speed(0)
    bola.shape("pocao2.gif")
    bola.goto(1, 0)
    bola.penup()
    bola.dx = 0.2
    bola.dy = 0.2
    bola.veloc = 1

    # Bola2
    bola2 = turtle.Turtle()
    bola2.speed(0)
    bola2.shape("pocao2.gif")
    bola2.goto(1, 1)
    bola2.penup()
    bola2.dx = 0.2
    bola2.dy = 0.2
    bola2.veloc = 1

    # Bola3
    bola3 = turtle.Turtle()
    bola3.speed(0)
    bola3.shape("pocao2.gif")
    bola3.goto(1, 0)
    bola3.penup()
    bola3.dx = -0.2
    bola3.dy = 0.2
    bola3.veloc = 1

    # Bola4
    bola4 = turtle.Turtle()
    bola4.speed(0)
    bola4.shape("pocao2.gif")
    bola4.goto(1, 1)
    bola4.penup()
    bola4.dx = -0.2
    bola4.dy = 0.2
    bola4.veloc = 1

    # maçã
    maca = turtle.Turtle()
    maca.speed(0)
    maca.shape("Apple.gif")
    maca.goto(0, 1)
    maca.penup()
    maca.dx = -0.2
    maca.dy = -0.2
    maca.veloc = 0.5

    # Vidas
    vidas = 3

    coracao = turtle.Turtle()
    coracao.speed(0)
    coracao.shape("coracao2.gif")
    coracao.penup()
    coracao.goto(-380, 210)

    coracao1 = turtle.Turtle()
    coracao1.speed(0)
    coracao1.shape("coracao2.gif")
    coracao1.penup()
    coracao1.goto(-340, 210)

    coracao2 = turtle.Turtle()
    coracao2.speed(0)
    coracao2.shape("coracao2.gif")
    coracao2.penup()
    coracao2.goto(-300, 210)

    # Caneta
    caneta = turtle.Turtle()
    caneta.speed(0)
    caneta.color("black")
    caneta.penup()
    caneta.hideturtle()
    caneta.goto(0, 180)
    caneta.write("Record atual: 0\nPontuação: 0", align="center", font=("courrier", 20, "normal"))

    # Funções
    def jogador_a_up():
        y = jogador_a.ycor()
        if y != 240:
            y += 20
            jogador_a.sety(y)

    def jogador_a_down():
        y = jogador_a.ycor()
        if y != -220:
            y -= 20
            jogador_a.sety(y)

    def jogador_a_left():
        jogador_a.shape("light.gif")
        x = jogador_a.xcor()
        if x != -400:
            x -= 20
            jogador_a.setx(x)

    def jogador_a_right():
        jogador_a.shape("among1.gif")
        x = jogador_a.xcor()
        if x != 400:
            x += 20
            jogador_a.setx(x)

    # Teclas
    wm.listen()
    wm.onkeypress(jogador_a_left, "Left")
    wm.onkeypress(jogador_a_right, "Right")
    wm.onkeypress(jogador_a_up, "Up")
    wm.onkeypress(jogador_a_down, "Down")

    while True:
        wm.update()

        # Limites da tela para bola
        bola.forward(bola.veloc)
        if bola.ycor() > 240:
            bola.sety(240)
            bola.setheading(random.randint(0, 360))

        if bola.ycor() < -240:
            bola.sety(-240)
            bola.setheading(random.randint(0, 360))

        if bola.xcor() > 400:
            bola.setx(400)
            bola.setheading(random.randint(0, 360))

        if bola.xcor() < -400:
            bola.setx(-400)
            bola.setheading(random.randint(0, 360))

        # Limites da tela para bola2
        bola2.forward(bola2.veloc)
        if bola2.ycor() > 240:
            bola2.sety(240)
            bola2.setheading(random.randint(0, 360))

        if bola2.ycor() < -240:
            bola2.sety(-240)
            bola2.setheading(random.randint(0, 360))

        if bola2.xcor() > 400:
            bola2.setx(400)
            bola2.setheading(random.randint(0, 360))

        if bola2.xcor() < -400:
            bola2.setx(-400)
            bola2.setheading(random.randint(0, 360))

        # Limites da tela para bola 3
        bola3.forward(bola3.veloc)
        if bola3.ycor() > 240:
            bola3.sety(240)
            bola3.setheading(random.randint(0, 360))

        if bola3.ycor() < -240:
            bola3.sety(-240)
            bola3.setheading(random.randint(0, 360))

        if bola3.xcor() > 400:
            bola3.setx(400)
            bola3.setheading(random.randint(0, 360))

        if bola3.xcor() < -400:
            bola3.setx(-400)
            bola3.setheading(random.randint(0, 360))

        # Limites da tela para bola 4
        bola4.forward(bola4.veloc)
        if bola4.ycor() > 240:
            bola4.sety(240)
            bola4.setheading(random.randint(0, 360))

        if bola4.ycor() < -240:
            bola4.sety(-240)
            bola4.setheading(random.randint(0, 360))

        if bola4.xcor() > 400:
            bola4.setx(400)
            bola4.setheading(random.randint(0, 360))

        if bola4.xcor() < -400:
            bola4.setx(-400)
            bola4.setheading(random.randint(0, 360))

        # Limites da tela para maçã
        maca.forward(maca.veloc)
        if maca.ycor() > 240:
            maca.sety(240)
            maca.setheading(random.randint(0, 360))

        if maca.ycor() < -240:
            maca.sety(-240)
            maca.setheading(random.randint(0, 360))

        if maca.xcor() > 400:
            maca.setx(400)
            maca.setheading(random.randint(0, 360))

        if maca.xcor() < -400:
            maca.setx(-400)
            maca.setheading(random.randint(0, 360))

        # Colisão da bola com o jogador
        if bola.xcor() + 20 >= jogador_a.xcor() - 20 and bola.xcor() - 20 <= jogador_a.xcor() + 20 and bola.ycor() + 20 >= jogador_a.ycor() - 20 and bola.ycor() - 20 <= jogador_a.ycor() + 20:
            bola.goto(random.randint(-400, 400), random.randint(-240, 240))
            if vidas == 3:
                coracao2.shape("blank")
                vidas -= 1
            elif vidas == 2:
                coracao1.shape("blank")
                vidas -= 1
            elif vidas == 1:
                coracao.shape("blank")
                vidas -= 1

        # Colisão da bola2 com o jogador
        if bola2.xcor() + 20 >= jogador_a.xcor() - 20 and bola2.xcor() - 20 <= jogador_a.xcor() + 20 and bola2.ycor() + 20 >= jogador_a.ycor() - 20 and bola2.ycor() - 20 <= jogador_a.ycor() + 20:
            bola2.goto(random.randint(-400, 400), random.randint(-240, 240))
            if vidas == 3:
                coracao2.shape("blank")
                vidas -= 1
            elif vidas == 2:
                coracao1.shape("blank")
                vidas -= 1
            elif vidas == 1:
                coracao.shape("blank")
                vidas -= 1

        # Colisão da bola3 com o jogador
        if bola3.xcor() + 20 >= jogador_a.xcor() - 20 and bola3.xcor() - 20 <= jogador_a.xcor() + 20 and bola3.ycor() + 20 >= jogador_a.ycor() - 20 and bola3.ycor() - 20 <= jogador_a.ycor() + 20:
            bola3.goto(random.randint(-400, 400), random.randint(-240, 240))
            if vidas == 3:
                coracao2.shape("blank")
                vidas -= 1
            elif vidas == 2:
                coracao1.shape("blank")
                vidas -= 1
            elif vidas == 1:
                coracao.shape("blank")
                vidas -= 1

        # Colisão da bola4 com o jogador
        if bola4.xcor() + 20 >= jogador_a.xcor() - 20 and bola4.xcor() - 20 <= jogador_a.xcor() + 20 and bola4.ycor() + 20 >= jogador_a.ycor() - 20 and bola4.ycor() - 20 <= jogador_a.ycor() + 20:
            bola4.goto(random.randint(-400, 400), random.randint(-240, 240))
            if vidas == 3:
                coracao2.shape("blank")
                vidas -= 1
            elif vidas == 2:
                coracao1.shape("blank")
                vidas -= 1
            elif vidas == 1:
                coracao.shape("blank")
                vidas -= 1

        # Colisão da fruta com o jogador
        if maca.xcor() + 20 >= jogador_a.xcor() - 20 and maca.xcor() - 20 <= jogador_a.xcor() + 20 and maca.ycor() + 20 >= jogador_a.ycor() - 20 and maca.ycor() - 20 <= jogador_a.ycor() + 20:
            maca.goto(random.randint(-400, 400), random.randint(-240, 240))
            record += 1
            caneta.clear()
            caneta.write(f"Record atual: {total}\nPontuação: {record}", align="center", font=("courrier", 20, "normal"))

        if vidas == 0:
            if record > total:
                total = record
            bola.goto(1, 0)
            bola2.goto(1, 1)
            bola3.goto(1, 0)
            bola4.goto(1, 1)
            vidas = 3
            record = 0
            caneta.clear()
            caneta.write(f"Record atual: {total}\nPontuação: {record}", align="center", font=("courrier", 20, "normal"))
            coracao2.shape("coracao2.gif")
            coracao1.shape("coracao2.gif")
            coracao.shape("coracao2.gif")


janela = Tk()
janela.geometry("500x500")
janela.title("SE CADASTRAR")
janela.config(bg='#7474ff')

texto_tela1 = Button(janela, text='Gostaria de se cadastrar pra salvar seu progresso?', width=40, height=5, bg='#ebebeb',relief='ridge',font=20)
texto_tela1.grid(column=0, row=0, pady=25, padx=65)

texto_tela2 = Button(janela, text='SIM', width=20, height=5, bg='#1139ec',relief='ridge',font=20, command=botaosim)
texto_tela2.grid(column=0, row=1, pady=25, padx=65)

texto_tela2 = Button(janela, text='NÃO', width=20, height=5, bg='#1139ec',relief='ridge',font=20, command=botaonao)
texto_tela2.grid(column=0, row=2, pady=25, padx=65)

janela.mainloop()
