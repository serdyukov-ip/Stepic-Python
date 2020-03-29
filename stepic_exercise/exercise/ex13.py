n = int(input())

if n % 100 in [0, 10, 11, 12, 13, 14]: print(n, 'программистов')
elif n % 10 in [2, 3, 4]: print(n, 'программиста')
elif n % 10 in [1]: print(n, 'программист')
elif n % 10 in [0, 5, 6, 7, 8, 9]: print(n, 'программистов')