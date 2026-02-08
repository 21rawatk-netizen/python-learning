#dictionary
# key:value pairs
# ordered,changeable,and do not allow duplicates
d={
    "name":"kiran",
    "age":21
}
print(d)
print(type(d))
print(len(d))
print(d["name"])
print(d["age"])
#dict():constructor for disctionary

#Acessing items
#1.refering to the key
d={
    "name":"kiran",
    "age":21
}
print(d["name"])
#2. get(): method that give the same result
d={
    "name":"kiran",
    "age":21
}
x=d.get("name")
print(x)
#3. key():method that gives the list of all the keys in the dictionary
d={
    "name":"kiran",
    "age":21
}
x=d.keys()
print(x)
#4. values():method return the list of all the value in dictionary 
d={
    "name":"kiran",
    "age":21
}
x=d.values()
print(x)
# items():method that will return each item in the dictionary as a tuple in a list
d={
    "name":"kiran",
    "age":21
}
x=d.items()
print(x)

#Existence
d={
    "name":"kiran",
    "age":21
}
if "age" in d:
    print("yes")

#changing
#1. referring to its key name
d={
    "name":"kiran",
     "age": 21
 }
d["age"]=22
print(d)
#2. update():update the dictionary items
d={
    "name":"kiran",
     "age": 21
 }
d.update({"age":23})
print(d)

#Adding:adding item into a dictionay using a new index key and assinging 
#1. using new index item
d={
    "name":"kiran",
     "age": 21
 }
d["hobby"]="draw"
print(d)
#2. update():method will update if the item already exist. IF the item does not exist, the item will be added.
d={
    "name":"kiran",
     "age": 21
 }
d.update({"hobby":"draw"})

#Removing
#1.pop():removes the item with the specified key name
d={
    "name":"kiran",
     "age": 21
 }
d.pop("age")
print(d)
#2. popitem():method remove the last inserted item
d={
    "name":"kiran",
     "age": 21
 }
d.popitem()
print(d)
#3. del key can delete the item using key name or completely delete the dictionary
d={
    "name":"kiran",
    "age":21
}
del d
# print(d): it will throw the error
#4. clear(): empty the dictionary
d={
    "name":"kiran",
    "age":21
    }
d.clear()
print(d)

#loop
# 1.the return values are the keys of the dictionary , but there are the method to return value as well
d={
    "name":"kiran",
    "age":21
    }
for x in d:
    print("key:",x)# all key name in the dictionary
# 2. print all the values in the dictionary
d={
    "name":"kiran",
    "age":21
    }
for x in d:
    print("items:",d[x])
# 3.return values of dictionary
d={
    "name":"kiran",
    "age":21
    }
for x in d.values():
    print("values:",x)
# 4. return the key of a dictionary
d={
    "name":"kiran",
    "age":21
    }
for x in d.keys():
    print("keys:",x)
#5.looping through both values and keys using method called items
d={
    "name":"kiran",
    "age":21
    }
for x,y in d.items():
    print("items:",x,y)

#COPY DICTIONARIES
d={
    "name":"kiran",
    "age":21
    }
d2=d.copy()
print(d2)
#using dict()
d={
    "name":"kiran",
    "age":21
    }
d1=dict(d)
print(d1)

#nested dictionaries
family={
    "child1":{
        "name":"kiran",
        "age":21
    },
    "child2":{
        "name":"thomas",
        "age":21
    },
    "child3":{
        "name":"sam",
        "age":21
    }
}
print(family)
print(family["child2"]["age"])
