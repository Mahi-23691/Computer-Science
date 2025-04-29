'''This is a simple program to check if a person can vote or not
   By Mahi Mahatab on 25/02/2025'''

is_resident = False

#ask the user for their name
name = input("What's your name?\n>> ")

while True:
    try:
        #ask the user for their age
        age = int(input("What's your age?\n>> "))
        break
    except ValueError:
        print("Please enter a valid number!")
#end of while loop

#ask the user if they are a resident or not
resident = input("Are you a reasident of New Zealand? (Y/N)\n>> ").lower()
while True:
    if resident == 'y':
        is_resident = True
        break
    elif resident == 'n':
        is_resident = False
        break
    else:
        print("Please enter Y or N!")

#Check if the user can vote or not
if age > 17 and is_resident:
    print("You can Vote!!!\n")
else:
    print("You cannot Vote!!!\n")
    