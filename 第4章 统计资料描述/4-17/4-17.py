import pandas as pd  # 导入pandas库
import matplotlib.pyplot as plt  # 导入matplotlib库

plt.rcParams['font.sans-serif'] = ['Songti SC']  # 设置中文

df = pd.read_spss('例4-22数据.sav')  # 读取spss文件
data1 = df['淋巴细胞转换率'][df['分组'] == '新药组']
data2 = df['淋巴细胞转换率'][df['分组'] == '安慰剂组']

fig = plt.figure()
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
ax.boxplot([data1, data2], labels=['新药组', '安慰剂组'])
ax.set_xlabel('分组')
ax.set_ylabel('淋巴细胞转换率')
ax.set_title('淋巴细胞转换率的箱线图')
plt.show()  # 显示图形
