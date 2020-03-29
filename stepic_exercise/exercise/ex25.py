abc = input().lower()


print(float(((abc.count('g') + abc.count('c')) / len(abc)) * 100))