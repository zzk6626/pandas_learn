import pandas as pd
import numpy as np

dates = pd.date_range('20220408',periods=6)  # 日期类型，逐个增加
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)

# 设置值的话会直接改变 pd数组 元素
df.iloc[2,2] = 1111  # 位置筛选---更改元素
df.loc['20220408','B'] = 2222  # 标签筛选---更改元素
df.A[df.A>16] = 0  # 把A这一列大于16的   A列元素   全部赋值为0
print(df)
df.B[df.A>16] = 0  # 把A这一列大于16的   B列元素   全部赋值为0
print(df)
df[df.A>8] = 0    # 把A这一列大于8的    A,B,C,D列元素  全部赋值为0
print(df)

print('-----------------------------------')

df['F'] = np.nan  # 添加一列，并且把此列元素全部设置为 nan
df['E'] = pd.Series([1,2,3,4,5,6],index=dates)   # 必须设置index与行参数dates对应，若不设置全部为 nan
print(df)