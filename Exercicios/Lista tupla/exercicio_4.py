lista=1,2,13,44,21,8,4,9,72,14,18,15,22,16,12,6,52,47,1,1,1,1,1,1,1,1,2,2,2,44
repetidos=[]
for item in lista:
    if lista.count(item)>=2:
        if repetidos.count(item)==0:
            repetidos.append(item)
print(repetidos,"esses itens se repetem na lista")