import matplotlib.pyplot as plt
import pandas as pd #导入pandas库
plt.rcParams['font.sans-serif'] = ['Songti SC'] #设置中文
df = pd.read_spss('例4-19数据.sav') #读取spss文件
data1 = df[df['分组'] == '城市'].copy()
data2 = df[df['分组'] == '农村'].copy()

fig = plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
F1 = ax.plot('年份','对数死亡率',data=data1)
F2 = ax.plot('年份','对数死亡率',data=data2)
ax.axis([1991,2000,0.8,2])
ax.legend([F1,F2],['城市','农村'])
ax.set_xlabel('年份')
ax.set_ylabel('对数死亡率')
ax.set_title('城市和农村死亡率的比较')
plt.show()