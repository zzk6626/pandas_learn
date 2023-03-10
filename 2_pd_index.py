import pandas as pd
import numpy as np

dates = pd.date_range('20220408',periods=6)  # 日期类型，逐个增加
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)

print(df['A'],df.A)  # 打印第A列的数据，两个命令的作用相同。打印的数据包括 行（日期参数） - 数值
print('--------------------------')
print(df[0:3])
print(df['20220408':'20220410'])  # 采用切片的方法，第[0:3]行的数据，包括行-列说明，或者采用行名称['20220408':'20220410']进行顺序索引

# 标签筛选 select by label:loc
print(df.loc['20220408'])  # 仅打印该行的信息，打印出来的元素，若shape不包含行列名信息
print(df.loc[:,['A','B']])   # 选择两列，把所有行的信息打印出来，打印出来的元素，若shape不包含行列名信息
print(df.loc['20220408',['A','B']])  # 选择两列，然后仅打印20220408行的信息,A,B仍然出现对应数据，但是打印出来元素的shape为(2,)

# 位置筛选 select by position:iloc
print(df.iloc[3,1])  # 13，打印出元素
print(df.iloc[[1,3,5],1:3])  # 切片操作

# mixed selection:ix  ix用法在pandas-0.20.0后不被使用
# print(df.ix)

# 条件筛选 Boolean indexing
print(df[df.A>8])  # 筛选第A列大于8的数据，并且显示B,C,D列的数据

