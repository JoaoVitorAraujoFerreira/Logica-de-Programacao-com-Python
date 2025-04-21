#tarfa trazer função que pega a ultima palavra
def ultima_palavra(frase):
    qtda_espacos=frase.count(' ')
    posicao=0
    for a in range(qtda_espacos):
        posicao=frase.find(' ',posicao+1)
    return frase[posicao+1::]
print(ultima_palavra(input("Digite a frase: ",)))