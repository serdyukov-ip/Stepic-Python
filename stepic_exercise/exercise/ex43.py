def f(i):
    print(i ** 2)

f_dict = {}
n = int(input())
for i in range(n):
    x = int(input())
    if x not in f_dict:
        f_dict[x] = f(x)
    print(f_dict[x])