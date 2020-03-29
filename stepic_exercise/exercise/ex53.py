n = int(input())
words = [input().lower() for word in range(n)]
n = int(input())
text = [input().lower().split() for txt in range(n)]

result = []
for word in text:
    for word1 in word:
        if words.count(word1) == 0:
            result += [word1]

for r in list(set(result)):
    print(r)
