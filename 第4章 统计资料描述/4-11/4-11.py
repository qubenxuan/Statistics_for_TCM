import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC']  # 设置中文

df = pd.read_spss('例4-16数据.sav').copy()  # 读取spss文件
data1 = df['例数'].copy()
data2 = df['分型'].copy()
a = []
for i in range(len(data1)):
    a.append(data1[i] / sum(data1))

fig1, ax1 = plt.subplots(1, 1, figsize=(10, 10))
ax1.pie(a,
        explode=[0.3, 0.3, 0, 0],
        labels=data2,
        labeldistance=1,
        startangle=90,
        counterclock=False,
        rotatelabels=True,
        autopct='%1.1f%%',
        pctdistance=1.2)
plt.title('孕妇分娩情况', loc='left')
plt.legend()
plt.show()
