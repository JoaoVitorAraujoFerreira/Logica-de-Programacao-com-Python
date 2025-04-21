import turtle
import os
import random
import time
score=0
high_score=0
delay=0.1
high_score_name='em breve'#depois se altera isto
#movimento
def GoDown():
    if head.direction != 'up':
        head.direction='down'
def GoUp():
    if head.direction != 'down':
        head.direction='up'
def GoRight():
    if head.direction != 'left':
        head.direction='right'
def GoLeft():
    if head.direction != 'right':
        head.direction='left'
def Continuar_andando():
    if head.direction == 'up':
        y=head.ycor()#diz que y recebe cordenadas de y da cabeca da cobra
        head.sety(y+20)#adiciona mais 20 a cordenada y
    if head.direction == 'down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction == 'left':
        x=head.xcor()
        head.setx(x-20)
#fazer a comida reaparecer
def New_food():
    food.goto(2000,2000)
    corpos=random.choice(['triangle','square','circle'])
    cores=random.choice(['cyan','blue','pink','black'])
    food.speed(0)
    food.shape(corpos)
    food.color(cores)
    food.penup()
    y_food= random.randint(-270,270)
    x_food= random.randint(-270,270)
    food.goto(x_food,y_food)
#final e recomeso de jogo
def Fim_de_jogo():
    global high_score, score, especial_controle
    Efood.goto(2000,2000)
    especial_controle=1
    head.direction=='stop'
    time.sleep(1)
    Tlose=turtle.Turtle()
    Tlose.shape('square')
    Tlose.color('red')
    Tlose.speed(0)
    Tlose.hideturtle()
    Tlose.penup()
    Tlose.goto(0,0)
    Tlose.write("GAME OVER",align='center',font=('candara',70,'bold'))
    if score>high_score:
        high_score=score
    for objeto in segments[::-1]:
        objeto.clear()
        objeto.goto(2000,2000)
    segments.clear()
    head.goto(0,0)
    score=0
    head.direction='stop'
    time.sleep(3)
    Tlose.clear()
    New_food()
#controla os seguimentos
def Movimento_corporal():
    if len(segments)>0:
        if head.direction=='up':
            segments[0].goto(head.xcor(),head.ycor()-20)
        if head.direction=='down':
            segments[0].goto(head.xcor(),head.ycor()+20)
        if head.direction=='right':
            segments[0].goto(head.xcor()-20,head.ycor())
        if head.direction=='left':
            segments[0].goto(head.xcor()+20,head.ycor())
    for anel in range(len(segments)-1,0,-1):
        x=segments[anel-1].xcor()
        y=segments[anel-1].ycor()
        segments[anel].goto(x,y)
#gerencia a comida bonus
def Especial_food():
    global tfim, score, especial_controle
    '''tini=time.time()
    if tfim-tini>=5:
        especial_controle+=1
        Efood.goto(2000,2000)'''
    if score%(100*especial_controle)==0:
        especial_controle+=1
        aleX=random.randint(-270,270)
        aleY=random.randint(-270,270)
        Efood.shape('triangle')
        Efood.color('yellow')
        Efood.speed(0)
        Efood.goto(aleX,aleY)
    if head.distance(Efood)<=20:
        segments.append(New_segment)
        score+=100
        especial_controle+=1
        Efood.goto(2000,2000)
#gerar a janela
wn=turtle.Screen()#criar janela
wn.title('Snake Game')#nomear janela
wn.bgcolor('green')#cor de fundo da janela
altura_da_janela=600
largura_da_janela=600
wn.setup(width=largura_da_janela,height=altura_da_janela)#tamanho da janela
wn.tracer(0)#Passa o comando dos fps para o codigo 
#gerar a cobra
head=turtle.Turtle()#atribuindo a variavel as caracteristicas do turtle
head.shape('square')#dando forma ao corpo da coblra
head.color('white')#pinta a cobra
head.penup()#levanta a caneta
head.goto(0,0)#centraliza a cobra
head.direction='stop'#Ordena que a cobra inicie parada
#gerar a comida
food=turtle.Turtle()#atribuindo a variavel as caracteristicas do turtle
colors=random.choice(['red','green','cyan','blue','pink'])#estabelece que cores possui valores em ordem variada dos prestabelecidos
shapes=random.choice(['square','triangle','circle'])#estabelece que a comida tem formatos aleatorios ao preestabelecidos
food.speed(0)#define a velocidade da comida
food.shape(shapes)# define que a cor do corpo e o valor da variavel shapes
food.color(colors)# defina que a cor é o valor da variavel colors
food.penup()#levanta a caneta
y_food= random.randint(-289,289)
x_food= random.randint(-289,289)
food.goto(x_food,y_food)#orden a posicao em que deve estar
#gerar a comida especial
Efood=turtle.Turtle()
Efood.speed(0)
Efood.shape('triangle')
Efood.color('yellow')
Efood.penup()
Efood.goto(2000,2000)
#gerando o mostrador de pontuacao
pen=turtle.Turtle()#atribuindo a variavel as caracteristicas do turtle
pen.speed(0)#regula a velocidade da escrita
pen.shape('square')#dando forma ao
pen.color('white')#pinta
pen.penup()#levanta a caneta
pen.hideturtle()
pen.goto(0,250)
#movimento
wn.listen()
wn.onkeypress(GoUp,"Up")
wn.onkeypress(GoLeft,'Left')
wn.onkeypress(GoRight,'Right')
wn.onkeypress(GoDown,'Down')
wn.onkeypress(GoUp,"w")
wn.onkeypress(GoLeft,'a')
wn.onkeypress(GoRight,'d')
wn.onkeypress(GoDown,'s')
segments=[]
#continuar movendo na ultima posição
Continuar_andando()
especial_controle=1#desbugar a aparição da fruta bonus
controle2=0
#Necessario para dar continuidade
while True:
    """tfim=time.time()
    print(tfim)"""
    Continuar_andando()
    #objeto corpo da cobra
    New_segment=turtle.Turtle()
    New_segment.shape('square')
    New_segment.color('orange')
    New_segment.penup()
    New_segment.goto(2000,2000)
    New_segment.direction='stop'
    while controle2==1:
        controle2+=1
        segments.append(New_segment)
    if head.distance(food)<=20:
        score+=10
        segments.append(New_segment)
        controle2+=1
        New_food()
    if score%100==0 and score>0:
        Especial_food()
    else:
        Efood.goto(2000,2000)
    Movimento_corporal()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() >290 or head.ycor()<-290 or head.distance(New_segment)<=0:
        Fim_de_jogo()
    pen.clear()
    pen.write(f"Score: {score} High Score: {high_score} by {high_score_name}", align='center',font=('candara',24,'bold'))
    wn.update()
    time.sleep(delay)
wn.mainloop()
turtle.done()