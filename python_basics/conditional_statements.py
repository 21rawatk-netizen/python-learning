# voting condition
age = int(input("enter the age"))
documents = True
if (age>18 and documents):
    print("ready to vote")
else:
    print("minor")
# Electricity bill calculation
past_units=int(input("enter the last month meet units"))
units=int(input("Enter this months meter readings"))
final_readings = units - past_units
relaxtation=final_readings - 20
money = relaxtation*7
text=f"your total bill is{money} Rs"
print(text)

# Small Traffic Light System

signal = input("Enter traffic light color (Red/Yellow/Green): ").lower()
if signal == "red":
    print("STOP")
elif signal == "yellow":
    print("GET READY")
elif signal == "green":
    print("GO")
else:
    print("Invalid signal color")
