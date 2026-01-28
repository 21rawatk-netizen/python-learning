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

#Decorato can take there own arguments
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

#Multiple decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

#LAMBDA
#it is also called the anonymus function
# it can take any number of aguments but can have only one expession
# mostly used as a function inside another function
# lambda aguments:expression
x=lambda a: a+10
print(x(5))
y=lambda a,b:a*b
print(y(5,6))
# doubler
def myfunc(n):
   return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
# tripler
def func(n):
   return lambda a:a*n
tripler=func(3)
print(tripler(12))

# lambda with built in functions 
# map()=its applies a function to every item in an iterable
n=[1,2,3,4,5,6]
doubled=list(map(lambda x:x*2,n))
print(doubled)

#filter()=function created alist of item fo whic a function returns true
n=[1,2,3,4,5,6]
odd=list(filter(lambda x:x%2!=0,n))
print("odd numbers:",odd)
even=list(filter(lambda x:x%2==0,n))
print("even number:",even)

#sorted()=function can use lambda as a key for custom sorting
words=["apple","kiwi","banana","pie","orange"]
s=sorted(words,key=lambda x:len(x))
print("sorting by length:",s)

#generator function
#These are the function that can pause and resume their execution
# when a generator function is called it returns a generator object which is an iterator
# instead of using return it uses yield keyword
# yield does not provide the ouput directly it provides the memoay address
# you must iterate over generator to get values
# mmemoay efficient cause they do not store everything in memoray
def counting(n):
    count=1
    while count<=n:
        yield count
        count+=1
print(counting(4))   #it gives memoray address
for i in counting(4):
    print(i)
# you can manually iterate through generato function using the next() function
#1.
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"
gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#2.
def large_sequence(n):
  for i in range(n):
    yield i
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#The send() method allows you to send a value to the generator:
def echo_generator():
  while True:
    received = yield
    print("Received:", received)
gen = echo_generator()
next(gen) 
gen.send("Hello")
gen.send("World")

#The close() method stops the generator:
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close()

#Recursion
def countdown(n):
   if n<=0:
      print("stop")
   else:
      print(n)
      countdown(n-1)
countdown(10)

#Fibonnaci sequence
def fibo(n):
   if n<=1:
      return n
   else:
      return fibo(n-1)+fibo(n-2)
print(fibo(7))
    
#factorial 
def fact(n):
   if n==0 or n==1:
      return 1
   else:
      return n*fact(n-1)
print(fact(5))  

#recursion with lists
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))
