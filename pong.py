import turtle
import os

tela = turtle.Screen()
tela.title("Pong-Classic")
tela.bgcolor("blue")
tela.setup(width=800, height=600)
tela.tracer(0)

#barra A

barra_A=turtle.Turtle()
barra_A.speed(0)
barra_A.shape('square')
barra_A.color('black')
barra_A.shapesize(stretch_wid=5, stretch_len=1)
barra_A.penup()
barra_A.goto(-350,0)

#barra B

barra_B=turtle.Turtle()
barra_B.speed(0)
barra_B.shape('square')
barra_B.color('black')
barra_B.shapesize(stretch_wid=5, stretch_len=1)
barra_B.penup()
barra_B.goto(350,0)


#bola

bola=turtle.Turtle()
bola.speed(0)
bola.shape('square')
bola.color('black')
bola.penup()
bola.goto(0,0)

#adicionando o movimento
bola.dx=0.1
bola.dy=0.1

#atribuindo a pontuação
pontuacao_A = 0
pontuacao_B = 0

#desenhando o placar
placar=turtle.Turtle()
placar.speed()
placar.color('black')
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write("Jogador A: {} Jogador B: {}".format(pontuacao_A, pontuacao_B), align="center", font=("Courier",32,"normal"))

#funções para o movimento

#cimaA
def barra_A_cima():
    y = barra_A.ycor()
    y=y+20
    barra_A.sety(y)

#baixoA
def barra_A_baixo():
    y = barra_A.ycor()
    y=y-20
    barra_A.sety(y)

#cimaB
def barra_B_cima():
    y = barra_B.ycor()
    y=y+20
    barra_B.sety(y)

#baixoB
def barra_B_baixo():
    y = barra_B.ycor()
    y=y-20
    barra_B.sety(y)


#recebendo dados do teclado
tela.listen()
tela.onkeypress(barra_A_cima,"w")
tela.onkeypress(barra_A_baixo,"s")
tela.onkeypress(barra_B_cima,"Up")
tela.onkeypress(barra_B_baixo,"Down")

#loop principal

while True:
    tela.update()

    #adicionando o movimento da bola
    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    #definindo as bordas da imagem
    if bola.ycor()>290:
        bola.sety(290)
        #reverte o movimento
        bola.dy=bola.dy*-1

    #definindo as bordas da imagem
    if bola.ycor()<-290:
        bola.sety(-290)
        #reverte o movimento
        bola.dy=bola.dy*-1

    #definindo as bordas da imagem - ponto jogador A
    if bola.xcor()>390:
        bola.goto(0,0)
        #reverte o movimento
        bola.dx=bola.dx*-1
        pontuacao_A =pontuacao_A+1
        placar.clear()
        placar.write("Jogador A: {} Jogador B: {}".format(pontuacao_A, pontuacao_B), align="center", font=("Courier",32,"normal"))

       #definindo as bordas da imagem - ponto Jogador B
    if bola.xcor()<-390:
        bola.goto(0,0)
        #reverte o movimento
        bola.dx=bola.dx*-1
        pontuacao_B =pontuacao_B+1
        placar.clear()
        placar.write("Jogador A: {} Jogador B: {}".format(pontuacao_A, pontuacao_B), align="center", font=("Courier",32,"normal"))

    #colisão da bola com a barra
    if(bola.xcor()>340 and bola.xcor()<350) and (bola.ycor() < barra_B.ycor() + 40 and bola.ycor()>barra_B.ycor() -40):
            bola.setx(340)
            bola.dx=bola.dx*-1

    if(bola.xcor()< -340 and bola.xcor()> -350) and (bola.ycor() < barra_A.ycor() + 40 and bola.ycor()>barra_A.ycor() -40):
            bola.setx(-340)
            bola.dx=bola.dx*-1
