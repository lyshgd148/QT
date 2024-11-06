from xlutils.copy import copy
import xlrd

# 打开
read_book = xlrd.open_workbook('电影数据.xls')

wb = copy(read_book)

# 选则工作表
sh = wb.get_sheet(0)
sh.write(5, 0, '报道可拉斯基')
sh.write(5, 1, '报道可')
sh.write(5, 2, '拉斯基')
sh.write(5, 3, '斯基')
sh.write(5, 4, '2123拉基')
# sh1=wb.sheet_by_index(0)
rs=read_book.sheet_by_index(0)
sh2 = wb.add_sheet('汇总')
count=0
for i in range(1,rs.nrows):
    # num=rs.cell_value(i,3)
    # count+=num
    pass

sh2.write(0,0,'12312')
sh2.write(0,1,'3')
wb.save('电影数据.xls')