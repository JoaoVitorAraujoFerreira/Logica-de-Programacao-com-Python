def checar_lista(tupla):
    if len(tupla)==0:
        return'a lista esta vazia'
    else:
        return'a lista possui itens'
lista=10,20,30,20,10,50,60,40,80,50,40
#lista=[]
print(checar_lista(lista))