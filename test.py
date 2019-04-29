import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series
from matplotlib import pyplot

# Data
df = pd.read_csv('C:\\Users\\rbasn\\Documents\\Arundo\\src\\server\\data\\data.csv')
#series = Series.from_csv('C:\\Users\\rbasn\\Documents\\Arundo\\src\\server\\data\\data.csv', header=0)
#series.plot()
#pyplot.show()
plt.plot(df['current_temp'])
plt.plot(df['outside_temp'])
plt.plot(df['target_temp'])
#plt.plot(df['time'])
#df.dropna()
#plt.plot(df['weather'])
plt.show()
#print(df['time'])

#df.dropna()
#plt.bar(df['weather'], df['outside_temp'], align='center', alpha=0.5)
#plt.show()
# multiple line plot
#plt.plot('x', 'y1', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue', linewidth=4)
#plt.plot('x', 'y2', data=df, marker='', color='olive', linewidth=2)
#plt.plot('x', 'y3', data=df, marker='', color='olive', linewidth=2, linestyle='dashed', label="toto")
#plt.legend()