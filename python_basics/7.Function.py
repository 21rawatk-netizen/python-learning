#function is define using def keyword
# function definition
'''def my_function(parameter):
    return parameter
# function calling
my_function(argument)
# return values '''

# function with no parameter and argument
def func():
    print("Hello")
func()

# function with parameter and argument
def func(fname):
    print(fname,"Refsnes")
func("Kiran")

#number of  parameters should be equal to no. of arguments
def my_function(fname,lname):
    print(fname +"" +lname)
my_function("kiran","Rawat")

#default parameter used when function is called withhot arguments
def my_function(fname="ki"):
    print(fname)
my_function("kiran") 
my_function()

#keyword argument where the position of arguments dosent matter 
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function( name = "Buddy", animal="dog")

#positonal arguments= the arguments should be passed in correct order to the calling function
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")
#Mixing positional and keyword arguments while calling function the positional arguments shiuld come before the keyword arguments
def func(name,age,height):
   print("myself",name,"I am",age,"year's old",height,".")
func("kiran",age=21,height=6.4)

#Diffrnet data type as an argument in function
#list
def my_basket(fruit):
   for i in fruit:
      print(i)
my_fruits=["apple","banana","kiwi"]
my_basket(my_fruits)
#dictionary
def record(person):
   print("name:",person["name"])
   print("age:",person["age"])
my_record={
   "name":"kiran",
   "age":21
}
record(my_record)
#Returning of value
def r(x,y):
   return x+y

#Postional only arguments= where you can specify that a function can only have postional arguments by adding ,/ after arguments withou this you can give both positional and keyword argument but ,/ is strictly for the postional arguments
def my(name,/):
   print(name)
my("kiran")

#Keyword only arguments where you can only pass the keyword arguments to the function by adding the *, before the parameter
def my(*,lname):
   print(lname)
my(lname="Rawat")

# Combining positional only arguments and keyword only arguments 
def addition(a,b,/,*,c,d):
   return a+b+c+d
result=addition(5,10,c=4,d=2)
print(result)
