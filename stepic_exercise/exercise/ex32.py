spisok = [n for n in input().split()]
result = []

for n in spisok:
    if spisok.count(n) > 1:
        result.append(n)

for n in list(set((result))):
  print(int(n), ' ', end='')