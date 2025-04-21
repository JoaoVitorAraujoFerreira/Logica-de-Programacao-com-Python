import turtle as T
def retangulo(x,y=100):
    for b in range(2):
        T.forward(x)
        T.left(90)
        T.forward(y)
        T.left(90)
T.pensize(3)
T.pencolor("green")
retangulo(x=250)#VOCE É OBRIGADO A PASAR O VALOR DE UM ARGUMENTO VARIAVEL, MAS NÃO DE UM FIXO(CASO SEJA FIXO ELE LERA O VALOR QUE TIVER PASSADO OU O VALOR FIXO SE VC NÃO TIVER PASSADO VALOR )
T.pencolor("blue")
retangulo(y=480,x=310)
T.done()