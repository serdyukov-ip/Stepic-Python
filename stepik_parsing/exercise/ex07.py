import xlrd
from numpy import median
rb = xlrd.open_workbook('excel/salaries.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
max = 0.0
sum = 0.0
city = ''
spec = ''
specialty = {}

for i in range(1, 9):
    if max < median(vals[i][1:]):
        max = median(vals[i][1:])
        city = str(vals[i][0])
    for j in range(1, 8):
        if specialty.get(vals[0][j]) != None:
            specialty[vals[0][j]] = specialty.get(vals[0][j]) + vals[i][j]
        else:
            specialty[vals[0][j]] = vals[i][j]

max = 0
for key, val in specialty.items():
    specialty[key] = val / 8
    if val > max:
        max = val
        spec = key

print(city, spec)



