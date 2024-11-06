import xlwt

wb=xlwt.Workbook()

#创建工作簿
sh=wb.add_sheet('电影')
#写入数据
sh.write(0,0,'傻逼up')

wb.save('电影数据.xls')