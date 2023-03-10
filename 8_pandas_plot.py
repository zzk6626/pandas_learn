import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 随机生成1000个数据
data = pd.Series(np.random.randn(1000), index=np.arange(1000))

# 为了方便观看效果, 我们累加这个数据
data1 = data.cumsum()

# pandas 数据可以直接观看其可视化形式
data1.plot()

plt.show()

data = pd.DataFrame(
    np.random.randn(1000,4),
    index=np.arange(1000),
    columns=list("ABCD")
    )

# plot methods: bar, hist, box, kde, area, scatter, hexbin, pie
data2 = data.cumsum()
data2.plot()
plt.show()

ax = data2.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)   # ax=ax 在上面一个图中附上Class2
plt.show()
