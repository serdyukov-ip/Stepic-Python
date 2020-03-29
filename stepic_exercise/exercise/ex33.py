i = 0
spisok = [1]
result = []
while sum(spisok) != 0:
    if i == 0: spisok[i] = int(input())
    else:
        spisok.append(int(input()))
    i+= 1

result = [num * num for num in spisok]
print(sum(result))
