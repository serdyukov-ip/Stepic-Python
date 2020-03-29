f = str(input())

if (f == 'треугольник'):
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p*(p - a)*(p - b) * (p - c)) ** 0.5)
elif (f == 'прямоугольник'):
    a = int(input())
    b = int(input())
    print(a * b)
elif (f == 'круг'):
    r = int(input())
    print((r ** 2) * 3.14)