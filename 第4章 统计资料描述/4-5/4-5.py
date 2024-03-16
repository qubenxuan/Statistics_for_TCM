import pandas as pd
df = pd.read_spss('例4-7,4-8 实验4-5潜伏期.sav') #读取spss文件
data1 = df['下限值'].tolist()
data2 = df['频数'].tolist()
def p(x):
    for n in range(len(data2)):
        while (x * sum(data2)) < sum(data2[0:n+1]) and (x * sum(data2)) > (sum(data2[0:n])):
            return data1[n] + (data1[n]-data1[n-1]) * (x * sum(data2) - sum(data2[:n])) / (sum(data2[:n+1]) - sum(data2[:n]))
print(p(0.25),p(0.5),p(0.75))
