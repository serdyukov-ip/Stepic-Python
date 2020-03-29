spisok = [n for n in input().split()]
result = []
length = len(spisok) - 1
if length + 1 == 1:
    print(spisok[0])
else:
    i = 0
    while i < length:
        if i > 0 and i < length:
            result.append(int(spisok[i - 1]) + int(spisok[i + 1]))
        i+= 1
    result.insert(0, int(spisok[-1]) + int(spisok[1]))
    result.append(int(spisok[-2]) + int(spisok[0]))

    for item in result:
        print(item, ' ', end='')