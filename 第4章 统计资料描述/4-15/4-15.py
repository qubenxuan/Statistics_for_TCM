import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Songti SC']
df = pd.read_spss('例4-20数据.sav')  # 读取spss文件

fig = plt.figure()
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
ax.scatter(df['体重'], df['肺活量'], label="data")
coeff = np.polyfit(df['体重'], df['肺活量'], 1)
ax.plot(df['体重'], coeff[0] * df['体重'] + coeff[1], label="y=" + str(coeff[0]) + "x+" + str(coeff[1]))
ax.legend()
ax.set_xlabel('体重')
ax.set_ylabel('肺活量')
ax.set_title('体重和肺活量的关系')
plt.show()
