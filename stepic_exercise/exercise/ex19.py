a = int(input())
b = int(input())

max = a * b
min = max
i = 1

while i <= max:
    if (i % a == 0) and (i % b == 0) and (i < min):
        min = i
    i+= 1
print(min)

