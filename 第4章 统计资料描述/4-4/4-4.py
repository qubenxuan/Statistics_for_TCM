import pandas as pd
df = pd.read_spss('例4-6 实验4-4肥胖者体重.sav') #读取spss文件
data = df.values.tolist()
a = []
for sublist in data:
    for element in sublist:
        a.append(int(element))
a.sort()
if len(a) % 2 == 0:
    print(a[(len(a))//2] , a[(len(a))//2 + 1 ] ) #输出中位数
else:
    print((a[(len(a))//2]))
