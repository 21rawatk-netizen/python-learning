#Acessing properties with self:
# properties are variables that belong to a class. they store data for each object created from the class.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print("name:", self.name)
p1=person("kiran",21)

#ACESSING PROPERTIES: using dot notation to acess properties
print(p1.name) 
print(p1.age)
p1.printname()

# MODIFYING PROPERTIES:
p1.age=22
print(p1.age)

#DELETING PROPERTIES: deleting it using del keyword
del p1.age
# print(p1.age): it will give an error
# object properties: properties inside the __init__() belong to each object
# class properties: propeties outside methods belong to class, or can be shared by all objects.
class person:
    species="human" #class property
    def __init__(self,name):
        self.name=name #instance property
p1=person("Emil")
p2=person("Tobias")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

class person:
    lastname="" 
    def __init__(self,name):
        self.name=name
p1=person("kiran")
p2=person("rawat")
person.lastname="refsense"
print(p1.lastname)
print(p1.name,p1.lastname)
print(p2.name,p1.lastname)

#adding new properties:can add properties in existing objects
class person:
    def __init__(self,name):
        self.name=name
p1=person("kiran")
p1.age=21
p1.city= "delhi"
print(p1.name)
print(p1.age)
print(p1.city)
