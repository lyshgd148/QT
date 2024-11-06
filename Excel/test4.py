import xlrd
import xlwt

workbook = xlrd.open_workbook('Daily English.xls', formatting_info=True)
sheet = workbook.sheet_by_index(0)

workbook_copy = xlwt.Workbook()
sheet_copy = workbook_copy.add_sheet('Sheet1')

col1 = []
col2 = []
day = []
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell_value(row, col)
        if col % 2 == 0 and value != '':
            col1.append(value)
        elif col % 2 == 0 and sheet.cell_value(row, col + 1) != '' and row < sheet.nrows - 1 and sheet.cell_value(
                row + 1, col) != '':
            col1.append(value)
            day.append(row)
        elif col % 2 == 1 and value != '':
            col2.append(value)


def writeBlank(row, col):
    sheet_copy.write_blank(row, col, label="")
    sheet_copy.write_blank(row, col + 1, label="")
    sheet_copy.write_blank(row + 1, col, label="")
    sheet_copy.write_blank(row + 1, col + 1, label="")
    sheet_copy.write_blank(row + 2, col, label="")
    sheet_copy.write_blank(row + 2, col + 1, label="")


index = 0
for row in range(len(col1)):
    for col in range(len(col1)):
        if row != 0 and row == day[index]:
            writeBlank(row, col)
            index += 1
            break
        elif col % 2 == 0:
            sheet_copy.write(row + index * 2, col,col1[row-index])
        elif col % 2 == 1:
            sheet_copy.write(row + index * 2, col,col2[row-index])

workbook_copy.save('Daily English.xls')