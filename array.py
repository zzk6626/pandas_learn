import numpy as np

a = np.arange(1,9).reshape(2,4)
print(a)

b = a.copy() # 修改数组b内的元素，不会影响到a内的元素，倘若不加copy就会改变b的元素
print(b)

b[0,1] = 5
print(b)
print(a)