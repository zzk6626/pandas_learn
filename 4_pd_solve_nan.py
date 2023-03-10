import pandas as pd
import numpy as np

dates = pd.date_range('20220408',periods=6)  # pd.date_range 日期类型，逐个增加
df = pd.DataFrame(np.arange(24).reshape(6,4),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
print('-------------------------------------')
print(df.dropna(axis=0,how='any')) # axis=0 按行操作，竖向划分  how={'any','all'}  判断是存在任意一个nan即丢弃 / 全为nan即丢弃
print(df.dropna(axis=1,how='any'))
print(df.dropna(axis=1,how='all'))
print('-------------------------------------')
# 给nan进行填入数据
print(df.fillna(value=0))  # 用数据填入替代nan
print(df.isnull())  # 打印true/false的pd数组，判断每个元素是否丢失数据nan，每个元素是nan则输出true，不是则为false
print(np.any(df.isnull()) == True) # 是否存在一个及以上的isnull标志,np.any() 若有一个为true则输出true
