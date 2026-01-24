# for loop
fruits=['apple',"banana","kiwi"] #for loop in list through words
for i in fruits:
    print(i)
for a in "kiran":# for loop in word through chracters
    print(a)
for x in range(6):#for loops leaves last word
    print(x)

#while loop (first condition always true)
count=1
while(count<8):
    print(count)
    count+=1

#conditional statements in loops(pass,break,continue)
#break 
for x in range(6):#for loops leaves last word
    print(x)
    if x==3:
     break

#continue
for x in range(6):#for loops leaves last word
    if x==4:
        continue
    print(x)

    #loop control statement
#Break = immediately terminates the loop
for i in range(1,11):
    if i==5:
        break
    print(i)
# Continue = skip the current iteration
for i in range(1,6):
    if i==3:
        continue
    print(i)
#pass = It does nothing , used when you want to write code later or keep block empty
for i in range(1,4):
    if i==2:
        pass
    print(i)

#Factorial Calculator

#using for loop
n=int(input("Enter the value of n"))
fact=1
for i in range(1,n+1):
     fact=fact*i
print("Factorial=",fact)
#using while loop
n=int(input("Enter a number"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print("Factorial=",fact)
#using function
def factorial(n):
    fact=1
    for i in range(n,n+1):
        fact=fact*i
    return fact
n=int(input("Enter the number"))
print("Factorial=",factorial(n))
#using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number:"))
if n<0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial=",factorial(n))

#Fibonacci Series 

#using for loop
n=int(input("Enter number of terms"))
a=0
b=1
print("Fibonacci series")
for i in range(n):
    print(a,end="")
    a,b=b,a+b
#using function and recursion
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter number of terms"))
print("Fibonacci series")
for i in range(n):
    print(fib(i),end="")

#Prime Number Checker and Generator
n=int(input("Enter a number:"))
if n<=1:
    print("Not prime")
else:
    is_prime=True
    for i in range(2,n):
        if n%i ==0:
            is_prime=False
            break
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")

# ATM Simulation System
balance = 10000  # Initial balance
pin = 1234       # Default PIN
print("----- Welcome to ATM -----")

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n---- ATM MENU ----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your Balance is:", balance)

        elif choice == 2:
            deposit = int(input("Enter amount to deposit: "))
            balance= balance + deposit
            print("Deposit Successful ")
            print("Updated Balance:", balance)

        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw > balance:
                print("Insufficient Balance ")
            else:
                balance -= withdraw
                print("Withdrawal Successful ")
                print("Updated Balance:", balance)

        elif choice == 4:
            print("Thank you for using ATM ")
            break

        else:
            print("Invalid choice Please try again!")

else:
    print("Wrong PIN Access Denied")
