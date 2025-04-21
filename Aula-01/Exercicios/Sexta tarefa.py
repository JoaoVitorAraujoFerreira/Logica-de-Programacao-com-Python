a=float(input("Quanto vale o cateto A ? "))
b=float(input("Qaunto vale o cateto B ? "))
c=float(input("Quanto vale a hipotenusa ? "))
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**.5
print("A area desse triangulo é: ",area)