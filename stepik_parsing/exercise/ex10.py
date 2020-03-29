import xlrd
rb = xlrd.open_workbook('excel/trekking3.xlsx')
sprav = rb.sheet_by_index(0)
raskl = rb.sheet_by_index(1)

vals_s = [sprav.row_values(rownum) for rownum in range(sprav.nrows)]
vals_r = [raskl.row_values(rownum) for rownum in range(raskl.nrows)]
sp = {}
days = {1:[0.0, 0.0, 0.0, 0.0], 2:[0.0, 0.0, 0.0, 0.0], 3:[0.0, 0.0, 0.0, 0.0], 4:[0.0, 0.0, 0.0, 0.0], 5:[0.0, 0.0, 0.0, 0.0], 6:[0.0, 0.0, 0.0, 0.0], 7:[0.0, 0.0, 0.0, 0.0], 8:[0.0, 0.0, 0.0, 0.0], 9:[0.0, 0.0, 0.0, 0.0]}

for item in range(1, sprav.nrows):
    sp[vals_s[item][0]] = vals_s[item][1:]

for i in range(1, len(vals_r)):
    if vals_r[i][1] in sp:
        days[int(vals_r[i][0])][0] += float(vals_r[i][2]) * float(sp[vals_r[i][1]][0]) / float(100.00)
        days[int(vals_r[i][0])][1] += float(vals_r[i][2]) * float(sp[vals_r[i][1]][1]) / float(100.00)
        days[int(vals_r[i][0])][2] += float(vals_r[i][2]) * float(sp[vals_r[i][1]][2]) / float(100.00)
        days[int(vals_r[i][0])][3] += float(vals_r[i][2]) * float(sp[vals_r[i][1]][3]) / float(100.00)

for values in days.values():
    for val in values:
        print(int(val), ' ', end='')
    print()