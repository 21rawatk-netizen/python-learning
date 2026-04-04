a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(a1)#1D array you call it as a vector
print(a2)#2D array you call it as a matrices
print(a3)#3D vecto you call it as a tensor

#ndim:no. of dimension in the given array
dim1=a1.ndim
dim2=a2.ndim
dim3=a3.ndim
print(dim1,dim2,dim3)

#shape: it gives the shape of an array. It gives no. of  items for 1D, it gives no. of rows and olumns for matrices
s1=a1.shape
s2=a2.shape
s3=a3.shape
print(s1,s2,s3)

#size : it gives no. of item in the array.
i1=a1.size
i2=a2.size
i3=a3.size
print(i1,i2,i3)

#itemsize : it gives every what one item in the array occupy how much space.
#note the a1 id int and a2 is float but in google colab it gives same value for int and float where in other platform it & float occupy different space
i1=a1.itemsize
i2=a2.itemsize
i3=a3.itemsize
print(i1,i2,i3)

#dtype=datatype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

3Changing datatype
#astype : using astype for changing the datatype of the array
a3.astype(np.int32)
# since i have not stored the new array in a varaible so the datatype is not actually changing
datatypeofa3=a3.dtype
print(datatypeofa3)
print(a1.dtype)
print(a1.itemsize,a3.itemsize)
#in numpy most function are immutable they dont change the original data just return the new copy 
