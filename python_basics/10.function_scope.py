#local scope
#the variable which is declared inside the function and can only be acessed inside the function 
def my_func():
    x=200
    print(x)
my_func()
# the local variables can also be acessed by within an same function
def outer():
    x=201
    def inner():
        print(x)
    inner()
outer()

#Global Scope
#a variable which is created in the main body so that it can be accesd globaly and locally mostly outside the function
x=202
def g():
    print(x)
g()
print(x)
#Note: if the variable the global variable mostly defined outide the function and the local variable which is defined inside the function are assigned by same name then the program treat them as two seperate variable
x=204
def k():
    x=203
    print(x)
k()
print(x)

#GLOBAL KEYWORD
# it is used to make the local variable globally acessible using the global keyword
def g():
    global x 
    x = 205
    print(x)
g()
print(x)
# the global keyword can als be ised a to update the existi ng value of global varable
x=206
def g():
    global x
    x=207
    print(x)
g()
print(x)

#NON LOCAL KEYWORD
# it is used to work with the variable inside the nested function 
# The non local keyword make the variable belong to the outer function
def outer():
    x=201
    print("outer:",x)
    def inner():
        nonlocal x
        x =500
        print("inner:",x)
    inner()
    print("outer after non local:",x)
outer()

# LEGB rule
#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

