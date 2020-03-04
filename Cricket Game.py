import random

print("Two player Static Cricket Game")

# Getting the two player name
player1 = input("Enter the first player name : ")
player2 = input("Enter the second player name : ")

# Variables for the scores and wickets
p1score = 0
p1wic = 0
p1runs = 0
p1extras = 0
p2score = 0
p2wic = 0
p2runs = 0
p2extras = 0
p1sixes = 0
p1fours = 0
p2sixes = 0
p2fours = 0

# Variables for Overs and Balls
overs = 0
balls = 0

print(player1 + " innings started")

# Innings Logic
for overs in range(1, 6, 1):
    if p1wic == 10:
        break

    print("================== NEW OVER STARTED. OVER NUMBER : %s ==================" % overs)

    for balls in range(1, 7, 1):
        if p1wic == 10:
            break

        p1runs = random.randrange(1, 9)

        if p1runs == 1:
            p1score += p1runs
            print("\n\nBall number : ", balls)
            print("Single. \nScore is : ", p1score)

        if p1runs == 2:
            p1score += p1runs
            print("\n\nBall number : ", balls)
            print("Two runs. \nScore is : ", p1score)

        if p1runs == 3:
            p1score += p1runs
            print("\n\nBall number : ", balls)
            print("Three runs. \nScore is : ", p1score)

        if p1runs == 4:
            p1score += p1runs
            p1fours += 1
            print("\n\nBall number : ", balls)
            print("======================== Smashed Four. ===================== \nScore is : ", p1score)

        if p1runs == 5:

            print("\n\nBall number : ", balls)
            print("Dot ball. \nScore is : ", p1score)

        if p1runs == 6:
            p1score += p1runs
            p1sixes += 1
            print("\n\nBall number : ", balls)
            print("======================== That's a SIX. ====================== \nScore is : ", p1score)

        if p1runs == 7:
            p1wic += 1
            print("\n\nBall number : ", balls)
            print("----------------------- Wicket Gone -------------------------")

        if p1runs == 8:
            balls = balls - 1
            p1score += 1
            p1extras += 1
            print("\n\nBall number : ", balls)
            print("\n\nWide ball. \nScore is : ", p1score)

        if p1runs == 9:
            balls = balls - 1
            p1score += 1
            p1extras += 1
            print("\n\nBall number : ", balls)
            print("\n\nNo Ball. Free hit....... \nScore is : ", p1score)

    if overs == 5:
        print("Overs Ended")
        print("Total Extras : ", p1extras)
        print("Total wickets fallen are : ", p1wic)

    if p1wic == 10:
        print("That's All Out")
        print("Total Extras : ", p1extras)

print("\n\n\n\n\n", player2, " need ", (p1score + 1), " to win. ")

print("Press enter to start ", player2, " innings")
input()

print(player2, " innings started.")

# PLAYER 2 STARTS

for overs in range(1, 6, 1):
    if p2wic == 10:
        break

    print("================== NEW OVER STARTED. OVER NUMBER : %s ==================" % overs)

    for balls in range(1, 7, 1):
        if p2wic == 10:
            break

        p2runs = random.randrange(1, 9)

        if p2runs == 1:
            p2score += p2runs
            print("\n\nBall number : ", balls)
            print("Single. \nScore is : ", p2score)

        if p2runs == 2:
            p2score += p2runs
            print("\n\nBall number : ", balls)
            print("Two runs. \nScore is : ", p2score)

        if p2runs == 3:
            p2score += p2runs
            print("\n\nBall number : ", balls)
            print("Three runs. \nScore is : ", p2score)

        if p2runs == 4:
            p2score += p2runs
            p2fours += 1
            print("\n\nBall number : ", balls)
            print("======================== Smashed Four. ===================== \nScore is : ", p2score)

        if p2runs == 5:

            print("\n\nBall number : ", balls)
            print("Dot ball. \nScore is : ", p2score)

        if p2runs == 6:
            p2score += p2runs
            p2sixes += 1
            print("\n\nBall number : ", balls)
            print("======================== That's a SIX. ====================== \nScore is : ", p2score)

        if p2runs == 7:
            p2wic += 1
            print("\n\nBall number : ", balls)
            print("----------------------- Wicket Gone -------------------------")

        if p2runs == 8:
            balls = balls - 1
            p2score += 1
            p2extras += 1
            print("\n\nBall number : ", balls)
            print("\n\nWide ball. \nScore is : ", p2score)

        if p2runs == 9:
            balls = balls - 1
            p2score += 1
            p1extras += 1
            print("\n\nBall number : ", balls)
            print("\n\nNo Ball. Free hit....... \nScore is : ", p2score)

    if overs == 5:
        print("Overs Ended")
        print("Total Extras : ", p2extras)
        print("Total wickets fallen are : ", p2wic)

    if p2wic == 10:
        print("That's All Out")
        print("Total Extras : ", p2extras)

if p1score > p2score:
    print("Winner is : ", player1)
    print(player1, " won by ", (p1score - p2score), " runs.")

if p1score < p2score:
    print("Winner is : ", player2)
    print(player1, " won by ", (10 - p2wic), " wickets.")


print("Total fours of : ", player1, " is : ", p1fours)
print("Total sixes of : ", player1, " is : ", p1sixes)
print("Total fours of : ", player2, " is : ", p2fours)
print("Total sixes of : ", player2, " is : ", p2sixes)
