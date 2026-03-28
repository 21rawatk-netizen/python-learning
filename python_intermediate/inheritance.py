#Inheritance: inherting the methods and properties from another class 
#parent class: it is the base class from which we inherit the properties
#child class:it is the class that inherits from another class also called the derived class.
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lastname=lname
    def printname(self):
        print(self.fname,self.lastname)
x=person("kiran",21)
x.printname()

#create a child class: 
# 1. when you want to create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class student(person):
    pass
x=student("mike","olsen")
x.printname()

#when you add the __init__() function the child class will no longer inherit the parent's __init__() function
# child's __init__() function overrides the inheritance of the parent's __init__() function
# To keep the inheritance of the parents's __init__() function, add a call to the parent's __init__() function
