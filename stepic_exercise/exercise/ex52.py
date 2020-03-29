code = input()
decode = input()
s1 = input()
s2 = input()
result = ''

for c in s1:
    result += decode[code.index(c)]

print(result)
result = ''

for c in s2:
    result += code[decode.index(c)]

print(result)