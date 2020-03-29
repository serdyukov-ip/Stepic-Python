import xlrd

sotr = []
for i in range(1, 1001):
    rb = xlrd.open_workbook('excel/rogaikopyta/' + str(i) +'.xlsx')
    sheet = rb.sheet_by_index(0)
    val = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    sotr.append([val[1][1], val[1][3]])

sotr.sort()
for item in sotr:
    print(item [0], int(item[1]))
