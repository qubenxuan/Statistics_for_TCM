import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC']  # 设置中文
df = pd.read_spss('例4-15数据.sav').copy()  # 读取spss文件
dfa = df.loc[df['分组'] == 'A'].copy()
dfb = df.loc[df['分组'] == 'B'].copy()
dfc = df.loc[df['分组'] == 'C'].copy()
data1 = dfa.loc[:, 'x'].values.copy()
data2 = dfb.loc[:, 'x'].values.copy()
data3 = dfc.loc[:, 'x'].values.copy()
average1 = dfa.loc[:, 'x'].mean()
average2 = dfb.loc[:, 'x'].mean()
average3 = dfc.loc[:, 'x'].mean()


def s(a):
    b = 0
    for i in range(len(a)):
        b = (a[i] - sum(a) / len(a)) ** 2 + b
    return (b / (len(a) - 1)) ** 0.5


fig = plt.figure()
x = list(range(3))
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
F1 = ax.bar(x, [average1, average2, average3], color='grey', width=0.5, edgecolor='black', tick_label=['A', 'B', 'C'])
ax.errorbar(x, [average1, average2, average3], yerr=[s(data1), s(data2), s(data3)], fmt='none', lolims=True, capsize=5,
            color='black')
ax.set_ylim(0, 4)
ax.set_xlabel('分组')
ax.set_ylabel('平均值')
ax.set_title('不同分组的平均值比较')
plt.show()
