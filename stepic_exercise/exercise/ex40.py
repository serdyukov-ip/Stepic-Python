def modify_lst(l):
    i = 0
    while i != len(l):
        if l[i] % 2 == 1:
            l.pop(i)
        else:
            l[i]//= 2
            i+= 1

lst = [int(i) for i in input().split()]
modify_lst(lst)
print(lst)
