import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)

res1 = pd.concat([df1,df2,df3],axis=0)  # axis=0 按行操作，默认axis=0，   axis=0 ==> 竖向划分
print(res1)  # 这样合并的话前面的index会有重复

res2 = pd.concat([df1,df2,df3],axis=0,ignore_index=True) # 忽略自身的index，重新排序
print(res2)


print('----------------------------------------------------')
df4 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])  # 设置index的具体内容
df5 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])  # 设置index的具体内容
df6 =  pd.DataFrame(np.ones((3,4))*2,columns=['c','d','e','f'],index=[2,3,4])  # 设置index的具体内容
print(df4)
print(df5)
print(df6)
print('----------------------------------------------------')

# out-并集    inner-交集
res3 = pd.concat([df4,df5],join='outer')  # 默认joint = 'outer'标志df4中没有‘e’，那么df4中a的位置填充nan，同理，拼接后的df5中'a'的位置填充nan
res4 = pd.concat([df4,df5],join='inner')  # join='inner' 仅保留两者相同的东西，'b','c','d'
print(res3)
print(res4)

res5 = pd.concat([df4,df5],join='inner',ignore_index=True)  # 在res4基础上，忽略index的相同位置，重新构建index
print(res5)

res6 = pd.concat([df4,df5],axis=1)
print(res6)

# how: One of ‘left’, ‘right’, ‘outer’, ‘inner’. 默认inner。inner是取交集，outer取并集。比如left：[‘A’,‘B’,‘C’];right[’A',‘C’,‘D’]
# inner取交集的话，结果[A,C]
# outer取并集的话，结果[A,B,C,D]
# left以左侧df为准，匹配右侧，结果[A,B,C]。right以右侧df为准，匹配左侧，结果[A,C,D]。

res7 = pd.merge(df4,df5,how='left',left_index=True, right_index=True)   # 以index为链接键,left_index,right_left_index必须全为True,按照索引进行合并，保留df4的索引编号
print(res7)

res8 = df4.append(df5,ignore_index=True)  # append 保持行不变，按行来看，竖向拼接
print(res8)

res9 = df4.append([df5,df6],ignore_index=True)
print(res9)

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res10 = df4.append(s1,ignore_index=True)  # 合并一个pd.Series样本
print(res10)