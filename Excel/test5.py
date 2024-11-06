import xlrd
import xlwt

# 打开现有的 Excel 文件
workbook = xlrd.open_workbook('电影数据.xls', formatting_info=True)
sheet = workbook.sheet_by_name('Sheet1')

# 创建一个可以编辑的拷贝
workbook_copy = xlwt.Workbook()
sheet_copy = workbook_copy.add_sheet('Sheet1')

# 复制现有 Excel 文件中的数据到新文件
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        if col>1 and row>1:
            value = sheet.cell_value(row, col)
            sheet_copy.write(row, col, value)

# 写入新数据到新文件
new_data = ['New Data 1', 'New Data 2']
for index, data in enumerate(new_data):
    sheet_copy.write(sheet.nrows + index, 0, data)

# 保存修改后的 Excel 文件
workbook_copy.save('电影数据.xls')