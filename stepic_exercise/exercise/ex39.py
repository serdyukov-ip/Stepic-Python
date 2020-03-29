def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    if -2 < x and x <= 2:
        return -1 * (x / 2)
    if 2 < x:
        return (x - 2) ** 2 + 1

print(f(float(input())))