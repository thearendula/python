import random

print("Dice Simulator\n\n")

x = "y"

while(x == "y"):

    randNum = random.randint(1, 6)

    if randNum == 1:
        print("----------")
        print("|        |")
        print("|    0   |")
        print("|        |")
        print("----------")

    if randNum == 2:
        print("----------")
        print("|        |")
        print("| 0    0 |")
        print("|        |")
        print("----------")

    if randNum == 3:
        print("----------")
        print("|    0    |")
        print("|         |")
        print("| 0     0 |")
        print("----------")

    if randNum == 4:
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")

    if randNum == 5:
        print("----------")
        print("| 0     0|")
        print("|    0   |")
        print("| 0     0|")
        print("----------")

    if randNum == 6:
        print("----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("----------")

    x = input("Press Y to roll the dice again\n\n")

