num = int(input())
count = 0
if num == 1: print(1)
else:
    for n in range(1, num):
        i = 1
        while i <= n:
            if count > num - 1: break
            print(n, ' ', end='')
            i+= 1
            count+=1
        if count > num - 1: break
