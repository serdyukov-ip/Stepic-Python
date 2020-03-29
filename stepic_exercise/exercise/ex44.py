with open('txt/data.txt', 'r') as data:
    a = data.readline().strip()
c = ''
i = 0
while i < len(a) - 1:
    if a[i].isalpha():
        s = a[i]
        i += 1
        p = a[i]
        while i < len(a) - 1 and a[i + 1].isdigit():
            i += 1
            p += a[i]
        c += s * int(p)
    else:
        i += 1

with open('txt/result.txt', 'w') as result:
    result.write(str(c))
