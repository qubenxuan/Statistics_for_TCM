import matplotlib.pyplot as plt
import pandas as pd  # 导入pandas库

plt.rcParams['font.sans-serif'] = ['Songti SC']  # 设置中文
df = pd.read_spss('例4-14数据.sav').copy()  # 读取spss文件
data1 = df.loc[:, '阳性率'].copy()
data2 = df.loc[:, '强阳性率'].copy()
data3 = df.loc[:, '年龄'].copy()

fig = plt.figure()
x = list(range(3))
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
F1 = ax.bar(x, data1, color='b', width=0.25)
F2 = ax.bar(x, data2, color='g', width=0.25, tick_label=data3)
ax.legend((F1, F2), ("阳性率", "强阳性率"))
ax.set_xlabel('年龄')
ax.set_ylabel('阳性率/强阳性率')
ax.set_title('不同年龄段阳性率和强阳性率的比较')
plt.show()
