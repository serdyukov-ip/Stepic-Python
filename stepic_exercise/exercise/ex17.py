i = 0
count = 0
while i < 5:
    print('*')
    count += 1
    if i % 2 == 0:
        print('**')
        count += 2
    if i > 2:
        print('***')
        count += 3
    i = i + 1
print("Всего выведено звезд:", count)