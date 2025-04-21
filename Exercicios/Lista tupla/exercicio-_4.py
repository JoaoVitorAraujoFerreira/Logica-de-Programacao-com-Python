def repetidos(repetido):
    resultado=[]
    if resultado.count(repetido)==0:
        resultado.append(repetido)
    return resultado
def procurar(tupla):
    for item in tupla:
        if tupla.count(item)>1:
            repetidos(item)
            return(repetidos(item))
lista=2,4,5,6,2,4,4,7
print(procurar(lista))