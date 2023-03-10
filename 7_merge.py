import pandas as pd
import numpy as np

left1 = pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})

right1 = pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

print(left1)
print(right1)

res1 = pd.merge(left1,right1,on='key')  # on参数，选定在哪一个columns上面合并
print(res1)

left2 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

# mercy函数how默认为inner
res2 = pd.merge(left2, right2, on=['key1', 'key2'], how='inner') # 依据key1与key2 columns进行合并，并打印出四种结果
print(res2)  # left中只有一个K1-K0序列，因此要复制left一次，为了和right2中两个K1-K0合并

# outer
res3 = pd.merge(left2, right2, on=['key1', 'key2'], how='outer') # 依据key1与key2 columns进行合并，并打印出四种结果
print(res3)  # 如果key1-key2中left有，right没有，那么设为nan

# right
res4 = pd.merge(left2, right2, on=['key1', 'key2'], how='right') # 依据key1与key2 columns进行合并，并打印出四种结果
print(res4)  # 保证右侧所有数据完整性，取左侧key1-key2相同的数据，若存在1-2的关系，那么left复制1个对应上right，若不存在，那么设为nan

# left
res5 = pd.merge(left2, right2, on=['key1', 'key2'], how='right') # 依据key1与key2 columns进行合并，并打印出四种结果
print(res5)  # 与right相反

# indicator 将合并的记录放在新的一列  _merge列  left_only both right_only
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
res6 = pd.merge(df1, df2, on='col1', how='outer', indicator=True)  # indicator='indicator_column',在True的基础上修改_merge列的名字
print(res6)

left3 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right3 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(left3)
print(right3)

# 考虑index的关系进行合并 left_index=True, right_index=True
# 依据左右资料集的index进行合并，how='outer',并打印出
res7 = pd.merge(left3, right3, left_index=True, right_index=True, how='outer')
print(res7)
# 依据左右资料集的index进行合并，how='inner',并打印出
res8 = pd.merge(left3, right3, left_index=True, right_index=True, how='inner')
print(res8)

boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
print(boys)
print(girls)
# 使用suffixes解决columns中overlapping(部分重叠)的问题，将其转移到索引上,区分名字相同，但是内容不同的数据
res = pd.merge(boys, girls, on='k', suffixes=('_boy', '_girl'), how='inner') # suffixes 在非on上加上后缀
print(res)
