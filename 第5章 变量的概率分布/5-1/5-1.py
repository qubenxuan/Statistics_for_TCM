import pandas as pd
from scipy.stats import norm

df = pd.read_spss('例5-1.sav')
data = df.values
dis = norm(data.mean(), data.std())
a = dis.cdf(15.60)
m = round(len(df) * a)
print(m)


def l(b):
    n = dis.cdf((data.mean() + b * data.std())) - dis.cdf((data.mean() - b * data.std()))
    return round(n, 2)


def s(b):
    d = data[(data[:] > float(data.mean() - b * data.std())) & (data[:] < float(data.mean() + b * data.std()))]
    c = len(d)
    return round(c / len(df), 2)


print(l(1), s(1), '\n', l(1.96), s(1.96), '\n', l(2.58), s(2.58))
