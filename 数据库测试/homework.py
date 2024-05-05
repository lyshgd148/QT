import sqlite3

####这一段的代码用于将mysql数据库的 .sql文件数据（就是一堆sql语句） 转换成.db数据文件 这样好用sqlite3库来操作
# import re
#
# with open('city_table.sql', 'r') as f:
#     table = f.read()
# with open('city_data.sql', 'r') as f:
#     data = f.read()
# data = re.sub(r'network_test.city', 'city', data)
# data = data.split(';')
# data_ = list()
# for i in data:
#     if '\n' in i:
#         i = i.replace('\n', '')
#     if i:
#         i += ';'
#         data_.append(i)
#
# coon = sqlite3.connect('./data/city.db')
# c = coon.cursor()
# c.execute(table)
# for i in data_:
#     c.execute(i)
# coon.commit()
# coon.close()


coon = sqlite3.connect('./data/city.db')
c = coon.cursor()
distance_data_db = c.execute('''select * from city''')
coon.close()
for i in distance_data_db:
    print(i)
