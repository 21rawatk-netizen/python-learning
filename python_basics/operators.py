# operators
# arithmetic operators
x=10
y=12
a="kiran"
b="rawat"
print(x+y)
print(a+b)# can be used for bothe strings and integer
print(x*y)#multiplication
print(x/y)#division
print(x%y)# remainder
print(x**y)# exponentiation ooerator raise x to the power of y
print(x//y)# floor division divide the result and returns the greatest integer leass than or equal to the result
# Assignment operator
x+=3
print(x)
x-=3
print(x)
x*=3
print(x)
x/=5
print(x)
#Comparision operator
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
# Logical operator
print(x<5 and x<10)
print(x>3 and x<18)
print(x<5 or x<10)
print(x>3 or x<18)
print(not(x>6 and x<2))
#identity operator (is and is not)
z=12
print(x is y)
print(y is z)
print(x is not y)
print(y==z)
# Membersipe operator(in and not in)
print("k" in a)
print("i" in b)
print("i" not in b)
# operator precedenc (),**,unary operator,*,/,//,%,+,-
print(5+4-7+3)
print((6+3)+(6+4))
print(100+5*3)
# Loan Eligibility Checker

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))

if age >= 21 and income >= 25000 and credit_score >= 650:
    print("Congratulations! You are eligible for the loan.")
else:
    print("Sorry, you are not eligible for the loan.")
    
# Traffic Rule Violation Detection System

speed = int(input("Enter vehicle speed (km/h): "))
helmet = input("Wearing helmet? (yes/no): ").lower()
signal = input("Signal crossed? (yes/no): ").lower()

if speed > 60 or helmet == "no" or signal == "yes":
    print("Traffic rule violated!")
else:
    print("No violation. Drive safely.")
