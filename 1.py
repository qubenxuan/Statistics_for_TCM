import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Songti SC']
import numpy as np
df = pd.read_spss('例4-22数据.sav') #读取sps
df.to_excel('例4-22数据.xlsx')