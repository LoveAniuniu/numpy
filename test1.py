
import numpy as np

print("ndarray的布尔型索引")

x = np.array([1,2,3,4,5,6])
y = np.array([True,False,False,False,False,False])
print(x[y])

print(x[y==False])

print(x>3)

print(x[(x==2) | (x==1)])

print(x[[1,2,3]])

print(x[[-1]])

x = np.array([[1,2],[3,4],[5,6]])
print([[0,1]])
print(x[[[0,1],[0,1]]])
print(x[0,1])

print(x[[0,1]][:1,[0,1]])

x = np.arange(24).reshape(2,3,4)

print(x)
print(x[:2,:1,:1])


