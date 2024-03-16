import matplotlib.pyplot as plt
import pandas as pd #导入pandas库
plt.rcParams['font.sans-serif'] = ['Songti SC'] #设置中文
df = pd.read_spss('例4-17数据.sav') #读取spss文件
data1 = df['分化癌'].copy().values
data2 = df['低分化癌'].copy().values
data3 = df['未分化癌'].copy().values

fig, ax = plt.subplots(1,1,figsize=(10,10)) 
y = list(range(2))

F3 = ax.barh(y,data3, color = 'w',left = data1+data2,edgecolor = 'black',linewidth = 1,hatch = '----',height=.5)
F2 = ax.barh(y,data2, color = 'w',left=data1,height=.5,edgecolor = 'black',linewidth = 1,hatch = '++++')
F1 = ax.barh(y,data1, color = 'w',height=.5,edgecolor = 'black',linewidth = 1,hatch = '////')
ax.set_yticks(y)
ax.set_yticklabels(['男','女'])
ax.legend((F1,F2,F3),("分化癌","低分化癌",'未分化癌'))
ax.set_xlabel('发生率')
ax.set_ylabel('性别')
ax.set_title('不同性别癌症发生率的比较')
plt.show()