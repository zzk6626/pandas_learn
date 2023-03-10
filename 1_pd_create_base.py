import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,44,1])
print(s)  # dtype: float64

dates = pd.date_range('20160101',periods=6)
print(dates) # ['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04','2016-01-05', '2016-01-06']

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d']) # 每一行每一列都有自己的元素/行名/列名
print(df)

df1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df1)  # 生成了数列，但是行列名变成了 '0-1-2'
print('-----------------')
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20210101'),            # 返回日期格式
                    'C':pd.Categorical(['test','train','test','train'])})   # 利用字典对齐
print(df2)  # 虽然A，B只写了1一个值，但是利用字典对齐，C存在两个值，那么A，B会复制自己对齐C
print(df2.dtypes)  # A-float64   B-datetime64[ns]   C-category类别   dtype: object对象   查看每一列的具体数据类型
print(df2.index)  # RangeIndex(start=0, stop=2, step=1) 返回行的大小信息： start:stop-1 ==> start:stop:step
print(df2.columns)  # 列号[A,B,C] 类型object
print(df2.values)  # 全部的元素信息，列表[2,3]
print(df2.describe())  # 获取dataframe中数字 列 的信息，包括个数，均值，标准差，最大值，最小值等
print(df2.T)  # 对数据表进行了转置操作
print(df2.sort_index(axis=1,ascending=False))  # axis=1从列标题的角度思考 倒叙排序 A-B-C => C-B-A ascending-上升
print(df2.sort_index(axis=0,ascending=False))  # axis=0从行标题的角度思考 倒叙排序 0-1 => 1-0
print(df2)  # 以上操作都不会改变df2本身，需要重新定义变量
print(df2.sort_values(by='C'))  # 对第C列的值进行排序，test,train,那么就是相同的将排在一起