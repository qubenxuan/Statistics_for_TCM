import pandas as pd  # 导入pandas库

df = pd.read_spss('例4-4 实验4-2血清滴度倒数.sav')  # 读取spss文件
data = df.values.tolist()
a = 1
for i in data:  # 遍历data
    a = a * (i[0])
ave = a ** (1 / len(data))  # 计算几何平均数
print('几何平均数为{}'.format(round(ave)))  # 输出几何平均数
