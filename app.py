# Working with data types

character_name = "Siddharth"
character_age = 21
isMale = True
decimal_val = 22.550545

print("The name is : " + character_name)
print("The age is : ", character_age)
print("The decimal value is : ", decimal_val)
print("The bool value is : ", isMale)


# Working with strings

demoTxt = "This is a Demo Text"
print(demoTxt.lower())
print(demoTxt.upper())
print(demoTxt.islower())
print(demoTxt.isupper())
print(demoTxt.upper().isupper())
print(demoTxt.lower().islower())
print(len(demoTxt))
print(demoTxt[-1])
print(demoTxt.replace("This","That"))
print(demoTxt)

# Getting input from the user

name = input("Enter your name : ")
age = input("Enter your age : ")

print("Name is : "+name+" and the age is : ", age)


# Calculator App

num1 = input("Enter the first number : ")
num2 = input("Enter the second number : ")

num3 = int(num1) + int(num2)

print("The addition is : ", num3)

# Lists...


# friends = ["Adam", "Bennett", "Carlo", "David", "Elliot", "Gannet", "Falcon", "Gadot", "Henry", "Imy"]
# numberList = [46, 8, 12, 55, 37, 39, 348, 40, 71]
# friends.extend(numberList)
# print(len(friends))
# print(friends)

# x = 45
# y = 12
# print((x, y))

# Fibonacci Series...

# a, b = 0, 1
# while a < 200:
#     print(a)
#     a, b = b, a+b

# Functions....

def firstFunc():
    print("This is the first function")

firstFunc()

# Parameterized function...

def paraFunc(num):
    num = int(num)
    print("The entered number is : ", num)

no = input("Enter the number : ")
paraFunc(no)

# Return Statement...

def circleArea(radius):
    return (2*22*radius*radius)/7

print("The Area of the circle with radius 45 is : ", circleArea(45))