def pares(tudo):
    importante=[]
    for i in tudo:
        if i%2==0:
            importante.append(i)
    return importante
lista=[1,2,13,44,21,8,4,9,72,14,18,15,22,16,12,6,52,47]
corre=2
print(pares(lista))