import turtle

def desenhar(x,y):
    turtle.goto(x,y)
    p=x,y
    if x>0:
        turtle.write('tartaruga na pisicao'+str(p))
turtle.onscreenclick(desenhar)
turtle.done()