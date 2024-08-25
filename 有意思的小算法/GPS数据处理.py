import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel('./GPS.xlsx')

time=data[data.columns[0]]

print(time[0])
