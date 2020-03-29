n = 0
numbers = []

while n <= 100:
    n = int(input())
    if (n > 9) and (n < 101):
        numbers.append(n)

for item in numbers[:]:
    print(item)