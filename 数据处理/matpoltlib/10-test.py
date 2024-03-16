import numpy as np
import matplotlib.pyplot as mp

x = np.arange(12)
apples = np.random.randint(10, 49, 12)
oranges = np.random.randint(30, 69, 12)
print(x, apples, oranges)
mp.figure('柱状图', facecolor='lightgray')
mp.bar(x, apples, 0.8, label='Apples', align='center')
mp.bar(x, oranges, 0.8, apples, label='Oranges', align='center')
mp.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
