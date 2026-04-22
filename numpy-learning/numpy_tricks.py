#np.sort
# it returns sported copy of an array 
# syntax: np.sort(array , axis= ,kind : what kind of sorting you wanna do , order)
#1D
import numpy as np
a=np.random.randint(1,100,15)
print(a)
print(np.sort(a))
#2D
b=np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.sort(b,axis=0))#column
print(np.sort(b,axis=1))#row
#np.append=append the values along the mentioned axis at the end of the array
#1D
a=np.random.randint(1,100,15)
print(a)
print(np.append(a,200))
#2D
b=np.random.randint(1,100,24).reshape(6,4)
print(b)
print(np.append(b,np.ones((b.shape[0],1)),axis=1))
print(np.append(b,np.ones((1,b.shape[1])),axis=0))
#np.conactenate:the fnction concatenate a sequence of array along an existing axis
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
print(c)
print(d)
print(np.concatenate((c,d),axis=0))
print(np.concatenate((c,d),axis=1))
#np.unique:with the help of this function we can get unique values from an array given as parameter in np.unique() method
e=np.array([1,2,1,1,1,1,2,2,2,23,3,3,4,4,4,5,5,56,6,7])
np.unique(e)
#np.expand_dims:getting expanded dimension of an array
#1D
a=np.random.randint(1,100,15)
print(a)
np.expand_dims(a,axis=0)
np.expand_dims(a,axis=1)
#np.where:it return the indices of the element in an array where the given cindition is satistfied
#find where a >80
print(a)
print(np.where(a>80))
# syntax np.where(condition,true,false)
# replace all values >50 with 0
print(np.where(a>50,0,a))
print(np.where(a>50,0,1))
#np.argmax:this function returns the indices of elements of the array with maximum value but not the value itself.
print(np.argmax(a))
#np.argmin:this function returns the indices of elemnts woth the smallest value but not the value itself
print(np.argmin(a))
#np.cumsum:cummulative sum of array
print(a)
print(np.cumsum(a))
#np.cumprod:cummulative product of elements
print(a)
print(np.cumprod(a))
#np.percentile:it is used to compute the nth percentile of the given data along with the specified axis
print(a)
print(np.percentile(a,50))
#np.histogram:This function less the frequency of data distribution in the graphical form
print(a)
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100]))
#np.corrcoef: it returns the pearson product_moment correlation coefficients
salary=np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,2])
print(np.corrcoef(salary,experience))
#np.isin:we can see that one array having values are checked in a different numpy array having , are is array me woh array ke otem hai ki nhi
print(a)
item=[10,20,70,90,100,60,40]
print(np.isin(a,item))
#np.flip:reverse the order of array elements along the specific axis, preserving the slope of the array.
#1D
print(a)
print(np.flip(a))
#2D
print(b)
print(np.flip(b))#both type of fliping
print(np.flip(b,axis=0))#col,vertical
print(np.flip(b,axis=1))#row,horizontal
#np.put:eplace specific elements of an array with the given values of p.array
#syntax: np.put(array,index to replace,new data)
#modifies the original array
np.put(a,[1,2],[24,30])
print(a)
#np.delete:returns a new array with the deletion of sub array along with the mentioned axis 
#syntax/: np.delete(array,index,axis=)
print(a)
np.delete(a,[0,2])
#set functions
import numpy as np

m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

print(np.union1d(m,n))         # union
print(np.intersect1d(m,n))     # intersection
print(np.setdiff1d(m,n))       # m - n
print(np.setdiff1d(n,m))       # n - m
#np.clip:function used to clip limit of the values in an array
print(a)
print(np.clip(a, a_min=60, a_max=75))
