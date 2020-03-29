s = []
words = {}
count = 0
maths = 0
physics = 0
language = 0
with open('txt/mark.txt', 'r') as f:
    for line in f:
        line = line.strip()
        s = line.strip().split(';')
        words[str(s[0])] = [int(s[1]), int(s[2]), int(s[3])]
        count+= 1

with open('txt/mark_result.txt', 'w') as result:
    for key, value in words.items():
        result.write(str(round(sum(value) / 3, 9)) + '\n')
        maths+= value[0]
        physics+= value[1]
        language+= value[2]
    result.write(str(round(maths/count, 9)) + ' ')
    result.write(str(round(physics/count, 9)) + ' ')
    result.write(str(round(language/count, 9)))