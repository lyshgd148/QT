import pandas as pd

t1 = pd.Series(['2024-9-14 06:41:00'])
t1 = pd.to_datetime(t1)
delta = t1 - pd.to_datetime('2024-8-12')
print(delta)
print(delta.dt.days)
print("--" * 40)
data_list = pd.date_range("2024/9/14", periods=5)
print(data_list, type(data_list), '\n')
a = data_list[0]
print(data_list[0], type(data_list[0]),'\n',a, type(a))
