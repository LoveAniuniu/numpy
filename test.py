import numpy as np

print(np.__version__)

print("使用列表生成一维数组")
data = [1,2,3,4,5,6]
print(data)
print(type(data))

x = np.array(data)
print(x)
print(type(x))
print(x.ndim)
print(x.dtype)#数据类型
print(x.shape)#数组类型

print("使用列表生成二维数组")
data = [[1,2],[3,4],[5,6]]
x = np.array(data)
print(x)
print(x.ndim)
print(x.shape)

print("使用zeros/ones创建数组")
x = np.zeros((2,3,4),dtype = np.int8)
print(x)
print(x.dtype)


print("使用arange生连续元素 ")

print(np.arange(6))
print(np.arange(1,6,2))

print("使用astype复制元素，并且转化类型")
x = np.array([1,2,3,4,5], dtype=np.float32)
y = x.astype(dtype = np.int32)

print(x)
print(y)


x = np.array(['1'], dtype = np.string_)
y = x.astype(np.int8)
print(x)
print(y)

print("将字符串元素转化为其它的数组的数据类型")

x = np.array([1,23,4,5], dtype= np.float64)
y = np.arange(3, dtype=np.int32)

print(x)
print(y.astype(x.dtype))

print("ndarray数组与标量的运算")

x= np.array([1,2,4])
y = np.array([1,2,4])
print(x*2)
print(x>2)

print(x*y)


print("ndarray基本索引")

x = np.array([[1,2],[3,4]])
print(x.shape)
print(x[1])
print(x[1][0])
print(x[1,0])

y = x[0].copy()
print(y)

print("ndarray切片")
x = np.array([1,2,3,4,5])
print(x[1:4])
print(x[:3])
print(x[0:4:2])

x = np.array([[1,2],[4,3]])
print(x[:2])
print(x[:2,:1])


x= np.arange(24).reshape(24,1)
print(x)