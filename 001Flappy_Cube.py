import turtle
import random
from time import sleep


move = 1
recorde = 0
recorde1 = 0

# Colocar imagens

# Tela
wm = turtle.Screen()
wm.title('Game by @Allef.K')
wm.bgcolor('black')
wm.setup(width=830, height=485)
wm.tracer(0)

# Adicionando imagens
wm.addshape('img.gif')

# imagem da tela de inicio
img = turtle.Turtle()
img.shape('img.gif')
img.color('blue')
img.penup()
img.goto(0,0)

# cubo
jogador_a = turtle.Turtle()
jogador_a.speed(2)
jogador_a.shape('blank')
jogador_a.color('white')
jogador_a.penup()
jogador_a.goto(-300, -220)
jogador_a.shapesize(1)
jogador_a.dy = -0.5
jogador_a.dx = -0.2

# Barras de colisão
qcima = turtle.Turtle()
qcima.speed(0)
qcima.color('white')
qcima.shape('blank')
qcima.shapesize(stretch_wid=20,stretch_len=2)
qcima.penup()
qcima.goto(0,-300)
qcima.dy = -0.2
qcima.dx = -0.8

qcima1 = turtle.Turtle()
qcima1.speed(0)
qcima1.color('white')
qcima1.shape('blank')
qcima1.shapesize(stretch_wid=20,stretch_len=2)
qcima1.penup()
qcima1.goto(0,200)
qcima1.dy = -0.2
qcima1.dx = -0.8

# Ferramenta pra mostar pontuaçaõ e record
record = turtle.Turtle()
record.speed(0)
record.color('white')
record.penup()
record.hideturtle()
record.goto(-30,204)

# Funções
def jogador_a_up():
    global move, recorde1, recorde
    if move > 0:
        move = 0
        if recorde > recorde1:
            recorde1 = recorde
        record.clear()
        recorde = 0
        record.write(f'Record {recorde1} Pontução {recorde}', align="center", font=("courrier", 20, "normal"))
    y = jogador_a.ycor()
    y += 60
    jogador_a.sety(y)

def jogador_a_down():
    jogador_a.sety(jogador_a.ycor() + jogador_a.dy)
    if jogador_a.ycor() < -220:
        jogador_a.sety(-220)

# teclas
wm.listen()
wm.onkeypress(jogador_a_up, "space")

while True:
    wm.update()
    jogador_a_down()


    # Movimentação
    if move == 0:

        img.shape('blank')
        qcima1.color('white')
        qcima.color('white')
        qcima1.shape('square')
        qcima.shape('square')
        jogador_a.shape('square')
        record.clear()
        record.write(f'Record {recorde1} Pontução {recorde}', align="center", font=("courrier", 20, "normal"))
        qcima.setx(qcima.xcor() + qcima.dx)
        qcima1.setx(qcima1.xcor() + qcima1.dx)

    # Alterando a posição das barras
    if qcima1.xcor() < -440:
        record.clear()
        recorde += 1
        record.write(f'Record {recorde1} Pontução {recorde}', align="center", font=("courrier", 20, "normal"))
        qcima1.setx(440)
        qcima.setx(440)
        qcima1.sety(random.randint(150, 400))
        qcima.sety(qcima1.ycor() - 500)


    # Colisão das barras com o cubo
    if qcima1.xcor() + 20 >= jogador_a.xcor() - 20 and qcima1.xcor() - 20 <= jogador_a.xcor() + 20 and qcima1.ycor() + 100 >= jogador_a.ycor() - 100 and qcima1.ycor() - 100 <= jogador_a.ycor() + 100:
        qcima1.color('red')
        qcima.color('red')
        move += 1
        qcima1.setx(300)
        qcima.setx(300)
        qcima1.sety(random.randint(150, 400))
        qcima.sety(qcima1.ycor() - 500)


    if qcima.xcor() + 20 >= jogador_a.xcor() - 20 and qcima.xcor() - 20 <= jogador_a.xcor() + 20 and qcima.ycor() + 100 >= jogador_a.ycor() - 100 and qcima.ycor() - 100 <= jogador_a.ycor() + 100:
        qcima.color('red')
        qcima1.color('red')
        move += 1
        qcima1.setx(300)
        qcima.setx(300)
        qcima1.sety(random.randint(150, 400))
        qcima.sety(qcima1.ycor() - 500)

