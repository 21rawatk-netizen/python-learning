# importing pandas files
import pandas as pd
import numpy as np

# Series from list
a=["india","usa","russia","canada"]
p=pd.Series(a)
print(p)
#Series from integer
i=["23","45","67","89"]
i_series=pd.Series(i)
print(i_series)

# Custom index   or labels: we can sepcify the labels of items if not specified then values are labels based on the oindex number
marks=["45","89","97","55"]
subjects=["english","maths","hindi","science"]
m=pd.Series(marks,index=subjects)
print(m)

# setting name:using name attribute to give the name to series
marks=["45","89","97","55"]
subjects=["english","maths","hindi","science"]
m=pd.Series(marks,index=subjects,name="kiran ke marks")
print(m)

#Series from the dictionarty
marks = {
    "maths":67,
    "english":34,
    "hindi":97,
    "science":88
}
d=pd.Series(marks)
print(d)

#attributes
#size: it gives the no. of items in the Series
print(p.size)
print(i_series.size)
print(m.size)
print(d.size)
#dtype; it give the data type of the items
print(p.dtype)
print(i_series.dtype)
print(m.dtype)
print(d.dtype)
#name:it give and tells the name of the series
print(p.name)
print(d.name)
print(m.name)
#is_unique: it tell that all items in the series is unique or not
print(p.is_unique)
print(d.is_unique)
print(m.is_unique)
