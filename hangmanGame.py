import random
def hangMan():
    
    word = random.choice(["blast", "cup", "soccer", "mobile", "camera", "result", "admission", "college", 
            "window", "computer", "laptop", "game", "elephant", "dark", "song", "witch", 
            "gymnastics", "yatch", "blazer", "aerodynamics", "demolition", "emaciation"])

    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    chance = 10
    guessMade = ''
    
    while len(word) > 0:
        
        main = ""
        missed = 0

        for letter in word:
            if letter  in guessMade:
                main = main + letter
            else:
                main = main + "_" + ""

        if main == word:
            print(main)
            print("You won")
            break
        
        print("Guess the word : ", main)
        guess = input()
        
        if guess in validLetters:
            guessMade = guessMade + guess
        else:
            print("Enter a valid character")
            guess = input()
        
        if guess not in word:
            chance = chance - 1
            
            if chance == 9:
                print("9 chances left")
                print("  ----------  ")
            
            if chance == 8:
                print("8 chances left")
                print("  ----------  ") 
                print("       0      ")
            
            if chance == 7:
                print("7 chances left")
                print("  ----------  ")
                print("       0      ")
                print("       |      ")

            if chance == 6:
                print("6 chances left")
                print("  ----------  ")
                print("       0      ")
                print("       |      ")
                print("       /      ")
            
            if chance == 5:
                print("5 chances left")
                print("  ----------  ")
                print("       0      ")
                print("       |      ")
                print("      / \      ")
                
            if chance == 4:
                print("4 chances left")
                print("  ----------  ")
                print("     \ 0      ")
                print("       |      ")
                print("      / \     ")

            if chance == 3:
                print("3 chances left")
                print("  ----------  ")
                print("     \ 0 /    ")
                print("       |      ")
                print("      / \     ")

            if chance == 2:
                print("2 chances left")
                print("  ----------  ")
                print("     \ 0 /|   ")
                print("       |      ")
                print("      / \     ")

            if chance == 1:
                print("Last chance left")
                print("  ----------  ")
                print("     \ 0_/|   ")
                print("       |      ")
                print("      / \     ")

            if chance == 0:
                print("You loose")
                print("You let a kind man die")
                print("  ----------  ")
                print("       0_|    ")
                print("      /|\     ")
                print("      / \     ")

                print("The word was : ", word)
                break


name = input("Enter your name : ")
print("\nWelcome ", name)

print("-----------------------------------------")
print("\nTry to guess the word in less then 10 try")
hangMan()