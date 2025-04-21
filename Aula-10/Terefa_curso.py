qFatorial=int(input("Digite um numero: "))
for z in range(qFatorial):
    if z==0:
        inicial=qFatorial
    else:
        inicial=final
    final=inicial*((qFatorial-1)-z)
print("O resultado de",qFatorial,"fatorial é",inicial)