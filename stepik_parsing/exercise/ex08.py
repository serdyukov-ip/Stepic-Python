import xlrd
rb = xlrd.open_workbook('excel/trekking1.xlsx')
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
my_table = []

for i in range(1, sheet.nrows):
    my_table.append(vals[i][1::-1])

my_table = sorted(my_table, reverse=True)

for item in my_table:
    print(item[1].strip())
