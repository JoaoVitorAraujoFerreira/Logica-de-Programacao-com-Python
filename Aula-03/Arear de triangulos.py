def area_triangulo(a,b,c):
    p=(a+b+c)/2
    return((p*(p-a)*(p-b)*(p-c))**.5)
a=4.72
b=5.3
c=4.42
d=3.65
e=3.39
print(area_triangulo(a, b, c)+area_triangulo(c, d, e))