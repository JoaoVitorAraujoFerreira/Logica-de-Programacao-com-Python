#trazer proximo curso as formulas do seno, cosseno e tangente (FORMULAS)
def seno(cato,hipo):
    resultadoS=cato/hipo
    if resultadoS==.5:
        print("O angulo é 30°")
    elif resultadoS==(2**.5)/2:
        print("O angulo é 45°")
    else:
        print("O angulo é 60°")
def cosseno(cata,hipo):
    resultadoC=cata/hipo
    if resultadoC==(3**.5)/2:
        print("O angulo é 30°")
    elif resultadoC==(2**.5)/2:
        print(" Oangulo é 45°")
    else:
        print("O angulo é 60°")
def tangente(cato,cata):
    resultadoT=cato/cata
    if resultadoT==.5:
        print("O angulo é 30°")
    elif resultadoT==(2**.5)/2:
        print("O angulo é 45°")
    else:
        print("O angulo é 60°")
print("digite sn para seno, co para cosseno ou tg  para tangente")
calculo=str(input("Gostaria de calcular seno(sn), cosseno(co) ou tangente(tg)?"))
if calculo=="sn":
    cato=float(input("Qual é o valor do cateto oposto?"))
    hipo=float(input("Qual é o valor da hipotenusa?"))
    print(seno(cato,hipo))
elif calculo=="co":
    cata=float(input("Qaul é o valor do cateto adjacentnte?"))
    hipo=float(input("Qual é o valor da hipotenusa?"))
    print(cosseno(cata,hipo))
else:
    cata=float(input("Qaul é o valor do cateto adjacentnte?"))
    cato=float(input("Qual é o valor do cateto oposto?"))
    print(tangente(cato,cata))