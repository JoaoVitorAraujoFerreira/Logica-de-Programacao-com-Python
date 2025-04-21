import turtle

def desenhar(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    if x>0:
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
    turtle.circle(30)

turtle.Screen()
turtle.title('Apresentação python')
turtle.speed('fastest')
turtle.onscreenclick(desenhar)

turtle.done()