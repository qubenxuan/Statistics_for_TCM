import pandas as pd #导入pandas库
import math #导入math库
df = pd.read_spss('例4-5 实验4-3血清抗体滴度倒数.sav') #读取spss文件
data1 = df['血清抗体滴度倒数'].tolist()
data2 = df['频数'].tolist()
b = 0
for i in range(len(data1)):
    b =  (math.log(data1[i],10) * data2[i]) + b 
ave = (10) ** (b/sum(data2)) #计算几何平均数
print('几何平均数为：{}'.format(round(ave))) #输出几何平均数
