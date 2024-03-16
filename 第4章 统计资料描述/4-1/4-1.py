import pandas as pd  # 导入pandas库
import matplotlib.pyplot as plt  # 导入matplotlib库
import numpy as np  # 导入numpy库

plt.rcParams['font.sans-serif'] = ['Songti SC']  # 设置中文 (Windows环境下请改为'simhei')

df = pd.read_spss('例4-1 实验4-1身高.sav')  # 读取spss文件
data1 = df.iloc[:, 1]  # 提取第二列数据
y1 = data1.value_counts().values  # 导出频数
x1 = data1.value_counts().index  # 导出标签（身高）的值
x = x1.values.tolist()  # 将x1转换为列表
y = y1.tolist()  # 将y1转换为列表

# 计算平均数
data2 = list(df.iloc[:, 0])  # 提取第一列数据
a = 0
for i in data2:  # 计算总和
    a = a + i
ave1 = a / len(data1)  # 直接平均数
c = np.array(x) * np.array(y)  # x和y相乘
ave2 = np.sum(c) / len(data1)  # 加权平均数
print("直接法：{:.2f}\n加权法：{:.2f}".format(ave1, ave2))  # 输出平均数

fig, ax = plt.subplots(1, 3, figsize=(15, 5))  # 创建画布
# 绘制表格
z = list(zip(x, y))  # 将x和y合并
ax[0].table(cellText=z,  # 简单理解为表示表格里的数据
            colLabels=["身高", "频数"],  # 每列的名称
            rowLoc="center",  # 行名称的对齐方式
            loc="center",  # 表格的位置
            colLoc="center",  # 列名称的对齐方式
            cellLoc="center",  # 单元格的对齐方式
            colWidths=[0.5, 0.5]  # 列宽
            )
ax[0].axis('off')
# 绘制直方图
p2 = ax[1].bar(x, y)  # 绘制直方图
ax[1].set_xlabel('身高')  # x轴标签
ax[1].set_ylabel('频数')  # y轴标签
ax[1].set_title('身高频数分布直方图')  # 标题
ax[1].bar_label(p2)  # 显示频数
ax[1].set_xticks(x)  # x轴刻度
# 绘制茎叶图
ax[2].stem(x, y)  # 绘制茎叶图
ax[2].set_xticks(x)  # x轴刻度
ax[2].set_xlabel('身高')  # x轴标签
ax[2].set_ylabel('频数')  # y轴标签
ax[2].set_title('身高频数分布茎叶图')  # 标题
# 显示图形
plt.show()
