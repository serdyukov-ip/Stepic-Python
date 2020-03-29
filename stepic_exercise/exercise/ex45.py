with open('txt/words.txt', 'r') as f:
    s = list(map(lambda i: i.strip('.,!?'), f.read().lower().split()))
    m = max(sorted(s), key = lambda j: s.count(j))
    print("%s %d" % (m, s.count(m)))