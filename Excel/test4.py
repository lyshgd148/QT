import xlrd
import xlwt

workbook = xlrd.open_workbook('电影数据.xls', formatting_info=True)
sheet = workbook.sheet_by_index(0)

workbook_copy = xlwt.Workbook()
sheet_copy = workbook_copy.add_sheet('Sheet1')

col1 = []
col2 = []
day = 0
daylist = []
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell_value(row, col)
        if col % 2 == 0 and value != '':
            col1.append(value)
        elif col % 2 == 0 and sheet.cell_value(row, col + 1) != '':
            col1.append(value)
            day += 1
            daylist.append(row)

        elif col % 2 == 1 and value != '':
            col2.append(value)
