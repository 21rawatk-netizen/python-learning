#tuple= ordered, unchangeable,allow duplicates
t=("a",1,2,3,4)
print(type(t))
print(t)
print(len(t))
u=tuple(("a",1,2,3,4))
print(u)
print(t.count(1))

#Acessing
t=("a",1,2,3,4)
print(t[1])
print(t[-1])

# acessing range of elements
t=("a",1,2,3,4)
print(t[2:4])
print(t[:4])
print(t[2:])
print(t[-4:-1])

#checking the existence using in operator
t=("a",1,2,3,4)
if "a" in t:
    print(" ahahaha")

#since they are unchangable so you cannot ,add or remove once the tuple is created
# To add items in a tuple

#1. convert the tuple into list and add the items
t=("a",1,2,3,4)
y=list(t)
y.append(5)
t=tuple(y)
print(y)
#2.adding tuple to a tuple
t=("a",1,2,3,4)
y=("orange",)
#always remember the comma othereosw it will refer as string
t+=y
print(t)

#Removing items: since they are unchangeable
#1.convert tuple into a list
t=("a",1,2,3,4)
y=list(t)
y.remove("a")
t=tuple(y)
print(t)
#2.or completely delete the tuple usng the del keyword
t=("a",1,2,3,4)
del t
# it will raise an error (print(t))

# packing = assigning values
# unpacking = extract the value back into variables
fruits=("a",1,2,3,4)
(green,red,yellow,blue,white)=fruits
print(green)
print(red)
print(yellow)
print(blue)
print(white)
# using asterick for unpacking
# if the number of vaiables is less tha the number of values you can add an* to the variables name and the value
fruits=("a",1,2,3,4)
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#looping the tuples
#for
t=("apple",1,2,3,4)
for i in t:
    print(i)

#loop through index
t=("apple",1,2,3,4)
for i in range(len(t)):
    print(t[i])

#while
t=("apple",1,2,3,4)
i=0
while i<len(t):
    print(t[i])
    i+=1

#joining tuples
t1=("apple",1,2,3,4)
t2=("apple",1,2,3,4)
t3=t1+t2
print(t3)

#multiplying tuples
t1=("apple",1,2,3,4)
t2=t1*2
print(t2)
