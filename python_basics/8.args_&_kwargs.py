#*args = arbitary arguments 
#if your dont know that what are the number of arguments that are going to be passed in a function 
# * added before the parameter name .
# the most important the function will recieve the tuple of arguments and ca acess the items accordingly (tuples that are ordered and unchageable)
def my(*kid):
    print("Type;",type(kid))
    print("First argument",kid[0])
    print("First argument"+ kid[1])
    print("First argument"+ kid[2])
    print("First argument", kid)
my("kiran","rawat","emil")
# make sure to always use the , beacuse + concatenate 
# Combinig *args with regular arguments
def my_func(greeting,*name):
    for i in name:
        print(greeting,i)
my_func("hello","emil","tobias","linus")

#sum of any number
def sum_of(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
print(sum_of(1,2,3))
print(sum_of(10,20,30,40))
print(sum_of(5))

#**kwargs=Arbitary keyword arguments
# when you don't know how many keyword arguments will be pssed on toyour function so we add ** befor the parameter name
# Here the most impotant the function receives a dictionary of arguments and can acess the items accordingly
def myfunc(**kid):
    print("kid name", kid["fname"])
myfunc(fname="kiran",lname="rawat")

def myfunc(**kid):
    print("Type:",type(kid))
    print("Name",kid["name"])
    print("Age:",kid["age"])
    print("all data",kid)
myfunc(name="kiran",age=21)

#Combining **kwargs with regular arguments
def myfunc(username,**details):
    print("username",username)
    print("Additional details:")
    for key,value in details.items():
        print("",key+":",value)
myfunc("krawat123",age=25,city="oslo", hobby="code")

## combining regular para meter,arbitary positional arguments, arbitary keyword arguments
def myfunc(title,*args,**kwargs):
    print("Title:",title)
    print("positional arguments",args)
    print("keyword arguments",kwargs)
myfunc("user info","Emil","Tobias",age=21,city="oslo")
