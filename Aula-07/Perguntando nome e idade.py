def informacõesP ():
    nome1=input('Entre com o primeiro nome: ',)
    print(nome1)
    idade1=int(input('Qual a sua idade? ',))
    nome2=input('Entre com o segundo nome: ',)
    print(nome2)
    idade2=int(input('Qual a sua idade? ',))
    if idade1>idade2:
        print(nome1,'É mais velho que ',nome2,'em ',abs(idade1-idade2),'anos.')
    elif idade2>idade1:
        print(nome2,'É mais velho que ',nome1,'em ',abs(idade1-idade2),'anos.')
    else:
        print(nome1,'e',nome2,'possuem a mesma idade.')
print(informacõesP())