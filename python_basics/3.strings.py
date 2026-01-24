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
print(a.title())# first letter of each word is capital
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
text=f"My name is kiran and i am {age} years old"
print(text)
# String slicing
print(a[2:8])
print(a[3:])
print(a[:8])
print(a[-5:-2])
print(a[::2])
print(a[::-1])# string reverseing

#String analyzer tool
name="kiran rawat"
number_of_characters=len(name)
print(number_of_characters)
vowels=0
consonants=0
special_characters=0
for ch in name:
    if( ch.lower() in "aeiou" ):
       vowels+=1
    elif(ch.isalpha()):
        consonants+=1
    else:
        special_characters+=1
print("vowels",vowels)
print("consonants",consonants)
print("special_characters",special_characters)

# Simple Chatbot Using String Matching

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you?")
    
    elif "how are you" in user_input:
        print("Chatbot: I'm fine, thank you! How about you?")
    
    elif "your name" in user_input:
        print("Chatbot: I am a simple Python chatbot.")
    
    elif "help" in user_input:
        print("Chatbot: I can answer basic questions like greetings, name, and time.")
    
    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a nice day ")
        break
    
    else:
        print("Chatbot: Sorry, I didn't understand that.")

#Check if two strings anagrams
s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
#Program 2 for anagrams
def is_anagrams(a,b):
    a=a.replace("","").lower()
    b=b.replace("","").lower()
    return sorted(a)==sorted(b)
print(is_anagrams("Dormitory","Dirty room"))
# Reverse words in a sentence
s="I love Python"
words=s.split()
print("".join(words[::-1]))

#palindrome checker
def is_palindrome(s):
    s=s.replace("","").lower()
    return s==s[::-1]
print(is_palindrome("A man a plan a canal Panama"))
