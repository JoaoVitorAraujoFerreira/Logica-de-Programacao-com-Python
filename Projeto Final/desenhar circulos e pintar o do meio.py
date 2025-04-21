import turtle

def desenhar(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(30)
    if x>0:
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
turtle.speed("fastest")
turtle.onscreenclick(desenhar)

turtle.done()