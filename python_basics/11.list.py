#list = ordered, changeable, allow duplicates
list1=[1,2,3,4,5]
list2=["a","b","c",45]
print(type(list1))
print(type(list2))
# count= no. of times a word phrase used in a list
a=(list1.count(2))
print(a)
print(list2.count("a"))
#using list constructor to make a list
list1=list((1,2,3,4,5))
print(list1)
# len (length) of list
print(len(list1))
print(len(list2))
# acessing the elements in list
print(list1[0])
print(list1[1])
print(list1[4])
print(list1[-1])
print(list2[0])
print(list2[1])
print(list2[3])
print(list2[-1])

# slicing
print(list1[2:5])
print(list2[:5])

# checking the existence
if 2 in list1:
    print("True")
if 2 in list2:
    print("True") 
else:
    print("False")  

# changing the value
list1[1]=45
print(list1)
list2[3]="d"
print(list2)

#inserting new items
# insert(index,element)
# insert returns none so you can't assign it to a variable
list1.insert(5,7)
print(list1)
#extend=element from another list add to the existing list
list1=[1, 45, 3, 4, 5, 7] 
list2=['a', 'b', 'c', 'd']
list1.extend(list2)
print(list1)

#Removing
#remove()= removing specific index item.if they have same value more than one time so it remoe the first occurence of that word
list1=[1, 45, 3, 4, 5, 7, 'a', 'b', 'c', 'd']
list1.remove("d")
print(list1)
#pop()=remove specific index
list1=[1, 45, 3, 4, 5, 7, 'a', 'b', 'c']
list1.pop(8)
print(list1)
#without specifying the index number it directly removes the last index
list1.pop()
print(list1)
# del keyword remove the specified index or without the index it remove completly
del list1[6]
print(list1)
del list2
#clear=removes all the leements form the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

#looping
list1=[1, 45, 3, 4, 5, 7, 'a', 'b', 'c', 'd']
#for loop
for i in list1:
    print(i)
#loop through index number
for i in range(len(list1)):
    print(list1[i])
#while loop
i=0
while i<len(list1):
    print(list1[i])
    i=i+1

#List comprehension="when you want to create new list based on the values of an existing list"
fruits=["apple","mango","banana","kiwi","grapes"]
newlist=[]
for i in fruits:
    if "a" in i:
        newlist.append(i)
print(newlist)

# list sorting
# sort()=this method sort the list ascending,descendong and alphanumerically
list3=[5,6,7,2,3,1,99,45]
list3.sort()
print(list3)

#Descending sort=using keyword argument reverse=True
list3=[5,6,7,2,3,1,99,45]
list3.sort(reverse=True)
print(list3)

#reversing the order of list
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.reverse()
print(fruits)
