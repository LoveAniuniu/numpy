import numpy as np

print("adarray数组的转置和轴堆成")
k = np.arange(12).reshape(3,4)
print(k.T)

#内积
print(np.dot(k,k.T))
print("=======================")

print("高维数组的轴对象")
y = np.arange(24).reshape(2,3,4)
print(y)
print(y[1][1][1])