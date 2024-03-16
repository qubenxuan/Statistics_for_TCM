import pandas as pd #导入pandas库
import matplotlib.pyplot as plt #导入matplotlib库
plt.rcParams['font.sans-serif'] = ['Songti SC'] #设置中文
import numpy as np

df = pd.read_spss('例4-13数据.sav') #读取spss文件
data1 = df.接种率.copy()
data2 = df.疫苗.copy()
data3 = df.地区.copy()
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
X = np.arange(3)
ax.set_ylim(0,100) 
ax.set_xlabel('地区')
ax.set_ylabel('接种率')
ax.set_title('各地区疫苗接种率')

F1 = ax.bar(X + 0.00, data1.iloc[:3,].copy(), color = 'b', width = 0.2)
F2 = ax.bar(X + 0.2, data1.iloc[3:6,].copy(),color = 'c', width = 0.2)
F3 = ax.bar(X + 0.4, data1.iloc[6:9,].copy(),color = 'r', width = 0.2)
F4 = ax.bar(X + 0.6, data1.iloc[9:,].copy(), color = 'y', width = 0.2)
F5 = ax.bar(X + 0.3, 0, color = 'r', width = 0.2,tick_label=data3.iloc[:3].copy())
ax.legend((F1,F2,F3,F4),("卡介苗","脊灰","百白破","麻疹"))
for c in [F1,F2,F3,F4]:
    ax.bar_label(c)
plt.show()
