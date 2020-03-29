with open('txt/height.txt', 'r') as f, open('txt/height_result.txt', 'w') as g:
    s = []
    v = 0
    for line in f:
        s += line.split()
        v += 1

    t = [0] * 11
    t2 = [0] * 11
    k = 0
    for i in range(2, v * 3, 3):
        k = int(s[i - 2])
        if 1 <= k <= 11:
            t[k - 1] += int(s[i])
            t2[k - 1] += 1

    for i in range(0, 11):
        value = [i + 1, ' ', t[i] / t2[i], '\n']
        for x in value:
            g.write(str(x))