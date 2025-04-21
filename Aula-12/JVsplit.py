def minha_split(tupla):
    bolsos=[]
    primeiro=0
    for vezes in range(len(tupla)):
        if tupla[vezes]==' ':
            bolsos.append(tupla[primeiro:vezes])
            primeiro=vezes
        elif primeiro!=0 and tupla[:vezes+1]==tupla[:vezes*99]:
            bolsos.append(tupla[primeiro:vezes*99])
            primeiro=vezes
    return bolsos
personagens=input('Digite uma frase: ')
print(minha_split(personagens))