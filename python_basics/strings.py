# string
a="kiran rawat"
print(type(a))
print(a)
# Acessing strings since strings act as arrays so it has indexing we can acess single chracter from it
print([1])
print([6])
# string length using len()
print(len(a))
# looping through strings
for x in "kiran":
    print(x)
#checking string using in operator cab be used for word in sentences or character in words
print('i' in a )
print("k" not in a )
# string replication repeating single string multiple times
r=a*3
print(r)
# String cancatenation using the + operator
x="python"
y="code"
z=x+y
print(z)
#some string methods
print(a.upper())# all character into upper case
print(a.lower())# all character in lower case
print(a.strip("k"))# removing specified argument
print(a.strip())# without arguments used for removing leading and trailing whitepc3
print(a.replace("k","h"))# replacing one chracter with another
print(a.split("r"))# coverting string into list based on specid character
print(a.split())#string into list without argument based in available 
index = a.find("w")
print(index)
print(a.count("r"))
print(a.capitalize())#capitalize firt character
print(a.casefold()) # small case first character
print(a.startswith("s")) # check if the word starts with specified character
print(a.endswith("t")) 
# formal strings used to combine the numbers and string using the f strings
age =36
text="My name is kiran and i am {age} years old"
print(text)
# String slicing
print(a[2:8])
print(a[3:])
print(a[:8])
print(a[-5:-2])
print(a[::2])
print(a[::-1])# string reverseing
