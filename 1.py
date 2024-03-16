import pandas as pd

df = pd.read_spss('例4-22数据.sav')  # 读取spss
df.to_excel('例4-22数据.xlsx')
