def area_triangulo(a,b,c):
    p=(a+b+c)/2
    return  ((p*(p-a)*(p-b)*(p-c))**.5)
a=1.28
b=1.4
c=1.19
print('area_triangulo=',area_triangulo(a, b, c))