X = int(input())
H = int(input())
M = int(input())
print(int(((H * 60 + M) + X) / 60))
print(int(((H * 60 + M) + X) % 60))