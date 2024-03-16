import pandas as pd

df = pd.read_spss('例4-9 实验4-6丸重.sav')  # 读取spss文件
data = df.values.tolist()
data1 = sum(data, [])
ave = sum(data1) / len(data1)
a = 0
for i in range(len(data1)):
    a = (data1[i] - ave) ** 2 + a
s2 = a / (len(data1) - 1)
s = s2 ** 0.5
print('样本方差为：{:.3f}\n样本标准差为：{:.3f}'.format(s2, s))  # 输出样本均值和样本标准差
cv = s / ave
print('变异系数为：{:.3%}'.format(cv))  # 输出变异系数
