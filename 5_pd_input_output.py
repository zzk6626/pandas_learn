import pandas as pd
import numpy as np

# read_csv(最常见的读取方法),read_excel,read_pickle(python最大压缩的一种数据格式),read_html(读取网页)
# to_csv,to_excel,to_pickle 保存方法

df = pd.read_csv('1D.csv',header=None)     # read_csv可以读取txt文件，header=None设置文件不包含标题行

df.columns = ['ID','Point','Man']   # 通过pd数组列名称信息 重新赋值 构建好看的表格

print(df)

# 变量本身加后缀保存文件，index参数标志是否保存左边的索引名[0,1,2,3]，header参数标志是否保存列名,index_label为索引名，在表格数据的左上角
df.to_csv('1D_trans1.csv',index_label='index_label',header=None)