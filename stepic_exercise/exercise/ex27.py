abc = input()

result = ''
count = 1
i = 0
while i < len(abc) - 1:
    while (abc[i] == abc[i + 1]):
        if i >= len(abc) - 2:
            count += 1
            break
        count += 1
        i+=1
    result += abc[i] + str(count)
    count = 1
    i+= 1

if abc.count(abc[len(abc) - 1]) == 1:
    result += abc[len(abc) - 1] + '1'

print(result)