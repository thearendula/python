import random

randNum = random.randrange(1, 100, 1)

chances = 5
num = 0

print("The number is guessed by the computer between 1 to 100 let's start the game. You have got 5 chances.")

while chances > 0:
    num = input("Enter the number : ")
    num = int(num)

    chances -= 1

    if num < randNum:
        print("Hint : Entered number is less than generated number.")
    elif num > randNum:
        print("Hint : Entered number is greater than generated number.")

    if randNum == num:
        break
    elif chances == 0:
        print("You are out of chances")
        break

if chances == 0:
    print("The number guessed by the computer is : ", randNum)
elif num == randNum:
    print("Guesses remaining : ", chances)
else:
    print("Well done !!")
