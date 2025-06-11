# Python Basics #1: Core Data Types Pt 1, Control Flow
    # Numbers, text, booleans, truth values
    # if, elif, for loops, for else, while
    # (f""") formatting
import math

# multiplies "*" by ten when it prints
print("*" * 10)  # prints an expression

# naming variables
# when making variable, single letter is cap
hello = 0
hi = "hello"
print(hi)  # prints string variable
print("thats nice")  # prints message
print(2 + 3)  # prints math
newVariable = 3  # integer or float
isPublished = True  # Boolean
print(isPublished)
longString = """
Hi Raameen,

Three quotes is actually called a long string and
can be used to make a long string just like this!
Run the program to see the print funtion print this
entire string :)
"""
print(longString)

practiceString = "Raameen Ahmed"

# Some built in fucntions in Python!

print(len(practiceString))  # returns length of string

# uses 0 index,
#   positive = start from front,
#   negative = start from back
print(practiceString[0])  # returns "R"
print(practiceString[-1])  # returns "d" (last letter in the string)
print(practiceString[-2])  # returns "e" (second to last letter)
print(practiceString[0:7])  # SLICING - returns first 7 letters of string
print(practiceString[0:] + " (index functions)")  # reutns whole string // same w [:]

# Escape Sequences:
# \" \' \n \\

first = "Raameen"
last = "Ahmed"
full = first + last + "adding string vars together 1"
full2 = f"{first} {last} + adding string vars together 2 using formatting"
print(full2)
print(first.upper())  # original string is still the same
print(first.lower())
print(first.title())
print(first.strip())  # removes white spaces in beginng and end
print(first.lstrip())  # removes white spaces (  beginning)
print(first.rstrip())  # removes white space (end  )

print(first.replace("ee", "EE"))  # replace(these letters, w these)

print(first.find("aa"))  # returns index !!!
print("Raa" in first)  # returns True or False !!!
print("ahmed" not in first)  # returns True or False


# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}") # formats variables and text into a string

# if - statements in Python
temp = 35
if temp > 30:  # make sure to remember the colon !
    print("Make sure to remember the indentation")
    print("This statement will still print in the if statement")
elif temp > 20:
    print("This is Python's else if statment")
else:
    print("This is python's else statment")
print("This statement is not in the if statement")

message = "Over 30" if temp > 30 else "lower than 30"
print(message)  # an easier and way simple way to make an if statment !
# similiar to booleans ?

# words u can use in code: and, or, not
high_income = True
good_credit = True
if (high_income and good_credit):
    print("Both true")
else:
    print("One or both aren't true")

# loops in python
for number in range(1,10,2): # 1 to 10, step 2
    print("Sending a message")

# for else loops , if loop doesnt do what u want, else runs
successful = False
for number in range(3): # 1 to 10, step 2
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted three times and failed")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

number = 100
while number > 0:
    print(number)
    number //= 2

"""

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

"""

print("BYE")
counter = 0
for i in range(1,10):
    if (i % 2 == 0):
        print(i)
        counter = counter +1
else:
    print(f"We have {counter} even numbers")