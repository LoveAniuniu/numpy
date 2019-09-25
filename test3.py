import numpy as np

print("换轴")

k = np.arange(12).reshape(4,3)
print(k)

print("numpy基本统计方法")
x = np.array([[1,2],[3,4],[5,6]])
print(x)
print(x.shape)
# axis=0 对列相加求均值  axis=1对每一行求均值
print(x.mean(axis=1))

print("求和")
print(x.sum())
print(x.sum(axis=1))

x=np.array([[6,1,3],[5,3,1]])
x.sort()
print(x)

print("ndarray的存取")

x=np.array([[1,6,2],[6,1,3],[1,5,2]])
np.save("file", x)#已二进制

y=np.load("file.npy")
print(y)


print("矩阵求逆")
x=np.array([[1,1],[1,2]])
y = np.linalg.inv(x)
print(y)

print("ndarray随机数")
x=np.random.randint(0,2, size=10000)
print(x)
print("正面次数")
print((x>0).sum())

print("where函数")
cand = np.array([True,False,True,False])
x = np.where(cand,-2,2)
print(x)