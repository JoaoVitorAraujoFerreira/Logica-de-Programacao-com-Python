import turtle
def quadrado(x):
    for i in range(4):    
        turtle.forward(x)
        turtle.left(90)
def triangulo(x):
    for a in range(3):
        turtle.forward(x)
        turtle.left(120)
def retangulo(x,y):
    for b in range(2):
        turtle.forward(x)
        turtle.left(90)
        turtle.forward(y)
        turtle.left(90)
turtle.pensize(6)
'''quadrado(100)
turtle.up()#para de escrever
turtle.forward(300)
turtle.down()
quadrado(150)

turtle.forward(300)
turtle.left(70)
turtle.circle(50)

quadrado(100)
turtle.left(10)
quadrado(150)
turtle.left(20)
quadrado(200)
turtle.left(30)
quadrado(250)
turtle.left(40)
quadrado(300)
turtle.left(50)
quadrado(350)
turtle.left(60)
quadrado(400)
turtle.left(70)
quadrado(450)
turtle.left(80)
quadrado(500)
turtle.left(90)'''


quadrado(100)
turtle.pencolor("yellow")
retangulo(100, 300)
turtle.pencolor("blue")
triangulo(150)


turtle.done()