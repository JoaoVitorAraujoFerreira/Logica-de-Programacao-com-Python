import turtle

def desenhar(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(20)
    if x>0:
        turtle.circle(30)
turtle.speed('fastest')
turtle.onscreenclick(desenhar)
turtle.done()