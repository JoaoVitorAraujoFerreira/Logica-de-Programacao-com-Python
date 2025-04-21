def primeira_palavra(frase):
    return(frase[:frase.find(" ")])

def contar_palavra(palavra):
    return(frase.count(palavra))
frase='eu me remecho muito, eu me remecho muito, remecho, muito!'
print(contar_palavra(primeira_palavra(frase)))