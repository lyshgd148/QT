import xlrd

ob = xlrd.open_workbook('电影数据.xls')

# 选择工作表
print(f'EXCEL中有{ob.nsheets}个工作表')
print(f'EXCEL中的sheet:{ob.sheet_names()}')

sh1 = ob.sheet_by_index(0)
sh2 = ob.sheet_by_name('电影')
print(f'sheet中有{sh1.nrows}行{sh1.ncols}列')

print(f'1行2列:{sh1.cell_value(0, 1)}')
print(f'1行2列:{sh1.cell(0, 1).value}')
print(f'1行2列:{sh1.row(0)[1].value}')  # row:行; col:列

print(sh1.row_values(0))
print(sh1.col_values(0))

# 遍历
for r in range(sh1.nrows):
    for c in range(sh1.ncols):
        print(f'{r + 1}行{c + 1}列:数据{sh1.cell_value(r, c)}')
