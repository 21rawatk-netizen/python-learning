#creating a class
class myclass:
    x=5
#creating an object
p1=myclass()
print(p1.x)
#deleting object
del p1
#Multiple object
p2=myclass()
p3=myclass()
p4=myclass()
print(p2.x)
print(p3.x)
print(p4.x)

#_init_():all classes have a built in method which is always executed when the class is being initiated,it is used to assign value to object peoperties or to perform operations that are necessay when the object is being created

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("emil",21)
print(p1.name)
print(p1.age)

#default values in __init__()
class person:
    def __init__(self,name,age=21):
        self.name=name
        self.age=age
p1=person("emil",21)
p2=person('kiran')
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

#Multiple parametrs
class person:
    def __init__(self,name,age,city,country):
        self.name=name
        self.age=age
        self.city=city
        self.country=country
p1=person("emil",21,'oslo','Norway')
print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#self parameter:it must be the first parameter of any method,without self python would not be able to know which object property to acess
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print("hello, my name is "+ self.name)
p1=person("emil",21)
print(p1.name)
print(p1.age)
p1.greet()

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print('name:',self.name)
    def printage(self):
        print('age:',self.age)
p1=person("emil",21)
print(p1.name)
print(p1.age)
p1.printname()
p1.printage()
