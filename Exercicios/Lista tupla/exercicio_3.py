busca=str(input("Digite o nome que deseja encontrar: "))
lista="Joao","Carlos","Maria","Antonio","Luncas","Daniela","Paulo"
for nome in lista:
    if nome.upper()==busca.upper():
        print(lista.index(nome))
