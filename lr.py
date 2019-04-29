from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df = pd.read_csv('C:\\Users\\rbasn\\Documents\\Arundo\\src\\server\\data\\data.csv')
#sns.pairplot(df)
df.dropna()
#df['current_temp']
#df['target_temp']
#df['outside_temp'].dropna()
df.dropna(how='any')
df.dropna(how='all')
df = df[np.isfinite(df['outside_temp'])]
df = df[np.isfinite(df['pressure'])]

reg = LinearRegression().fit(df[['outside_temp','target_temp','heater_val','humidity','pressure']][1:60000], df['current_temp'].astype(int)[1:60000])
predict = reg.predict(df[['outside_temp','target_temp','heater_val','humidity','pressure']][60000:90000])
plt.scatter( df['outside_temp'].astype(int)[60000:90000],predict)
plt.show()
plt.scatter( df['heater_val'].astype(int)[60000:90000],predict)
plt.show()
plt.scatter( df['humidity'].astype(int)[60000:90000],predict)
plt.show()
plt.scatter( df['pressure'].astype(int)[60000:90000],predict)
plt.show()
#print(df['current_temp'].astype(int)[1:10000])