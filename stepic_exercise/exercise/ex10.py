a = float(input())
b = float(input())
o = str(input())

if (o == '+'):
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif (o == '/'):
    if (b != 0): print(a / b);
    else: print("Деление на 0!")
elif o == 'mod':
    if (b != 0): print(a % b);
    else: print("Деление на 0!")
elif o == 'pow':
    print(a ** b)
elif o == 'div':
    if (b != 0): print(a // b);
    else: print("Деление на 0!")
