import turtle

#Criar parte em que um jogador vence!

# Tela
wm = turtle.Screen()
wm.title('Pong by @Allef.K')
wm.bgcolor('black')
wm.setup(width=800, height=600)
wm.tracer(0)

# Placar
placar_a = 0
placar_b = 0
cont = 3

# Jogador A
jogador_a = turtle.Turtle()
jogador_a.speed(0)
jogador_a.shape('square')
jogador_a.color('white')
jogador_a.shapesize(stretch_wid=5, stretch_len=1)
jogador_a.penup()
jogador_a.goto(-350, 0)

# Jogador B
jogador_b = turtle.Turtle()
jogador_b.speed(0)
jogador_b.shape('square')
jogador_b.color('white')
jogador_b.shapesize(stretch_wid=5, stretch_len=1)
jogador_b.penup()
jogador_b.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color('white')
bola.goto(0, 0)
bola.penup()
bola.dx = 0.4
bola.dy = -0.4

# Bola2
bola2 = turtle.Turtle()
bola2.speed(0)
bola2.shape('blank')
bola2.color('')
bola2.goto(200, 0)
bola2.penup()
bola2.dx = 0.4
bola2.dy = -0.4


caneta = turtle.Turtle()
caneta.speed(0)
caneta.color("white")
caneta.penup()
caneta.hideturtle()
caneta.goto(0, 230)
caneta.write("Jogador A: 0\nJogador B: 0", align="center",font=("courier", 20, "normal"))

# Funções
def jogador_a_up():
    y = jogador_a.ycor()
    y += 20
    jogador_a.sety(y)

def jogador_a_down():
    y = jogador_a.ycor()
    y -= 20
    jogador_a.sety(y)

def jogador_b_up():
    y = jogador_b.ycor()
    y += 20
    jogador_b.sety(y)

def jogador_b_down():
    y = jogador_b.ycor()
    y -= 20
    jogador_b.sety(y)

# Teclas
wm.listen()
wm.onkeypress(jogador_a_up, "w")
wm.onkeypress(jogador_a_down, "s")
wm.onkeypress(jogador_b_up, "Up")
wm.onkeypress(jogador_b_down, "Down")



while True:
    wm.update()

    if placar_a >= 15 or placar_b >= 15:
        # Movimento da bola2
        bola2.setx(bola2.xcor() + bola2.dx)
        bola2.sety(bola2.ycor() + bola2.dy)
        bola2.color('white')
        bola2.shape('square')

    # Movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)


    # Limites da tela
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        placar_a += 1
        caneta.clear()
        caneta.write(f"Jogador A: {placar_a}\nJogador B: {placar_b}", align="center", font=("courier", 20, "normal"))

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        placar_b += 1
        caneta.clear()
        caneta.write(f"Jogador A: {placar_a}\nJogador B: {placar_b}", align="center", font=("courier", 20, "normal"))

    #Bola2
    if bola2.ycor() > 290:
        bola2.sety(290)
        bola2.dy *= -1

    if bola2.ycor() < -290:
        bola2.sety(-290)
        bola2.dy *= -1

    if bola2.xcor() > 390:
        bola2.goto(0,0)
        bola2.dx *= -1
        placar_a += 1
        caneta.clear()
        caneta.write(f"Jogador A: {placar_a}\nJogador B: {placar_b}", align="center", font=("courier", 20, "normal"))

    if bola2.xcor() < -390:
        bola2.goto(0,0)
        bola2.dx *= -1
        placar_b += 1
        caneta.clear()
        caneta.write(f"Jogador A: {placar_a}\nJogador B: {placar_b}", align="center", font=("courier", 20, "normal"))


    # Colisão da bola com o jogador
    if (bola.xcor() > 340 and bola.xcor() < 350) and (
            bola.ycor() < jogador_b.ycor() + 40 and bola.ycor() > jogador_b.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (
            bola.ycor() < jogador_a.ycor() + 40 and bola.ycor() > jogador_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1

        #Bola2
    if (bola2.xcor() > 340 and bola2.xcor() < 350) and (
            bola2.ycor() < jogador_b.ycor() + 40 and bola2.ycor() > jogador_b.ycor() - 40):
        bola2.setx(340)
        bola2.dx *= -1

    if (bola2.xcor() < -340 and bola2.xcor() > -350) and (
            bola2.ycor() < jogador_a.ycor() + 40 and bola2.ycor() > jogador_a.ycor() - 40):
        bola2.setx(-340)
        bola2.dx *= -1

