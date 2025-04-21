import turtle

def desenhar(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    if x>0 and y>0:
        turtle.color('red')
    elif x>0:
        turtle.color('blue')
    elif y>0 and x<0:
        turtle.color('cyan')
    else:
        turtle.color('black')
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

turtle.speed('fastest')
turtle.onscreenclick(desenhar)
turtle.done()