import turtle
import random

# Game by Allef
# Cometário de auxílio ao programador!
# O jogo contem 1 personagem, 1 poção de veneno, 1 fruta de pontos e 3 vidas!
# Cada vez o jogo ficará mais dificil add mais poções!


# Tela
wm = turtle.Screen()
wm.title('Game by @Allef.K')
wm.bgpic('background_03.jpg')
wm.bgcolor('black')
wm.setup(width=830, height=485)
wm.tracer(0)

wm.addshape("pocao2.gif")

'''# Jogador A
jogador_a = turtle.Turtle()
jogador_a.speed(0)
jogador_a.shape("square")
jogador_a.shapesize(stretch_wid=1, stretch_len=1)
jogador_a.color('white')
jogador_a.penup()
jogador_a.goto(0, 0)'''

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("pocao2.gif")
bola.color('white')
bola.goto(0, 0)
bola.penup()
bola.dx = 0.1
bola.dy = -0.1



'''# Funções
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
    x = jogador_a.xcor()
    if x != -400:
        x -= 20
        jogador_a.setx(x)

def jogador_a_right():
    x = jogador_a.xcor()
    if x != 400:
        x += 20
        jogador_a.setx(x)


# Teclas
wm.listen()
wm.onkeypress(jogador_a_left, "Left")
wm.onkeypress(jogador_a_right, "Right")
wm.onkeypress(jogador_a_up, "Up")
wm.onkeypress(jogador_a_down, "Down")'''



while True:
    wm.update()

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)


    # Limites da tela
    if bola.ycor() > 240:
        bola.sety(240)
        bola.dy *= -1

    if bola.ycor() < -240:
        bola.sety(-240)
        bola.dy *= -1

    if bola.xcor() > 400:
        bola.setx(400)
        bola.dx *= -1

    if bola.xcor() < -400:
        bola.setx(-400)
        bola.dx *= -1






