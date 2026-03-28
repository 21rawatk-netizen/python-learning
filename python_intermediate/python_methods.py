#class methods: methods are function that belong to a class . they define the behaviour of objects created from the class
class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print("hello, my name is " + self.name)
p1=person("kiran")
p1.greet()

#Medtoh with parameter
class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
p1=calculator()
print(p1.add(2,3))
print(p1.sub(2,3))
print(p1.mul(2,3))
print(p1.div(2,3))

#method acessing properties:acess and modify using self
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_info(self):
        return f"{self.name} is {self.age} years old"
p1=person("kiran",21)
print(p1.get_info())

#Method modifying properties:method that changes the property value
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def celebrate_birthday(self):
        self.age+=1
        print(f"Happy birthday {self.name} ! you are {self.age} now")
p1=person("kiran",21)
print(p1.name)
print(p1.age)
p1.celebrate_birthday()

# The str() method:it is the specil method that controls what is returned when the object is printed
# without __str__()
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("kiran",21)
print(p1)
# with __str__()
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name},{self.age}"
p1=person("kiran",21)
print(p1)

#music playlist
class playlist:
    def __init__(self,name):
        self.name=name
        self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
        print(f"added:{song}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"removed:{song}")
    def show_song(self):
        print(f"playlist {self.name}:")
        for song in self.songs:
            print(f"{song}")
p=playlist("fav")
p.add_song("b")
p.add_song("c")
p.add_song("d")
p.show_song()
p.remove_song("b")
p.show_song()
