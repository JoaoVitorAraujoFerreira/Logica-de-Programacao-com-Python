def palavrasSimetricas(palavras):
    if not(palavras[::].upper()==palavras[::-1].upper()):
        print(palavras[::])
palavras="Anilin","Reviewer","ovo","oi","A","Abba","banana"
for posicao in palavras:
    palavrasSimetricas(posicao)