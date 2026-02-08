#set:unordered=cannot be acessed using the index no.,unchangeable=no adding and reoving,duplicates are not allowed
s={"apple","b","c",1,2,3}
print(s)
print(type(s))
print(len(s))

#set constructor
t=set(("a","b",1,2,3))
print(t)

#copying set
x=s.copy()
print(x)

#acessing set items
#cannot acess items in set using index
#But you can use loop to get items in a set
s={"apple","b","c",1,2,3}
for i in s:
    print(i)
#check if a item present or not
s={"apple","b","c",1,2,3}
print("banana" in s)
print("apple" in s)

#adding: since it is unchangeable but you can add new item
#1. add():one item addititon
s={"apple","b","c",1,2,3}
s.add("kiwi")
print(s)
#2. update():it can be used in any iterable object,add item from another set into current set
# it updates the current object
s={"apple","b","c",1,2,3}
t={2,3,4,5}
s.update(t)
print(s)

#Removing items
#1.remove():it will emove the specific item
# if the item you are removing is not present in the set it will thorw the error
s={"apple","b","c",1,2,3}
s.remove("apple")
print(s)
#2.discard():remove the specific item.If the item to remove does not exist,It will not raise an error
s={"apple","b","c",1,2,3}
s.discard("apple")
print(s)
#3. pop():this removes the random item cause sets are unindexed
#it can also return the pop item
s={"apple","b","c",1,2,3}
x=s.pop()
print(x)
print(s)
#4.clear():method empties the set
s={"apple","b","c",1,2,3}
s.clear()
print(s)
#5.del keyword delete the set completely
s={"apple","b","c",1,2,3}
# del s (it will raise an error)
print(s)

#Looping:
s={"apple","b","c",1,2,3}
for x in s:
    print(x)

# Joining sets
# 1.union():it combines the all items of the both sets
s1={1,2,3}
s2={"a","b","c"}
s3=s1.union(s2)
print(s3)
#it can be used for joining other data types
#2.update():method insert all irems from one set to another set
# changes the original set and does not retun a new set
s={"apple","b","c",1,2,3}
t={2,3,4,5}
s.update(t)
print(s)
#3. intersection():method will return a new set.that only contains the items that are present in both sets
s1={1,2,3}
s2={"a","b","c",1}
s3=s1.intersection(s2)
print(s3)
#4. intersection_update():this method will also keep only the duplicates , but it will change the original set instead of returnng the new set
s1={1,2,3}
s2={"a","b","c",1}
s1.intersection_update(s2)
print(s1)
#5.Diffrence():method will remove a new set that will contain only the items  from the first set that ae not present in the other set
s1={1,2,3}
s2={"a","b","c",1}
s3=s1.difference(s2)#s1-s2
s4=s2.difference(s1)#s2-s1
print(s3)
print(s4)
#6.differencce_update():it does the diffrence between two set but do not return a new set 
s1={1,2,3}
s2={"a","b","c",1}
s1.difference_update(s2)
print(s1)
#7. symmetric_difference():this method willl keep the item that are not present in the both sets
s1={1,2,3}
s2={"a","b","c",1}
s3=s1.symmetric_difference(s2)
print(s3)
#7. symmetric_difference_update():this method willl keep the item that are not present in the both sets.it will not return the new set it will update the existing set
s1={1,2,3}
s2={"a","b","c",1}
s3=s1.symmetric_difference_update(s2)
print(s3)

#Python frozen set
# it is the immutable vesion of a set
# it contain unique,unordered,unchangeable elements
# unlike sets, elements cannot be added or emove from a frozenset
#frozenset():constructor to create a frozenset
x=frozenset({"apple","b","c"})
print(x)
print(type(x))

#methods
#isdisjoint():retuns whether two set have intersection or not
s1={1,2,3}
s2={"a","b","c"}
z=s1.isdisjoint(s2)
print(z)
#issubset():returns true if all elements of this set is present in another set
x={1,2,3}
y={"a","b","c",1,2,3}
z=x.issubset(y)
w=y.issuperset(x)
print(z)
