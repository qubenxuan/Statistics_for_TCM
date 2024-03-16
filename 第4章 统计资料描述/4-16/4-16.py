import pandas as pd #导入pandas库
import matplotlib.pyplot as plt #导入matplotlib库
plt.rcParams['font.sans-serif'] = ['Songti SC'] #设置中文

d = pd.read_spss('例4-21数据.sav') #读取spss文件
data1 = d['红细胞数']
data2 = d['频数']
data3 = d['红细胞数2']

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
X = list(range(len(data1)))
ax.set_ylim(0,100) 
ax.set_xlabel('红细胞数')
ax.set_ylabel('频数')
ax.set_title('红细胞数的频数分布')
ax.bar(X, (data2), color = 'grey', width = 1,edgecolor = 'black',hatch = '\\\\\\\\ ')
ax.set_ylim(0,40)
ax.set_xticks(X)
ax.set_xticklabels("%.1f"%i for i in data3)
plt.show()

