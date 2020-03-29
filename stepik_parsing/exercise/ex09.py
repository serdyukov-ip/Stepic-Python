import xlrd
rb = xlrd.open_workbook('excel/trekking2.xlsx')
sprav = rb.sheet_by_index(0)
raskl = rb.sheet_by_index(1)

vals_s = [sprav.row_values(rownum) for rownum in range(sprav.nrows)]
vals_r = [raskl.row_values(rownum) for rownum in range(raskl.nrows)]
sp = {}
check = {}
kall = 0
bel = 0
j = 0
u = 0
for item in range(1, sprav.nrows):
    sp[vals_s[item][0]] = vals_s[item][1:]

for item in range(1, raskl.nrows):
    if vals_r[item][0] in sp:
        kall += vals_r[item][1] * sp[vals_r[item][0]][0] / 100.00
        bel += vals_r[item][1] * sp[vals_r[item][0]][1] / 100.00
        j += vals_r[item][1] * sp[vals_r[item][0]][2] / 100.00
        u += vals_r[item][1] * sp[vals_r[item][0]][3] / 100.00

print(int(kall), int(bel), int(j), int(u))
