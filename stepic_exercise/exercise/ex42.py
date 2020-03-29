words = [w.lower() for w in input().split()]

for w in list(set(words)):
    print(w, words.count(w))



