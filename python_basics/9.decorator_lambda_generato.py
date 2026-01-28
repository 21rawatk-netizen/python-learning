#Decoator
# it lets you add extra behaviour to the function without changing the code
# it takes another function as the input and return the new function
# first define the decorator function then apply @decorator name above the dceoated function
def changecase(func):
    def myinner():
       return func().upper()
    return myinner
@changecase
def myfunc():
    return "hello sally"
print(myfunc())

# can use the same decorator function for more function
def changecase(func):
    def myinner():
       return func().upper()
    return myinner
@changecase
def myfunc():
    return "hello sally"
print(myfunc())
@changecase
def m():
    return "kiran"
print(m())

# arguments in decorator function
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

