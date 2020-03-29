spisok = [int(n) for n in input().split()]
x = int(input())
result = []
i = 0
if len(spisok) == 1 and spisok[0] == x:
    print(0)
else:
    while i < len(spisok):
        if spisok[i] == x:
            result.append(i)
        i+= 1

    if len(result) == 0:
        print("Отсутствует")
    else:
        for r in result:
            print(r, ' ', end='')