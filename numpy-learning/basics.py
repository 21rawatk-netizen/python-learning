#creating numpy array
#simple 1D array
import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))

#2D
b=np.array([[1,2,3],[4,5,6]])
print(b)
print(type(b))

#3D
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)
print(type(c))

#if you want to change the datatype of an array
#dtype
d=np.array([1,2,3],dtype=float)
print(d)

#if you want to print numbers till a rangr use arange array ki rang
#arange
e=np.arange(1,11)
print(e)

# if you want to change the shape of your array using reshape
#reshape
f=np.arange(1,11).reshape(2,5)
print(f)

#np.ones & np.seros
#using this you can make array whose all items are 1 or 0
g=np.ones((3,4))
h=np.zeros((3,4))
print(g)
print(h)

#np.random
#when you want to intialize the array using random numbers
i=np.random.random((3,4))
print("array:",i)

#np.linspace
#another way of creating array where you give the low range,uppaer range ,the number of items you want generate
j=np.linspace(-10,10,10)
print(j)

#np.identity
#it is use to create i dentity matrix we just give the number of 1 in the matrix
np.identity(3)
